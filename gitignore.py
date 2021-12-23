import os

import sublime
import sublime_plugin


class compilegitignoreCommand(sublime_plugin.WindowCommand):
    _file_listing = None
    _search_path = None

    def _delayed_init(self):
        # Put off init until first run to save resources
        if not self._file_listing:
            self._search_path = os.path.join(sublime.packages_path(), 'Gitignore', 'gitignore')
            # Deprecating zipfile package support (sorry!)
            # It didn't really support unzipped overrides. This will, but I guess an update would wipe it out?
            # This won't recurse, sorry! I would if we had pathlib!
            # Also, I suppose it's vulnerable to directories ending in .gitignore
            self._file_listing = sorted(f[:-10] for f in os.listdir(self._search_path) if f.endswith('.gitignore'))
            # A set would be much more efficient, but a sorted list is way nicer to display
            # Might be able to use a sorted dict key set, but it's iffy

    def _run_selection(self):
        # Gotta do some scoping tricks to maintain the list through the callbacks
        selection = []
        # Just gotta keep a copy :(
        # You COULD stitch iterators together ['Done'], [x for x in self._list_items if x not in selection]
        # BUT then the selection indices are off
        listing = self._file_listing.copy()

        def selection_callback(index):
            if index < 0:
                # User cancel
                pass
            elif selection and index == 0:
                # Done!
                self._write_file(selection)
            else:
                # user selected something from the list
                selection.append(listing[index])
                del listing[index]
                # Could do some fancy stitching.... but could also not!
                if len(selection) == 1:
                    listing.insert(0, 'Done')
                self.window.show_quick_panel(listing, selection_callback)

        self.window.show_quick_panel(listing, selection_callback)  # sublime.KEEP_OPEN_ON_FOCUS_LOST ?

    def run(self):
        self._delayed_init()
        self._run_selection()

    def _write_file(self, chosen_files):
        export = []
        for name in chosen_files:
            # if the file disappeared, post-indexing, it's not our fault.
            with open(os.path.join(self._search_path, name + '.gitignore'), 'r') as f:
                export.append(' '.join(('###', name, '###')))
                export.append(f.read())

        export = '\n\n'.join(export)
        # An unconstrained (r)strip may be bad?
        # For example, the MacOS one has '.Icon\r\r', which strip would mangle if it was at the end of the list
        #  (and sublime mangles if you open it which drives me crazy when I try to add to it)
        # The gitignore syntax file doesn't mention line endings at all, which is rude.
        if not export.endswith('\n'):
            export += '\n'
        view = sublime.active_window().new_file()
        # Wild, we can't inject text in a new window without an edit object, so it has to be a second command(??)
        view.run_command('writegitignore', {'text': export})


class writegitignoreCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        self.view.insert(edit, 0, kwargs['text'])
        self.view.set_name('.gitignore')

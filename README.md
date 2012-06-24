<h1>Sublime Text 2 Gitignore plug-in</h1>

<h3>Sublime Text 2 plug-in for fetching gitignore boilerplates from <a href="https://github.com/github/gitignore">the collection of gitignore boilerplates by Github</a></h3>

<h3>How it works</h3>
Press <code>Cmd + Shift + P</code> for Mac and <code>Ctrl + Shift + P</code> for Linux<br />
Write <code>Gitignore</code> and select <code>Gitignore: new gitignore</code>

Then select the desired gitignore boilerplate.<br>
Now select another boilerplate. When you are done, select <code>Done</code>.

Save the newly open file as <code><i>something</i>.gitignore</code> and your done!

<h2>Installation</h2>

Install via package control

<h3>Or</h3>

<h4>Linux</h4>

<code>
git clone https://github.com/theadamlt/Sublime-Gitignore ~/.config/sublime-text-2/Packages/Gitignore
</code>


<h4>Mac</h4>

<code>
git clone https://github.com/theadamlt/Sublime-Gitignore ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Gitignore
</code>


Make sure that Git is installed

<hr>

The plugin works via <a href="https://github.com/simonwhitaker/gitignore-boilerplates">gibo</a> so thanks to Simon Whitaker.

<h2>TODO</h2>
Remove independence of gibo, create own db of gitignore boilerplates


<h2>How bout' Windows support?</h2>
This plugin doesn't support windows, yet.
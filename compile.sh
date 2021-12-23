#!/bin/bash

# Throw out what we have
rm -rf gitignore

# Clone the current listing
git clone --depth 1 https://github.com/github/gitignore.git MASTER_GITIGNORE

# Compile listing
mkdir gitignore
cp MASTER_GITIGNORE/Global/*.gitignore gitignore/
cp MASTER_GITIGNORE/*.gitignore gitignore/
rm -rf MASTER_GITIGNORE

# I was gonna record commits and diff them... or I could just have git notice any changes
# git status --porcelain | wc -l | tr -d ' ' != "0" == differences

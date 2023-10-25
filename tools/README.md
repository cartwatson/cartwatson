# Instructions for tools

## setup.sh

- setup.sh should be run from this dir

## todo_generator

- todo_generator should be run from the home directory of any git repo
  - arguments may be provided to it for the root directory to search and the readme filepath
  - if no arguments are provided root dir is ./ and readme path is ./README.md

## TODO

- [ ] IMPLEMENT: fuzzy matching, minor changes shouldn't create a new todo but should replace an old one
- [ ] EXPERIMENT: find a good way to incorperate meta todos; maybe using file location
- [ ] RESEARCH: see if theres a way to find if a line is a comment
- [ ] create function to take file paths as arguments and create "cd\<letter\>" aliases for them
- [X] BUGFIX: replace any < or > with escaped characters for md rendering

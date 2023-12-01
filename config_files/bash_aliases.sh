# aliases
# --bash
alias egs="echo -e '\n---- Git Status ----'; git status;"
alias ell="echo -e '---- ll -al ----';"
alias cdh="clear; cd ~"
alias cds="clear; cd <School Dir>"
alias cdm="clear; cd <Personal Projects Dir>"
alias cdd="clear; cd <Other Working Location>"
alias ll="ls -Al"
alias vbr="vim ~/.bash_aliases"
alias sbr="source ~/.bashrc"
alias ebr="cat ~/.bash_aliases"
# --git
alias gs="git status -sb"
alias ga="git add"
alias gl="git log --oneline --graph"
alias gc="git commit -m"
alias gd="git diff"
alias gp="git push"
alias gco="git checkout"
alias gcod="git checkout dev"
alias gsll="clear; ell; ll; egs; git status;"
function gcp() { git commit -m "$@" && git push ;}
function gpsu() { git push --set-upstream origin $(git branch --show-current); }
# --override builtins
function cd() { builtin cd "$@" && ls -Al; }
# --windows
alias e="explorer ."
alias c="code ."
# --markdown
# pandoc_md2pdf() { pandoc -V geometry:margin=0.75in --pdf-engine=xelatex -s -o "$1.pdf" "$1.md"; }
# --custom scripts
function todo_gen() { python3 ~/.todo_gen.py "$@"; }

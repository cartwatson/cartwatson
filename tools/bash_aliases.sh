# aliases
# --bash
alias egs="echo -e '\n---- Git Status ----'; git status;"
alias ell="echo -e '---- ll -al ----';"
alias cds="clear; ell; cd <School Dir>"
alias cdm="clear; ell; cd <Personal Projects Dir>"
alias cdd="clear; cd <Other Working Location>"
alias ll="ls -al"
alias vbr="vim ~/.bash_aliases"
alias sbr="source ~/.bashrc"
alias ebr="cat ~/.bash_aliases"
# --git
alias gs="git status"
alias ga="git add"
alias gl="git log --oneline --graph"
alias gc="git commit -m"
alias gp="git push"
alias gco="git checkout"
alias gcod="git checkout dev"
alias gsll="clear; ell; ll; egs; git status;"
function gcp() { git commit -m "$@" && git push ;}
function gpsu() { git push --set-upstream origin $(git branch --show-current); }
# --override builtins
function cd() { builtin cd "$@" && ls -al; }
# --windows
alias e="explorer ."
alias c="code ."

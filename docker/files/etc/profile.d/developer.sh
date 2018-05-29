export GPG_TTY=$(tty)

alias ll="ls -al"
alias gc="git commit"
alias gs="git status"
alias ga="git add"
alias gcs="git commit -S"
alias gcb="git checkout -b"
alias gdc="git diff --no-color"
alias gdcc="git diff --cached --no-color"
alias glsc="git log --no-color --show-signature"

git config --global gpg.program gpg
git config --global commit.gpgsign true
git config --global user.name "$GIT_USER_NAME"
git config --global user.email "$GIT_USER_EMAIL"
git config --global user.signingkey "$GIT_USER_GPG_KEY"

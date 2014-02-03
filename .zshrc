# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/gregg/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

setopt HIST_IGNORE_DUPS

export EDITOR="emacsclient -t"
alias e=emacsclient -t
alias ec=emacsclient -c
alias vim=emacsclient -t
alias vi=emacsclient -t
alias mvn3=/home/gregg/workspace/apache-maven-3.0.5/apache-maven/target/apache-maven-3.0.5/bin/mvn
alias trayer=trayer --edge top

alias -s csv=libreoffice
alias -s rtf=abiword
alias -s doc=abiword
alias -s docx=libreoffice
alias -s ppt=libreoffice
alias -s pptx=libreoffice
alias -s pdf=okular

# lucid vpn
alias lucidvpn="sudo openvpn --config /etc/openvpn/lucid.conf"

# lucid clear local
alias lucidrm="rm -rf /opt/play-2.1.1/repository/*/com.lucidchart/*; rm -rf ~/.ivy2/*/com.lucidchart/*"

# quick cd
alias cd-chromechart="cd ~/workspace/chart/extensions/chrome/chrome-app"
alias cd-chart-cake="cd ~/workspace/chart/cake"
alias cd-chart-js="cd ~/workspace/chart/cake/app/webroot/js"
alias cd-chart-css="cd ~/workspace/chart/cake/app/webroot/css"

setopt completealiases

autoload -U promptinit && promptinit
autoload -U colors && colors

PROMPT="%{$fg[red]%}%n%{$reset_color%}@%{$fg[blue]%}%m %{$fg_no_bold[green]%}%1~ %{$reset_color%}[%{$fg_no_bold[green]%}%?%{$reset_color%}] %# "
RPROMPT=""

# Cool aliases and things
alias -s zip='unzip'

# Path and other env
export GOPATH=~/workspace/go
export GOBIN=~/workspace/go/bin


#source ~/.gozsh

export PATH=$PATH:$HOME/.local/bin
export PATH=$PATH:$HOME/.gem/ruby/2.0.0/bin
export ANDROID_HOME=/opt/android-sdk

export PATH=$PATH:/usr/lib/smlnj/bin

# bc
export BC_ENV_ARGS=$HOME/.bcrc

# rvm
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"

# show path in titlebar
WMII_IS_RUNNING=`ps a | grep wmii | awk '/[^"grep"] wmii$/'`
if [ -n "$WMII_IS_RUNNING" ]; then
    PROMPT_COMMAND='dirs | wmiir /client/sel/label'
fi

PATH=$PATH:$HOME/.rvm/bin # Add RVM to PATH for scripting

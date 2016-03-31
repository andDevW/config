#!/bin/zsh

# generate php tags
rm -f /home/gregg/lucid/main/cake/TAGS
find /home/gregg/lucid/main/cake/ -name "*.php" -exec ctags -e --append -f /home/gregg/lucid/main/cake/TAGS {} \;

# generate js tags

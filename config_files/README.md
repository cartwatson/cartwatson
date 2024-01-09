# File instructions

## bash_aliases

to use the md to pdf function, run the following command

```sh
sudo apt-get install -y pandoc texlive-xetex
```

## bashrc

if the git prompt isnt working make sure to copy the git file from [here](https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh) to `/usr/share/git-core/contrib/completion/git-prompt.sh`. Note: user will need root access to copy file to this location; if not attainable cp to different location and change lines 31-32 of .bashrc.

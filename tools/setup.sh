# hush login
touch /home/$(whoami)/.hushlogin

# copy tools
# cp ./todo_generator.py ~/.todo_gen.py

# copy config files
cp ../config_files/vimrc.vim ~/.vimrc

# TODO: create function to take file paths as arguments and create "cd<letter>" aliases for them
cp ../config_files/bash_aliases.sh ~/.bash_aliases
cp ../config_files/bashrc.sh ~/.bashrc
source ~/.bashrc

# install vscode extensions
# code --install-extension ms-vscode-remote.remote-wsl  # wsl extension
# code --install-extension ritwickdey.liveserver        # live server
# code --install-extension yzhang.markdown-all-in-one   # markdown all in one
# code --install-extension pkief.material-icon-theme    # material icon theme

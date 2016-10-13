!#/bin/bash

# install homebrew with 
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update
brew install ffmpeg --with-libfdk-aac --with-libx264 --with-libmp3lame
brew upgrade ffmpeg
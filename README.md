# Audio-video transcription

Extract audio from videos with this project

## Installation

install ffmpeg

```sh
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg

# fedora

sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf -y install ffmpeg
sudo dnf -y install ffmpeg-devel
```

create virutal env and activate
```sh
python -m venv env

source env/bin/activate
```

install dependecies and setup rust

```sh
pip install git+https://github.com/openai/whisper.git
pip install setuptools-rust
pip install pytube

```

## [more info](https://github.com/openai/whisper) about whisper

## usage

run the follow script en insert the url of video and then the name of the output file

```sh
python main.py

```


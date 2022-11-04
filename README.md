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

```

create virutal env and activate
```sh
python -m venv env

source env/bin/activate
```

install dependecies

```sh
pip install -r requirements.txt

```

## usage

run the follow script en insert the url of video and then the name of the output file

```sh
python main.py

```


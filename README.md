# HEIC TO JPG

Converts all pictures in a given folder from HEIC to JPG. Stores the new photos with the same name in `/converted` folder in the same directory unless target folder provided in flags.


Thanks to [this link](https://stackoverflow.com/a/65462590).

## Installing prerequisites

1. Install libheif via Homebrew

Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Libheif
```bash
brew install libheif
```

```bash
pip install heic-to-jpeg-converter
```


## Usage

Convert everything in current folder and store in `/converted`
```bash
jpeg-converter convert
```
Find all files in the Downloads directory and save the converted pictures in current directory
```bash
jpeg-converter convert -s ~/Downloads -t .
```
Only list the files in the Downloads directory that will be converted
```bash
jpeg-converter convert -s ~/Downloads -l
```

## Testing Locally

1. Create a virtualenv

```bash
python3 -m venv env
```

2. Activate the virtual environment

```bash
source env/bin/activate
```

3. Use script
```bash
development.sh
```

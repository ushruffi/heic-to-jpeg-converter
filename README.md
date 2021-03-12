# HEIC TO JPG

Converts all pictures in a given folder from HEIC to JPG. Stores the new photos with the same name in `/converted` folder in the same directory.

Thanks to [this link](https://stackoverflow.com/a/65462590).

## Installing prerequisites

1. Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install Python3

3. Create a virtualenv

```bash
python3 -m venv env
```

4. Activate the virtual environment

```bash
source env/bin/activate
```

5. Install all the requirements

To install the libeheif Python package you first need to install libheif
```bash
brew install libheif
```

This command should be able to install everything now.

```bash
pip3 install requirements.txt
```

6. Run the script

```bash
python3 convert.py
```
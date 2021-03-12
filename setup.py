from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'heic-to-jpeg-converter',
    version = '1.0.0',
    author = 'Talal Ashraf',
    author_email = 'ushruffi@gmail.com',
    license = 'MIT License',
    description = 'HEIC to JPEG Converter',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/ushruffi/heic-to-jpeg-converter',
    py_modules = ['converter'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        jpeg-converter=converter:cli
    '''
)
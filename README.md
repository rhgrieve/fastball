# fastball.py

A simple command-line tool for uploading temporary files to https://file.io

[![](https://media.giphy.com/media/1X6RHF2GZQ6Jsq7GC8/giphy.gif)](#)

## Installation

Clone the repository: 

```
git clone https://github.com/rhgrieve/fastball.git && cd fastball
```

Install with Pip

```
pip install .
```

## Usage

```
$ fastball <filename> {options}
```

## Options

**--e, --expires**: Set an expiry date for the upload

From File.io docs: 
> The query param expires must be a positive integer which, by default, represents the number of days until the file will be deleted (defaults to 14 days). If you follow it with w, it will be the number of weeks. m for months and y for years. 

**Example**

*Set expiry to 1 week*
```
$ fastball foo.pdf --e=1w
```

*Set expiry to 2 years*
```
$ fastball foo.pdf --e=2y
```

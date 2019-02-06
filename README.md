# fastball.py

A simple command-line tool for uploading temporary files to https://file.io

## Installation

Clone the repository: 

```
git clone https://github.com/rhgrieve/fastball.git
```

Install with Pip

```
cd fastball && pip install .
```

## Usage

```
$ fastball {options} <filename>
```

## Options

**--e, --expires**: Set an expiry date for the upload

From File.io docs: 
> The query param expires must be a positive integer which, by default, represents the number of days until the file will be deleted (defaults to 14 days). If you follow it with w, it will be the number of weeks. m for months and y for years. 


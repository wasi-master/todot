# dpylint

dpylint is a pylint extension for linting python code using the discord.py library

## Installation

You'll need [python](https://www.python.org) and [pylint](https://www.pylint.org) installed in order to use the extension

Currently there are two ways to install dpylint

* Installing via pip
  1. Directly installing via pip (Recommended)

     ```sh
     pip install dpylint
     ```

  2. Installing using pip and git

     ```sh
     pip install git+https://github.com/wasi-master/dpylint.git
     ```

* Cloning then installing
  1. Clone the repo

     ```sh
     git clone https://github.com/wasi-master/dpylint.git
     ```

  2. Install using pip

     ```sh
     pip install .
     ```

## Configuration

You can configure the tool in various ways, for more info see [Options](https://wasi-master.github.io/todot/config)

### **command line arguments**

There are a lot of options that can be passed to the tool, for a list of all the available options run

```sh
todot -h
```

### **.todotrc file**

You can create a new file called `.todotrc` and add your configuration inside it.

```ini
[TODOT]

# specify a file to write the output to, by default stdout
output=file
# specify a format to create the output using
format=color
# comma delimited list input of files to ignore
ignore=file1.py,file2.md
# OR
exclude=file1.py,file2.md
# comma delimited list input of extra tags to parse
tags=OPTIMIZE,MYCOOLTAG
# specify a github repository to add file hyperlinks to
repo=https://github.com/wasi-master/todot
# specify a github repository branch to add hyperlinks to, by default master
branch=main
# if used, ignores files in .gitignore
gitignore=yes
```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

* For a list of things that need to be done, see the [todo list](https://github.com/wasi-master/dpylint/blob/main/TODO.md)

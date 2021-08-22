# Options

These are the options usable, all of these should work inside `.todotrc` files unless stated otherwise, if you want to use these in the config file then change `--name value` to `name=value`\
All of these options are optional and the tool works fine without them

## `--version`

Shows the current python and todot version in the console, this does not work inside config files

## `--output [file]`

Outputs the todos to a file instead of the console

- This does not check for file extensions so make sure you specify one
- When used with some formats, the output may not be as expected
  - There are specific formats for recommended files
  - Such as `text` for `.txt` files and `markdown` or `github` for `.md` files
  - So if you are using any of those files make sure the format is correct

## `--format [default|text|color|markdown|github]`

Sets the format for the output

- Valid formats are
  - `default`: The default style, prints to the console
  - `text`: The default style, prints to a text file provided by the --output option
  - `color`: The default style, but colorized that looks beautiful in the terminal
  - `markdown`: Markdown style, prints to a markdown file
  - `github`: GitHub flavoured markdown style, prints to a markdown file

## `--configfile [file]`

Sets the config file to read the configuration from, this can not be set inside the config file

- The file needs to be a valid file in a `.ini` like format

## `--ignore file1,file2`, `--exclude file1,file2`

Ignores the specified files

- The files need to be valid and separated by commas

## `--gitignore`

Ignores all files in `.gitignore`

- The `.gitignore` file needs to valid ([docs](https://git-scm.com/docs/gitignore#_pattern_format))

## `--tags tag1,tag2`

Also parses the specified [tags](https://en.wikipedia.org/wiki/Comment_(computer_programming)#Tags)

- The [tags](https://en.wikipedia.org/wiki/Comment_(computer_programming)#Tags) must not already exist

## `--repo repository_url`

Use to hyperlink lines where the todos were found

- Only works if format is set to `github`

## `--branch repository_branch`

Use to hyperlink lines where the todos were found, by default master

- Only works if format is set to `github`

# Simple Morse Code Converter

## Core Features

- Simple Conversion from a string to morse code

## Additional Features

- Backwards support (Morse code to string)
- Supporting [Pro-signs](https://en.wikipedia.org/wiki/Prosigns_for_Morse_code)
- I/O to file
    - Read line by line and output to given file
- Different versions
    - User input / interactive
    - Command Line Argument input to immediate translate (look at argv)
- Other ideas

## Morse Code Table

[Online Table](https://modernout.com/pages/morse-code-chart)

## Running

`python3 morse.py`

### Command Line Arguments

`python3 morse.py` : interactive mode

`python3 morse.py -t "<text to translate>"` : instant translation

`python3 morse.py -i "<input file>"` : translate from an input file, auto outputs to `output.txt`

`python3 morse.py -i "<input file>" -o "<output file>"`: translate from an input file to a specified output file

# Assembler with python
 converts assembly source code to machine code

## Requirements
* Python 3 🐍

## Usage
```
python main.py [source] [output]
```
* `[source]` : Path to assembely source file. (REQUIRED)
* `[output]` : Path to store program output file. i.e. binary code. If not specified, uses "binary.txt" as output file name(OPTINAL)

### example
```
python main.py c:\asm.txt
```
```
python main.py c:\asm.txt c:\binary.txt
```
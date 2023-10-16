# Assembler with python
 converts assembly source code to machine code

## Requirements
* Python 3 🐍

## Usage
```
python main.py [source] [output]
```
* `[source]` : Path to assembly source file. (REQUIRED)
* `[output]` : Path to store program output file. i.e. binary code. If not specified, uses "binary.txt" as output file name (OPTINAL)

### Example
```
python main.py c:\asm.txt
```
```
python main.py c:\asm.txt c:\binary.txt
```
input
```asm
ORG 100 /this is start
LDA SUB
CMA
INC
inc
ADD MIN
STA DIF
HLT
MIN,DEC 83
SUB,DEC -23
DIF,HEX 0
END
```
output
```
1000 0000 0	    0010 0001 0000 1000
1000 0000 1	    0111 0010 0000 0000
1000 0001 0	    0111 0000 0010 0000
1000 0001 1	    0111 0000 0010 0000
1000 0010 0	    0001 0001 0000 0111
1000 0010 1	    0011 0001 0000 1001
1000 0011 0	    0111 0000 0000 0001
1000 0011 1	    0000 0000 0101 0011
1000 0100 0	    1000 0000 0001 0111
1000 0100 1	    0000 0000 0000 0000
```

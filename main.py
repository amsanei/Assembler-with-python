import sys
import re

def get_asm_file():
    if len(sys.argv) > 1:
        asm_file = sys.argv[1]
    else:
        print('\aPlease specify a Assembely source code.')
        exit(0)
    
    return asm_file

def get_label(line):
    if ',' in line:
        return line.split(',')[0]
    return None

def get_ORG_value(line):
    if line.startswith('ORG'):
        split = line.split(' ')
        return int(split[1])
    return None

def is_END(line):
    if line.startswith('END'):
        return True
    return False

def is_pseudo(line):
    for i in table_pseudo:
        if i in line:
            return True
    return False

def is_DEC(line):
    return 'DEC' in line

def get_DEC_value(line):
    return int(line.split(' ')[1])

def is_HEX(line):
    return 'HEX' in line

def get_HEX_value(line):
    return int(line.split(' ')[1])

def dec_to_bin(num):
    num = str(num)
    return pertty_formating("{0:016b}".format(int(num, 10)).replace("-", "1"))
    
def hex_to_bin(num):
    num = str(num)
    return pertty_formating("{0:016b}".format(int(num, 16)))

def is_MRI(line):
    for i in table_MRI:
        if i in line:
            return True
    return False

def is_none_MRI(line):
    for i in table_none_MRI:
        if i in line:
            return True
    return False

def pertty_formating(num):
    # adds space after every 4 character
    return ' '.join([num[i:i+4] for i in range(0,len(num),4)])

def comment_cleaner(code):
    # cleans all the comments in asembely code
    return re.sub("\/(.*)", "", code).strip()
                

table_pseudo = ['ORG','HEX','END','DEC']

table_MRI = {
    'AND' : '0',
    'ADD' : '1',
    'LDA' : '2',
    'STA' : '3',
    'BUN' : '4',
    'BSA' : '5',
    'ISZ' : '6'
}

table_none_MRI = {
    'CLA' : '7800',
    'CLE' : '7400',
    'CMA' : '7200',
    'CME' : '7100',
    'CIR' : '7080',
    'CIL' : '7040',
    'INC' : '7020',
    'SPA' : '7010',
    'SNA' : '7008',
    'SZA' : '7004',
    'SZE' : '7002',
    'HLT' : '7001',
    'INP' : 'F800',
    'OUT' : 'F400',
    'SKI' : 'F200',
    'SKO' : 'F100',
    'ION' : 'F080',
    'IOF' : 'F040'
}

table_symbol_address_16 = {}
table_result = {}

asm_file_path = get_asm_file()

code = open(asm_file_path, 'r').read()
code = comment_cleaner(code)
code = code.upper()
lines = code.split('\n')

#Pass 1 is start here 
LC = 0
i = 0
for i in range(len(lines)):
    label = get_label(lines[i])
    if label:
        table_symbol_address_16[label] = LC
        LC += 1
    else:
        ORG_value = get_ORG_value(lines[i])
        if ORG_value:
            LC = ORG_value
        elif is_END(lines[i]):
            break
        else:
            LC += 1


#Pass 2 is start here 
LC = 0
i = 0
for i in range(len(lines)):
    if is_pseudo(lines[i]):
        ORG_value = get_ORG_value(lines[i])
        if ORG_value:
            LC = ORG_value
        elif is_END(lines[i]):
            break
        elif is_DEC(lines[i]):
            DEC_value = get_DEC_value(lines[i])
            table_result[LC] = dec_to_bin(DEC_value)
            LC += 1
        elif is_HEX(lines[i]):
            HEX_value = get_HEX_value(lines[i])
            table_result[LC] = hex_to_bin(HEX_value)
            LC += 1

    elif is_MRI(lines[i]):
        commend = lines[i].split(' ')
        symbol = commend[0]
        symbol_code = hex_to_bin(table_MRI[symbol])
        operand = commend[1]
        operand_code = hex_to_bin(table_symbol_address_16[operand])
        result = '0'
        I = 0

        if len(commend) == 3:
            I = 1
            result[0] = '1'

        result = result + symbol_code[-3:] + operand_code[4:]
        table_result[LC] = result
        LC += 1

    elif is_none_MRI(lines[i]):
        symbol = lines[i].split(' ')[0]
        table_result[LC] = hex_to_bin(table_none_MRI[symbol])
        LC += 1
    
    else:
        print("\ainvalid syntax at line", i)
        LC += 1


with open('binary.txt', 'w') as file:
    for key, value in table_result.items():
        key = pertty_formating("{0:b}".format(int(str(key), 16)))
        file.write(key + '\t' + value + '\n')

if input('your file is ready, do you want me to open it?(y/n)') == 'y':
    print()
    bin_file = open('binary.txt', 'r').read()
    print(bin_file)
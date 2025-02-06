"""CS-77 Spring Lab 1
    Group 6 members: Louis Nguyen, Thuan Thanh Lam, Ian Ramin
    The purpose of this program is to take an value(String) in the format of either Binary or Decimal(specified), value check, and then translate it to the other 3 formats
    
"""

def isValid(value: str, type: str):
    
    
    #Decimal is 0-9, Bin is 0-1
    if type not in "BD":
        return False
    if type == "D":
        for i in value:
            if i not in "0123456789.":
                return False
    elif type == "B":
        for i in value:
            if i not in "01.":
                return False
    else:
        return True
    return True       

DECHEXTABLE = {
    '10' : 'A',
    '11' : 'B',
    '12' : 'C',
    '13' : 'D',
    '14' : 'E',
    '15' : 'F',
}

HEXBINTABLE = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

BINOCTTABLE = {
    '000' :'0',
    '001':'1',
    '010':'2', 
    '011':'3',
    '100':'4',
    '101':'5',
    '110':'6',
    '111':'7'
}

def useHexTable(value: int, HEXVALUE):
    #idk why i worded it like this
    result = value%HEXVALUE
    if result > 9:
        return DECHEXTABLE.get(str(result))
    else:
        return str(result)

def removeLeadAndTrailZeroes(value: str)->str:
    return value.strip("0")    

def dexToHexInteger(value: str)-> str:
    HEXVALUE = 16
    quotient = int(value)
    remainder = ""
    while quotient != 0:
        remainder = useHexTable(quotient, HEXVALUE) + remainder
        quotient//=HEXVALUE
    return remainder
    
 
def dexToHexFractional(value: str)-> str:
     #need to convert to decimal as it enters as just a string of numbers
     #I am going to decide to use precision to 4 numbers
    HEXVALUE = 16
    value = toFraction(value)
    sep = ""
    for i in range(4):
        result = value * HEXVALUE
        sep += useHexTable((int(result//1)), HEXVALUE)
        value = result - result//1
    return str(sep)
 
def toFraction(value: str)-> int:
    length = len(value)*-1
    value = (int(value)*pow(10, length))
    return value
     
    
def decToHex(value: str)-> str:
    #Seperate based on "."
    integerValue, fractionalValue = value.split(".")
    result = dexToHexInteger(integerValue) + "." + dexToHexFractional(fractionalValue)
    return result
    
  
def decToBin(value: str)-> str:
    #Assuming unsigned numbers. We can add sign functionality later might be good to add a subroutine to convert to hex then to binary using a hashmap
    #We already have the hex representation, just split and use a map(?)
    integerAsHex, fractionalAsHex = value.split(".")
    
    result = ""
    for i in integerAsHex:
        result += HEXBINTABLE.get(i)
    result += "."
    for i in fractionalAsHex:
        result += HEXBINTABLE.get(i)
    return removeLeadAndTrailZeroes(result)


    
def binToDec(value: str)-> str:
    pass

def binToHex(value: str)-> str:
    #Translate Hex/Bin table
    pass

def zeroesToAdd(value: int, power: int)-> int:
    return value*(power-1)%power

def binToOct(value: str)-> str:
    #Translate Oct/Bin table
    #How do i get it to be the right size? 
    #8 is 2^3
    OCTALPOWER = 3
    integerAsBin, fractionAsBin = value.split(".")
    integerZeroesToAdd = zeroesToAdd(len(integerAsBin), OCTALPOWER)
    fractionZeroesToAdd = zeroesToAdd(len(fractionAsBin), OCTALPOWER)
    integerAsBin = '0' * integerZeroesToAdd + integerAsBin
    fractionAsBin += '0' * fractionZeroesToAdd
    #We should add a trimming function to make sure it looks nice
    #Section it into 3s 
    #Turn this into functions to look neat
    integerAsBin = [integerAsBin[i:i+3] for i in range(0, len(integerAsBin), 3)]
    result = ""
    for i in integerAsBin:
        result += BINOCTTABLE.get(i)
    result += "."
    fractionAsBin = [fractionAsBin[i:i+3] for i in range(0,len(fractionAsBin), 3)]
    for i in fractionAsBin:
        result += BINOCTTABLE.get(i)
    return removeLeadAndTrailZeroes(result)

def main():
    """"
    The logic in here will be to take a String value, ask which form it is in(Decimal/Binary), error check, and translate to the other three formats
    If not in the right format, add 0s until it is. 
    """""
    while True:
        valid = False
        while valid == False:
            value = input("Please enter a string: ")
            valueType = input("Please specify [D]ecimal or [B]inary: ").upper() #Do we need to add error checking for here?
            print("Checking for validity")
            valid = isValid(value, valueType)
            #Give it a period just to make sure
            if "." not in value:
                value+=".0"
            if not valid:
                print("Not valid input. Try again")
            else:
                print("Valid value")
        
        if valueType == "D":
        #The Decimal -> BHO flow goes here. We want to use Dec to Hex then the other functions(?). Hex to Bin. Bin to Oct using a map(?). Try to reuse functions
            hex = decToHex(value)
            print("Hexadecimal number: " + hex)
            bin = decToBin(hex)
            print("Binary number: " + bin)
            oct = binToOct(bin)
            print("Octal number: " + oct)
        else:
        #The Binary -> DHO flow goes here
            print("Decimal number: " + binToDec(value))
            print("Hexadecimal number: " + binToHex(value))
            print("Octal number: " + binToOct(value))
        
        #Ask for a loop
        repeat = input("Do you want to continue? Y/N: ").upper()
        if repeat == "N":
            break


main()
    
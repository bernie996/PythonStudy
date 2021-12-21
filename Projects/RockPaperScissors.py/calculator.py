import os
import math
def clear(): return os.system('cls')
dictionarySelector = {
    '+': lambda x,y : x + y,
    '-': lambda x,y : x - y,
    '*': lambda x,y : x * y,
    '/': lambda x,y : x / y if y != 0 else '∞',
}
def inputNum():
    num = input('\n');
    while (num.isnumeric() == False):
        print('Invalid input.');
        num = input('Please try again!\n');
    return int(num);

def inputOp():
    operation = input('Please, select one of the operations:\n(1) +\n(2) - \n(3) *\n(4) / \n');
    while not (operation.isnumeric() and int(operation) in list(range(1,5) ) ):
        operation = input('Please, select one of the operations:\n(1) +\n(2) - \n(3) *\n(4) / \n');
    return int(operation);

def calculador(lastResult):
    if lastResult == '':
        print('What is the first number?\n');
        num1 = inputNum();
    else:
        num1 = lastResult;
    clear();
    operator = inputOp();
    clear();
    print('What is the second number?\n');
    num2 = inputNum();
    clear();
    if (num2 == 0 and operator == 4 ):
        print('Error, division by zero!');
        return 0;
    result = dictionarySelector[list(dictionarySelector.keys())[operator-1]](int(num1),int(num2));
    print(f'{num1} {list(dictionarySelector.keys())[operator-1]} {num2} = {result}');
    return result;

def programa():
    print('Hello, good afternoon!');
    respuesta = 1;
    result = '';
    while respuesta == 1:
        result = calculador(result);be
        respuesta = int(input('Do you want to keep calculating?\n(1) Yes \n(2) No\n'))
        clear();
    print(f'The final result is {result}. Thank you!')
programa();
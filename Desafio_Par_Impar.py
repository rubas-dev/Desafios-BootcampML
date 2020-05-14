
def integerValue(value):
    return type(value) == int

def pairValue(value):
    return value % 2 == 0


def printPairValue(value, Epair):
    print(f'{value} é um valor { "par" if Epair else "impar"} ! ')

def notIntegerValue():
    print('Valor inserido não é um inteiro')


def main():
    try:
        value = int(input('Digite um valor: '))
        if integerValue(value):
            printPairValue(value, pairValue(value)) 
        else:
           notIntegerValue()
    except:
       notIntegerValue()



if __name__ == "__main__":
    main()

def invertendo(num):
    ordem = 0
    while num > 0:
        ordem = ordem*10 + (num%10)
        num = num//10
    return ordem



def main():
    numero = int(input(" "))

    inv = invertendo(numero)
    print(f'{inv}')
    

if __name__ == '__main__':
    main()
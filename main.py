#Define Function Decimal Entry
def dec(n):
    binary = []
    number = n
    while(number != 0):
         binary.insert(0, number % 2)
         number = number // 2
    oct = []
    m, n = len(binary)+3, len(binary)
    while (n != 0):
        m, n = n, n-3
        if n < 0:
            n = 0
        x = binary[n:m]
        x.reverse()
        if len(x) < 3:
            x.append(0)
            if len(x) < 3:
                x.append(0)
        x = x[0] * 1 + x[1] * 2 + x[2] * 4
        oct.insert(0,x)
    hex = []
    m, n = len(binary)+4, len(binary)
    while (n != 0):
        m, n = n, n-4
        if n < 0:
            n = 0
        x = binary[n:m]
        x.reverse()
        while(len(x) < 4):
            x.append(0)
        x = x[0] * 1 + x[1] * 2 + x[2] * 4 + x[3] * 8
        hex.insert(0,x)
        if hex[0] == 10:
            hex[0] = "A"
        elif hex[0] == 11:
            hex[0] = "B"
        elif hex[0] == 12:
            hex[0] = "C"
        elif hex[0] == 13:
            hex[0] = "D"
        elif hex[0] == 14:
            hex[0] = "E"
        elif hex[0] == 15:
            hex[0] = "F"
    print("Binario: ", *binary, sep="")
    print("Octal: ", *oct, sep="")
    print("Hexadecimal: ", *hex, sep="")

#Define Function Binary Entry
def bin(n):
    binary = [int(x) for x in str(n)]
    bin = [int(x) for x in str(n)]
    bin.reverse()
    m = 0
    dec = 0
    for n in bin:
        dec = dec + n*(2**m)
        m = m+1
    oct = []
    m, n = len(binary)+3, len(binary)
    while (n != 0):
        m, n = n, n-3
        if n < 0:
            n = 0
        x = binary[n:m]
        x.reverse()
        if len(x) < 3:
            x.append(0)
            if len(x) < 3:
                x.append(0)
        x = x[0] * 1 + x[1] * 2 + x[2] * 4
        oct.insert(0,x)
    hex = []
    m, n = len(binary)+4, len(binary)
    while (n != 0):
        m, n = n, n-4
        if n < 0:
            n = 0
        x = binary[n:m]
        x.reverse()
        while(len(x) < 4):
            x.append(0)
        x = x[0] * 1 + x[1] * 2 + x[2] * 4 + x[3] * 8
        hex.insert(0,x)
        if hex[0] == 10:
            hex[0] = "A"
        elif hex[0] == 11:
            hex[0] = "B"
        elif hex[0] == 12:
            hex[0] = "C"
        elif hex[0] == 13:
            hex[0] = "D"
        elif hex[0] == 14:
            hex[0] = "E"
        elif hex[0] == 15:
            hex[0] = "F"
    print("Decimal:", dec)
    print("Octal: ", *oct, sep="")
    print("Hexadecimal: ", *hex, sep="")

#Define Function Octal Entry
def oct(n):
    octal = [int(x) for x in str(n)]
    octal.reverse()
    dec = 0
    m = 0
    for n in octal:
        dec = dec + n*(8**m)
        m = m+1
    binary = []
    number = dec
    while(number != 0):
         binary.insert(0, number % 2)
         number = number // 2
    hex = []
    m, n = len(binary)+4, len(binary)
    while (n != 0):
        m, n = n, n-4
        if n < 0:
            n = 0
        x = binary[n:m]
        x.reverse()
        while(len(x) < 4):
            x.append(0)
        x = x[0] * 1 + x[1] * 2 + x[2] * 4 + x[3] * 8
        hex.insert(0,x)
        if hex[0] == 10:
            hex[0] = "A"
        elif hex[0] == 11:
            hex[0] = "B"
        elif hex[0] == 12:
            hex[0] = "C"
        elif hex[0] == 13:
            hex[0] = "D"
        elif hex[0] == 14:
            hex[0] = "E"
        elif hex[0] == 15:
            hex[0] = "F"
    print("Decimal:", dec)
    print("Binario: ", *binary, sep="")
    print("Hexadecimal: ", *hex, sep="")

#Define Function Hexadecimal Entry
def hex(n):
    hexadec = list(n)
    hex = []
    for x in hexadec:
        if x == "A":
            x = 10
        elif x == "B":
            x = 11
        elif x == "C":
            x = 12
        elif x == "D":
            x = 13
        elif x == "E":
            x = 14
        elif x == "F":
            x = 15
        x = int(x)
        hex.insert(0, x)
    dec = 0
    m = 0
    for n in hex:
        dec = dec + n * (16**m)
        m = m + 1
    binary = []
    number = dec
    while(number != 0):
         binary.insert(0, number % 2)
         number = number // 2
    oct = []
    m, n = len(binary)+3, len(binary)
    while (n != 0):
        m, n = n, n-3
        if n < 0:
            n = 0
        x = binary[n:m]
        x.reverse()
        if len(x) < 3:
            x.append(0)
            if len(x) < 3:
                x.append(0)
        x = x[0] * 1 + x[1] * 2 + x[2] * 4
        oct.insert(0,x)
    print("Decimal: ", dec)
    print("Binario: ", *binary, sep="")
    print("Octal: ", *oct, sep="")

#Say Welcome
print("Bem vindo(a) conversora de bases computacionais do Will!")
print("Selecione sua base:\n10 para decimal\n2 para binario\n8 para octal\ne 16 para hexadecimal")
base = int(input())
if base == 10:
    print("Base: decimal.")
    n = int(input("Insira o valor: "))
    dec(n)
elif base == 2:
    print("Base: binario.")
    n = int(input("Insira o valor: "))
    bin(n)
elif base == 8:
    print("Base: octal.")
    n = int(input("Insira o valor: "))
    oct(n)
elif base == 16:
    print("Base: hexadecimal.")
    n = str(input("Insira o valor: "))
    hex(n)
else:
    print("Base invalida.")
input()

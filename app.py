nb1 = input("Entrez nombre 1 : ")
nb2 = input("Entrez nombre 2 : ")
op = input("Entrez un opérateur : ")

def calc():
    try:
        if op == '+':
            res = int(nb1) + int(nb2)
        elif op == '-':
            res = int(nb1) - int(nb2)
        elif op == '*':
            res = int(nb1) * int(nb2)
        elif op == '/':
            res = int(nb1) / int(nb2)
        return res
    except ValueError:
        print("FF")
        res = "FF"
        return res

print(calc())
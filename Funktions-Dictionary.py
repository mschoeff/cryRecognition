def add(var1, var2):
    print(var1 + var2)
    return

def sub(var1, var2):
    print(var1 - var2)
    return

def mult(var1, var2):
    print(var1 * var2)
    return

def div(var1, var2):
    print(var1 / var2)
    return

functionDictionary = {
    "Addiere": add,
    "Subtrahiere": sub,
    "Multipliziere": mult,
    "Dividiere": div,

}

def main():
    functionDictionary["Addiere"](1, 2)
    functionDictionary["Subtrahiere"](10, 2)
    functionDictionary["Multipliziere"](2, 2)
    functionDictionary["Dividiere"](10, 5)

main()
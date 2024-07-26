def sum(a,b):
    resultat = a + b
    return(resultat)

def substract(a,b):
    resultat = a - b
    return(resultat)

def multiply(a,b):
    resultat = a * b
    return(resultat)

def divide(a,b):
    if b != 0:
        resultat = a / b
        return(resultat)
    else:
        print("ERROR-01 : You can't divide by 0.")
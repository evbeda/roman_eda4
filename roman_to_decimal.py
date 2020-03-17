
def roman_to_decimal(roman):
    result=0
    romano_valor = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

    result = romano_valor[roman[0]]

    import pdb;
    pdb.set_trace()

    for i in range(1, len(roman)):
        if romano_valor[roman[i]] < romano_valor[roman[i-1]]:
            result -= romano_valor[roman[i-1]]
        else:
            result += romano_valor[roman[i-1]]



    return result

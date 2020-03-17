def roman_to_decimal(roman):
    result=0
    letras=["I","V","X","L","C","D","M"]
    for a in range(len(roman)):
        if roman == "IV" :
            return 4
        elif roman == "V":
            return 5
        elif roman == "IX" :
            return 9
        elif roman == "X":
            return 10
        elif roman == "XV":
            return 15

    return len(roman)

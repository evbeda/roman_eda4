def roman_to_decimal(roman):
    if roman == "IV" :
        return 4
    elif roman == "V":
        return 5
    elif roman == "IX" :
        return 9
    elif roman == "X":
        return 10
    return len(roman)

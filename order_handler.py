def number_to_ordinal(number):
    if number % 100 in [11, 12, 13]:
        return str(number) + "th"
    elif number % 10 == 1:
        return str(number) + "st" 
    elif number % 10 == 2:
        return str(number) + "nd"
    elif number % 10 == 3:
        return str(number) + "rd"
    else:
        return str(number) + "th"

if __name__ == "__main__":
    for i in range(10, 22):
        print(number_to_ordinal(i))



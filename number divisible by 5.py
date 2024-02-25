def divisible_by_5(number):

    while number != "ok":
        if number % 5 == 0 or number % 10 == 5:
            return True
        else:
            return False


while True:
    input_value = input("Enter the number to check if it's dividible by 5: or 'ok'for stop. ")
    if input_value.lower() == "ok":
       print("Exiting the program.")
       break

    if input_value.isdigit():
        number = int(input_value)

        if divisible_by_5(number):
            print(f"{input_value} is divisible by 5.")
        else:
            print(f"{input_value} is not divisible by 5.")
    else:
        print("Enter the valid keyword or 'ok' to exit.")
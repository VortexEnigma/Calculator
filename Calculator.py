# Python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Important note: Converting it to int or float is important otherwise the program will handle the input as str


if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)


# Note: If round function is placed in front of result we can get int as result
# print(round(result))
# OR if we want three(or more/less) decimal places we can modify it as: print (round(result, 3))

elif operator not in ["+", "-", "*", "/"]:
    print(f"{operator} is not a valid operator")

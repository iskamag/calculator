num1 = float(input("enter a number\n"))
num2 = float(input("enter another number\n"))
op = input("enter an operator\nadd with +\nsubtract with -\n multiply with *\n divide with /\n you can also do this by typing the operator name")
if op == "+" or op == "add" or op == "addition":
    print(num1 + num2)
if op == "-" or op == "subtract" or op == "subtraction":
        print(num1 - num2)
if op == "*" or op == "multiply" or op == "multiplication":
    print(num1 * num2)
if op == "/" or op == "division" or op == "divide":
    print(num1 / num2)
if op == "%":
    print(num1 % num2)
if op == "^" or op == "power" or op == "square":
    print(pow(num1, num2))
else:
    print("sorry, the operator is invalid. please check your grammar")

# calculator project
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))


def multiply(n1, n2):
    return n1 * n2

def subract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def add(n1, n2):
    return n1 + n2

def choice():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("which perform do you want to do?: ")
    if choice == '1' :
        print(add(n1,n2))
    elif choice == '2':
        print(subract(n1,n2))
    elif choice == '3':
        print((multiply(n1,n2)))
    elif choice == '4':
        print(divide(n1,n2))
    else:
        print("number is not given")
choice()
while True:
    user = input("do you want to proceed further?: ('yes/no')")
    if user == "yes":
        N2 = int(input("Enter the number: "))
        n2 = N2
        choice()
    else:
        print("number is not coorect")
        break

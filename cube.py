"""check = False;
while check == False:
    try:
        number = int(input("How long is a side of the cube?"))
        if number < 0:
            print("Please enter a positive number.")
            check = False;
        else :
            check = True;
            break;
    except ValueError:
        print("Please enter an integer")
        continue

number *= (number * number)

print("The volume of the cube is", number)
"""
def vol(x):
    if x < 0:
        print("Error: value has to be a positive number.")
        return -1
    return (x*x*x)

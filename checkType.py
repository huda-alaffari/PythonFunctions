num = int(input("=>"))
def check_type(number):
    if(number%2 == 0):
        return "Even"
    else:
        return"Odd"
n = check_type(num)
print(n)
num = int(input("Enter Number"))
def is_palindrome(x):
    number = str(x)
    
    return number == number[::-1]

result = is_palindrome(num)
print(result)  

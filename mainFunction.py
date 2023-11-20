def main():
    result= sum_num(1,4,3)
    print(result)
    
def sum_num(*args):
    sum1=0
    for n in args:
        sum1+=n
    return sum1

# result= sum_num(1,4,3)
# print (result)
# 
# result= sum_num(1,4)
# print (result)
# 
# result= sum_num(1,4,3,11)
# print (result)

main()

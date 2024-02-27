#function
#Date:26/02/2024
#Name:Angie

factorial_num=1
max_val=int(input("enter the max value:"))
for x in range(1,max_val + 1):
    factorial_num=factorial_num * x
    print("sum of the numbers:",factorial_num)
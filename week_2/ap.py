#This is a programme used to calculate the sum in an arithmetic progression
#Date:21/02/2024
#Name:Angela

a=int(input("Enter the first term in the series:"))
n=int(input("Enter the number of terms:"))
d=int(input("Enter the common difference of the series:"))
n_1=int(n/2)
a_1=int(2*a)
t=(n_1*(a_1+(n-1)*d))
print("The sum of ap is equal to:",t)


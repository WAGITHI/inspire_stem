#this is a programme used to compute earnings of an employee ina company
#26/02/2024
#Angie

salary=120000
if salary > 100000:
        salary_2=salary * 1.3
        print("New salary is:", salary_2)
elif salary >=150000 and salary<=300000:
        salary_3=salary * 1.5
        print("New salary is:", salary_3)
else:
        salary_4=salary * 0.05
        print("New salary is:", salary_4)
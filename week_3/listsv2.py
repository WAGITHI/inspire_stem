#stuff about lists
#28/02/2024
#Wagithi Angela

friends=["Karen","Sky","Stacy","Evelyn","Matilda"]
for friend in friends:
    print(friend)

enemies=friends[:]     #copy one list into another
print(enemies)

#slicing a list
fruits=["apple","banana","avocado","peaches","passion"]
print(fruits[0:3])
del fruits[0]  #deletes items from the list
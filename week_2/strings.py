#strings in python
#22/02/2024
#Angela Wagithi

city="Nairobi"
#convert to upper case

print(city)
print("\n")
print(city.upper())  #converts to upper case

name="ANGELA"
print(name)
print("\n")
print(name.lower()) #converts to lower case

town="  Juja   "
print(town)
print("\t") #new tab
print(town.strip())

first_name="Olive"
second_name="Waithera"
full_name=first_name + second_name
print(full_name)
#designaing specific characters
subject="chemistry"
print(subject[0])
print(subject[1])
print(subject[2])
print(subject[3])
print(subject[4])
print(subject[5])
print(subject[6])
print(subject[7])
print(subject[8])
print(subject[-1])
print(subject[-2])

word="madam"
print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
#write a programme to reverse a string

#replacing characters in a string
fruit="apple"
print(fruit.replace('a','b'))

artist="21,savage"
print(artist.split(","))

age=18
height=1.2
print("I am {0} years old and {1} metres tall".format(age)(height))

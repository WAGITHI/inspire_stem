#creating descriptions of stuff,deletng elements,changing elements within a description
#28/02/2024
#Angie

cat={"gender":"girl cat","breed":"ragdoll","fur type":"fluffy","weight":"2.5kgs","name":"Queen"}
cat["gender"]="boy cat" 
cat["breed"]="Calico"
cat_2=cat.copy()
print(cat_2)
print(cat)
print(cat["breed"])
print(cat["weight"])
print(cat["name"])

#for key,value in my_cat.items():
    #print(key)
    #print(value)
#del cat ('weight')
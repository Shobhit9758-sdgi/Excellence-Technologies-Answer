def MaxVAlue(dict1):
    
    # taking dict2 bacause i need max value and key in dictionary.
    dict2={}
    #logic
    key_max = max(dict1.keys(), key=(lambda k: dict1[k]))

    dict2.update({key_max:dict1[key_max]})
    return(dict2)




# create a dictionary
dict1={1 : 50,2 : 60 ,3 : 70} #it should have any no of keys and pair

# function 
print(MaxVAlue(dict1))





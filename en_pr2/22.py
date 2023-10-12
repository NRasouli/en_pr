def dictionary(key):
    dict={"Name":"Narges","LastName":"Rasouli","Father":"Abolqhasem"}
    print(dict)
    if key != None:
        dict.pop(key)
        print("after remove:\n"+str(dict))
dictionary("Father")

def planetList(i):
    pList=["Mercury","Venus","Earth","Mars","Jupiter","Saturn"]
    print("\n"+str(pList))
    if i != None:
        pList.pop(i)
        print("after remove:\n"+str(pList))
planetList(1)

def animalTuple():
    animalT=("Lion","Snake","Raven","Lizard","Turtle","Tiger")
    print("\n"+str(animalT))
    #Tuples are unchangeable, so you cannot remove items from it but you can convert the tuple
    #into a list, change the list, and convert the list back into a tuple.
    #if I do that it be like the second function, except two line of codes to convert the tupple into list and back.
animalTuple()
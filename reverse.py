def reversing(mysentence):
    mysentence = mysentence.split()
    mysentence.reverse()
    mysentence = " ".join(mysentence)
    return mysentence 

print(reversing("my name is ömer"))
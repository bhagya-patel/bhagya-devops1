#nested dictionary
student = {
    "name" : "bhagya patel",
    "subjects" : {
        "phy" : 79,
        "chem" : 51,
        "maths" : 89
    }
}
print(student.keys())
print(list(student.keys()))


print(len(student)) #it's value is same as below syntax
print(len(list(student.keys())))

print(student.values())

print(student.items())  #output is in touple form
print(student)
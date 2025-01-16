#nested dictionary
student = {
    "name" : "bhagya patel",
    "subjects" : {
        "phy" : 79,
        "chem" : 51,
        "maths" : 89
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])
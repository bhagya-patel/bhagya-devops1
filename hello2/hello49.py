student = {
    "name" : "bhagya patel",
    "subjects" : {
        "phy" : 79,
        "chem" : 51,
        "maths" : 89
    }
}

print(student["name"])
print(student.get("name"))


# print(student["name2"]) #error
print(student.get("name2"))  #no error -->None

 
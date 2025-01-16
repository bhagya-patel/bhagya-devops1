student = {
    "name" : "bhagya patel",
    "subjects" : {
        "phy" : 79,
        "chem" : 51,
        "maths" : 89
    }
}

# student["city"] = "delhi"
# print(student)

# student.update({"city" : "delhi"})
# print(student)

new_dict = {"city" : "delhi"}
student.update(new_dict)
print(student)

 
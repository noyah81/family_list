import json
# dictionaries
p1 = {"name": "Noya", "age":"16", "city":"San Diego", "Food": "salad"}
p2 = {"name": "Sarah", "age":"4", "city":"Fresno", "Food": "cherry"}
p3 = {"name": "Tom", "age":"43", "city":"Venice", "Food": "pizza"}
p4 = {"name": "Jerry", "age":"7", "city":"Orlando", "Food": "burger"}
p5 = {"name": "Kim", "age": "5", "city": "Miami", "Food": "banana"}

# list of dictionaries
list_of_family = [p1, p2, p3, p4,p5]

# write some code to Print List of people one by one
print("List of people")
print(type(list_of_family))
print(list_of_family)
print()

# turn list to dictionary of people in a family
family = {'family': list_of_family}
print("Dictionary of members")
List = family["family"]
for member in List:
    print("age" + ": " + member["age"] + " ,name" + ": " + member["name"] + " ,city" + ": " + member["city"]+ " ,food" + ": " + member["Food"]  )
    #print(members["name"] + " , " + members["age"]+ " , " + members["city"]+ " , " + members["Food"])

# turn dictionary to JSON (aka string)
json_people = json.dumps(list_of_family)
print("Dictionary to JSON")
for char in json_people:
    print(char, end="+")
# turn dictionary to JSON, this can be sent via a browser
# unwind JSON using json.loads and print the people
print("JSON to Python")
PythonList = {"family": json.loads(json_people)}
NewList = {"people":[PythonList["family"][3],PythonList["family"][4]], "Parents":[PythonList["family"][1],PythonList["family"][2]]}
print(NewList)
for people in PythonList["family"]:
    print(people['name'] + "," + str(people['age']) + "," + people['city'])



# 1. What is JSON?
# JSON stands for JavaScript Object Notation.

# JSON is a format used to store and exchange data between applications.

# For example:
# - React frontend sends data to a Python Flask backend.
# - Python backend sends data to a React frontend.
# - APIs exchange data using JSON.
# - Applications store configuration and user information in JSON files.
# Example of JSON data:
# {
#     "name": "Chandan",
#     "age": 25,
#     "skills": ["Python", "React", "JavaScript"],
#     "is_active": true
# }


# This is JSON format, not Python dictionary syntax.



# ===================================================


# 2. Python Dictionary vs JSON
# They look similar, but they are different.

# Python dictionary:
# student = {    "name": "Chandan",    "age": 25,    "is_active": True,    "marks": None}



# JSON:
# {
#     "name": "Chandan",
#     "age": 25,
#     "is_active": true,
#     "marks": null
# }


# 4. Example 1: Python Dictionary to JSON (dumps)

import json

student = {
    "name": "Chandan",
    "age": 25,
    "city": "Goa"
}

result = json.dumps(student)

print(result)
print(type(result))


# 5. Example 2: JSON to Python Dictionary (loads)


import json

data = '{"name": "Chandan", "age": 25, "city": "Goa"}'

result = json.loads(data)

print(result)
print(type(result))
print(result["name"])
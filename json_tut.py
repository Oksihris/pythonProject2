import json
from json import JSONEncoder

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

person_json = json.dumps(person)
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

print(person_json) 
print(person_json2) 

# with open('person.json', 'w') as f:
#     json.dump(person, f)


person1_json = """
{
    "age": 30, 
    "city": "New York",
    "hasChildren": false, 
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""
person = json.loads(person1_json)
print(person)

with open('person.json', 'r') as f:
    person = json.load(f)
    print(person)


class User:
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends
        
class Player:
    def __init__(self, name, nickname, level):
        self.name = name
        self.nickname = nickname
        self.level = level
          
            
def encode_obj(obj):

    obj_dict = {
      "__class__": obj.__class__.__name__,
      "__module__": obj.__module__
    }

    obj_dict.update(obj.__dict__)
  
    return obj_dict


def decode_dct(dct):

    if "__class__" in dct:
        class_name = dct.pop("__class__")
        
        module_name = dct.pop("__module__")
        
        module = __import__(module_name)
        
        class_ = getattr(module,class_name)
        obj = class_(**dct)
    else:
        obj = dct
    return obj

user = User(name = "John",age = 28, friends = ["Jane", "Tom"], balance = 20.70, active = True)

userJSON = json.dumps(user,default=encode_obj,indent=4, sort_keys=True)
print(userJSON)

user_decoded = json.loads(userJSON, object_hook=decode_dct)
print(type(user_decoded))

player = Player('Max', 'max1234', 5)
playerJSON = json.dumps(player,default=encode_obj,indent=4, sort_keys=True)
print(playerJSON)

player_decoded = json.loads(playerJSON, object_hook=decode_dct)
print(type(player_decoded))
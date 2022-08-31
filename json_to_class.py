import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, "className": o.__class__.__name__}
    else:
        raise TypeError


def decode_user(dct):
    if User.__name__ in dct['className']:
        return User(name=dct['name'], age=dct['age'])
    return dct


from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, "className": o.__class__.__name__}
        else:
            return JSONEncoder.default(self, o)


user = User("Bharat", 32)

user_json = json.dumps(user, default=encode_user)
print(user_json)

user_json_1 = UserEncoder().encode(user)
print(user_json_1)

user_obj = json.loads(user_json, object_hook=decode_user)
print(type(user_obj))
print(user_obj.age)

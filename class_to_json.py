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

from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

USERS = [
        
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"},
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"}

]

def search_users(args):
   
    id = args.get("id")
    name = args.get("name")
    age = args.get("age")
    occupation = args.get("occupation")
    
    results = []


    for user in USERS:
         
        if id == user["id"]:
            results.append(user)
            return results
    
        elif( 
            (name is None or name.lower() in user["name"].lower()) and
            (age is None or (int(age) - 1 <= user["age"] <= int(age) + 1)) and
            (occupation is None or occupation.lower() in user["occupation"].lower())
        ):
            results.append(user)
    
    
    return results

    # Implement search here!

if __name__ == "__main__":
    print(search_users({"id": "1"}))  
    print(search_users({"name": "John"}))  
    print(search_users({"age": "29"}))  
    print(search_users({"occupation": "Developer"}))  
    print(search_users({"id": "5", "name": "Jane", "age": "31", "occupation": "Manager"})) 
    print(search_users({}))
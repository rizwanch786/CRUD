import requests
import json
URL = 'http://127.0.0.1:8000/studentapi/'
def get_data(id = None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

def post_data(): 
    data = {
        'name': input("Enter name: "),
        "roll": int(input("Enter Roll: ")),
        "city": input("Enter City: ")
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL ,data = json_data)
    data = r.json()
    print(data)

def update_data():
    id = int(input("Enter ID: "))
    name = input("Enter name: ")
    roll = int(input("Enter Roll: "))
    # city = input("Enter City: ")
    data = {
        'id': id,
        'name': name,
        "roll": roll,
        # "city": city
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL ,data = json_data)
    data = r.json()
    print(data)

def delete_data(id = None):
    data = {'id': int(input("Enter ID: "))}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

# get_data()
# post_data()
# update_data()
# delete_data()
print("Client View\n1 : Get Data\n2 : Post Data\n3 : Update Data\n4 : Delete Data ")
choice = int(input("Enter Your Choice 1-4: "))
if choice == 1:
    id = int(input("Enter ID: "))
    get_data(id)
elif choice == 2:
    post_data()
elif choice == 3:
    update_data()
elif choice == 4:
    delete_data()
else:
    print("Invalide Input")



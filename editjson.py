import json

# Load JSON data from the file
with open('devices.json', 'r') as file:
    data = json.load(file)

def moredev():
    # Prompt user to enter more devices
    print("Want to enter more devices?")
    print("[0]: No")
    print("[1]: Yes")
    ans = int(input("Answer: "))
    if ans == 0:
        return False
    elif ans == 1:
        return True 
    else:
        print("Error: Invalid Input")
        return False
  
# Create a dictionary to map brands to their index in the JSON data
List_items = {data[i]["brand"]: i for i in range(len(data))}
k=List_items.keys()
print("\n", "Available Brands: ", k)

# Main loop to add new devices
g = True
while g:
    print("\n")
    brand = input("brand: ")
    if brand.lower() in str(k).lower():
        # Collect new device information
        name = input("name: ")
        codename = input("codename: ")
        maintainer = input("maintainer: ")
        xda = input("xda: ")
        telegram = input("telegram: ")
        download = input("download: ")

        # Append the new device information to the existing dictionary
        mainindex = List_items[brand] 
        lenindex = data[mainindex]['devices']
        p=lenindex[len(lenindex)]={}
        p['name']=name
        p['codename']=codename
        p['maintainer']=maintainer
        p['xda']=xda
        p['telegram']=telegram
        p['download']=download

        # Write the updated JSON data back to the file
        with open('devices.json', 'w') as file:
            json.dump(data, file, indent=4)
        
    else:
        print("Error: No such Brand")

    print(" ")
    g = moredev()

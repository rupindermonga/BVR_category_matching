import glob
import json
import os

path_to_json = '/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise'

categories = []
parent = {}
def add(data, p):
    global parent
    global categories
    for key in data:
        categories.append(key)
        if key not in parent:
            parent[key] = set()
        parent[key] = p
        add(data[key],key)


# for f in glob.iglob(os.path.join(path_to_json +'*.json')):
#     data = json.load(open(f,'r'))
#     top = f.replace('.json','')
#     categories.add(top)
#     add(data,top)
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

all_files = []
file_names = []
for eachFile in json_files:
    with open(os.path.join(path_to_json, eachFile)) as f:
        data = json.load(f)
        top = eachFile.replace('.json','')
        categories.append(top)
        add(data, top)

# print(len(categories))
# print(categories[:100])
# print(parent['Art Tissue & Crepe Paper'])

# print(parent['Paper'])

# print(parent['Office & School Supplies'])

# print(parent['Office Products'])

# print(parent['Fan Shop'])

# print(parent['Sports & Outdoors'])

# print(parent['Teen & Young Adult'])

# print(parent['Kindle eBooks'])

# # print(parent['Kindle Store'])

# print(parent['Backpacks'])

# print(parent['Tops'])

print([c for c in parent if 'Tops' in parent[c]])

print(list(filter(lambda x: 'Tops' in parent[x], parent)))

new_parent = []
for a in parent:
    if 'Tops' in parent[a]: new_parent.append(a)

print(new_parent)
 # print([c for c in parent if '2 in 1 Laptops' in parent[c]])

# print([c for c in parent if 'Laptop Backpacks' in parent[c]])

# print([c for c in parent if 'Backpacks' in parent[c]])
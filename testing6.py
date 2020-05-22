import glob
import json
import os

path_to_json = '/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise'
# path_to_json = '/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/Testing'
# categories = []
# parent = {}
# def add(data, p):
#     global parent
#     global categories
#     for key in data:
#         categories.append(key)
#         if key not in parent:
#             parent[key] = set()
#         parent[key] = p
#         add(data[key],key)

json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


categories = []
parent = {}
def add(data, p):
    global categories
    global parent
    for key in data:
        categories.append(key)
        if key not in parent:
            parent[key] = []
        parent[key].append(p)
        add(data[key], key)
    # return "True"

all_files = []
file_names = []
for eachFile in json_files:
    with open(os.path.join(path_to_json, eachFile)) as f:
        data = json.load(f)
        top = eachFile.replace('.json','')
        categories.append(top)
        add(data, top)

# print(parent['Backpacks'])
top = "Luggage & Travel Gear"
final_list = []
text = 'Backpacks'
for eachC in parent[text]:
    new_list = []
    new_list.append(text)
    
    new_list.append(eachC)
    while eachC != top:
        eachC = parent[eachC][0]
        new_list.append(eachC)
    final_list.append(new_list)
print(final_list)
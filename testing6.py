import glob
import json
import os
import copy

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
super_final_list = []
n = []

# for eachFile in json_files:
#     with open(os.path.join(path_to_json, eachFile)) as f:
#         data = json.load(f)
#         top = eachFile.replace('.json','')
#         categories.append(top)
#         add(data, top)

# print(len(categories))
# all_categories = copy.deepcopy(categories)
# print(len(all_categories))


for eachFile in json_files:
    with open(os.path.join(path_to_json, eachFile)) as f:
        data = json.load(f)
        top = eachFile.replace('.json','')
        categories = []
        parent = {}
        categories.append(top)
        add(data, top)
        final_list = []
        for text in categories:
        # text = 'Tops'
            parent_text = []
            # if text in categories:
                # print(parent[text])
            try:
                parent_text = parent[text]
            except:
                pass
            # print(parent_text)
            for eachC in parent_text:
                new_list = []
                new_list.append(text)            
                new_list.append(eachC)
                while eachC != top:
                    if eachC == categories[1]:
                        eachC = top
                    else:
                        eachC = parent[eachC][0]
                    new_list.append(eachC)
                final_list.append(new_list)
        super_final_list.append(final_list)
    n.append(super_final_list)

filter_list = list(filter(lambda x: x != [], n))

# print(len(filter_list))
# print(filter_list)

print(filter_list[:1])
def getSizeOfNestedList(listOfElem):
    ''' Get number of elements in a nested list'''
    count = 0
    # Iterate over the list
    for elem in listOfElem:
        # Check if type of element is list
        if type(elem) == list:  
            # Again call this function to get the size of this element
            count += getSizeOfNestedList(elem)
        else:
            count += 1    
    return count

f = getSizeOfNestedList(filter_list)
print(f)

'''

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
'''
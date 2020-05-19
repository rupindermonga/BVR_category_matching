import os, json, csv
import pandas as pd
import glob

path_to_json = '/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise'


with open(os.path.join(path_to_json, 'Clothing, Shoes & Jewelry.json')) as f:
    test_file = json.load(f)


# categories = set()
parent = {}
count = 0
node_id = {}
def add(data, p):
    # global categories
    global parent
    global count
    global node_id
    for key in data:
        # categories.add(key)
        if key not in parent:
            parent[key] = []
            node_id[key] = []
        parent[key].append(p)
        node_id[key].append(count)
        count += 1
        add(data[key], key)
    return count

top = "Clothing, Shoes & Jewelry"
# categories.add(top)
f = add(test_file,top)
print(f)
test_text = "Tops"
parent_list = parent[test_text]
node_list = node_id[test_text]
print(parent_list)
print(node_list)

parent_node_list = []
parent_position = 0
for eachValue in parent[test_text]:
    my_list = node_id[eachValue]
    parent_position += 1
    if eachValue == top:
        parent_node_list.append("Zero")
    else:
        if len(my_list) > 1:
            eachValue_index = parent_position - 1
            my_number =  node_list[eachValue_index]
            new_parent_id = min([ i for i in my_list if i < my_number], key=lambda x:abs(x-my_number))
            parent_node_list.append(new_parent_id)
        else:
            parent_node_list.append(node_id[eachValue][0])

        
print(parent_node_list)
            
            
            # min_value = 1000
            # for eachN in node_id[eachValue]:
#                 if int(eachN) < int(eachValue):
#                     min_value = min(eachValue - eachN, min_value)
#                     if min_value == eachValue - eachN:
#                         parent_list.append(eachN)
#         else:
#             parent_list.append(node_id[eachValue])

# print(parent_list)

# categories = set()
# parent = {}
# node_id = {}
# count = 0
# title_list = []
# node_list = []
# parent_list = []
# parent_node_id = []
# def add(data,p):
#     global parent
#     global categories
#     global node_id
#     global count
#     global title_list
#     # global parent_list
#     for key in data:
#         title_list.append(key)
#         node_list.append(count)
#         categories.add(key)
#         if key not in parent:
#             parent[key] = set()
#             node_id[key] = set()
#         parent[key].add(p)
#         node_id[key].add(count)
#         count += 1
#         add(data[key],key)



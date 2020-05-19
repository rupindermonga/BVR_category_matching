import os, json, csv
import pandas as pd
import glob

path_to_json = '/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise'


with open(os.path.join(path_to_json, 'Movies & TV.json')) as f:
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
            parent[key] = set()
            node_id[key] = set()
        parent[key].add(p)
        node_id[key].add(count)
        count += 1
        add(data[key], key)
    return count

top = "Clothing, Shoes & Jewelry"
# categories.add(top)
f = add(test_file,top)
print(f)
print(parent["TV"])
print(node_id['TV'])


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



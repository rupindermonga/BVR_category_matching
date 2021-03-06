# Matching categories with browse nodes
import os, json, csv
import pandas as pd
import glob

path_to_json = '/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise'
# json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

# bvr_data = pd.read_csv("/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise/category_url.csv")

# all_files = []
# file_names = []
# for eachFile in json_files:
#     try:
#         with open(os.path.join(path_to_json, eachFile)) as f:
#             new_file = json.load(f)
#             file_names.append(eachFile)
#             all_files.append(new_file)
#     except:
#         pass


with open(os.path.join(path_to_json, 'Luggage & Travel Gear.json')) as f:
    test_file = json.load(f)


categories = set()
parent = {}
node_id = {}
count = 0
title_list = []
node_list = []
parent_list = []
parent_node_id = []
def add(data,p):
    global parent
    global categories
    global node_id
    global count
    global title_list
    # global parent_list
    for key in data:
        title_list.append(key)
        node_list.append(count)
        categories.add(key)
        if key not in parent:
            parent[key] = set()
            node_id[key] = set()
        parent[key].add(p)
        node_id[key].add(count)
        count += 1
        add(data[key],key)
    # d = {"List": title_list, "Node_Id": node_list}
    # final_data = pd.DataFrame(d)
    # final_data.to_csv("check.csv")



top = 'App'
categories.add(top)
add(test_file,top)
# print(len(categories))
# print(list(categories)[:100])
# print(parent['Backpacks'])
# (element,) = parent['Laptop Backpacks']
# print(element)
# print(node_id['Laptop Backpacks'])
# print(node_id[element])


for eachElement in title_list:
    new_list = []
    parent_list.append(parent[eachElement])
    print(parent[eachElement])
    for e in parent[eachElement]:
        print(e)
        try:
            new_list.append(node_id[e])
        except:
            new_list.append("NA")
    # (element, ) = parent[eachElement]
    parent_node_id.append(new_list)

d = {"List": title_list, "Node_Id": node_list, "Parent": parent_list, "Parent_node_id": parent_node_id}
final_data = pd.DataFrame(d)
final_data.to_csv("check.csv")



# print([c for c in parent if 'Washers' in parent[c]])




# # Python3 Program to find depth of a dictionary 
# # def dict_depth(dic, level = 1): 	
# # 	if not isinstance(dic, dict) or not dic: 
# # 		return level 
# # 	return max(dict_depth(dic[key], level + 1) 
# # 							for key in dic) 


# # for eF, fN in zip(all_files, file_names):
# #     print(fN, dict_depth(eF))

# # example_dict = { 'key1' : 'value1',
# #                  'key2' : 'value2',
# #                  'key3' : { 'key3a': 'value3a' },
# #                  'key4' : { 'key4a': { 'key4aa': 'value4aa',
# #                                        'key4ab': 'value4ab',
# #                                        'key4ac': 'value4ac'},
# #                             'key4b': 'value4b'}
#                 # }

# parent = []
# def findParent(d, value):
#     global parent
#     for k, v in d.items():
#         if v == value:
#             return parent
#         elif isinstance(v, dict):
#             parent = [k]
#             findParent(v, value)
#         return parent

# f = findParent(test_file, 'Ranges')
# print(f)

# # def find_key(d, value):


# #     for k,v in d.items():
# #         if isinstance(v, dict):
# #             p = find_key(v, value)
# #             if p:
# #                 return [k] + p
# #         elif v == value:
# #             return [k]

# # print(find_key(example_dict,'key3a'))






# # # Driver code 
# # dic = {1:'a', 2: {3: {4: {}}}} 

# # print(dict_depth(dic)) 

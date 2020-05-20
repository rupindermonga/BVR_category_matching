import os, json, csv
import pandas as pd
import glob, re

path_to_json = '/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise'
save_path = '/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/Result'

with open(os.path.join(path_to_json, 'Luggage & Travel Gear.json')) as f:
    test_file = json.load(f)

json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

bvr_data = pd.read_csv("/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise/category_url.csv")

all_files = []
file_names = []
for eachFile in json_files:
    try:
        with open(os.path.join(path_to_json, eachFile)) as f:
            new_file = json.load(f)
            file_names.append(eachFile)
            all_files.append(new_file)
    except:
        pass



categories = []
parent = {}
count = 0
node_id = {}
def add(data, p):
    global categories
    global parent
    global count
    global node_id
    for key in data:
        # categories.add(key)
        categories.append(key)
        if key not in parent:
            parent[key] = []
            node_id[key] = []
        parent[key].append(p)
        node_id[key].append(count)
        count += 1
        add(data[key], key)
    return count




def parentList(category):
    # category = test_text
    node_list = node_id[category]
    parent_node_list = []
    parent_position = 0
    for eachValue in parent[category]:  
        parent_position += 1
        if eachValue == top:
            parent_node_list.append("Zero")
        else:
            my_list = node_id[eachValue]
            if len(my_list) > 1:
                eachValue_index = parent_position - 1
                my_number =  node_list[eachValue_index]
                new_parent_id = min([ i for i in my_list if i < my_number], key=lambda x:abs(x-my_number))
                parent_node_list.append(new_parent_id)
            else:
                parent_node_list.append(node_id[eachValue][0])
    return parent_node_list


for fileName, fullFile in zip(file_names, all_files):
    parent_column = []
    parent_final_list =[]
    node_final_list = []
    top = fileName.rstrip(".json")
    categories = []
    parent = {}
    count = 0
    node_id = {}
    categories.append(top)
    adding_data = add(fullFile, top)
    for eachCategory in categories:
        
        if eachCategory != top:
            parent_column.append(parentList(eachCategory))
            parent_final_list.append(parent[eachCategory])
            node_final_list.append(node_id[eachCategory])
        # else:
        #     pass
    del categories[0]
    final_dataFrame = pd.DataFrame({
                                        "Category": categories,
                                        "node_id": node_final_list, 
                                        "parent_list": parent_final_list,
                                        "parent_id": parent_column})
    final_dataFrame.to_csv(os.path.join(save_path, top +".csv"))







# category_dataframe = pd.DataFrame({"Category": categories})

# category_dataframe.to_csv("category_check.csv")


# print(parentList(test_text))
# # print(parent_node_list)
# print(len(categories))
            
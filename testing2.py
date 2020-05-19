import os, json, csv
import pandas as pd
import glob

path_to_json = '/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise'


with open(os.path.join(path_to_json, 'Luggage & Travel Gear.json')) as f:
    test_file = json.load(f)


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



# top = "Clothing, Shoes & Jewelry"
# # categories.add(top)
# categories.append(top)
# f = add(test_file,top)
# print(f)
# test_text = "Girls' Watch Bands"
# parent_list = parent[test_text]
# node_list = node_id[test_text]
# print(parent_list)
# print(node_list)


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

parent_column = []
parent_final_list =[]
node_final_list = []
top = "Clothing, Shoes & Jewelry"
categories.append(top)
adding_data = add(test_file, top)


for eachCategory in categories:
    if eachCategory != top:
        parent_column.append(parentList(eachCategory))
        parent_final_list.append(parent[eachCategory])
        node_final_list.append(node_id[eachCategory])
    else:
        pass

del categories[0]
final_dataFrame = pd.DataFrame({
                                    "Category": categories,
                                    "node_id": node_final_list, 
                                    "parent_list": parent_final_list,
                                    "parent_id": parent_column})

category_dataframe = pd.DataFrame({"Category": categories})
final_dataFrame.to_csv("checking.csv")
category_dataframe.to_csv("category_check.csv")


# print(parentList(test_text))
# # print(parent_node_list)
# print(len(categories))
            
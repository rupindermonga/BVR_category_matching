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

# print(bvr_data)
bvr_node_id = []
bvr_node_name = []
for val, eachElement in enumerate(bvr_data.iloc[:,0], 0):
    # print(eachElement)
    bvr_node_id.append(val)
    bvr_node_name.append(eachElement)


bvr_data_frame = pd.DataFrame({"Category": bvr_node_name, "BVR Node ID": bvr_node_id})

# merged_dataframe = pd.DataFrame({"Category": [1], "BVR Node ID": [1], "node_id": [1], "parent_id":[1], "File_Name":[1] })
# column_names = ["Category", "BVR Node ID", "node_id", "parent_id", "File_Name" ]
# merged_dataframe = pd.DataFrame(columns=  column_names)

check_data = pd.read_csv("/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise/Clothing_Shoes_Jewelry.csv")



merged_dataframe = pd.DataFrame()


dataframe_list = []
fileNames_list = []
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
    dataframe_list.append(final_dataFrame)
    fileNames_list.append(top)

    

    new_dataframe = pd.merge(bvr_data_frame, final_dataFrame, on="Category", how = "inner")
    new_dataframe['File_Name'] = top
    new_dataframe = new_dataframe.drop_duplicates(subset="Category")
    merged_dataframe = merged_dataframe.append(new_dataframe, ignore_index = True)
    
    merged_dataframe.sort_values(by = 'BVR Node ID', inplace= True)
    merged_dataframe.to_csv("merged.csv")

    final_dataFrame.to_csv(os.path.join(save_path, top +".csv"))


# merged_dataframe = pd.DataFrame()
# for eachDataFrame, file_name in zip(dataframe_list, fileNames_list):
#     new_dataframe = pd.merge(bvr_data_frame, eachDataFrame, on="Category", how = "inner")
#     # new_dataframe.drop(new_dataframe.columns[2], axis = 1, inplace = True)
#     new_dataframe['File_Name'] = file_name
#     new_dataframe = new_dataframe.drop_duplicates(subset="Category")
#     merged_dataframe = merged_dataframe.append(new_dataframe, ignore_index = True)
    
merged_dataframe.sort_values(by = 'BVR Node ID', inplace= True)
merged_dataframe.to_csv("merged.csv")


    
    




# bvr_data_frame.to_csv("bvr_check.csv")

# check_data = pd.read_csv("/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise/Clothing_Shoes_Jewelry.csv")


# merged_stuff = pd.merge(bvr_data_frame, check_data, on="Category", how = "inner")
# merged_stuff.drop(merged_stuff.columns[2], axis = 1, inplace = True)
# # print(merged_stuff) #prints all matches separately. deleting the column for now
# merged_stuff['File_Name'] = "Clothing_Shoes_Jewelry"
# # merged_stuff.append(merged_stuff)
# print(merged_stuff.drop_duplicates(subset="Category"))

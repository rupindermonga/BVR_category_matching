import os, json, csv
import pandas as pd
import glob, re
import time
import numpy as np
import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity

class USEClassifier:

    def __init__(self):
        self.model_path = 'https://tfhub.dev/google/universal-sentence-encoder/4'
        self.embed = hub.load(self.model_path)

    def set_contexts(self,contexts):
        self.contexts = list(contexts)
        self.context_vectors = np.array(self.embed(self.contexts))

    def classify(self,texts,topn=2):
        text_vectors = np.array(self.embed(texts))
        sim = cosine_similarity(text_vectors,self.context_vectors)
        # sim.shape == (len(texts),len(self.contexts))                                                                                                                            

        retval = {}
        for i in range(len(texts)):
            sort = sorted(range(len(self.context_vectors)),
                          key=lambda k:sim[i][k],
                          reverse=True)
            sort = sort[:topn]
            retval[texts[i]] = [(self.contexts[s],sim[i][s]) for s in sort[:topn]]
        return retval

start_time = time.time()

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




merged_dataframe = pd.DataFrame()

over_all_count = 0
over_all_list = []
all_path_list = []
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
    new_file_path_list = []
    new_category_path_list = []
    for eachCategory in categories:
        new_category_path_list.append(eachCategory)
        # print(len(new_category_path_list))
        new_file_path_list.append(new_category_path_list)
        over_all_count += 1
        # over_all_list.append[eachCategory]
        # print(eachCategory)
        over_all_list.append(eachCategory)
        
        if eachCategory != top:
            parent_column.append(parentList(eachCategory))
            parent_final_list.append(parent[eachCategory])
            node_final_list.append(node_id[eachCategory])
        # else:
        #     pass
    all_path_list.append(new_file_path_list)
    # print([fileName,len(new_file_path_list), len(categories)])
    del categories[0]
    final_dataFrame = pd.DataFrame({
                                        "Category": categories,
                                        "node_id": node_final_list, 
                                        "parent_list": parent_final_list,
                                        "parent_id": parent_column})

    new_dataframe = pd.merge(bvr_data_frame, final_dataFrame, on="Category", how = "inner")
    new_dataframe['File_Name'] = fileName
    new_dataframe = new_dataframe.drop_duplicates(subset="Category")
    merged_dataframe = merged_dataframe.append(new_dataframe, ignore_index = True)
    
    merged_dataframe.sort_values(by = 'BVR Node ID', inplace= True)
    merged_dataframe.to_csv("merged.csv")

    final_dataFrame.to_csv(os.path.join(save_path, top +".csv"))

not_merged_dataFrame = bvr_data_frame.merge(merged_dataframe, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']
not_merged_dataFrame = not_merged_dataFrame.drop(not_merged_dataFrame.columns[2:], axis = 1)
merged_dataframe.sort_values(by = 'BVR Node ID', inplace= True)
merged_dataframe.to_csv("merged.csv")
not_merged_dataFrame.to_csv("not_merged.csv")
# over_all_list_dataframe = pd.DataFrame({"abc": all_path_list})
# over_all_list_dataframe.to_csv("path_list.csv")
# over_all_list_dataframe = pd.DataFrame({"abc": over_all_list})
# over_all_list_dataframe.to_csv()

# print(time.time() - start_time)
# print(over_all_count)
# print(len(over_all_list))
# print("Amazon Instant Video.json" in over_all_list)
# print("Amazon Instant Video" in over_all_list)
# print("Amazon Instant Vide" in over_all_list)
# print("Amazon Instant Video." in over_all_list)
# print(over_all_list.index("Amazon Instant Video."))
# for eachName in file_names:
#     new_name = eachName.rstrip(".json")
#     print_list = [new_name,over_all_list.index(new_name) ]
#     print(print_list)
# print(len(all_path_list))
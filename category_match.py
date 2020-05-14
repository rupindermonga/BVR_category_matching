# Matching categories with browse nodes
import os, json, csv
import pandas as pd

path_to_json = '/media/rupinder/C49A5A1B9A5A0A76/Users/Rupinder/Desktop/BVR/MatchingCategory/AmazonNodescategorywise'
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


my_log = []
            
def mydict(d):
    for k, v in d.items():
        if isinstance(v,dict):
            my_log.append(k)
            mydict(v)
        else:
            pass
        return my_log


counting = 0
final_file = []
for eachCategory in bvr_data["Category Name"]:
    eachList = []
    for filename, eachFile in zip(file_names,all_files):
        my_log = []
        my_log = mydict(eachFile)
        if eachCategory in my_log:
            position = my_log.index(eachCategory)
            eachList.append(filename+"-"+str(position))
            counting += 1
        else:
            pass
    final_file.append(eachList)

d = {"Name":bvr_data["Category Name"], "review_flag": final_file}
data_review_flag = pd.DataFrame(d)
data_review_flag.to_csv("final.csv")
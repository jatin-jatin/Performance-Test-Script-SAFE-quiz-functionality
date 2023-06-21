import os
import csv
from numpy import e
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('seaborn')
plt.tight_layout()
folder_list =[]
for name in os.listdir("."):
    if name[-1] == 'q':
        folder_list.append(int(name[:-1]))
folder_list.sort()
question_list = folder_list.copy()
folder_list = list(map(lambda x : str(x)+'q',folder_list))
# print(folder_list)

user_list =[]
for name in os.listdir(folder_list[0]):
    user_list.append(int(name[:-4]))
user_list.sort()
# print(user_list)

user_file_list = list(map(lambda x : str(x) + ".csv",user_list))
# print(user_file_list)

fetch_csv = open(folder_list[0] + "/" + user_file_list[0])
reader = csv.reader(fetch_csv)
header = next(reader)
api_dictionary_med_rt={}
api_dictionary_nf_rt={}
for row in reader:
    api_dictionary_med_rt[row[1]]=[]
    api_dictionary_nf_rt[row[1]]=[]
fetch_csv.close()

# print(api_dictionary_med_rt)
# print(api_dictionary_nf_rt)
xlab ="number of questions"
ylab ="response time(ms)"
med_rt = 0
nf_rt = 0
# print(header)
for i in range(len(header)):
    if header[i] == 'Median Response Time':
        med_rt = i
    if header[i] == '95%':
        nf_rt = i
for element in user_file_list:
    for folder in folder_list:
        fetch_csv = open(folder + "/" + element)
        reader = csv.reader(fetch_csv)
        header = next(reader)
        for row in reader:
            api_dictionary_med_rt[row[1]].append(float(row[med_rt]))
            api_dictionary_nf_rt[row[1]].append(float(row[nf_rt]))
    
    color_list=["blue","black","green","red","purple","yellow","orange","gold","indigo"]
    color_dict= {}
    api_list = list(api_dictionary_med_rt)
    for i in range(len(api_list)):
        color_dict[api_list[i]] = color_list[i]
    for part in api_list:
        plt.plot(question_list,api_dictionary_med_rt[part],color_dict[part],label = part + " api")
        plt.plot(question_list,api_dictionary_nf_rt[part],color_dict[part])
    graph_folder = "questions " + " vs "+ ylab +" graphs"
    if not os.path.exists(graph_folder):
        os.mkdir(graph_folder)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.figtext(.5, .9, "for " +element[:-4] +" user")
    plt.legend()
    # plt.show()
    path = "./"+graph_folder+"/" +  element[:-4] +" users.png"
    plt.savefig(path)
    plt.close()
    for api in api_list:
        api_dictionary_med_rt[api] = []
        api_dictionary_nf_rt[api] = []
    print(element)

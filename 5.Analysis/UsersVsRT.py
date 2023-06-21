# the naming convention of the folder should be ##q where ## represents a number
# from _typeshed import ReadableBuffer
import os
import csv
from numpy import e
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('seaborn')
plt.tight_layout()

def Uanalysis(folder_name):
    num_user_lst = []
    for filename in os.listdir(folder_name):
        num_user_lst.append(int(filename[:-4]))
    num_user_lst.sort()
    file_lst =[]
    for file in num_user_lst:
        file_lst.append(str(file)+".csv")
    fetch_csv = open(folder_name + "/" + file_lst[0])
    reader = csv.reader(fetch_csv)
    header = next(reader)
    api_dictionary_med_rt={}
    api_dictionary_nf_rt={}
    for row in reader:
        api_dictionary_med_rt[row[1]]=[]
        api_dictionary_nf_rt[row[1]]=[]
    fetch_csv.close()
    xlab ="number of users"
    ylab ="response time(ms)"
    med_rt = 0
    nf_rt = 0

    for i in range(len(header)):
        if header[i] == 'Median Response Time':
            med_rt = i
        if header[i] == '95%':
            nf_rt = i
    for element in file_lst:
        fetch_csv = open(folder_name + "/" + element)
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
    for element in api_list:
        plt.plot(num_user_lst,api_dictionary_med_rt[element],color_dict[element],label = element + " api")
        plt.plot(num_user_lst,api_dictionary_nf_rt[element],color_dict[element])
    graph_folder = "users " + " vs "+ ylab +" graphs"
    if not os.path.exists(graph_folder):
        os.mkdir(graph_folder)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.figtext(.5, .9, "for " + folder_name[:-1] +" questions")
    plt.legend()
    path = "./"+graph_folder+"/" + folder_name[:-1] + " questions.png"
    plt.savefig(path)
    plt.close()
    




if __name__ =="__main__":
    folder_lst = []
    for folder in os.listdir("."):
        if folder[-1] =='q':
            folder_lst.append(folder)
    folder_lst.sort()
    for folder in folder_lst:
        print(folder)
        Uanalysis(folder)

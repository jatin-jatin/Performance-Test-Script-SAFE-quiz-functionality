import csv
from typing import DefaultDict

def answers(type1,type2,type3):
    val = float(input("Enter the id of the first uploaded question from the quiz : "))
    file_name = input("Enter the name of the answer file without the (.py extension) : ")
    file_name = file_name + ".py"
    answer_file = open(file_name,"w+")
    topstr = "answers = ["
    botstr = "]"
    answer_file.write(topstr)
    for i in range(type1):
        qstr =  f'{{"question" :{val},"reason_text":"","response":"1"}},'
        val = val + 1.0
        answer_file.write(qstr)
    for i in range(type2):
        qstr =  f'{{"question" :{val},"reason_text":"","response":"0 1"}},'
        val = val + 1.0
        answer_file.write(qstr)
    for i in range(type3):
        qstr =  f'{{"question" :{val},"reason_text":"","response":"3.9"}},'
        val = val + 1.0
        answer_file.write(qstr)
    answer_file.write(botstr)


def questions(type1,type2,type3):
    """
    inputs: 
    3 integers ->for all question types
    1 filename -> for csv name 

    output:
    1 file -> csv file that can be added to the safe.
    """

    header = ['Question', ' Type', ' Answer', 'Marks', ' Category', ' Option 1', ' Option 2', ' Option 3', ' Option 4', ' Option 5', ' Remarks', ' Answer Description']
    filename= input("Enter the name of the question file( without csv extension) : ")
    filename = filename + '.csv'
    val = 0
    
    with open(filename,'w+') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(header)

        for i in range(type1):
            csv_writer.writerow(['Question description text ' + f"{val}", ' singlecorrect', ' 2', ' 1', '', ' Option 1', ' Option 2', ' Option 3', ' Option 4', ' Option 5', ' Remarks', ' Answer Description'])
            val = str(int(val) + 1)

        for i in range(type2):
            csv_writer.writerow(['Question description text '+ f"{val}", ' setcorrect',  "2,3", ' 1', '', ' Option 1', ' Option 2', ' Option 3', ' Option 4', ' Option 5', ' Remarks', ' Answer Description'])
            val = str(int(val) + 1)

        for i in range(type3):
            csv_writer.writerow(['Question description text '+ f"{val}", ' numeric',"[3.14, 3.15]", ' 1', '', '', '', '', '', '', ' Remarks', " Answer Description"])
            val = str(int(val) + 1)

    print("Upload the "+filename+" to the quiz app and publish the quiz that will generate the name of the quiz .")
    print("Note the id of the first question .")
    # print("")
    # print("Use that quiz name as an input to the answer_quiz.py to generate the api/quiz response")


if __name__ == "__main__" :
    type1 = int(input("Enter the number of questions of single correct : "))
    type2 = int(input("Enter the number of questions of setcorrect : "))
    type3 = int(input("Enter the number of questions of numeric type : "))
    questions(type1,type2,type3)
    answers(type1,type2,type3)

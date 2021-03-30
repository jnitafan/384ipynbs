import pandas as pd

# read the text file and put it in the variable result
result = pd.read_csv("result_withoutTotal.csv")

# print out the averages, min and max of Assignment 1
print("Ass1 average: " + str(result["Ass1"].mean()))
print("Ass1 min: " + str(result["Ass1"].min()))
print("Ass1 max: " + str(result["Ass1"].max()))
print()
# print out the averages, min and max of Assignment 2
print("Ass2 average: " + str(result["Ass2"].mean()))
print("Ass2 min: " + str(result["Ass2"].min()))
print("Ass2 max: " + str(result["Ass2"].max()))
print()
# print out the averages, min and max of Assignment 3
print("Ass3 average: " + str(result["Ass3"].mean()))
print("Ass3 min: " + str(result["Ass3"].min()))
print("Ass3 max: " + str(result["Ass3"].max()))
print()
# print out the averages, min and max of Assignment 4
print("Ass4 average: " + str(result["Ass4"].mean()))
print("Ass4 min: " + str(result["Ass4"].min()))
print("Ass4 max: " + str(result["Ass4"].max()))
print()
# print out the averages, min and max of Exam
print("Exam average: " + str(result["Exam"].mean()))
print("Exam min: " + str(result["Exam"].min()))
print("Exam max: " + str(result["Exam"].max()))
print()
# print out (and if multiple students) with the highest result of Assignment 1
print("Student(s) with highest Ass1: ")
# for every row with the maximum result, print out the index of such result and DataFrame.loc[] (locate) them
print(result.loc[result["Ass1"] == result["Ass1"].max()])
print()
# print out (and if multiple students) with the highest result of Assignment 2
print("Student(s) with highest Ass2: ")
print(result.loc[result["Ass2"] == result["Ass2"].max()])
print()
# print out (and if multiple students) with the highest result of Assignment 3
print("Student(s) with highest Ass3: ")
print(result.loc[result["Ass3"] == result["Ass3"].max()])
print()
# print out (and if multiple students) with the highest result of Assignment 4
print("Student(s) with highest Ass4: ")
print(result.loc[result["Ass4"] == result["Ass4"].max()])
print()
# print out (and if multiple students) with the highest result of Exam
print("Student(s) with highest Exam: ")
print(result.loc[result["Exam"] == result["Exam"].max()])
print()

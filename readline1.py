import csv
import os

f = 1
count = 0
fName = "file" + str(f) + ".csv"          #initial file Name
query = ["insert into systemevent values"] #query

if os.path.exists(fName):     #it will stop to overwrite the file
    os.remove(fName)

def writeFile(fName, line, count) :      
    reader_pipe = csv.reader(line, delimiter='|')
    with open(fName, 'a+') as file_comma:
        writer_comma = csv.writer(file_comma, delimiter=',')
        for row in reader_pipe:
            if row == query:                 # if query 
                writer_comma.writerow(row)   #write query
            else :                           # else 
                if row :                     # row means line 
                    if count < 2 :
                        print(count)
                        row.append("'y'")
                        row.append("'now()'")
                        row.append("'now')")
                        row.append('')
                    else :
                        print("----")
                        row.append("'y'")
                        row.append("'now()'")
                        row.append("'now'")
                        temp = row[-1] + ");"
                        row[-1] = temp
                    str1 = "(" + row[0]
                    row[0] = str1
                    writer_comma.writerow(row) #write here row

with open("file.txt", "r+") as file_pipe: 
    next(file_pipe)                   #skipping first line
    for line in file_pipe :
        if count == 0:                 #only for first file query at first line 
            writeFile(fName, query, count)    # write query at first lile for first file
        if count == 3 :
            f += 1
            fName = "file" + str(f)+".csv"    #file name
            if os.path.exists(fName):         #it will stop to overwrite the file
                os.remove(fName)
            writeFile(fName, query, count)           # write query at first line for every file except first file  
            count = 0                         #making count 0 for new file counting

        writeFile(fName, [line], count)              #write the line 
        count+=1 
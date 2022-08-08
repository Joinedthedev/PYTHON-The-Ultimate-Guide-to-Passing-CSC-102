# 1. scenario: given a paragraph, with five lines: write a python code to:.
# read from ext file
# tell no, of lines
# tell no. of words contained
# tell the occurrence of every word in the paragraph

LineCount = 0
Wordcount = []
Wordoccurence = {}
Infile = open("ParagraphWith5_lines.txt", "r")
for line in Infile:
     Linecount+=1 #count = count + 1
     line.strip()  #THEBOYISNOTNICE
     for strippedlines in line.split():
        Wordcount.append(strippedlines) #This will append our values to a list which we can take the length of
        Wordoccurence[strippedlines] = Wordoccurence.get(strippedlines, 0) + 1 # counts the number of times the word appears
print("no lines", LineCount, '\n', "no of words is:", len(Wordcount), '\n', "word occurence is:", Wordoccurence)


#2.	You are presented with an essay written by your close friend about leadership. Write a python code that will achieve the following task with the paragraph
# Print You are presented with an essay written by you close friend about leadership. Write a python code that will achieve the following task with the paragraph
# a.	Print the second line.
# b.	Split the entire second line into words
# c.	Print the words
# d.	Print words that starts with letter c.



whereMyFileIs = "C:/Users/salim/Desktop/Questions he said would come out/Friend_Essay.txt"
#a, b, c
# count = 0
ReadingFile = open(whereMyFileIs, "r")
# for line in ReadingFile:
#     count+=1 # count = count +1
#     if count ==2:
#         print(line) #a
#         s = line.split() #b
#         print(s) #c
#
#d
for line in ReadingFile:
    for strippedlines in line.split():
        if strippedlines.startswith('c'):
            print(strippedlines)

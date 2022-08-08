#This should go without saying but the questions that will pop up on the exam are not gonna be the exact same. He'll prolly
#mix it up a bit but the concept is synonymous.
# 1. scenario: given a paragraph, with five lines: write a python code to:.
# read from ext file
# tell no, of lines
# tell no. of words contained
# tell the occurrence of every word in the paragraph
count = 0
WordCount= []
WordOcurrence={}
infile = open("ParagraphWith5_lines.txt", "r") #Reading from an external file
for line in infile:
    count+=1 #no of all the lines
    line.rstrip()
    for words in line.split():
        WordCount.append(words)
        WordOcurrence[words] =WordOcurrence.get(words, 0) +1 #Ocurrence of every word
print("The no of lines is", count, '\n',"the no of words is", len(WordCount),'\n', "Wordocurrence is", WordOcurrence)

#len(Wordcount) is the no of all the words


#2.	You are presented with an essay written by you close friend about leadership. Write a python code that will achieve the following task with the paragraph
# Print You are presented with an essay written by you close friend about leadership. Write a python code that will achieve the following task with the paragraph

# a.	Print the second line.
# b.	Split the entire second line into words
# c.	Print the words
# d.	Print words that starts with letter c.

#a, b ,c
Infile = open("Friend_Essay.txt", "r")
# count = 0
# for line in Infile:
#     count= count + 1
#     if count == 2:
#          print(line)
#          s = line.split()
#          print(s)

#d
for line in Infile:
    line.rstrip()
    for words in line.split():
        if words.startswith('c'):
            print(words)
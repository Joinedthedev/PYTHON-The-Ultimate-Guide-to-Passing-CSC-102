#1.
# words = list()
# School_Paragraph = open("My School.txt")
# for sentences in School_Paragraph:
#         sentences.rstrip()
#         for SonGoku in sentences.split():
#             words.append(SonGoku)
# print(len(words))

#2. HE SAID WE SHOULD LEARN THIS CUZ IT MIGHT COME OUT

Input_File=open("Student_Score.txt", "r") #Me again =
OutPut_File =open("Sum_Avg.txt", "w")
s = 0
count = 0
for scores in Input_File:
     s += int(scores.strip())
     count += 1
average = s/count
OutPut_File.write("SUM OF STUDENTS SCORE IS")
OutPut_File.write(str(s))
OutPut_File.write("\n")
OutPut_File.write("Average is")
OutPut_File.write(str(average))
Input_File.close()
OutPut_File.close()

#3.
#a & #b
Infile = open("Friend_Essay.txt", "r")
count = 0
for line in Infile:
     count+= 1
     if count == 2:
         print(line)
         s = line.split()
         print(s)

#c
# for line in Infile:
#     line.rstrip()
#     for words in line.split():
#         if words.startswith('c'):
#             print(words)


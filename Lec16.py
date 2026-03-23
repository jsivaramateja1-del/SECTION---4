'''
with open("text.txt","r") as f:
    # data = f.read() # will read the file
    # data = f.readline() # will read the first line of the file
    data = f.readlines() # list of each line
print(type(data))
print(data)
'''

'''
with open("text2.txt","w") as f:
    f.write("Hello from Lec16.py \n you can write anything \n then again write something")
with open("text.txt","w") as f1:
    f1.write("my name")
with open("text.txt","a") as f2:  # append mode more like append in the list
    f2.write("\nAudi")
'''

'''
text_file = "text2.txt"
with open(text_file,"r") as f:
    data = f.read()
    c_count = 0
    for ch in data:
        if ch != "\n" and ch != " ":
            c_count += 1
    print(c_count)
    
with open(text_file,"r") as f1:
    data3 = f1.readlines()
length = len(data3) # number of lines
words = data.split() # display words in a list
word_list = len(data.split()) # display number of words
print(length)
print(words)
print(word_list)
'''
# replace word anything into something in the file text2.txt
text_file = "text2.txt"
with open(text_file, "r") as f:
    data = f.read()
data = data.replace("anything", "something")
with open(text_file, "w") as f:
    f.write(data)
    
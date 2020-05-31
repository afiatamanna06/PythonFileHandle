file = open("student.txt", "r")
text = file.read()
print(text)
size = len(text)
print(size)
'''for line in file:
    print(line)'''
    
file.close()
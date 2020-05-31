file = open("student.txt", "r+")
#text = file.read()
#print(text)
#size = len(text)
#print(size)
'''for line in file:
    print(line)'''
    
lines = file.readlines()
print(lines)
file.close()
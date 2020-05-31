file = open("student.txt", "a")  
#lines = file.readlines()
#print(lines)
file.write("\nViktor von Granzreich-age 40")
file.close()

file = open("student1.txt", "w")
file.write("Viktor von Granzreich-age 40\n")
file.close()
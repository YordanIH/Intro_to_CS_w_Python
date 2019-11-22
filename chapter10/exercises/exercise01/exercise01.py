file_name = input("Please enter a name for your file:")
file=open('file_example.txt', 'r')
contents = file.read()
file.close()
with open(file_name+".bak", 'w') as output_file:
    output_file.write(contents)
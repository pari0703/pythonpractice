from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())
txt.close()  # It's important to close the file after you're done using it

print("Type the filename again:")
file_again = input("> ")  # Changed raw_input to input for Python 3 compatibility

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()  # It's important to close the file after you're done using it

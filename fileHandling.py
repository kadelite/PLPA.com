filename = input("Enter the filename to read: ")
    
try:
  with open(filename, "r") as file:
    content = file.readlines()  # Read file line by line

        # No modification, just copying the content
  new_filename = "copy_" + filename
  with open(new_filename, "w") as new_file:
    new_file.writelines(content)

  print("File copied successfully as", new_filename)

except FileNotFoundError:
    print("Error: The file does not exist.")

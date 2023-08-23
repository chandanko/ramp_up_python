import re

pattern = "^[a-z]|[A-Z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

while True:
    User_input = input("Still want to validate Gmail!!! please enter Yes or No -> ").lower()
    if User_input == "yes":
         Gmail=input("Enter a gmail to validate -> ")
         data = re.search(pattern,Gmail)
         if data:
           with open("output.txt", 'a') as file:
            file.write(Gmail)
           print("The given mail address is valid and appended to the output.txt file")
         else:
             print("The given mail address is invalid")
    else:
        with open("output.txt", 'r') as file:
            for line in file:
                print(line, end=" ")
        break

        #     file_content = file.read()
        # print(file_content)




import re
import subprocess

pattern= "^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$"
# pattern="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

while True:
    User_input=input("Want to validate and ping Ip address !!! Type an option Yes or No -> ").lower()
    if User_input=="yes":
        Ip_address=input("Enter an ip address --> ")

        data=re.search(pattern,Ip_address)
        if data:
            result=subprocess.run(['ping',Ip_address])
            if result.returncode ==0:
                print(f"The ping to {Ip_address} was successful")
                with open("successful_Ips.txt", 'a') as file:
                    file.write(Ip_address)
            else:
                print(f"The ping to {Ip_address} was unsuccessful")
                with open("Unsuccessful_Ips.txt", 'a') as file:
                    file.write(Ip_address)
        else:
            pass
    else:
        break

# if data:
#     print("valid")
# else:
#     print("invalid")

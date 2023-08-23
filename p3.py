import re
import subprocess


# pattern= "^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$"
# pattern="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def ip_val():
    try:
        pattern = "^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$"
        while True:

            Ip_address = input("Enter an ip address --> ")

            data = re.search(pattern, Ip_address)
            if data:
                result = subprocess.run(['ping', Ip_address])
                if result.returncode == 0:
                    print(f"The ping to {Ip_address} was successful")
                    with open("successful_Ips.txt", 'a') as file:
                        file.write(Ip_address + '\n')
                else:
                    print(f"The ping to {Ip_address} was unsuccessful")
                    with open("Unsuccessful_Ips.txt", 'a') as file:
                        file.write(Ip_address + '\n')
            else:
                pass

            User_input = input("Want to validate and ping Ip address !!! Type an option Yes or No -> ").lower()
            if User_input == "yes":
                pass
            else:
                break


    except:
        print("Executed except block")


ip_val()

# 255=         25[0-5]
# 200-249=    2[0-4][0-9]
# 100-199=    1[0-9][0-9]
# 0-99=       [1-9]?[0-9]

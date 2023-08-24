import random

try:
    Number_of_emp = int(input("Enter the number of employee list need to create -> "))


    def generate_emp_details(num_of_emp):
        locations = ["Kormangala", "HSR Layout", "Bellari", "Mumbai", "Chennai", "Nellore", "Gurgaon", "Hyderabad"]
        for gen in range(num_of_emp):
            emp_id = random.randint(1, 999)
            emp_location = random.choice(locations)
            emp_sal = random.randint(20000, 150000)

            yield f"Emp Id: {emp_id} , Emp Location: {emp_location} , Emp Salary: {emp_sal} "

except ValueError:
    print("Enter valid number")

emp_list_generator = generate_emp_details(Number_of_emp)

for gen in range(Number_of_emp):
    print(next(emp_list_generator))

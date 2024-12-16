# Define the dataset as a dictionary
dataset = {
    "123-45-6789": {
        "first_name": "John",
        "last_name": "Doe",
        "address": "123 Main St"
    },
    "234-56-7890": {
        "first_name": "Jane",
        "last_name": "Smith",
        "address": "456 Elm St"
    },
    "345-67-8901": {
        "first_name": "Bob", 
        "last_name": "Johnson",
        "address": "789 Oak St"
    }
}

last_four_digits = input("Enter last 4 digits: ")
# Loop through the dataset and print last name and last 4 digits of SSN
for ssn, info in dataset.items():
    if ssn[-4:] == last_four_digits:
        print("The last name is",info["last_name"])
    

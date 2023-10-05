import csv
import random

# Initialize an empty dictionary to store client information
client_data = {}

# Define the admin password
admin_password = "9761"

# Define the file name for storing client data
file_name = "bank_data.csv"

# Function to generate a three-digit account number
def generate_account_number(client_number):
    return f"{client_number}{random.randint(10, 99)}"

# Function to add a new client
def add_client():
    client_number = len(client_data) + 1
    account_number = generate_account_number(client_number)
    password = input("Enter a password for the new client: ")
    initial_balance = float(input("Enter the initial balance for the new client: "))
    client_data[account_number] = {"Client Number": client_number, "Password": password, "Balance": initial_balance}
    print(f"Client created successfully. Account Number: {account_number}, Client Number: {client_number}, Password: {password}")

# Function to remove a client
def remove_client(account_number):
    if account_number in client_data:
        del client_data[account_number]
        print(f"Client with Account Number {account_number} removed successfully.")
    else:
        print("Client not found.")

# Function to change password
def change_password(account_number, old_password, new_password):
    if account_number in client_data:
        if client_data[account_number]["Password"] == old_password:
            client_data[account_number]["Password"] = new_password
            print("Password changed successfully.")
        else:
            print("Incorrect old password.")
    else:
        print("Client not found.")

# Function to display balance
def display_balance(account_number):
    if account_number in client_data:
        print(f"Account Balance: {client_data[account_number]['Balance']}")
    else:
        print("Client not found.")

# Function to deposit money
def deposit_money(account_number, amount):
    if account_number in client_data:
        client_data[account_number]["Balance"] += amount
        print("Deposit successful.")
    else:
        print("Client not found.")

# Function to withdraw money
def withdraw_money(account_number, amount):
    if account_number in client_data:
        if client_data[account_number]["Balance"] >= amount:
            client_data[account_number]["Balance"] -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")
    else:
        print("Client not found.")

# Function to save client data to a CSV file
def save_to_csv():
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Account Number", "Client Number", "Password", "Balance"])
        for account_number, data in client_data.items():
            writer.writerow([account_number, data["Client Number"], data["Password"], data["Balance"]])

# Function to load client data from a CSV file
def load_from_csv():
    try:
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                account_number = row["Account Number"]
                client_number = int(row["Client Number"])
                password = row["Password"]
                balance = float(row["Balance"])
                client_data[account_number] = {"Client Number": client_number, "Password": password, "Balance": balance}
    except FileNotFoundError:
        pass

# Function to handle client operations
def handle_client():
    while True:
        print("\nClient Menu:")
        print("1. Change Password")
        print("2. Display Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Logout")
        client_choice = input("Enter your choice: ")
        if client_choice == "1":
            old_password_input = input("Enter old password: ")
            if old_password_input != client_data[account_number]["Password"]:
                print("Incorrect old password.")
                continue
            new_password = input("Enter new password: ")
            change_password(account_number, password, new_password)
        elif client_choice == "2":
            display_balance(account_number)
        elif client_choice == "3":
            amount = float(input("Enter the amount to deposit: "))
            deposit_money(account_number, amount)
        elif client_choice == "4":
            amount = float(input("Enter the amount to withdraw: "))
            withdraw_money(account_number, amount)
        elif client_choice == "5":
            save_to_csv()  # Save data before exiting
            break  # Exit the client menu
        else:
            print("Invalid choice.")

# Load existing data from CSV file if available
load_from_csv()

while True:
    print("\nBank Application Menu:")
    print("1. Admin")
    print("2. Client")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        admin_password_input = input("Enter the admin password: ")
        if admin_password_input == admin_password:
            while True:
                print("\nAdmin Menu:")
                print("1. Add a Client")
                print("2. Remove a Client")
                print("3. Logout")
                admin_choice = input("Enter your choice: ")
                if admin_choice == "1":
                    add_client()
                elif admin_choice == "2":
                    account_number = input("Enter the account number to remove: ")
                    remove_client(account_number)
                elif admin_choice == "3":
                    break
                else:
                    print("Invalid choice.")

    elif choice == "2":
        print("\nClient Login:")
        account_number = input("Enter your account number: ")
        password = input("Enter your password: ")
        if account_number in client_data and client_data[account_number]["Password"] == password:
            handle_client()  # Call the client menu function
        else:
            print("Invalid account number or password.")

    elif choice == "3":
        save_to_csv()
        print("Exiting the application. Data saved.")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

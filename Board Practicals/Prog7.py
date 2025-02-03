import csv

# Create a csv file by entering user-id and password, read and search the password for given user-id
def create_csv(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "password"])
        while True:
            user_id = input("Enter user-id (or 'exit' to stop): ")
            if user_id.lower() == 'exit':
                break
            password = input("Enter password: ")
            writer.writerow([user_id, password])

def search_password(file_path, search_user_id):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == search_user_id:
                return row[1]
    return None

file_path = 'user_data.csv'
create_csv(file_path)
search_user_id = input("Enter user-id to search for password: ")
password = search_password(file_path, search_user_id)
if password:
    print(f"Password for user-id '{search_user_id}' is: {password}")
else:
    print(f"No password found for user-id '{search_user_id}'")
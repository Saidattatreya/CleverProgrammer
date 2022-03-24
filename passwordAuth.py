import getpass

database = {"Datta Padal":"123456", "Datta Padal1":"789012", "Datta Padal2":"345678"}
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Incorrect password. Please try again: ")
        break
print('Verified')

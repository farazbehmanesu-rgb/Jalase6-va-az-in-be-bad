#با کمک هوش مصنوعی برای سرعت بخشیدن و دی باگینگ نوشته شده
# Class User

class User:
    def __init__(self, username, password, email, status):
        self.username = username
        self.password = password
        self.email = email
        self.status = status

    def to_format(self):
        return self.username + "|" + self.password + "|" + self.email + "|" + self.status

    def __str__(self):
        return "User: " + self.username


# Class FileManager

class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.users = []
        self.read_users()

    # Khandan file

    def read_users(self):
        self.users = []

        try:
            file = open(self.filename, "r")

            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    user = User(data[0], data[1], data[2], data[3])
                    self.users.append(user)

            file.close()

        except FileNotFoundError:
            file = open(self.filename, "w")
            file.close()
            print("File sakhte shod")

    # Peyda kardan user

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user

        return None

    # Ezafe kardan user

    def add_user(self, username, password, email, status):

        if self.find_user(username) != None:
            print("Username tekrari ast")
            return

        if status != "active" and status != "blocked":
            print("Status eshtebah ast")
            return

        user = User(username, password, email, status)

        self.users.append(user)

        file = open(self.filename, "a")
        file.write(user.to_format() + "\n")
        file.close()

        print("User ba movafaghiat ezafe shod")

    # Hazf user

    def delete_user(self, username):

        user = self.find_user(username)

        if user == None:
            print("User peyda nashod")
            return

        self.users.remove(user)

        file = open(self.filename, "w")

        for user in self.users:
            file.write(user.to_format() + "\n")

        file.close()

        print("User hazf shod")

    # Taghir status

    def update_status(self, username, status):

        if status != "active" and status != "blocked":
            print("Status eshtebah ast")
            return

        user = self.find_user(username)

        if user == None:
            print("User peyda nashod")
            return

        user.status = status

        file = open(self.filename, "w")

        for user in self.users:
            file.write(user.to_format() + "\n")

        file.close()

        print("Status taghir kard")

    # Login

    def login(self, username, password):

        user = self.find_user(username)

        if user == None:
            print("Username peyda nashod")

        elif user.password != password:
            print("Password eshtebah ast")

        elif user.status == "blocked":
            print("Account shoma block shode ast")

        else:
            print("Login ba movafaghiat anjam shod")

    # Report

    def generate_report(self):

        active_count = 0
        blocked_count = 0

        for user in self.users:
            if user.status == "active":
                active_count += 1

            elif user.status == "blocked":
                blocked_count += 1

        print("Active Users:", active_count)
        print("Blocked Users:", blocked_count)


# Sakht object

manager = FileManager("users.txt")


# Menu

while True:

    print("\n========== USER MANAGEMENT ==========")
    print("1. Add User")
    print("2. Find User")
    print("3. Delete User")
    print("4. Update Status")
    print("5. Login")
    print("6. Generate Report")
    print("7. Exit")

    entekhab = input("Choose an option: ")

    if entekhab == "1":

        username = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")
        status = input("Status (active/blocked): ")

        manager.add_user(username, password, email, status)

    elif entekhab == "2":

        username = input("Username: ")

        user = manager.find_user(username)

        if user != None:
            print(user)
            print(user.to_format())
        else:
            print("User peyda nashod")

    elif entekhab == "3":

        username = input("Username: ")

        manager.delete_user(username)

    elif entekhab == "4":

        username = input("Username: ")
        status = input("New status (active/blocked): ")

        manager.update_status(username, status)

    elif entekhab == "5":

        username = input("Username: ")
        password = input("Password: ")

        manager.login(username, password)

    elif entekhab == "6":

        manager.generate_report()

    elif entekhab == "7":

        print("Goodbye!")
        break

    else:
        print("Entekhab eshtebah ast")

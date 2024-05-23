class User():
    def __init__(self,first_name,last_name,logi_attempts = 0):
        self.first = first_name
        self.last = last_name
        self.logi_attempts = logi_attempts

    def describe_user(self):
        full_name = f"{self.first} {self.last}"
        print(f"User: {self.first} {self.last}")
    def greeting(self):
        print(f"Hello {self.first} {self.last}")
    def  increment_login_attempts(self,increment):
        self.logi_attempts += increment
    def reset_login_attempts(self):
        self.logi_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name,priviliges, logi_attempts=0):
        super().__init__(first_name, last_name, logi_attempts)
        self.priviliges = priviliges
    def show_priviliges(self):
        print(self.priviliges)
class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

    def show_privileges(self):
        """Prints the privileges of the admin."""
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
# Creating instances and testing
user1 = User("John", "Doe")
user2 = User("Alice", "Smith")
user1.describe_user()
user1.greeting()
user2.describe_user()
user2.greeting()

admin = Admin("Admin", "Adminovich",[["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]])
admin.describe_user()

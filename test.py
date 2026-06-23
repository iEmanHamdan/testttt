# Data Access Layer
class DataAccessLayer:
    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

# Business Logic Layer
class BusinessLogicLayer:
    def __init__(self, dal):
        self.dal = dal

    def add_user(self, user_id, user_name):
        if not user_id or not user_name:
            raise ValueError("Invalid user data")
        self.dal.set(user_id, user_name)

    def get_user(self, user_id):
        return self.dal.get(user_id)

# Presentation Layer
class PresentationLayer:
    def __init__(self, bll):
        self.bll = bll

    def display_user(self, user_id):
        user = self.bll.get_user(user_id)
        if user:
            print(f"User ID: {user_id}, User Name: {user}")
        else:
            print("User not found!")

    def add_user_interface(self, user_id, user_name):
        try:
            self.bll.add_user(user_id, user_name)
            print("User added successfully!")
        except ValueError as e:
            print(e)

# Example usage:
dal = DataAccessLayer()
bll = BusinessLogicLayer(dal)
pl = PresentationLayer(bll)

pl.add_user_interface("1", "Alice")
pl.display_user("1")

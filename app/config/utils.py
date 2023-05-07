from os import path

# Hide Passwords and Hosts...
DB_URL = f"sqlite:///{path.abspath('.')}/database.sqlite"

print(DB_URL)
import os
from .user import User

class UserManager:
	def __init__(self):
		self.users = {}
		self.current_user = None
		self.users_text_filepath = ""
		self.load_users()

	def load_users(self):
		current_dir = os.path.dirname(os.path.abspath(__file__))
		root_dir = os.path.dirname(current_dir)
		folder_name = "data"
		new_folder_path = os.path.join(root_dir, folder_name)
		os.makedirs(new_folder_path, exist_ok=True)

		user_text_filename = "users.txt"
		self.users_text_filepath = os.path.join(new_folder_path, user_text_filename)

		file = open(self.users_text_filepath, 'w')
		file.close() # comment if want to keep old users

	def save_users(self, username, password):
		self.users[username] = User(username, password)

		with open(self.users_text_filepath, 'a') as file: 
			file.write(f"{username}, {self.users[username].password}\n")
			

	def validate_username(self, username):
		if len(username) < 4:
			print("Username must be at least 4 characters long.")
			return False
		if username in self.users:
			print("Username already exists.")
			return False
		return True

	def validate_password(self, password):
		if len(password) < 8:
			print("Username must be at least 8 characters long.")
			return False
		return True

	def register(self):
		while True:
			print("\nRegistration")
			username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
			if not username: return	
			if not self.validate_username(username): continue
		
			password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
			if not password: return
			if not self.validate_password(password): continue

			break

		self.save_users(username, password)
		print("Registration complete.")
		
		return

	def login(self):
		while True:
			print("\nLogin")
			username = input("Enter username, or leave blank to cancel: ")
			if not username: return	
			if username not in self.users:
				print("Username does not exist.")
				continue
		
			password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
			if not password: return
			if password != self.users[username].password:
				print("Incorrect password.")
				continue

			break

		self.current_user = username
		print("Logged in")
		
		return	

	
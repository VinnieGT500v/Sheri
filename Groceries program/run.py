import os
import os.path
from os import listdir

class Groceries:
	def __init__(self):
		#1. Add new Grocery list
		#2. Delete Grocery list
		#3. Edit Grocery list
		pass

	def new_list(self):
		print("creating new list...\n")
		file_name = input("Give the file a name: ")
		while(True):
			if os.path.exists(os.getcwd()+"/Lists/{}.txt".format(file_name)):
				print("This file name is already used. Please give a new name")
				file_name = input("Give the file a name: ")
			else: 
				print("You can use this name")
				break
		print("Add items to your list\n")
		f = open(os.getcwd()+"/Lists/{}.txt".format(file_name), "w")
		while(True):
			item=input("Add Item: ")
			if item == "done":
				break
			else: 
				f.write(item + "\n")
		f.close()
		print("Successfully created the {}.txt list".format(file_name))

	def delete_list(self):
		print("delete one of the following list(s)\n")
		while(True):
			count = 0 
			count_end = 0
			file_list = {}
			for x in os.listdir(os.getcwd()+"/Lists/"):
				count += 1
				file_list.update({count:x})
			count_end = count + 1
			for x in file_list:
				print("\t{}.\t{}".format(x,file_list[x]))
			print("\t{}.\tgo back".format(count_end))
			choice = int(input("list number: "))
			if choice < 1 or choice > count_end:
				print("Invalid option. Please choose one of the options listed above")
			elif choice == count_end:
				break
			else:
				os.remove(os.getcwd() + "/Lists/{}".format(file_list[choice]))

		#for x in os.listdir(os.getcwd()+"/Lists/"):
			#print(x)

	def edit_list(self):
		print("edit one of the following list(s)\n")

	def close_program(self):
		exit() 	

	def run_interface(self):
		print("Choose one of the following options \n")
		print("\t1.Add new Grocery list\n\t2.Delete Grocery list\n\t3.Edit Grocery list\n\t4.Close Program\n")
		choice=int(input("Option: "))
		if choice < 1 or choice > 4:
			print("Please select a valid option")
			self.run_interface()
		if choice == 1:
			self.new_list()
			self.run_interface()
		elif choice == 2:
			self.delete_list()
			self.run_interface()
		elif choice == 3:
			self.edit_list()
			self.run_interface()
		elif choice == 4:
			self.close_program()
			self.run_interface()

start=Groceries()
start.run_interface()
#!/usr/bin/python

import sys, argparse
import os, json

DB = "~/.things_config"
to_do = {"items":[]}

def load_todo():
	global to_do
	global DB
	if(os.path.exists(DB)):
		with open(DB, 'r') as content_file:
			content = content_file.read()
			try:
				to_do = json.loads(content)
				#print(to_do)
				#exit()
			except:
				return False
		return True
	else:
		print("config file not found")
		return False

def write_todo():
	with open(DB, 'w+') as outfile:
		json.dump(to_do, outfile)

def clear_screen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def add_item():
	clear_screen()
	item = input("Enter Item Description:\n >> ")
	if(item != ""):
		to_do["items"].append(item)
		write_todo()
	else:
		input("Cannot add empty item (Press Enter)")
	printmenu()

def remove_item():
	clear_screen()
	list_all()
	r_num = input("Enter Number of Item to Remove\n >> ")
	if(int(r_num) <= len(to_do["items"]) and int(r_num) > 0):
		to_do["items"].pop(int(r_num)-1)
		write_todo()
	else:
		input("{} is out of range (press Enter)".format(r_num))
	printmenu()

def edit_item():
	clear_screen()
	list_all()
	e_num = input("Enter Number of Item to Edit\n >> ")
	if(int(e_num) <= len(to_do["items"]) and int(e_num) > 0):
		new_desc = input("Enter Replacement\n >> ")
		to_do["items"][int(e_num) -1 ] = new_desc
		write_todo()
	else:
		input("{} is out of range (press Enter)".format(r_num))
	printmenu()

def list_all():
	if len(to_do["items"]) > 0:
		print("To Do\n-------------")
		i = 1
		for item in to_do["items"]:
			print("{}. {}".format(i, item))
			i+=1
		print('')

def exec_choice(choice):
	if choice == 0:
		clear_screen()
		exit()
	elif choice == 1:
		add_item()
	elif choice == 2:
		remove_item()
	elif choice == 3:
		edit_item()
	else:
		print("Choice: {} is not valid".format(choice))


def printmenu():
	clear_screen()

	print(r""" 
  ________    _                 
 /_  __/ /_  (_)___  ____ ______
  / / / __ \/ / __ \/ __ `/ ___/
 / / / / / / / / / / /_/ (__  ) 
/_/ /_/ /_/_/_/ /_/\__, /____/  
                  /____/        
	""")

	list_all()

	print("Menu\n-------------")
	print("1. Add")
	print("2. Remove")
	print("3. Edit")
	print("0. Exit")
	choice = input(" >>  ")
	exec_choice(int(choice))

def main():
	home = os.path.expanduser('~')
	global DB
	DB = os.path.join(home, ".things_config")
	load_todo()
	printmenu()


if __name__ == "__main__":
	main()
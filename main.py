import os, time

title = "🌟Life Organizer!!🌟"
list = []

def printList():
  os.system("clear")
  print(f"{title:^50}\n")
  menu_options = {
      1: addItem,
      2: viewItem,
      3: edit,
      4: remove
  }
  menu = int(input(
      "What do you want to do?\n 1:add\n 2:view\n 3:edit\n 4:remove\n\n enter no.:> "
  ))
  if menu in menu_options:
      menu_options[menu]()

def addItem():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ").capitalize()
  date = input("Due Date > ").capitalize()
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  list.append(row)
  print("Added")

def viewItem():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in list:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in list:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  input("Press Enter to continue...")

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
  found = False
  for row in list:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in list:
    if find in row:
      list.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  list.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in list:
    if find in row:
      list.remove(row)

while True:
  printList()
  print()
  ask = input("Are you done(yes/no) ? > ").lower()
  if ask in ["y", "yes"]:
    break
  else:
    continue
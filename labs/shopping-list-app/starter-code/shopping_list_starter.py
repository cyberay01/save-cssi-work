#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")
    
    choice = raw_input("Enter your choice [a|b|c|d|e]:")
    
    # Your code below! Handle the cases when the user chooses a, b, c, d, or e
    if choice == 'a':
        add = raw_input("Enter what item to add: ")
        shopping_list.append(add)
    elif choice == 'b':
        rm = raw_input("Enter what item to remove: ")
        if rm in shopping_list:
            shopping_list.remove(rm)
        else:
            print("Item not found.")
    elif choice == 'c':
        check = raw_input("Enter what item to check")
        if check in shopping_list:
            print("The item is in the list.")
        else:
            print("Item not found.")
    elif choice == 'd':
        for item in shopping_list:
            print(item)
    else:
        print("Choose from choices a~e.")
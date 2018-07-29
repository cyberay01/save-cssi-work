import time

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

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
        self.transaction_list = []

    def __str__(self):
        return "Label: %s\nBalance: %0.2f" % (self.label, self.balance)

    def withdraw(self, amount):
        if amount < self.balance and amount > 0:
            self.balance -= amount
            trans = Transaction("Withdraw", amount)
            self.transaction_list.append(trans)
        else:
            print("Insert valid amount.")
        return
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            trans = Transaction("Deposit", amount)
            self.transaction_list.append(trans)
        else:
            print("Insert valid amount.")
        return
    
    def rename(self, new_label):
        if new_label != "" and not new_label.isspace():
            self.label = new_label
        else:
            print("Insert valid label")
        return

    def transfer(self, dest_acc, amount):
        if(amount < self.balance and amount <= dest_acc.balance and amount > 0):
            self.balance -= amount
            dest_acc.balance += amount
            trans = Transaction("Transfer", amount, dest_acc)
            self.transaction_list.append(trans)
            dest_acc.transaction_list.append(trans)

    def show_trans_list(self, index=None):
        list_instring = []
        if index is None:
            for i in self.transaction_list:
                list_instring.append(str(i))
            return list_instring
        else:
            return str(self.transaction_list[index])
        
    
class Transaction(object):
    def __init__(self, trans_type, amount, dest_acc=None):
        self.time = time.asctime( time.localtime(time.time()) )
        self.trans_type = trans_type
        self.amount = amount
        self.dest_acc = dest_acc
    
    def __str__(self):
        if self.dest_acc != None:
            return "<%(timestamp)s>: %(trans_type)s %(amount)0.2f to account %(dest_acc)s\n" % {"timestamp": self.time, "trans_type": self.trans_type, "amount": self.amount, "dest_acc": self.dest_acc.label}
        else:
            return "<%(timestamp)s>: %(trans_type)s %(amount)0.2f\n" % {"timestamp": self.time, "trans_type": self.trans_type, "amount": self.amount}

acc = BankAccount("test",1000)
acc2 = BankAccount("test2", 600)
acc.transfer(acc2,200)
print(acc.show_trans_list())
acc.deposit(400)
print(acc.show_trans_list())
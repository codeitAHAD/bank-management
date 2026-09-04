import json
import string
import random
from pathlib import Path






class Bank:

    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else :
            print("no such file exists")        

    except Exception as err:
        print(f"an exception occured as {err}")


    @classmethod
    def __update(cls):
        with open (cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k = 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return"".join(id)

    def Createaccount(self):
        try:
            info = {
                "name": input("tell your name:-"), 
                "age" : int(input("tell your age :- ")),
                "email" : input("tell yout email"),
                "pin" : int(input("tell your 4 digit pin")),
                "accountNo." : Bank.__accountgenerate(),
                "balance" : 0

            }
            

            if info['age'] < 18 or len(str(info['pin'])) != 4:
                print("sorry you cannot create your account")
            else :
                print("account has been created successfully") 
                for i in info:
                    print(f"{i} : {info[i]}")
                print("please note down your account number")

                Bank.data.append(info)

                Bank.__update()

        except Exception as err:
            print(f"an error occured as {err}")
        

    def depositmoney(self):
        try:
            accnumber = input("please tell your account number")
            pin = int(input("please tell your pin as well"))

            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i ['pin'] == pin]

            if userdata == False:
                print("sorry no data found")
            else:
                amount = int(input("how much you want to deposit"))

                if amount > 10000 or amount < 0:
                    print("the amount is too much you can deposit below 10000 and above zero")
                else :
                    userdata[0]['balance'] += amount
                    Bank.__update()
                    print("amount deposited successfully")

        except Exception as err:
            print(f"an error as {err}")
            
        

    def withdrawmoney(self):
        try:
            accnumber = input("please tell your account number")
            pin = int(input("please tell your pin as well"))

            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i ['pin'] == pin]

            if userdata == False:
                print("sorry no data found")
            else:
                amount = int(input("how much you want to withdraw"))
                if userdata[0]['balance'] < amount:
                    print("sorry you dont have that much money")

                else :
                    userdata[0]['balance'] -= amount
                    Bank.__update()
                    print("amount withdraw successfully")
        
        except Exception as err:
            print(f"an error occured as {err}")
        

    def showdetails(self):
        try:
            accnumber = input("please tell your account number")
            pin = int(input("please tell your pin as well"))

            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i ['pin'] == pin]
            print("your information are \n\n\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

        except Exception as err:
            print(f"an error occured as {err}")



    def updatedetails(self):
        try:
            accnumber = input("please tell your account number")
            pin = int(input("please tell your pin as well"))

            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i ['pin'] == pin]


            if userdata == False:
                print("no such user found")

            else:
                print("you cannot change the age , account number ,balance")

                print("fill the details for change or leave it empty if no change")


                newdata = {
                    "name" : input("please tell new name or press enter:- "),
                    "email" : input("please tell your new email or press enter to skip:- "),
                    "pin" :input("enter new pin or press enter to skip:- ")
                }
            
                if newdata["name"] == "":
                    newdata["name"] = userdata[0]["name"]
                
                if newdata["email"] == "":
                    newdata["email"] = userdata[0]["email"]

                if newdata["pin"] == "":
                    newdata["pin"] = userdata[0]["pin"]

                newdata['age'] = userdata[0]['age']

                newdata['accountNo.'] = userdata[0]['accountNo.']

                newdata['balance'] = userdata[0]['balance']

                if type(newdata['pin']) == str:
                    newdata['pin'] = int (newdata['pin'])

                for i in newdata:
                    if newdata [i] == userdata[0][i]:
                        continue
                    else :
                        userdata[0][i] = newdata[i]

                Bank.__update()
                print("details updated successfully")
        
        except Exception as err:
            print(f"an error occured as {err}")

    def delete(self):
        try:
            accnumber = input("please tell your account number:- ")
            pin = int(input("please tell your pin as well:- "))

            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i ['pin'] == pin]


            if userdata == False:
                print("sorry no such data exist")

            else :
                check = input("press y if you actually want yo delete the account ot press n")

                if check == 'n' or check == "N":
                    print("bypassed")
                
                else:
                    index = Bank.data.index(userdata[0])
                    Bank.data.pop(index)

                    print(" account deleted successfully")
                    Bank.__update()

        except Exception as err:
            print(f"an error occured as {err}")


user = Bank()

while True:
    print("press 1 for creating an account:- ")
    print("press 2 for deposit money in the bank:- ")
    print("press 3 for withdraw money:- ")
    print("press 4 for details:- ")
    print("press 5 for updating the details:- ")
    print("press 6 for deleting your account:- ")

    check = int(input(" tell your response:- "))

    if check == 1:
        user.Createaccount()

    if check == 2:
        user.depositmoney()

    if check == 3:
        user.withdrawmoney()

    if check == 4:
        user.showdetails()   

    if check == 5:
        user.updatedetails()

    if check == 6:
        user.delete()
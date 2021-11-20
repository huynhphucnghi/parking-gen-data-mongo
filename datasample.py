import random
import time

import names

timenow = 0
UserList = []



for i in range(10):
    User = {}
    User["ID"] = i
    User["username"] = names.get_last_name()
    User["password"] = ''.join(random.sample(User["username"],len(User["username"])))
    User["email"] = User["username"] + "@gmail.com"
    timenow += random.randint(0, 100)
    User["rstTime"] = timenow
    UserList.append(User)

print(UserList)

import json
employee=eval(input('Enter your Data{}'))
#eval is by default understance our input
str=json.dumps(employee)
#d=json.load(str)
with open('jsondata.txt','w') as f
#with meaans it will close  byitself
    f.write(str)
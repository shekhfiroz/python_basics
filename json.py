
import json
employee=eval(input('Enter your Data{}'))
#eval is by default understance our input
str=json.dumps(employee)
#with means it will close  byitself
with open('json_input_data','w') as file:
    file.write(str)
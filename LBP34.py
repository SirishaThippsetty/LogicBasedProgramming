'''
Email name should be starts with alphabet and should follw by number or 
underscore. 
It should contains either numbers or underscore finally ends with @gmail.com 
only, 
Then given email id is true otherwise false.
input ------> email id
constraint -> lowercase alphabet [a-z] followed by underscore or digit and 
gmail.com
output -----> true or false

'''
import re
m = re.fullmatch("[a-z]+[0-9|_]@gmail[.]com",input())
print("true" if m!=None else "false")
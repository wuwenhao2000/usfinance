# abc = {1:'abc',2:'def'}
# print (abc[1])
# import time
# print (time.ctime(1567641600)) # earnings
# print (time.ctime(1567641600))
# print (time.ctime(1567641600))
# print (time.strftime("%Y%m%d%H%M%S", time.localtime()))
import os
import json
import time
import pprint
one = "SE"
json_file = "{}_{}.json".format(one,time.strftime("%Y%m%d", time.localtime())) # today's variable file
target_json = "{}/{}".format(one,json_file) # today's variable file with relative path

with open(target_json,'r') as load_f: # get the variable from .json file
  curr_var = json.loads(json.dumps(eval(load_f.read()))) # transfer the variable from string -> json -> dict
pprint.pprint (curr_var)
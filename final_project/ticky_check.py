#!/usr/bin/env python3

import re
import operator
import sys
error = {}
per_user = {}

file_to_read=sys.argv[1]

def process():
    with open(file_to_read) as f:
        lines = f.readlines()
        for line in lines:
            result,msg,user = return_error_info(line.strip())
            if per_user.get(user) is None:
                per_user[user]={"error":0,"info":0}

            if result == "error":
                error[msg]=error.get(msg,0)+1
                per_user[user]["error"]=per_user[user]["error"]+1
        
            if result == "info":
                per_user[user]["info"]=per_user[user]["info"]+1
                
        f.close()
        sorted_error = sorted(error.items(),key=operator.itemgetter(1),reverse=True)
        sorted_per_user = sorted(per_user.items())
        print(sorted_error)
    


def return_error_info(line):
    print(line)
    success = re.search(r"ticky: INFO ([\w ]*).*(\([\w\.]*\))$",line)
    if success is not None:
        return "info",success.group(1),re.sub("[\(\)]",'',success.group(2))
    error = re.search(r"ticky: ERROR ([\w ]*).*(\([\w\.]*\))$",line)
    if error is not None:
        return "error",error.group(1),error.group(2)
    else:
        print("falle para "+line)


process()

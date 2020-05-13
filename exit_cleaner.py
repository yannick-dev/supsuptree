import json
import logging
import os
import collections

def cleaner(printer_que, upload_que):
    try:
        with open('printer_que.json', 'a') as file:
            file.write("{ \"data\":[")
            while printer_que:
                file.write(json.dumps(printer_que.popleft()))
                if printer_que:
                    file.write(",")
            file.write("]}")
        file.close()
    except IOError:
        logging.debug("CLEANER: could not save printer_que")



def revive_ques(printer_que, upload_que):
    try:
        with open('printer_que.json', 'r') as file:
            data = json.load(file)
            for dictionary in data["data"]:
                printer_que.append(dictionary)
        file.close()
        os.remove("printer_que.json")
    except IOError:
        logging.debug("REVIVE_QUES: no printer que to revive")


a  = {
    "hashcode": "abcdefg",
    "owner": "0",
    "data": "abcdf"
}

b = {
    "hashcode": "abcdefg",
    "owner": "0",
    "data": "abcdf"
}


que0 = collections.deque()
que0.append(a)
que0.append(b)
print(que0)

que1 = collections.deque()



status = cleaner(que0, que1 )

que1 = collections.deque()
que2 = collections.deque()

status = revive_ques(que1, que2)
print(str(que1), str(que2))


import json
import logging
import os


def cleaner(printer_que, upload_que):
    try:
        with open('printer_que.json', 'a') as file:
            file.write("{ \"data\":[")
            while printer_que:
                file.write(json.dumps(printer_que.popleft()))
                if printer_que:
                    file.write(",")
            file.write("]}")
    except IOError:
        logging.debug("CLEANER: could not save printer_que")
    try:
        with open('upload_que.json', 'a') as file:
            file.write("{ \"data\":[")
            while printer_que:
                file.write(json.dumps(printer_que.popleft()))
                if printer_que:
                    file.write(",")
            file.write("]}")
    except IOError:
        logging.debug("CLEANER: could not save upload_que")




def revive_ques(printer_que, upload_que):
    try:
        with open('printer_que.json', 'r') as file:
            data = json.load(file)
            for dictionary in data["data"]:
                printer_que.append(dictionary)
        os.remove("printer_que.json")
    except IOError:
        logging.debug("REVIVE_QUES: no printer que to revive")
    try:
        with open('upload_que.json', 'r') as file:
            data = json.load(file)
            for dictionary in data["data"]:
                printer_que.append(dictionary)
        os.remove("upload_que.json")
    except IOError:
        logging.debug("REVIVE_QUES: no upload que to revive")

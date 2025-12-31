import json
from colorama import Fore

def get_task_data():
   name  = input("Task Name: ")
   desc  = input("Task Description: ")
   data = {'name' : name , 'desc' : desc , 'is_finished' : "False"}
   return data


def readFile():
   with open('./data/tasks.json' , "r") as f:
      read = json.load(f)
      return read
   

def writeFile(data):
   try:
      with open('./data/tasks.json' , "w") as f:
         write = json.dump(data , f , indent=2)
         if write == None :
            return True
         else :
            return False
   
   except Exception as e :
      print(e)
   

def print_dict_format(data ,couter):
   print(f"{Fore.BLUE}==========> Task({couter})")
   for key,value in data.items():
      print(f'{Fore.YELLOW}{key} : {Fore.GREEN}{value}')

from datetime import datetime
from utils import get_task_data , writeFile , readFile


def selecAllTask ():
   data = readFile()
   return data



def addTask():
   data = get_task_data()
   id = len(readFile()) if len(readFile()) > 0 else 1
   now= datetime.now()
   create_at = now.strftime("%d/%m/%Y %I:%M %p")
   data.update({"id" : id , "create_at" : create_at})
   alltask = list(selecAllTask())
   alltask.append(data)
   return writeFile(alltask)




def removeTask(name):
   tasks = list(selecAllTask())
   newTasks = [x for x in tasks if x.get("name") != name]
   return writeFile(newTasks)









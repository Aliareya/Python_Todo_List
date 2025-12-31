from colorama import Fore 
from tasks import selecAllTask ,addTask ,removeTask
from utils import print_dict_format

sugges = """Write this to continue:
1 for Add Task
2 for Remove Task
3 for See all Task
0 for Stop App
"""
print(sugges)
choice = ''
while choice != "0":
   choice = input(f"{Fore.WHITE}Enter your choice (1/2/3/0): ") 
   if choice == "1" :
      if addTask() :
         print(f"{Fore.GREEN}Task Add Successfully....")
      else:
         print(f"{Fore.YELLOW}Feild To Add Task. Please Try Again Later.")

   elif choice == "2":
      name = input("Inter Task Name: ")
      if removeTask(name) :
         print(f"{Fore.GREEN}Task Remove Successfully....")
      else:
         print(f"{Fore.YELLOW}Feild To Remove Task. Please Try Again Later.")


   elif choice == "3":
      tasks = selecAllTask()
      couter = 0
      for task in tasks :
         couter+=1
         print_dict_format(task , couter)
      
   elif choice == "0":
      print("Thank you for using the app. Goodbye!")

   else:
      print(f"{Fore.RED} You Inetr Invalide Key.")
      print(f"{Fore.GREEN}{sugges}")








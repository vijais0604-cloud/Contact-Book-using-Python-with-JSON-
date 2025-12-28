import json
def load_contact():
    try:
     with open("contacts.json","r") as f:
         return json.load(f)
    except FileNotFoundError:
        return {} 
def save_contact():
    with open("contacts.json","w") as f:
        json.dump(book,f,indent=4)    
         
book=load_contact()
class contacts:
    def __init__(self,name):
        self.name=name
    def create(self,number):
        self.num=number
        if self.name in book:
            print("\nContact already exsist")
            return
        book[name]=self.num
        print(f"\n\n{self.name}:{self.num}\n")
        print("\n Contact added\n")
        save_contact()
    def delete(self):
        if self.name in book:
            print(f"\n\n{self.name}:{book[name]}\n")
            book.pop(self.name,None)
            print("\nContact deleted\n")
            save_contact()
            return
        print("\nContact not found\n")     
    def search(self):
        if self.name in book:
            print(f"\n\n{self.name}:{book[name]}\n")
            return
        print("\ncontact not found\n")      
while(1):           
 print("\n 1) Search contact \n 2) Add contact \n 3) Delete contact \n 4) Exit")
 vin=int(input("\nenter the option:"))
 match vin:
     case 1:
         name=input("\nEnter name: ")
         a=contacts(name)
         a.search()
     case 2:
         name=input("\nEnter name: ")
         number=input("\nEnter number: ")
         a=contacts(name)
         a.create(number)
     case 3:
         name=input("\nEnter name: ")
         a=contacts(name)
         a.delete()
     case 4:
         break    
     case _:
         print("\nInvalid option\n")




            


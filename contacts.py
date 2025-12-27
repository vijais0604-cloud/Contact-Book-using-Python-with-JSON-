import json
def load_contact():
    try:
     with open("contacts.json","r") as f:
         return json.load(f)
    except FileNotFoundError:
        return [] 
def save_contact():
    with open("contacts.json","w") as f:
        json.dump(book,f,indent=4)    
         
book=load_contact()
class contacts:
    def __init__(self,name):
        self.name=name
    def create(self,number):
        self.num=number
        for n in book:
            if n["name"]==self.name or n["number"]==self.num:
                print("\nContact already exsist")
                return
        book.append({"name":self.name,"number":self.num})
        print(f"\n{self.name}:{self.num}\n")
        print("\n Contact added\n")
        save_contact()
    def delete(self):
        for n in book:
            if n["name"] == self.name:
               print(f"\n{self.name}:{n["number"]}\n")
               book.remove(n)
               print("\nContact deleted\n")
               save_contact()
               return
        print("\nContact not found\n")     
    def search(self):
        for n in book:
            if n["name"] == self.name:
                print(f"\n{self.name}:{n["number"]}\n")
                return
        print("\ncontact not found\n")      
while(1):           
 print("\n 1) Search contact \n 2) Add contact \n 3) Delete contact \n 4) Exit")
 vin=int(input("\nenter the option:"))
 match vin:
     case 1:
         name=input("\nEnter name: \n")
         a=contacts(name)
         a.search()
     case 2:
         name=input("\nEnter name: \n")
         number=input("\nEnter number: \n")
         a=contacts(name)
         a.create(number)
     case 3:
         name=input("\nEnter name: \n")
         a=contacts(name)
         a.delete()
     case 4:
         break    
     case _:
         print("\nInvalid option\n")



            


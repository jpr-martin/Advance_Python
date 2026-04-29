"""Sample code for simple class and object creation with 
constructor and method with some opertions on the data members of the class"""

# Author: Raj_Joseph
class Fruits:

    def __init__(self,n1,n2,n3=None,n4=None):
        self.n1=n1
        self.n2=n2
        self.n3=n4
        self.n4=n4

    def fruit_names(self):
        a=[self.n1,self.n2,self.n3,self.n4]
        fruits={"Apple":220,"Grapes":150,"Orange":180,"Dates":100}


        amt=0
        namelist=[]
        print(f"\n \nGiven Fruits are:\n----------------\n")
        for n in a:

            if n is not None:
                namelist.append(n)
                amt+=fruits[n]
                print(f"{n}: {fruits[n]}")
       
        
        print(f"Total Amount: {amt}\n\n")



obj=Fruits('Apple','Grapes')
obj.fruit_names()

print("\n***********End of the program***********")

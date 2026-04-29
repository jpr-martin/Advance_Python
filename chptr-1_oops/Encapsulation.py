"""Sample code for simple class and object creation with 
constructor and method with some opertions on the data members of the class"""

# Author: Raj_Joseph
class Fruits:

    def __init__(self,n1,n2,n3=None,n4=None):
        self.__gst=18 #private variable
        self._sst=5 #protected variable
        self.n1=n1 #public variable
        self.n2=n2 #public variable
        self.n3=n3 #public variable
        self.n4=n4 #public variable 

    def fruit_names(self): #public method
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
    
    def fruit_names_withTaxes(self): #public method
        a=[self.n1,self.n2,self.n3,self.n4]
        fruits={"Apple":220,"Grapes":150,"Orange":180,"Dates":100}

        amt=0
        namelist=[]
        print(f"\n \nGiven Fruits are:\n----------------\n")
        for n in a:

            if n is not None:
                namelist.append(n)
                amt+=fruits[n]+(fruits[n]*self.__gst/100)+(fruits[n]*self._sst/100)
                print(f"{n}: {fruits[n]} + GST: {(fruits[n]*self.__gst/100)} + SST: {(fruits[n]*self._sst/100)} = {fruits[n]+(fruits[n]*self.__gst/100)+(fruits[n]*self._sst/100)}")
        print(f"Total Amount with Taxes: {amt}\n\n")

    def get_gst(self): #public method to access private variable
        return self.__gst
    
    def __taxOnly(self): #private method
        return self.__gst + self._sst


#Normally, we can access the public variable:
obj=Fruits('Apple','Grapes')
obj.fruit_names()    
obj.fruit_names_withTaxes()

#Normally, we can access the protected variable:
print(f"Accessing protected variable: {obj._sst}")  
       
#Error, we cannot access the private variable:
try:
    print(f"Accessing private variable: {obj.__gst}")   
except Exception as e:
    print(f"\n*****Access Private VariableError:*****\n {e}\n****************\n")  

#Error, we cannot access the private method:
try:    
    print(f"Accessing private method: {obj.__taxOnly()}")       
except Exception as e:
    print(f"\n***** Accessing private method Error:*****\n {e}\n****************\n")

#Anothere Way, We can access the private variable using name mangling:
print(f"Accessing private variable using name mangling(__gst): {obj._Fruits__gst}")
print(f"Accessing Private variable using public method (__gst): {obj.get_gst()}") #Accessing private variable using public method    
 
print(f"Accessing private method using name mangling(__taxOnly): {obj._Fruits__taxOnly()}") #Accessing private method using name mangling


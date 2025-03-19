#object oriented programming
# l=[2,3,4,2,32]
# l.upper() #it encounters a error list attribute has object upper
#python is full on object
#it is made it simplicity of code
#OOP -Object,class,polymorphism,encapsulation,inheritance,abstraction
#Class is Blueprint HAr koi object class ka hota hai
a=[2]
print(type(a))
#a.append() # yeh ek function hai joh ki l ek object hai list class ka toh jab humna a. dala toh itna sara option joh aaya uska mtlb hai ki l object list class mai sai kya kya utha skta hai 

# class has two data(property) or functions(behavior)
#class ka naam should be in pascal case means Thisispascalcase first letter capital
# thisiscamelcase means first letter small
# snake_case means it is like snake

#Function ek aise cheej hai joh sab jagah define hai 
#method ek aise cheej hai joh class mai define hai
class Atm:

    def __init__(self) :  #magic methhod hai isko object call nhi karta        #init is a special function or constructor
         self.pin=''
         self.balance=0
         self.menu()
    def menu(self):
         user_input=input('''
Hello How could you like to proceed?
                          1.enter 1 your pin
                          2.enter 2 your deposit
                          3.enter 3 your withdraw
                          4.enter 4 your check balance
                          5. enter 5 to exit
        ''')
         if user_input=='1':
              self.create_pin()
         elif user_input=='2':
              self.deposit()
         elif user_input=='3':
              self.withdraw()
         elif user_input=='4':
              self.check_balance()
         else:
              print("bye")
    def create_pin(self):
         self.pin=input("enter your pin")
         print("pin set successfull")
          
    def deposit(self):
         temp=input("entery your Pin")
         if temp==self.pin:
              amount=int(input("enter your amount"))
              self.balance=self.balance+amount
              print("Deposit Successful")
         else:
              print("invalid pin")
        
    def withdraw(self):
         temp=input("enter your pin")
         if temp==self.pin:
              amount=int(input("enter the amount"))
              if amount<=self.balance:
                   self.balance=self.balance-amount
                   print("operation succesful") 
              else:
                   print("Low Balance")
         else:
              print("invalide pin")

    def check_balance(self):
         temp=input("enter your pin")
         if temp==self.pin:
              print(self.balance)
         else:
              print("invalide pin")
        
atm=Atm()


#CREATE NEW DATATYPE
class Fraction:
     def __init__(self,n,d):
          self.num = n
          self.den = d
     def __str__(self):#peint aayega toh yeh apna apna aaap call ho jayega
          return "{}/{}".format(self.num,self.den)  
     def __add__(self,other):
          temp_num=self.num*other.den +other.num*self.den
          temp_den=self.den*other.den
          return "{}/{}".format(temp_num,temp_den)
     def __sub__(self,other):
          temp_num=self.num*other.den -other.num*self.den
          temp_den=self.den*other.den
          return "{}/{}".format(temp_num,temp_den)
     def __mul__(self,other):
          temp_num=self.num*other.num 
          temp_den=self.den*other.den
          return "{}/{}".format(temp_num,temp_den)
     def __truediv__(self,other):
          temp_num=self.num*other.den
          temp_den=self.num*other.den

          return "{}/{}".format(temp_num,temp_den)
b = Fraction(5,4)
c= Fraction(4,3)
print(b+c)
print(b-c)
print(b*c)
print(b/c)

#def __sub__(self,other) to subtract
#def __mul__(self,other) to multiply


#ENCLAPSULATION
# Private karne kai liya __ use karta hai
#Nothing in python is truly is private

class Atm:

    def __init__(self) :  #magic methhod hai isko object call nhi karta        #init is a special function or constructor
         self.__pin=''
         self.__balance=0
         self.menu()
    def get_pin(self):
         return self.__pin
    def set_pin(self,new_pin):
         self.__pin=new_pin
    
    def menu(self):
         user_input=input('''
Hello How could you like to proceed?
                          1.enter 1 your pin
                          2.enter 2 your deposit
                          3.enter 3 your withdraw
                          4.enter 4 your check balance
                          5. enter 5 to exit
        ''')
         if user_input=='1':
              self.create_pin()
         elif user_input=='2':
              self.deposit()
         elif user_input=='3':
              self.withdraw()
         elif user_input=='4':
              self.check_balance()
         else:
              print("bye")
    def create_pin(self):
         self.__pin=input("enter your pin")
         print("pin set successfull")
          
    def deposit(self):
         temp=input("entery your Pin")
         if temp==self.__pin:
              amount=int(input("enter your amount"))
              self.__balance=self.__balance+amount
              print("Deposit Successful")
         else:
              print("invalid pin")
        
    def withdraw(self):
         temp=input("enter your pin")
         if temp==self.__pin:
              amount=int(input("enter the amount"))
              if amount<=self.__balance:
                   self.__balance=self.__balance-amount
                   print("operation succesful") 
              else:
                   print("Low Balance")
         else:
              print("invalide pin")

    def check_balance(self):
         temp=input("enter your pin")
         if temp==self.__pin:
              print(self.__balance)
         else:
              print("invalide pin")
        
atm=Atm()
y=atm.get_pin()
print(y)


#Parking Space


class Car:
    no_of_cars = 0

    #Constructoor
    def __init__(self):
        self.vehicle = []

    #New Arrival addition 
    def new_arrival(self,slot,carNo,time):
        individual = (True,slot,carNo,time)
        self.vehicle.append(individual)
        self.no_of_cars += 1

    #Return the no of cars parked
    def no_cars_parked(self):
        return len(self.vehicle)

    #Return the filled in slots
    def filled_space(self):
        fill_space = []
        for i in range(len(self.vehicle)):
            if  self.vehicle[i][0]:
                fill_space.append(self.vehicle[i][1])
                fill_space.sort()
        return fill_space

    #Departure deletion
    def departure(self,slot):
        f = 0
        fill_space = []
        for i in range(len(self.vehicle)):
            if  self.vehicle[i][1]==slot:
                f = 1
                self.vehicle[i] = list(self.vehicle[i])
                self.vehicle[i][0] = False
                self.vehicle[i] = tuple(self.vehicle[i])
                parking_space.delete(i)
                break
        if(f==0):
            print("This Slot doesnot exist")

    #Delete the index for further arrival
    def delete(self, i):
        self.vehicle.remove(self.vehicle[i])

    #Clear the Entries  
    def clear(self):
        self.vehicle = []

#Composition
class Salary:

    def __int__(self):
        self.sal = 0

    def day_sal(self,hr):
        if(hr <= 5 & hr > 0):
            self.sal = 250.00
        elif(hr>5):
            ot = hr - 5
            self.sal = 250.00 + ot*75.0
        return self.sal
        

class Employee:

    def __init__(self,bonus,hr):
        self.bonus = bonus
        self.pay = Salary()
        self.sal = self.pay.day_sal(hr)
        self.total_pay = 0

    def month_sal(self):
        self.total_pay = self.sal + self.bonus
        return self.total_pay

    #Operator Overloading
    def __add__(self,other):
        return self.total_pay + other.total_pay
    


#Login Page
print("\t\t-------------------------------------------------")
print("\t\t+          >> Vehicle Parking Space <<          +")
print("\t\t-------------------------------------------------")

print("\n\t LET'S MOVE ON.....")
j = input("\t Press Enter to Continue.... ")

user = input("\n\t\tEnter the UserName : ")
if(user == "ParkSimple"):
    password = input("\t\tEnter the Password : ")
else:
    print("\t\tInvalid UserName")
    exit()

if(password == "Python"):

    #Object Creation
    parking_space = Car()

    #Parked vehicle details
    parking_space.new_arrival("2","TN-66-C-2284","09-05-2021 09:30:15")
    parking_space.new_arrival("3","TN-38-AP-0754","09-05-2021 10:35:43")
    parking_space.new_arrival("7","TN-37-S-0943","09-05-2021 13:10:46")
    parking_space.new_arrival("5","TN-67-X-3260","09-05-2021 14:17:28")

    #Check for Vehicles parked in slots
    print("\nNumber of vehicles currently Parked")
    print(parking_space.no_cars_parked())
    print("Parking Slots that are filled")
    print(parking_space.filled_space())


    #Entry of new arrival
    print("\nNew Arrival")
    no = input("Enter the Slot No : ")
    carNo = input("Enter the Car No(TN-xx-x-xxxx) : ")
    time = input("Enter the Time of Arrival(dd-mm-yy hr:min:sec) : ")
    parking_space.new_arrival(no,carNo,time)

    #Check for Vehicles Parked after arrival
    print("\nNumber of vehicles Parked after a Arrival")
    print(parking_space.no_cars_parked())
    print("Parking Slots that are filled")
    print(parking_space.filled_space())


    #Departure entry
    print("\nDeparture")
    slot = input("Enter the slot from which vehicle Departures : ")
    parking_space.departure(slot)

    #Check for slots after departure
    print("\nNumber of vehicles Parked after Departure")
    print(parking_space.no_cars_parked())
    print("Parking Slots that are filled")
    print(parking_space.filled_space())

    print("\nTotal number of cars parked till date : ",parking_space.no_of_cars)

    #Clear details
    parking_space.clear()


    #Thank you page
    print("\n\t\t-------------------------------------------------")
    print("\t\t+              >> Thank You !!! <<              +")
    print("\t\t-------------------------------------------------")


    print("\nEmployee Salary Calculation")
    hr1 = int(input("\nEnter the no of hours worked by Employee 1 : "))
    bonus1 = int(input("Enter the Bonus Amount for Employee 1 : "))
    emp1 = Employee(bonus1,hr1)
    sal1 = emp1.month_sal()
    print("\nTotal Salaray for Employee 1 is ",sal1,"Rs")


    hr2 = int(input("\nEnter the no of hours worked by Employee 2 : "))
    bonus2 = int(input("Enter the Bonus Amount for Employee 2 : "))
    emp2 = Employee(bonus2,hr2)
    sal2 = emp2.month_sal()
    print("\nTotal Salaray for Employee 2 is ",sal2,"Rs")


    sal = sal1 + sal2
    print("\nTotal Amount the Owner has to Give is : ",sal,"Rs")

else:
    print("\t\tInvalid Password")
    exit()
    

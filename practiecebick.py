class Bikerent:
    def __init__(self,stock=0):
        self.stock=stock
    def Display(self):
        print("we have avalable only {} bikes to rent".format(self.stock))
    def rentBikeonhourlybase(self,bikes,hours):
        if bikes<=0:
            print("number of bikes should be positive")
            return None
        elif bikes>self.stock:
            print("sorry! we have only {} bikes are avalable".format(self.stock))
        else:
            print("we have rented {} bikes on {} hours ".format(bikes,hours))
            self.stock=self.stock-bikes
            print("per hour bike rent is 3rupees")
            print("your paying amount is=",bikes*hours*3)

    def rentBikeondaywise(self,bike,days):
        if bike<=0:
            print("no of Bikes should be positive")
        elif bike>self.stock:
            print("sorry! we have only {} bikes are avalable".format(self.stock))
        else:
            print("we have rented {} bikes on {} days".format(bike,days))
            self.stock=self.stock-bike
            print("per day bike rent is 30rupees")
            print("your paying amount is=",bike*days*30)



a=Bikerent(10)
a.Display()
print("enter your options to bike rent days or hours")
print("D-days\n","h-hours")
options=input("choose your options=")
if options=="d" or options=="D":
    bike=int(input("enter your required bikes= "))
    days=int(input("enter your required days="))
    a.rentBikeondaywise(bike,days)
elif options=="h" or options=="H":
    bike = int(input("enter your required bikes= "))
    hours = int(input("enter your required hours="))
    a.rentBikeonhourlybase(bike,hours)


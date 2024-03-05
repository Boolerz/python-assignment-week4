#Base class
class Vehicle:
    def Vehicle_info(self):
        print('Insude Vehicle class')
        
#child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

#child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')
    
#create object of SportsCar
s_car=SportsCar()

#access Vehicle's and Car info using Sportscar object
s_car.Vehicle_info('My Vehicle is brand:')
s_car.car_info('Color Gray')
s_car.sports_car_info('cost 2k')
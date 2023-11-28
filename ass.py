class Car:
    def __init__(self,registration_number,maximum_speed):
        self.registration_number=registration_number
        self.maximum_speed=maximum_speed
        self.current_speed=0
        self.travelled_distance=0

    def accelerate(self,change_speed):
        if 0<=(self.current_speed+change_speed)<=self.maximum_speed:
            self.current_speed += change_speed
    def drive(self,time):
        self.travelled_distance+=time*self.current_speed

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed,capbattery):
        self.capbattery=capbattery
        super().__init__(registration_number, maximum_speed)

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed,voltank):
        self.voltank=voltank
        super().__init__(registration_number, maximum_speed)

car15=ElectricCar("ABC-15", 180, 52.5)
car123=GasolineCar("ACD-123", 165, 32.3)
car15.accelerate(90)
car15.drive(3)
print(f"travelled distance:{car15.travelled_distance}km")
car123.accelerate(95)
car123.drive(3)
print(f"travelled distance:{car123.travelled_distance}km")



car1=Car("ABC-123", 142)
print(f"registration number: {car1.registration_number}, maximum speed: {car1.maximum_speed}km/h")
car1.accelerate(+30)
print(f"current speed:{car1.current_speed}km/h")
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate(-200)
print(f"current speed:{car1.current_speed}km/h")
car1.accelerate(200)
car1.drive(1.5)
print(f"travelled distance:{car1.travelled_distance}km")
car2=Car("ABC-234",90)
car2.accelerate(40)
car2.drive(2.5)
print(f"travelled distance:{car2.travelled_distance}km")


cars=[]
for i in range(10):
    cars.append(Car("ABC-"+str(i+1),random.randint(100,200)))

traveldis_max=0
while traveldis_max<10000.:
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.drive(1.)
        traveldis_max=max(car.travelled_distance,traveldis_max)

for car in cars:
    print(f"{car.registration_number},{car.maximum_speed},{car.travelled_distance},{traveldis_max}")
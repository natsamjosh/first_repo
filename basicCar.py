class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def accelerate(self, footPressure):
        return (footPressure * self.engine)

class SUV(Car):
    def calculateCargo(self, l, w, h):
        print("Hello")
        self.space = l * w * h
        return self.space

class Supercar(Car):
    def calculatePowerScore(self, hp, torque):
        self.powerScore = hp + torque
        return self.powerScore

def ipValidate(ipAddr):
    ipOctets = ipAddr.split(".")
    if len(ipOctets) != 4:
        return False
    for octet in ipOctets:
        if int(octet) > 255:
            return False
    return True


car1 = Car("Chevy", 454)
pressure = 12             #psi
acceleration = car1.accelerate(pressure)
print (str(acceleration))

suv2 = SUV("Blazer", 300)
print(str(suv2.calculateCargo(5, 4, 3)))

sc1 = Supercar("Vette", 454)
print(str(sc1.calculatePowerScore(600, 625)))

if ipValidate("2.128.90.344"):
    print("Ip address is valid")
else:
    print("BADDDDD")
    print("Ip address is invalid")




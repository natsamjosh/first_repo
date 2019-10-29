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

suv2 = SUV("Chevy", 454)
l = 5
w = 4
h = 3
print(str(suv2.calculateCargo(l, w, h)))

if ipValidate("2.128.90.344"):
    print("Ip address is valid")
else:
    print("Ip address is invalid")




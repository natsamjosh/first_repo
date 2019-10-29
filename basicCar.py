class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def accelerate(self, footPressure):
        return (footPressure * self.engine)

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

if ipValidate("2.128.90.344"):
    print("Ip address is valid")
else:
    print("Ip address is invalid")




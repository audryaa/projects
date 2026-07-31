#POLYMORPHISM
#IT allows us to use the same method name for different types of objects
#IS WHEREBY ONE METHOD NAME CAN HAVE DIFFERENT BEHAVIOURS DEPENDING ON THE OBJECT USING IT

class Man:
    def language(self):
        print("Man speaks")

class Khoikhoi(Man):
    def language(self):
        print("click sounds")

class Kamba(Man):
    def language(self):
        print("Kikamba")

#creating objects
khoikhoi = Khoikhoi()
kamba = Kamba()

khoikhoi.language()
kamba.language()
import math
import random

class vector2 :          
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def set(self, x, y) :
        self.x = x
        self.y = y

    def lengthSquared(self):
        return self.x*self.x + self.y*self.y;
        
    def length(self):
        return math.sqrt(self.lengthSquared())

    def __mul__(self, other):
        return m.mulVector2(self)
    
    def __truediv__(self, other): 
        self.x /= other
        self.y /= other
        return self

    def __add__(self, other):
        v = vector2()
        v.x = other.x + self.x
        v.y = other.y + self.y
        return v
    
    def __sub__(self, other):
        v = vector2()
        v.x = self.x - other.x
        v.y = self.y - other.y
        return v
    
    def __isub__(self, other):  #-=
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __iadd__(self, other): #+=
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other): #*=
        self.x *= other
        self.y *= other
        return self
    
    def __idiv__(self, other): #/=
        self.x /= other
        self.y /= other
        return self
        
    def __str__(self):  #__str__ method is what happens when you print it
        return "(%f,%f)" % (self.x, self.y)
    
    def __repr__(self): #__repr__ method is what happens when you use the repr() function (or when you look at it with the interactive prompt)
        return "(%f,%f)" % (self.x, self.y)
        
    def normalize(self):
        len = self.length()
        if len == 0 :
            self.x = 0
            self.y = 0
            return
            
        self.x = self.x/len
        self.y = self.y/len

    def getRandomVector(self):
        self.x = random.uniform(-1, 1)
        self.y = random.uniform(-1, 1)

    def getRandomUnitVector(self):
        self.getRandomVector()
        self.normalize()
                
    def dot(self, v) :
        return self.x * v.x + self.y * v.y           

    def dot2(self, x, y) :
        return self.x * x + self.y * y        
        
    def getRotateCW90(self):
        v = vector2()
        v.x = self.y
        v.y =  -self.x
        return v

    def getRotateCCW90(self):
        v = vector2()
        v.x = -self.y
        v.y = self.x
        return v
        
    def getAreaRH(self, b): #signed area, right handed
        return (self.x*b.y) - (self.y*b.x);
                
    def getAreaLH(self, b): #signed area, left handed
        return -(self.x*b.y) + (self.y*b.x);

        
class vector3 :          
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def set(self, x, y, z) :
        self.x = x
        self.y = y
        self.z = z
        
    #def __init__(self, x, y, z):       #python thinks overloading constructor is a bad idea?
    #    self.x = x
    #    self.y = y
    #    self.z = z
        
    def lengthSquared(self):
        return self.x*self.x + self.y*self.y + self.z*self.z;
        
    def length(self):
        return math.sqrt(self.lengthSquared())
        
    def __mul__(self, other):
        return other.mulVector3(self)
    
    def __truediv__(self, other): 
        self.x /= other
        self.y /= other
        self.z /= other
        return self
    
    def __add__(self, other):
        v = vector3()
        v.x = self.x + other.x
        v.y = self.y + other.y
        v.z = self.z + other.z
        return v
    
    def __sub__(self, other):
        v = vector3()
        v.x = self.x - other.x
        v.y = self.y - other.y
        v.z = self.z - other.z
        return v
    
    def __isub__(self, other):  #-=
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    
    def __iadd__(self, other): #+=
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
        
    def __imul__(self, other): #*=
        self.x *= other
        self.y *= other
        self.z *= other
        return self
    
    def __idiv__(self, other): #/=
        self.x /= other
        self.y /= other
        self.z /= other 
        return self
        
    def __str__(self):  #__str__ method is what happens when you print it
        return "(%f,%f,%f)" % (self.x, self.y, self.z)
    
    def __repr__(self): #__repr__ method is what happens when you use the repr() function (or when you look at it with the interactive prompt)
        return "(%f,%f,%f)" % (self.x, self.y, self.z)
        
    def normalize(self):
        len = self.length()
        if len == 0 :
            self.x = 0
            self.y = 0
            self.z = 0
            return
            
        self.x = self.x/len
        self.y = self.y/len
        self.z = self.z/len
                
    def getRandomVector(self):
        self.x = random.uniform(-1, 1)
        self.y = random.uniform(-1, 1)
        self.z = random.uniform(-1, 1)

    def getRandomUnitVector(self):
        self.getRandomVector()
        self.normalize()
                
    def dot(self, v) :
        return self.x * v.x + self.y * v.y + self.z * v.z           

    def dot3(self, x, y, z) :
        return self.x * x + self.y * y + self.z * z           
        
    def cross(self, b):
        v = vector3()
        v.x = (self.y * b.z) - (self.z * b.y);
        v.y = (self.z * b.x) - (self.x * b.z);
        v.z = (self.x * b.y) - (self.y * b.x);
        return v
        

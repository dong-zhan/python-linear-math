

import math
import random

class vector3 :          
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        
    def lengthSquared(self):
        return self.x*self.x + self.y*self.y + self.z*self.z;
        
    def length(self):
        return math.sqrt(self.lengthSquared())
        
    def __mul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self
    
    def __truediv__(self, other): 
        self.x /= other
        self.y /= other
        self.z /= other
        return self
    
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    
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
            self.x = None
            self.y = None
            self.z = None
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

    def cross(self, b):
        v = vector3()
        v.x = (self.y * b.z) - (self.z * b.y);
        v.y = (self.z * b.x) - (self.x * b.z);
        v.z = (self.x * b.y) - (self.y * b.x);
        return v
        
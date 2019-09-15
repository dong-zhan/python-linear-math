import math
import random

import vector
from vector import vector3
from vector import vector2

class matrix22 :          
    def __init__(self):
        self.v = [vector2(), vector2()]     #why not use self.m???

    def __str__(self):  #__str__ method is what happens when you print it
        return "(%f,%f)\n(%f,%f)\n" % (self.v[0].x, self.v[0].y,
        self.v[1].x, self.v[1].y)
    
    def __repr__(self): #__repr__ method is what happens when you use the repr() function (or when you look at it with the interactive prompt)
        return "(%f,%f)\n(%f,%f)\n" % (self.v[0].x, self.v[0].y,
        self.v[1].x, self.v[1].y)

    def mulMatrix(self, m1, m2) :
        x = m1.v[0].x;
        y = m1.v[0].y;
        self.v[0].x = (m2.v[0].x*x)+(m2.v[1].x*y);
        self.v[0].y = (m2.v[0].y*x)+(m2.v[1].y*y);
        x = m1.v[1].x;
        y = m1.v[1].y;
        self.v[1].x = (m2.v[0].x*x)+(m2.v[1].x*y);
        self.v[1].y = (m2.v[0].y*x)+(m2.v[1].y*y);
        
    def mulVector2(self, v):
        r = vector2()
        r.x = v.dot2(self.v[0].x, self.v[1].x)
        r.y = v.dot2(self.v[0].y, self.v[1].y)
        return r    
    
    def __mul__(self, v):
        argClass = v.__class__.__name__
        if argClass == 'vector2' :
            return self.mulVector2(v)
        elif argClass == 'matrix22' :
            m = matrix22()
            m.mulMatrix(self, v)
            return m
            
    def rotateCCW(self, angle) :    
        sinA = math.sin(angle)
        cosA = math.cos(angle)
        self.v[0].set(cosA, sinA)
        self.v[1].set(-sinA, cosA)
 
    def rotateCW(self, angle) :    
        sinA = math.sin(angle)
        cosA = math.cos(angle)
        self.v[0].set(cosA, -sinA)
        self.v[1].set(sinA, cosA) 

class matrix33 :          
    def __init__(self):
        self.v = [vector3(), vector3(), vector3()]

    def __str__(self):  #__str__ method is what happens when you print it
        return "(%f,%f,%f)\n(%f,%f,%f)\n(%f,%f,%f)" % (self.v[0].x, self.v[0].y, self.v[0].z,
        self.v[1].x, self.v[1].y, self.v[1].z,
        self.v[2].x, self.v[2].y, self.v[2].z)
    
    def __repr__(self): #__repr__ method is what happens when you use the repr() function (or when you look at it with the interactive prompt)
        return "(%f,%f,%f)\n(%f,%f,%f)\n(%f,%f,%f)" % (self.v[0].x, self.v[0].y, self.v[0].z,
        self.v[1].x, self.v[1].y, self.v[1].z,
        self.v[2].x, self.v[2].y, self.v[2].z)
        
    def transpose(self):
        pass        #TODO: not done
        
    def mulMatrix(self, m1, m2) :
        x = m1.v[0].x;
        y = m1.v[0].y;
        z = m1.v[0].z;
        self.v[0].x = (m2.v[0].x*x)+(m2.v[1].x*y)+(m2.v[2].x*z);
        self.v[0].y = (m2.v[0].y*x)+(m2.v[1].y*y)+(m2.v[2].y*z);
        self.v[0].z = (m2.v[0].z*x)+(m2.v[1].z*y)+(m2.v[2].z*z);
        x = m1.v[1].x;
        y = m1.v[1].y;
        z = m1.v[1].z;
        self.v[1].x = (m2.v[0].x*x)+(m2.v[1].x*y)+(m2.v[2].x*z);
        self.v[1].y = (m2.v[0].y*x)+(m2.v[1].y*y)+(m2.v[2].y*z);
        self.v[1].z = (m2.v[0].z*x)+(m2.v[1].z*y)+(m2.v[2].z*z);
        x = m1.v[2].x;
        y = m1.v[2].y;
        z = m1.v[2].z;
        self.v[2].x = (m2.v[0].x*x)+(m2.v[1].x*y)+(m2.v[2].x*z);
        self.v[2].y = (m2.v[0].y*x)+(m2.v[1].y*y)+(m2.v[2].y*z);
        self.v[2].z = (m2.v[0].z*x)+(m2.v[1].z*y)+(m2.v[2].z*z);
        
    def mulVector3(self, v) :
        r = vector3()
        r.x = v.dot3(self.v[0].x, self.v[1].x, self.v[2].x)
        r.y = v.dot3(self.v[0].y, self.v[1].y, self.v[2].y)
        r.z = v.dot3(self.v[0].z, self.v[1].z, self.v[2].z)
        return r
        
    def __mul__(self, v):
        argClass = v.__class__.__name__
        if argClass == 'vector3' :
            return self.mulVector3(v)
        elif argClass == 'matrix33' :
            m = matrix33()
            m.mulMatrix(self, v)
            return m
                
    def rotateXCW(self, angle) :    
        sinA = math.sin(angle)
        cosA = math.cos(angle)
        self.v[0].set(1, 0, 0)
        self.v[1].set(0, cosA, sinA)
        self.v[2].set(0, -sinA, cosA)

    def rotateXCCW(self, angle) :    
        sinA = math.sin(angle)
        cosA = math.cos(angle)
        self.v[0].set(1, 0, 0)
        self.v[1].set(0, cosA, -sinA)
        self.v[2].set(0, sinA, cosA)
        
    def rotateYCW(self, angle) :        
        sinA = math.sin(angle)
        cosA = math.cos(angle)
        self.v[0].set(cosA, 0, -sinA)
        self.v[1].set(0,    1,  0)
        self.v[2].set(sinA, 0, cosA)       

    def rotateYCCW(self, angle) :       
        sinA = math.sin(angle)
        cosA = math.cos(angle)
        self.v[0].set(cosA, 0, sinA)
        self.v[1].set(0, 1, 0)
        self.v[2].set(-sinA, 0, cosA)       
        
    def rotateZCW(self, angle) :        
        sinA = math.sin(angle)
        cosA = math.cos(angle)
        self.v[0].set(cosA, sinA, 0)
        self.v[1].set(-sinA, cosA, 0)
        self.v[2].set(0,    0,      1)

    def rotateZCCW(self, angle) :       
        sinA = math.sin(angle)
        cosA = math.cos(angle)
        self.v[0].set(cosA, -sinA, 0)
        self.v[1].set(sinA, cosA, 0)
        self.v[2].set(0, 0, 1)
        
    def test(self) :
        m1 = matrix33()
        m2 = matrix33()
        m1.rotateX(2.22)
        m2.rotateY(3.33)
        m = matrix33()
        m.mulMatrix(m1,m2)
        v = vector3()
        v.set(1,1,1)
        v = m*v
        print(v)

    

        

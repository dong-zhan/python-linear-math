# python-vector-math
python vector math

sample usage in idle python 3.6.3 Shell.

>>> v = vector3()
>>> v.getRandomUnitVector()
>>> v
(-0.527931,0.673797,0.516998)
>>> vb = vector3()
>>> vb.getRandomUnitVector()
>>> vb
(-0.740618,0.248610,0.624242)
>>> a = v.dot(vb)
>>> a
0.8812398232913854
>>> b = v.cross(vb)
>>> b
(0.292081,-0.053341,0.367777)

hope you find this useful!

from pickle import Pickler
import pickle
"""
We create our custom Pickle Class
"""
class ScrappyPickler(Pickler):
    def __init__(self, file = None, protocol = None):
        Pickler.__init__(self, file, protocol)
    """
    We're going to overload the methot dump, and get the "dump" and get the data of the last state of the object
    that we want to save.
    Then we going to get Pickler class Method.
    """
    def dump(self, obj):
        obj = obj.getAttributes() 
        return Pickler.dump(self, obj)
"""
We create a Class to Pickling.
"""
class TestObject(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def getModu(self):
        return self.a % self.b
    def getSubstr(self):
        return self.a - self.b
    def getAttributes(self):
        return {
            'variableA': self.a,
            'variableB':self.b,
            'methodA': self.getModu.__name__,
            'methodB': self.getSubstr.__name__
        } # we return the serialized data to get in pickle.dump

testObj = TestObject(4, 8) #Object that we going to serliaze, to save the last state.
"""
We save the object in the file serialized.xyz
"""
with open("serialized.xyz", "wb") as x:
    pi = ScrappyPickler(x)
    pi.dump(testObj)
"""
We open the serialized.xyz and then we going load again the object.
"""
with open("serialized.xyz", "rb") as y:
 data = pickle.load(y)
 print type(data), data

"""
We going to load load the arguments of that data and show it.
"""
testObjLastState = TestObject(data['variableA'], data['variableB']) 
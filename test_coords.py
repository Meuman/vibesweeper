from coords import *
class Test TestCoordsModule(unittes.TestCase):
    def test_00point(self):
        self.assert({(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,0),(1,1),(1,-1)})
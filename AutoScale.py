import bge
from collections import OrderedDict

class AutoScale(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ("Scale Limit",5.9),
    ("Invert",True),
    ("Transform Type",{"Local","World"}),
    ])

    def start(self, args):
        self.scale = args["Scale Limit"]
        self.transf = args["Transform Type"]
        self.invert = args["Invert"]

    def update(self):
        if self.transf == "World":
            if self.invert == False:
                if self.object.worldScale.x < self.scale:
                    self.object.worldScale.x += 0.1
                if self.object.worldScale.y < self.scale:
                    self.object.worldScale.y += 0.1
                if self.object.worldScale.z < self.scale:
                    self.object.worldScale.z += 0.1
            if self.invert == True:
                if self.object.worldScale.x > -self.scale:
                    self.object.worldScale.x -= 0.1
                if self.object.worldScale.y > -self.scale:
                    self.object.worldScale.y -= 0.1
                if self.object.worldScale.z > -self.scale:
                    self.object.worldScale.z -= 0.1
        if self.transf == "Local":
            if self.invert == False:
                if self.object.localScale.x < self.scale:
                    self.object.localScale.x += 0.1
                if self.object.localScale.y < self.scale:
                    self.object.localScale.y += 0.1
                if self.object.localScale.z < self.scale:
                    self.object.localScale.z += 0.1
            if self.invert == True:
                if self.object.localScale.x > -self.scale:
                    self.object.localScale.x -= 0.1
                if self.object.localScale.y > -self.scale:
                    self.object.localScale.y -= 0.1
                if self.object.localScale.z > -self.scale:
                    self.object.localScale.z -= 0.1
                
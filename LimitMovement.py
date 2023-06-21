import bge
from collections import OrderedDict

class LimitMovement(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ("Limit X",0.0),
    ("Limit Y",0.0),
    ("Limit Z",0.0),
    ("Limit Type",{"Teleport","Block"}),
    ])

    def start(self, args):
        self.limitX = args["Limit X"] * 2
        self.limitY = args["Limit Y"] * 2
        self.limitZ = args["Limit Z"] * 2
        self.limit_tp = args["Limit Type"]

    def update(self):
        if self.limit_tp == "Teleport":
            if self.limitX != 0.0:
                if self.object.worldPosition.x > self.limitX:
                    self.object.worldPosition.x = -self.limitX
                elif self.object.worldPosition.x < -self.limitX:
                    self.object.worldPosition.x = self.limitX
            if self.limitY != 0.0:
                if self.object.worldPosition.y > self.limitY:
                    self.object.worldPosition.y = -self.limitY
                elif self.object.worldPosition.y < -self.limitY:
                    self.object.worldPosition.y = self.limitY
            if self.limitZ != 0.0:
                if self.object.worldPosition.z > self.limitZ:
                    self.object.worldPosition.z = -self.limitZ
                elif self.object.worldPosition.z < -self.limitZ:
                    self.object.worldPosition.z = self.limitZ
        if self.limit_tp == "Block":
            if self.limitX != 0.0:
                if self.object.worldPosition.x > self.limitX:
                    self.object.worldPosition.x = self.limitX
                elif self.object.worldPosition.x < -self.limitX:
                    self.object.worldPosition.x = -self.limitX
            if self.limitY != 0.0:
                if self.object.worldPosition.y > self.limitY:
                    self.object.worldPosition.y = self.limitY
                elif self.object.worldPosition.y < -self.limitY:
                    self.object.worldPosition.y = -self.limitY
            if self.limitZ != 0.0:
                if self.object.worldPosition.z > self.limitZ:
                    self.object.worldPosition.z = self.limitZ
                elif self.object.worldPosition.z < -self.limitZ:
                    self.object.worldPosition.z = -self.limitZ

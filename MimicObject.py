import bge
from collections import OrderedDict
from mathutils import Vector, Matrix

class MimicObject(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ("Target Name",""),
    ("Fix Type",{"Position","Rotation","Rotation And Position"}),
    ("Transform Type",{"Local","World"}),
    ("Axe X",False),
    ("Axe Y",False),
    ("Axe Z",False),
    ])

    def start(self, args):
        self.axe_x = args["Axe X"]
        self.axe_y = args["Axe Y"]
        self.axe_z = args["Axe Z"]
        self.fix_type = args["Fix Type"]
        self.target = args["Target Name"]
        self.transformType = args["Transform Type"]

    def update(self):
        if self.target in self.object.scene.objects:
            target_axe = self.object.scene.objects[self.target]
            if self.fix_type == "Position":
                if self.axe_x == True:
                    if self.transformType == "Local":
                        self.object.localPosition.x = target_axe.localPosition.x
                    elif self.transformType == "World":
                        self.object.worldPosition.x = target_axe.worldPosition.x
                if self.axe_y == True:
                    if self.transformType == "Local":
                        self.object.localPosition.y = target_axe.localPosition.y
                    elif self.transformType == "World":
                        self.object.worldPosition.y = target_axe.worldPosition.y
                if self.axe_z == True:
                    if self.transformType == "Local":
                        self.object.localPosition.z = target_axe.localPosition.z
                    elif self.transformType == "World":
                        self.object.worldPosition.z = target_axe.worldPosition.z
            if self.fix_type == "Rotation":
                if self.axe_x == True:
                    if self.transformType == "Local":
                        x_axe = self.object.localOrientation.to_euler()
                        x_axe2 = target_axe.localOrientation.to_euler()
                        x_axe[0] = x_axe2[0]
                        self.object.localOrientation = x_axe.to_matrix()
                    elif self.transformType == "World":
                        x_axe = self.object.worldOrientation.to_euler()
                        x_axe2 = target_axe.worldOrientation.to_euler()
                        x_axe[0] = x_axe2[0]
                        self.object.worldOrientation = x_axe.to_matrix()
                if self.axe_y == True:
                    if self.transformType == "Local":
                        y_axe = self.object.localOrientation.to_euler()
                        y_axe2 = target_axe.localOrientation.to_euler()
                        y_axe[1] = y_axe2[1]
                        self.object.localOrientation = y_axe.to_matrix()
                    elif self.transformType == "World":
                        y_axe = self.object.worldOrientation.to_euler()
                        y_axe2 = target_axe.worldOrientation.to_euler()
                        y_axe[1] = y_axe2[1]
                        self.object.worldOrientation = y_axe.to_matrix()
                if self.axe_z == True:
                    if self.transformType == "Local":
                        z_axe = self.object.localOrientation.to_euler()
                        z_axe2 = target_axe.localOrientation.to_euler()
                        z_axe[2] = z_axe2[2]
                        self.object.localOrientation = z_axe.to_matrix()
                    elif self.transformType == "World":
                        z_axe = self.object.worldOrientation.to_euler()
                        z_axe2 = target_axe.worldOrientation.to_euler()
                        z_axe[1] = z_axe2[1]
                        self.object.worldOrientation = z_axe.to_matrix()
            if self.fix_type == "Rotation And Position":
                if self.axe_x == True:
                    if self.transformType == "Local":
                        self.object.localPosition.x = target_axe.localPosition.x
                        x_axe = self.object.localOrientation.to_euler()
                        x_axe2 = target_axe.localOrientation.to_euler()
                        x_axe[0] = x_axe2[0]
                        self.object.localOrientation = x_axe.to_matrix()
                    elif self.transformType == "World":
                        self.object.worldPosition.x = target_axe.worldPosition.x
                        x_axe = self.object.worldOrientation.to_euler()
                        x_axe2 = target_axe.worldOrientation.to_euler()
                        x_axe[0] = x_axe2[0]
                        self.object.worldOrientation = x_axe.to_matrix()
                if self.axe_y == True:
                    if self.transformType == "Local":
                        self.object.localPosition.y = target_axe.localPosition.y
                        y_axe = self.object.localOrientation.to_euler()
                        y_axe2 = target_axe.localOrientation.to_euler()
                        y_axe[1] = y_axe2[1]
                        self.object.localOrientation = y_axe.to_matrix()
                    elif self.transformType == "World":
                        self.object.worldPosition.y = target_axe.worldPosition.y
                        y_axe = self.object.worldOrientation.to_euler()
                        y_axe2 = target_axe.worldOrientation.to_euler()
                        y_axe[1] = y_axe2[1]
                        self.object.worldOrientation = y_axe.to_matrix()
                if self.axe_z == True:
                    if self.transformType == "Local":
                        self.object.localPosition.z = target_axe.localPosition.z
                        z_axe = self.object.localOrientation.to_euler()
                        z_axe2 = target_axe.localOrientation.to_euler()
                        z_axe[2] = z_axe2[2]
                        self.object.localOrientation = z_axe.to_matrix()
                    elif self.transformType == "World":
                        self.object.worldPosition.z = target_axe.worldPosition.z
                        z_axe = self.object.worldOrientation.to_euler()
                        z_axe2 = target_axe.worldOrientation.to_euler()
                        z_axe[1] = z_axe2[1]
                        self.object.worldOrientation = z_axe.to_matrix()
        else:
            print("!ERROR!: [THE TARGET NOT EXIST OR NOT HAS FINDED!]")

import bge
from collections import OrderedDict

class Coin(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ("Action", {"Destroy","Hidden","Send Message"}),
        ("Message",""),
        ("OnColliderWith",""),
    ])

    def start(self, args):
        self.action = args["Action"]
        self.onCollider = args["OnColliderWith"]
        self.msg = args["Message"]
        
    def coin(self):
        if str(self.onCollider) in self.object.scene.objects:
            if self.object.collide(str(self.onCollider))[0]:
                if self.action == "Destroy":
                    self.object.endObject()
                if self.action == "Hidden":
                    self.object.visible = False
                if self.action == "Send Message":
                    if self.msg != "":
                        self.object.sendMessage(self.msg,"",str(self.onCollider))
                    else:
                        print("!ERROR! [ DON'T HAVE AN MESSAGE TO SEND OBJECT] !ERROR!")
        else:
            print("!ERROR! [ OBJECT "+self.onCollider+" NOT EXIST] !ERROR!")

    def update(self):
        self.coin()

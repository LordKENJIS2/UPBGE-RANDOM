import bge
from collections import OrderedDict

class TimeScale(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ("Time Scale",1.0),
    ])

    def start(self, args):
        self.timeScale = args["Time Scale"]
        self.slow = args["Slowed"]

    def update(self):
        if self.timeScale < 0:
            self.timeScale = 0
            
        bge.logic.setTimeScale(self.timeScale)

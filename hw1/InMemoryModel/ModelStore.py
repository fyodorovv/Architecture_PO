import sys

import zope.interface

sys.path.append("..")

from ModelElements.Camera import Camera
from ModelElements.Flash import Flash
from ModelElements.PoligonalModel import PoligonalModel
from ModelElements.Scene import Scene

from InMemoryModel.IModelChangedObserver import IModelChangedObserver
from InMemoryModel.IModelChanger import IModelChanger

Model1 = PoligonalModel()
Model2 = PoligonalModel()
Scene1 = Scene()
Scene2 = Scene()
Flash1 = Flash()
Flash2 = Flash()
Camera1 = Camera()
Camera2 = Camera()

@zope.interface.implementer(IModelChanger)
class ModelStore(object):
    Models = [Model1, Model2]
    Scenes = [Scene1, Scene2]
    Flashes = [Flash1,Flash2]
    Cameras = [Camera1, Camera2]
    __changedObservers = [IModelChangedObserver]

    def GetScene(self, int_arg):
        if int_arg:
            result = Scene()
        return result

ModelStore1 = ModelStore()



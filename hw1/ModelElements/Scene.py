from ModelElements.Flash import Flash
from ModelElements.PoligonalModel import PoligonalModel


class Scene(object):
    Id = int
    Models = [PoligonalModel()]
    Flashes = [Flash()]
    
    def Method1(arg1):
        result = arg1 * 2
        return result

    def Method2(arg1, arg2):
        result = arg1 + arg2
        return result

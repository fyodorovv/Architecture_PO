import zope.interface


class IModelChangedObserver(zope.interface.Interface):
    def ApplyUpdateModel():
        pass

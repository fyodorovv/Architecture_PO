import zope.interface


class IModelChanger(zope.interface.Interface):
    def NotifyChange():
        pass

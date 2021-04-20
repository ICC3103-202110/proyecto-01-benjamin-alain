from abc import abstractmethod,ABC

class IEspecialAtack(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def efect(self):
        pass

    @abstractmethod
    def counter(self):
        pass

    @abstractmethod
    def action(self):
        pass
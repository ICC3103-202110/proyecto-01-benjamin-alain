from abc import abstractmethod,ABC

class IEspecialAtack(ABC):

    @abstractmethod
    def efect(self):
        pass

    @abstractmethod
    def counter(self):
        pass
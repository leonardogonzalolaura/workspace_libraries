from abc import ABC, abstractmethod

class IStorage(ABC):

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def list(self):
        pass

        
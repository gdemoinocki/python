from abc import ABC, abstractmethod

class BaseClass(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def c_circle(self):
        pass

    @abstractmethod
    def i_circle(self):
        pass

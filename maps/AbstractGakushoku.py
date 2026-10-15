from abc import ABC, abstractmethod 
class AbstractGakushoku(ABC):
    @abstractmethod
    def get_menu(self):
        pass
    @abstractmethod
    def get_summary(self):
        pass
    @abstractmethod
    def get_author(self):
        pass
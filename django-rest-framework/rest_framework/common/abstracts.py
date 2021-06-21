from abc import *


class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def dframe(self):
        pass


class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def from_csv(self):
        pass

    @abstractmethod
    def from_xls(self):
        pass

    @abstractmethod
    def from_json(self):
        pass


class ScraperBase(metaclass=ABCMeta):
    @abstractmethod
    def driver(self):
        pass

    @abstractmethod
    def scrap_it(self):
        pass

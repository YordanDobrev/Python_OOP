from abc import ABC, abstractmethod
from typing import List

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):

    def __init__(self, name, strength, conquered_peaks, is_prepared: bool):
        self.name = name
        self.strength = strength
        self.conquered_peaks: List[conquered_peaks] = []
        self.is_prepared = is_prepared

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == " ":
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        ...

    @abstractmethod
    def climb(self, peak: BasePeak):
        ...

    @staticmethod
    def rest(self):
        self.strength += 15

    def __str__(self):
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * " \
               f"Left strength: {self.strength:.1f} * Conquered peaks: {', '.join([str(el) for el in self.conquered_peaks])} ///"

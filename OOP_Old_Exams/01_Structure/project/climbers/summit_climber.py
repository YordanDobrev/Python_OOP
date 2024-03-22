from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber, BasePeak):

    def __init__(self, name, strength, conquered_peaks, is_prepared: bool):
        super().__init__(name, strength, conquered_peaks, is_prepared)
        self.strength = 150

    def can_climb(self):
        if self.strength >= 75:
            self.is_prepared = True

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Advanced":
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5

        self.conquered_peaks.append(peak.name)

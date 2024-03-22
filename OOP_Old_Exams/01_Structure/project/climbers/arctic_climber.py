from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber, BasePeak):

    def __init__(self, name, strength, conquered_peaks, is_prepared: bool):
        super().__init__(name, strength, conquered_peaks, is_prepared)
        self.strength = 200

    def can_climb(self):
        if self.strength >= 100:
            self.is_prepared = True

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)

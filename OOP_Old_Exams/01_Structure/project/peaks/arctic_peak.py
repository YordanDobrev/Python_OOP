from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):

    def __init__(self, name, elevation, difficulty_level):
        super().__init__(name, elevation, difficulty_level)

    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        if self.elevation > 3000:
            self.difficulty_level = "Extreme"
        elif 2000 <= self.elevation <= 3000:
            self.difficulty_level = "Advanced"

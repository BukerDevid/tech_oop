class TempAuto():
    mark = str
    color = str
    gos_number = str
    start_year = str
    def __init__(self, mark, color, gos_number, start_year):
        self.mark = mark
        self.color = color
        self.gos_number = gos_number
        self.start_year = start_year

class TempAutoHight(TempAuto):
    pickup = bool
    def __init__(self, pickup, mark, color, gos_number, start_year):
        self.pickup = bool
        super().__init__(mark, color, gos_number, start_year)
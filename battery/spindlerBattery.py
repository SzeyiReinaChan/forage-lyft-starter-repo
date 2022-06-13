from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        year = self.last_service_date.year
        need_service_date = self.last_service_date.replace(self.last_service_date.year, year+2)

        if need_service_date <= self.current_date:
            return True
        else:
            return False

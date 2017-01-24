from datetime import date

class Data():
    def __init__(self):
        self.data = []
        self.os = ["ios", "android"]
        self.version = ""

        self.beginDate = date(2016, 5, 5)
        self.endDate = date(1993, 1, 11)

        self.reopened = 0
        self.total = 0
        self.sevenDayRetention = 0.0

    def set_retention(self, reopened, total):
        self.reopened = reopened
        self.total = total

        if(total != 0):   
            self.sevenDayRetention = (reopened/total)

    def set_data(self, data):
        self.data = data

    def set_begin_date(self, month, day, year):
        self.beginDate = date(year, month, day)

    def set_end_date(self, month, day, year):
        self.endDate = date(year, month, day)

    def set_os(self, os):
        self.os = os

    def set_version(self, version):
        if(version == "6.5"):
            self.version = "6.5.0"
        else:
            self.version = version

    def get_data(self):
        return self.data

    def get_begin_date(self):
        return self.beginDate

    def get_end_date(self):
        return self.endDate

    def get_os(self):
        return self.os

    def get_version(self):
        return self.version

    def get_retention(self):
        return self.sevenDayRetention

    def get_total_users(self):
        return self.total

    def get_reopened_users(self):
        return self.reopened

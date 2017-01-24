import numpy, time
import datetime
from datetime import date

class Model():
    def __init__(self, data):
        self.d = data
        self.beginDate = self.d.get_begin_date()
        self.endDate = self.d.get_end_date()
        self.os = self.d.get_os()
        self.appVersion = self.d.get_version()
        self.kamcordCSV = self.d.get_data()

        self.dateRange = 0
        self.userTotal = 0
        self.userReOpen = 0


    def seven_day_retention(self):
    #create list of only app opened actions
        userAppOpen = self.kamcordCSV[(self.kamcordCSV[:,1] == "APP_OPEN"),:]
        del self.kamcordCSV

        if(self.endDate == self.beginDate):
            self.dateRange = 0
        else:
            self.dateRange = int(str(self.endDate - self.beginDate)[:2])

    #filter for app version, specific OS.
    #loop through date range and find total users and who re-opened
        for i in range(self.dateRange+1):
            if(len(self.os) == 1 and self.appVersion != ""):
               opened  = (userAppOpen[(userAppOpen[:,2] == str(self.beginDate)) &
                                      (userAppOpen[:,3] == self.os[0]) &
                                      (userAppOpen[:,4] == self.appVersion),:])
            elif(self.appVersion != ""):
                opened = (userAppOpen[(userAppOpen[:,2] == str(self.beginDate)) &
                                      (userAppOpen[:,4] == self.appVersion),:])
            elif(len(self.os) == 1):
                opened = (userAppOpen[(userAppOpen[:,2] == str(self.beginDate)) &
                                      (userAppOpen[:,3] == self.os[0]),:])
            else:
                opened = (userAppOpen[(userAppOpen[:,2] == str(self.beginDate)),:])
                
        #add to user total count
            self.userTotal += opened.shape[0]
        #start looking 7-days ahead with userIDs
            futureDate = self.beginDate + datetime.timedelta(days=7)
            reopened = (userAppOpen[(userAppOpen[:,2] == str(futureDate)),:])
        #check intersection between opened & reopened
            self.userReOpen += len(numpy.intersect1d(reopened[:,0], opened[:,0]))
        #increment day
            #print(self.beginDate)
            self.beginDate += datetime.timedelta(days=1)


        self.d.set_retention(self.userReOpen, self.userTotal)
        retentionRate = str(round(self.d.get_retention(), 5))
        
        print("Total users: " + str(self.d.get_total_users()))
        print("Reopened: " + str(self.d.get_reopened_users()))
        print("")
        print("7-Day Retention Rate: " + retentionRate)
        print("")


    




            

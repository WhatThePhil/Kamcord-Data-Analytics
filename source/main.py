from Data import Data
from Model import Model
import tkinter as tk
from tkinter.filedialog import askopenfilename
import numpy, time

class Kamcord():
    def __init__(self, root):
        self.master = root
        self.master.title("Kamcord")
        self.file = "No File"
        self.d = Data()
        
        self.months = ("January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", "December")

        self.days = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                     "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
                     "26", "27", "28", "29", "30", "31")

        self.years = ("2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018")
        
        self.add_components()

    def open_file(self):
        
    #update tkinter label to loading
        self.filename = tk.Label(self.stepFour, text='Loading . . .').grid(row=0, column=2, sticky='WE', padx=5, pady=2)    

    #file opener
        self.file = askopenfilename(initialdir="C:/",
                                    filetypes =(("All Files","*.*"),("Text File", "*.txt")),
                                    title = "Choose a file.")
         
    #throw away first column and header
        self.dataCSV = numpy.genfromtxt(self.file, delimiter=",", dtype="U75", skip_header=1, usecols = range(1,6))

    #clean up date time (list comprehension)
        self.dataCSV[:,2] = [(self.dataCSV[i][2][:10]) for i in range(self.dataCSV.shape[0])]

    #make start button active
        self.startBtn = tk.Button(self.master, text='START', command=self.start, relief=tk.RAISED, state='normal')
        self.startBtn.grid(row=4, column=6, stick='WE', pady=10, padx=10)
        
    #for updating file name label on gui
        name = ""
        for i in range(len(self.file)-1, -1, -1):
            if(self.file[i] == '/'):
                break
            else:
                name += self.file[i]

        name = name[::-1]
        self.filename = tk.Label(self.stepFour, text=name).grid(row=0, column=2, sticky='WE', padx=5, pady=2)    

    def add_components(self):

    #menu bar
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save")

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo")
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index")
        helpmenu.add_command(label="About...")
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)

    #date range
        stepOne = tk.LabelFrame(self.master, text=" Date Range ")
        stepOne.grid(row=0, columnspan = 7, sticky='WE', padx=5, pady=5)

        self.vMonth = tk.StringVar()
        self.vMonth.set("September")
        month = tk.OptionMenu(stepOne, self.vMonth, *self.months)
        month.grid(row=0, column=0, sticky='W', padx=5, pady=10)

        self.vDay = tk.StringVar()
        self.vDay.set("19")
        day = tk.OptionMenu(stepOne, self.vDay, *self.days)
        day.grid(row=0, column=1, sticky='W', padx=5, pady=10)

        self.vYear = tk.StringVar()
        self.vYear.set("2016")
        year = tk.OptionMenu(stepOne, self.vYear, *self.years)
        year.grid(row=0, column=2, sticky='W', padx=5, pady=10)

        tk.Label(stepOne, text="To").grid(row=1, column=1, sticky='WE', padx=5)

        self.vMonth2 = tk.StringVar()
        self.vMonth2.set("September")
        month2 = tk.OptionMenu(stepOne, self.vMonth2, *self.months)
        month2.grid(row=2, column=0, sticky='W', padx=5, pady=10)

        self.vDay2 = tk.StringVar()
        self.vDay2.set("22")
        day2 = tk.OptionMenu(stepOne, self.vDay2, *self.days)
        day2.grid(row=2, column=1, sticky='W', padx=5, pady=10)

        self.vYear2 = tk.StringVar()
        self.vYear2.set("2016")
        year2 = tk.OptionMenu(stepOne, self.vYear2, *self.years)
        year2.grid(row=2, column=2, sticky='W', padx=5, pady=10)

    #Operating System
        stepTwo = tk.LabelFrame(self.master, text=" Device OS ")
        stepTwo.grid(row=1, columnspan=7, sticky='WE', padx=5, pady=5, ipadx=5)

        self.ios = tk.IntVar()
        self.ios.set(1)
        self.android = tk.IntVar()
        self.android.set(1)
        
        apple = tk.Checkbutton(stepTwo, text = "Apple", variable = self.ios, onvalue = 1)
        apple.grid(row=0, column=0, sticky='WE', padx=5, pady=2)

        droid = tk.Checkbutton(stepTwo, text = "Android", variable = self.android, onvalue = 1)
        droid.grid(row=0, column=1, sticky='WE', padx=5, pady=2)

    #App version
        stepThree = tk.LabelFrame(self.master, text=" App Version ")
        stepThree.grid(row=2, columnspan=7, stick='WE', padx=5, pady=5, ipadx=5)

        tk.Label(stepThree, text='Please enter app version: ').grid(row=0, column=0, sticky='WE', padx=5, pady=2)
        self.app = tk.Entry(stepThree, width=20)
        self.app.grid(row=0, column=1, sticky='WE', pady=10)

    #Find specific file
        self.stepFour = tk.LabelFrame(self.master, text=" Open CSV ")
        self.stepFour.grid(row=3, columnspan=7, stick='WE', padx=5, pady=5, ipadx=5)
        
        browse = tk.Button(self.stepFour, text='Find file', command=self.open_file, relief=tk.RAISED)
        browse.grid(row=0, column=0, stick='WE', pady=10, padx=10)

        self.filename = tk.Label(self.stepFour, text=self.file).grid(row=0, column=2, sticky='WE', padx=5, pady=2)    

    #Start 
        self.startBtn = tk.Button(self.master, text='START', command=self.start, relief=tk.RAISED, state='disabled')
        self.startBtn.grid(row=4, column=6, stick='WE', pady=10, padx=10)

    def start(self):

        self.d.set_data(self.dataCSV)
        
        try:
            self.d.set_begin_date(self.months.index(self.vMonth.get())+1, int(self.vDay.get()), int(self.vYear.get()))
            self.d.set_end_date(self.months.index(self.vMonth2.get())+1, int(self.vDay2.get()), int(self.vYear2.get()))
        except Exception as e:
            print(e)

        if(self.ios.get() == 1 and self.android.get() == 1):
            self.d.set_os(["ios", "android"])
        elif(self.ios.get() == 1):
            self.d.set_os(["ios"])
        elif(self.android.get() == 1):
            self.d.set_os(["android"])

        self.d.set_version(self.app.get())

        self.m = Model(self.d)
        self.m.seven_day_retention()


def main():
    root = tk.Tk()
    Kamcord(root)
    root.mainloop()
        
if __name__ == '__main__':
    main()

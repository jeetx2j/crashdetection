import tkinter
import tkinter.messagebox
import customtkinter
import sys
from time import sleep
from random import shuffle
from time import perf_counter as time
from time import sleep
import threading

import pandas
from sklearn.tree import DecisionTreeClassifier
import json
from twilio.rest import Client
import pyttsx3
import warnings
warnings.filterwarnings('ignore')

import geocoder


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")



class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Car Crash Detection")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        if sys.platform == "darwin":
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)
            self.createcommand('tk::mac::Quit', self.on_closing)

        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Car Crash Detection")
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=2, column=0, pady=10, padx=20)

        for i in [0, 1, 2, 3]:
            self.frame_right.rowconfigure(i, weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure(0, weight=1)
        self.frame_right.columnconfigure(1, weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")


        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Car Crash Detection.\n~by Bare Fox",
                                                   height=80,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="we", padx=15, pady=15)

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_info, placeholder_text="ax")
        self.entry_1.grid(column=0, row=1, sticky="we", padx=15, pady=15)

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_info, placeholder_text="ay")
        self.entry_2.grid(column=1, row=1, sticky="we", padx=15, pady=15)

        self.entry_3 = customtkinter.CTkEntry(master=self.frame_info, placeholder_text="az")
        self.entry_3.grid(column=2, row=1, sticky="we", padx=15, pady=15)

        self.entry_4 = customtkinter.CTkEntry(master=self.frame_info, placeholder_text="gx")
        self.entry_4.grid(column=0, row=2, sticky="we", padx=15, pady=15)

        self.entry_5 = customtkinter.CTkEntry(master=self.frame_info, placeholder_text="gy")
        self.entry_5.grid(column=1, row=2, sticky="we", padx=15, pady=15)

        self.entry_6 = customtkinter.CTkEntry(master=self.frame_info, placeholder_text="gz")
        self.entry_6.grid(column=2, row=2, sticky="we", padx=15, pady=15)

        

        

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Predict",
                                                command=self.test)
        self.button_5.grid(row=7, column=1, pady=20, padx=20, sticky="w")

        self.switch_2.select()

    def real(self, ax, ay, az, gx, gy, gz):
        data = pandas.read_csv("C:\\Users\\Somya Ranjan Kabi\\OneDrive\\Desktop\\CrashDetection-main\\src\\dataset\\data.csv")


        X = data[['ax','ay','az','gx','gy','gz']]
        y = data['result']

        set = DecisionTreeClassifier()
        set.fit(X, y)
        print(ax, ay, az, gx, gy, gz)

        # pred = set.predict([[-612, -1028, 17008, -60, 41, -308]])
        pred = set.predict([[ax, ay, az, gx, gy, gz]])

        # pred = 1
        # print(int(pred))

        if int(pred) == 1:
            print('Emgergency: Car Crash Detected\nCalling..')

            

            f = open('emergency.json')
            j = json.load(f)
            f.close()

            # account_sid = '<account_sid>'
            # auth_token = '<auth_token>'

            # for pepol in j:
            #     ph = j[pepol].key()

            #     client = Client(account_sid, auth_token)

            #     call = client.calls.create(
            #                             url='https://rdpzard.sh/test/neww.xml',
            #                             to='+918409604706',
            #                             from_='+13344381751')

        else:
            print('Normal')
        return pred[0]

    def foo(self):
        self.entry_1.grid_forget()
        self.entry_2.grid_forget()
        self.entry_3.grid_forget()
        self.entry_4.grid_forget()
        self.entry_5.grid_forget()
        self.entry_6.grid_forget()
        ax = self.entry_1.get()
        ay = self.entry_2.get()
        az = self.entry_3.get()
        gx = self.entry_4.get()
        gy = self.entry_5.get()
        gz = self.entry_6.get()

        if len(ax) == 0 or len(ay) == 0 or len(az) == 0 or len(gx) == 0 or len(gy) == 0 or len(gz) == 0:
            print('Invalid input! Using default values.')
            ax = -612
            ay = -1028
            az = 17008
            gx = -60
            gy = 41
            gz = -308

        
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Predicting",
                                                   height=80,
                                                   fg_color=("white", "gray38"),
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="we", padx=15, pady=15)

        self.progressbar_1 = customtkinter.CTkProgressBar(self.frame_info)
        self.progressbar_1.grid(row=1, column=0, sticky="ew", padx=15, pady=15)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()

        res = self.real(ax, ay, az, gx, gy, gz)
        sleep(2)
        # self.progressbar_1.stop()
        self.progressbar_1.grid_forget()
        if res == 1:
            resx = 'Not Crashed!'
        else:
            engine = pyttsx3.init()
            engine.setProperty('voice', 'com.apple.speech.synthesis.voice.veena')   
            engine.say("Emergency")
            engine.runAndWait()
            engine.stop()

            g = geocoder.ip('me')
            ll = g.latlng
            resx = f'Crashed\nCalling for help!\nLocation: Lattitude- {ll[0]}, Longitude- {ll[1]}'
            account_sid = 'AC1c3ba74db76eeb41b1c3315f5e15c97d'
            auth_token = 'eb846faf60612c9d5ab673573fc2ffd1'

            client = Client(account_sid, auth_token)

            call = client.calls.create(
                                    url='https://rdpzard.sh/test/neww.xml',
                                    to='+919668802730',
                                    from_='+19783964627')

            print(call.sid)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text=f"Result: {resx}",
                                                   height=80,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="we", padx=15, pady=15)

    def test(self):
        threading.Thread(target=self.foo).start()

        
    

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
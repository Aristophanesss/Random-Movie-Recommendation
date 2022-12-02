import tkinter as tk
from tkinter import messagebox, ttk
import webbrowser
import socket
import recommend

HOST = '127.0.0.1'
PORT = 65432


class basedesk:
    def __init__(self, master):
        # Set up the base frame
        self.root = master
        self.root.config()
        self.root.title('Movie Recommendation')
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (700, 400, (screenwidth - 700) / 2, (screenheight - 400) / 2))

        initface(self.root)

        def on_closing():
            if messagebox.askyesno("Quit", "You are going to quit the program"):
                root.destroy()

        self.root.protocol('WM_DELETE_WINDOW', on_closing)      # Unchangeable


class initface:
    def __init__(self, master):
        self.master = master
        self.initface = tk.Frame(self.master, )
        self.initface.pack()

        tk.Frame(self.initface, height=50, width=700).grid(row=0, column=0, sticky='w')
        tk.Frame(self.initface, height=300, width=700).grid(row=1, column=0, sticky='w')
        tk.Label(self.initface, text="Random Movie Recommendation", font=("Times", 32)).place(x=140, y=150, anchor='w')

        # Recommendation button
        tk.Button(self.initface, text="Generates a high score movie", command=self.getRecommendation).place(x=100,
                                                                                                            y=300,
                                                                                                            anchor='w')
        # Preference button
        tk.Button(self.initface, text="Recommends based on my preference", command=self.goToprefence).place(x=380,
                                                                                                            y=300,
                                                                                                            anchor='w')

    def getRecommendation(self, ):
        self.initface.destroy()
        recommend.setflag(True)
        face1(self.master)

    def goToprefence(self, ):
        self.initface.destroy()
        preferencepage(self.master)


class face1:
    def __init__(self, master):
        self.master = master
        self.face1 = tk.Frame(self.master, )
        self.face1.pack()
        self.movie = recommend.get_randommovie()    # get a movie and its related information

        tk.Label(self.face1, text="You are going to watch", font=("微软雅黑", 30)).pack(side="top", pady=50)
        tk.Label(self.face1, text=self.movie["moviename"] + '!', font=("微软雅黑", 30, "bold italic")).pack(side="top",
                                                                                                        pady=20)

        # Buttons for backtrack, URL, and exit
        tk.Button(self.face1, text="Back to home page", command=self.back).pack(side="left", padx=30, pady=50)
        tk.Button(self.face1, text="More information", command=self.more).pack(side="left", padx=30)
        tk.Button(self.face1, text="Click to exit", command=self.exit).pack(side="left", padx=30)

    def back(self):
        if messagebox.askyesno("Back to homepage", "You will return to the home page"):
            self.face1.destroy()
            recommend.set_param("", "", "", "", "", "")
            initface(self.master)

    def more(self):
        # Send movie titles to the microservice
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(self.movie["moviename"].encode('utf-8'))

            # receive the URL
            data = s.recv(1024)
            data.decode('utf-8')
            webbrowser.open(str(data, encoding='utf-8'))

    def exit(self):
        self.face1.destroy()
        if messagebox.askokcancel("Quit", "You are going to quit the program"):
            recommend.set_param("", "", "", "", "", "")
            root.destroy()


class preferencepage:
    def __init__(self, master):
        self.master = master
        self.preferencepage = tk.Frame(self.master, )
        self.preferencepage.pack()

        self.language = tk.StringVar()
        self.era = tk.StringVar()
        self.genre = tk.StringVar()

        self.xVariable1 = tk.StringVar()
        self.xVariable2 = tk.StringVar()
        self.xVariable3 = tk.StringVar()

        frame0 = tk.Frame(self.preferencepage, height=50, width=700)
        frame0.grid(row=0, column=0, sticky='w')
        tk.Button(frame0, text="Backward", command=self.back).pack(side="left", padx=10, pady=10)
        frame1 = tk.Frame(self.preferencepage, height=300, width=700, bg="ivory")
        frame1.grid(row=1, column=0, sticky='w')

        # Language Options
        tk.Checkbutton(self.preferencepage, variable=self.language, text="I prefer the movie in", onvalue="language",
                       offvalue="").place(x=200, y=120, anchor='w')
        com1 = ttk.Combobox(self.preferencepage, textvariable=self.xVariable1, width=6)
        com1["value"] = ("English", "Spanish", "Chinese", "French", "Japanese")
        com1.current(0)
        com1.place(x=350, y=120, anchor='w')

        # Era Options
        tk.Checkbutton(self.preferencepage, variable=self.era, text="I prefer the movie", onvalue="year",
                       offvalue="").place(x=200, y=160, anchor='w')
        com2 = ttk.Combobox(self.preferencepage, textvariable=self.xVariable2, width=6)
        com2["value"] = ("after", "before")
        com2.current(0)
        com2.place(x=335, y=160, anchor='w')
        tk.Label(self.preferencepage, text="the millennium").place(x=420, y=160, anchor='w')

        # Genre Options
        tk.Checkbutton(self.preferencepage, variable=self.genre, text="The genre of movies I prefer is ",
                       onvalue="type", offvalue="").place(x=200, y=200, anchor='w')
        com3 = ttk.Combobox(self.preferencepage, textvariable=self.xVariable3, width=6)
        com3["value"] = ("Action", "Comedy", "Drama", )
        com3.current(0)
        com3.place(x=418, y=200, anchor='w')

        # Generate results
        container_last = tk.Frame(self.preferencepage, height=50, width=700)
        container_last.grid(row=2, column=0)
        tk.Button(container_last, text="Generate recommendations", command=self.gotorecommendation).pack(padx=10,
                                                                                                         pady=10)

    def back(self):
        if messagebox.askyesno("Back homepage", "Do you want to go back to home page?"):
            self.preferencepage.destroy()
            recommend.set_param("", "", "", "", "", "")
            initface(self.master)

    def gotorecommendation(self):
        self.preferencepage.destroy()
        recommend.set_param(self.xVariable3.get(), self.genre.get(), self.xVariable2.get(), self.era.get(),
                            self.xVariable1.get(), self.language.get())
        recommend.setflag(False)
        face1(self.master)


if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()

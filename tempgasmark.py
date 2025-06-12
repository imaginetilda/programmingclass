'''v1 temp'''
from tkinter import *

class Converter:
    def __init__(self):
        '''Set up the GUI'''
        self.root = Tk()
        self.root.title("Temperature Converter")

        # container for frames
        self.container = Frame(self.root)
        self.container.pack(expand=True, fill="both")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # dictionary to hold frames
        self.frames = {}
        self.frames["Mainframe"] = self.create_main_frame(self.container)
        self.frames["to_cFrame"] = self.create_to_c_frame(self.container)
        self.frames["to_gFrame"] = self.create_to_g_frame(self.container)

        # show the initial frame
        self.show_frame("Mainframe")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def create_main_frame(self, parent):
        '''create the home screen of the app'''
        frame = Frame(parent)
        frame.grid(row=0, column=0, sticky="nsew")

        # main heading
        heading = Label(frame, text="Temperature converter!!!!1!!!!!!1! :3", font=('Comic Sans MS', 16, 'bold'))
        heading.pack(pady=20)

        # frame to make buttons next to eachother
        button_frame = Frame(frame)
        button_frame.pack(pady=10) 

        # buttons: to centigrade and to gasmark
        # pack buttons side by side within button_frame
        self.to_c_button = Button(button_frame, text="to centigrade (aka celsius)", bg="yellow",
                                     font=('Comic Sans MS', 12, 'bold'),
                                     command=lambda: self.show_frame("to_cFrame"))
        self.to_c_button.pack(side=LEFT, padx=10) 

        self.to_g_button = Button(button_frame, text="to gasmark", bg="pink",
                                     font=('Comic Sans MS', 12, 'bold'),
                                     command=lambda: self.show_frame("to_gFrame"))
        self.to_g_button.pack(side=RIGHT, padx=10) 

        return frame

    def create_to_c_frame(self, parent):
        '''gasmark screen'''
        frame = Frame(parent)
        frame.grid(row=0, column=0, sticky="nsew")

        label = Label(frame, text="gasmark temp",  font = ('Comic Sans MS', 10, 'bold'))
        label.pack(pady=10)

        self.gasmark_entry = Entry(frame)
        self.gasmark_entry.pack(pady=5)

        calculate_button = Button(frame, text="calculate", font = ('Comic Sans MS', 10, 'bold'), command=self.calculate_g_to_c)
        calculate_button.pack(pady=5)

        self.converted_c_label = Label(frame, text="converted temp here", font = ('Comic Sans MS', 10, 'bold'))
        self.converted_c_label.pack(pady=5)

        reset_button = Button(frame, text="reset", font = ('Comic Sans MS', 10, 'bold'), command=self.reset_c_frame)
        reset_button.pack(pady=5)

        back_button = Button(frame, text="back", font = ('Comic Sans MS', 10, 'bold'), command=lambda: self.show_frame("Mainframe"))
        back_button.pack(pady=5)
        return frame

    def create_to_g_frame(self, parent):
        '''centigrade screen'''
        frame = Frame(parent)
        frame.grid(row=0, column=0, sticky="nsew")

        label = Label(frame, text="centigrade temp",  font = ('Comic Sans MS', 10, 'bold'))
        label.pack(pady=10)

        self.celsius_entry = Entry(frame)
        self.celsius_entry.pack(pady=5)

        calculate_button = Button(frame, text="calculate", font = ('Comic Sans MS', 10, 'bold'), command=self.calculate_c_to_g)
        calculate_button.pack(pady=5)

        self.converted_g_label = Label(frame, text="converted temp here", font = ('Comic Sans MS', 10, 'bold'))
        self.converted_g_label.pack(pady=5)

        reset_button = Button(frame, text="reset", font = ('Comic Sans MS', 10, 'bold'), command=self.reset_g_frame)
        reset_button.pack(pady=5)

        back_button = Button(frame, text="back", font = ('Comic Sans MS', 10, 'bold'), command=lambda: self.show_frame("Mainframe"))
        back_button.pack(pady=5)
        return frame

    def calculate_g_to_c(self):
        '''f -> c'''
        try:
            gasmark = float(self.gasmark_entry.get())
            celsius = (gasmark * 14) + 121
            self.converted_c_label.config(text=f"{celsius:.2f}°C", font = ('Comic Sans MS', 10, 'bold'))
        except ValueError:
            self.converted_c_label.config(text="invalid", font = ('Comic Sans MS', 10, 'bold'))

    def reset_c_frame(self):
        '''clears the entry and bottom label for the f -> c frame'''
        self.gasmark_entry.delete(0, END)
        self.converted_c_label.config(text="converted temp here", font = ('Comic Sans MS', 10, 'bold'))

    def calculate_c_to_g(self):
        '''c -> g'''
        try:
            celsius = float(self.celsius_entry.get())
            gasmark = (celsius - 121) / 14
            self.converted_g_label.config(text=f"{gasmark:.2f} gas mark", font = ('Comic Sans MS', 10, 'bold'))
        except ValueError:
            self.converted_g_label.config(text="invalid", font = ('Comic Sans MS', 10, 'bold'))

    def reset_g_frame(self):
        '''clears the entry and bottom label for the c -> f frame'''
        self.celsius_entry.delete(0, END)
        self.converted_g_label.config(text="converted temp here", font = ('Comic Sans MS', 10, 'bold'))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Converter()
    app.run()
import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("280*200")
        self.window.resizable(True,True)

        self.padding: dict ={'padx':20, 'pady':10}

        self.lblIncome = ctk.CTkLabel(self.window, text='Income :')
        self.lblIncome.grid(row=0, column=0, **self.padding)

        self.income_label_entry = ctk.CTkEntry(self.window)
        self.income_label_entry.grid(row=0, column=0, **self.padding)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ct = TaxCalculator()
    ct.run()
import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("280x200")
        self.window.resizable(False,False)

        self.padding: dict ={'padx':20, 'pady':10}

        # Income Label and Entry
        self.lblIncome = ctk.CTkLabel(self.window, text='Income:')
        self.lblIncome.grid(row=0, column=0, **self.padding)
        self.income_label_entry = ctk.CTkEntry(self.window, placeholder_text="Enter Appropriate Income")
        self.income_label_entry.grid(row=0, column=1, **self.padding)

        # Tax Label and Entry
        self.taxLabel = ctk.CTkLabel(self.window, text="Tax:")
        self.taxLabel.grid(row=1,column=0, **self.padding)
        self.taxEntry = ctk.CTkEntry(self.window, placeholder_text="Enter Appropriate Value")
        self.taxEntry.grid(row=1,column=1, **self.padding)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ct = TaxCalculator()
    ct.run()
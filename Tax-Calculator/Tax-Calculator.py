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
        self.taxLabel = ctk.CTkLabel(self.window, text="Percent:")
        self.taxLabel.grid(row=1,column=0, **self.padding)
        self.taxEntry = ctk.CTkEntry(self.window, placeholder_text="Enter Appropriate Value")
        self.taxEntry.grid(row=1,column=1, **self.padding)

        #result
        self.result = ctk.CTkLabel(self.window, text="Result: ")
        self.result.grid(row=2,column=0, **self.padding)
        self.resultEntry = ctk.CTkEntry(self.window)
        self.resultEntry.insert(0,"0")
        self.resultEntry.grid(row=2, column=1, **self.padding)

        # Calculate Button
        self.add = ctk.CTkButton(self.window, text='Add', command=self.calculate_tax)
        self.add.grid(row=3,column=1, **self.padding)

    def update_result(self, text: str):
        self.resultEntry.delete(0, ctk.END)
        self.resultEntry.insert(0, text)

    def calculate_tax(self):
        try:
            income: float = float(self.income_label_entry.get())
            taxRate: float = float(self.taxEntry.get())
            self.update_result(f'${income * (taxRate / 100):,.2f}')
        except ValueError:
            self.update_result("Inavlid Input")

    def run(self):
        self.window.mainloop()
    
    def addSum(self):
        try:
            num1 = float(self.income_label_entry.get())
            num2 = float(self.taxEntry.get())
            self.update_result(num1 + num2)
        except ValueError as e:
            self.update_result("Invalid Input")


if __name__ == "__main__":
    ct = TaxCalculator()
    ct.run()

# Importing necessary modules
import tkinter as tk
from forex_python.converter import CurrencyRates

# Defining allowed currencies
common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'NZD']

# Creating a CurrencyConverter class
class CurrencyConverter:
    # Constructor method for GUI
    def __init__(self):
        # Creating the main window
        self.root = tk.Tk()
        # Setting the title of the window
        self.root.title("Currency Converter")
        # Setting the size of the window
        self.root.geometry("200x200")

        # Creating 'from' option menu
        self.from_var = tk.StringVar(self.root)
        self.from_var.set("USD")  # Default option
        #OptionMeny lets you change options as a drop down then we place it in self root then the string values are in self from var and then we unpack with * and get the common currencies
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *common_currencies)
        #10 pixels from top and bottom 
        self.from_menu.pack(pady=10)

        # Creating 'to' option menu
        self.to_var = tk.StringVar(self.root)
        self.to_var.set("EUR")  # Default option
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *common_currencies)
        self.to_menu.pack(pady=10)

        #here is the amount we will enter
        #label is the the label widget and we put it in root with the text amount
        self.amount_label = tk.Label(self.root, text = "Amount: ")
        self.amount_label.pack(pady = 1)

        #this is how you enter inside the widget
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady = 1)

        #here is the button we are going to initiate and it will have the text convert and the command is it will convert currency
        self.convert_button = tk.Button(self.root, text="convert", command = self.convert_currency)
        self.convert_button.pack(pady=1)

        #here is the results
        #it will be blank because the converted results will go there
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=1)

        #this runs the window
        self.root.mainloop()

    #convert currency method
    def convert_currency(self):
        #we do a try beacuse of invalid numbers nad currency to we do try so it can fail
        try:
            from_currency = self.from_var.get()
            to_currency = self.to_var.get()
            amount = float(self.amount_entry.get())

            #these are the current currency rates
            c_rates = CurrencyRates()

            rate = c_rates.get_rate(from_currency, to_currency)
            converted_amount = amount * rate
            self.result_label.config(text = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

        except ValueError:
            self.result_label.config(text = "Please enter a valid number")
        
        except Exception:
            self.result_label.config(text="Error Occured")
  

# Running the converter if the script is executed
if __name__ == "__main__":
    CurrencyConverter()


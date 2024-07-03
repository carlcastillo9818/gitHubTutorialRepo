# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import date class from datetime module
from datetime import date
 

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("How are you feeling?")
    # Returns the current local date    
    today = date.today()
    print("ITS MOONY TODAY ",today)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("carlos castillo")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

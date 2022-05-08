# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

def call_pylenin():
    r = requests.get("https://www.pylenin.com")
    if r.status_code == 200:
        return "It was a success!"
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(call_pylenin())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

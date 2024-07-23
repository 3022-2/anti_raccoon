import win10toast
import winreg
import shutil
import time
import os

appdata_path = os.environ['APPDATA']

class anti_raccoon:
    def main():
        toaster = win10toast.ToastNotifier()

        while True:
            persistance_dir = os.listdir(appdata_path)
            if "Storage0" in persistance_dir and "CLPPTH" in persistance_dir:
                toaster.show_toast("Anti Crypto Clipper",f"Raccoon Clipper detected in {appdata_path} - folders Storage0 and CLPPTH", duration=10)
            time.sleep(1) #can be adjusted to check more frequently. currently 1 second

def add_to_startup():
    current_script = os.path.abspath(__file__)
    startup_script = os.path.join(appdata_path, "anti_clipper.pyw")
    shutil.copyfile(current_script, startup_script)

    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    key = winreg.HKEY_CURRENT_USER
    with winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
        try:
            winreg.QueryValueEx(reg_key, "Anti Crypto Clipper")
        except FileNotFoundError:
            winreg.SetValueEx(reg_key, "Anti Crypto Clipper", 0, winreg.REG_SZ, startup_script)

    print("Script added to startup, will run after restart.")
def first_check():
    add_startup = input("Would you like to add the script to startup? (y/n): ").strip().lower()
    if add_startup == "y":
        add_to_startup()

if __name__ == "__main__":
    if os.name == "nt":
        cwd = os.getcwd()
        if cwd == appdata_path:
            if "anti_clipper.py" in __file__:
                anti_raccoon.main()
        else:
            first_check()
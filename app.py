import os
import sys
import threading
import webview
from keyauth import api

# 🔑 ผูกรหัสคีย์ออนไลน์ของร้านคุณเรียบร้อย
keyauthapp = api(
    name = "Teerasak's Application",
    ownerid = "s2otXiDhK2",
    secret = "f0b6c37b146add52d48475eb04c0163813de24d3dda24efb8925e97175a40e7b",
    version = "1.0"
)

DASHBOARD_URL = "https://tiiny.site"

class Colors:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

def run_login_flow():
    os.system("title GHOST LADY LOADER")
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{Colors.PURPLE}GHOST LADY{Colors.RESET}  |  {Colors.PURPLE}LOADER{Colors.RESET}")
    print("-" * 60)
    print("")

    license_input = input("[>] License : ").strip()
    print("\n[*] Connecting to GHOST LADY secure server...")

    try:
        keyauthapp.license(license_input)
        print(f"\n[{Colors.GREEN}✓{Colors.RESET}] License Success! Access Granted.")
        print("[*] Loading Premium Cheat UI Panel...")
        
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        show_cheat_ui()

    except Exception as e:
        print(f"\n[{Colors.RED}X{Colors.RESET}] Access Denied: {e}")
        input("\nPress Enter to exit...")
        sys.exit()

def show_cheat_ui():
    window = webview.create_window(
        title='GHOST LADY - PREMIUM MENU', 
        url=DASHBOARD_URL,
        width=960, 
        height=640,
        resizable=False,
        background_color='#06060e'
    )
    webview.start()

if __name__ == '__main__':
    run_login_flow()

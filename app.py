import os
import sys
import time
import webbrowser
from keyauth import api

# 🔑 ผูกรหัสคีย์ออนไลน์ตรงตามหน้าจอของคุณแบบถูกต้อง 100% แล้วครับ
keyauthapp = api(
    name = "Teerasak's Application",
    ownerid = "s2otXiDhK2",
    secret = "f0b6c37b146add52d48475eb04c0163813de24d3dda24efb8925e97175a40e7b",
    version = "1.0"
)

class Colors:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

def main():
    os.system("title GHOST LADY LOADER")
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{Colors.PURPLE}GHOST LADY{Colors.RESET}  |  {Colors.PURPLE}LOADER{Colors.RESET}")
    print("-" * 60)
    print("")

    # จุดกรอกคีย์ล็อกเครื่องอัตโนมัติ 1 คีย์ 1 เครื่อง (HWID)
    license_input = input("[>] License : ").strip()
    print("\n[*] Connecting to GHOST LADY secure server...")
    time.sleep(1)

    try:
        keyauthapp.license(license_input)
        print(f"\n[{Colors.GREEN}✓{Colors.RESET}] License Success! Access Granted.")
        print("[*] Redirecting to Web Control Panel...")
        time.sleep(1.5)
        
        # สั่งเปิดหน้าแผงควบคุมสูตรกระจกฝ้าสีม่วงผ่านเบราว์เซอร์ในเครื่อง
        webbrowser.open("https://tiiny.site")
        sys.exit()

    except Exception as e:
        print(f"\n[{Colors.RED}X{Colors.RESET}] Access Denied: {e}")
        input("\nPress Enter to exit...")
        sys.exit()

if __name__ == '__main__':
    main()

import webbrowser

def open_url(url):
    """Open a URL in the default web browser."""
    webbrowser.open(url)

def start_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nWelcome to SafeLinker")
        print("1. Surface URLs")
        print("2. Database URLs")
        print("3. Onion URLs")
        print("4. Pentest URLs")
        print("5. Pentest Tools")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            surface_urls()
        elif choice == "2":
            database_urls()
        elif choice == "3":
            onion_urls()
        elif choice == "4":
            pentest_urls()
        elif choice == "5":
            pentest_tools()
        elif choice == "6":
            print("Exiting SafeLinker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def surface_urls():
    """Display and open Surface URLs."""
    while True:
        print("\nSurface URLs")
        print("1. Who.is")
        print("2. Hacking Database")
        print("3. Shodan")
        print("4. Censys")
        print("5. Wayback Machine")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            open_url("https://who.is/")
        elif choice == "2":
            open_url("https://www.exploit-db.com/")
        elif choice == "3":
            open_url("https://www.shodan.io/")
        elif choice == "4":
            open_url("https://censys.io/")
        elif choice == "5":
            open_url("https://archive.org/web/")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# Define other menu options with similar structure
def database_urls():
    print("\nDatabase URLs")
    print("1. Dehashed")
    print("2. Leaked-DataBase")
    print("3. Pwned")
    print("4. Snusbase")
    print("5. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        open_url("https://dehashed.com/")
    elif choice == "2":
        open_url("https://www.leakedsource.ru/")
    elif choice == "3":
        open_url("https://haveibeenpwned.com/")
    elif choice == "4":
        open_url("https://snusbase.com/")
    elif choice == "5":
        return
    else:
        print("Invalid choice. Please try again.")

def onion_urls():
    print("\nOnion URLs")
    print("1. Ahmia")
    print("2. BreachForums")
    print("3. Leaked Password Database")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        open_url("http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/")
    elif choice == "2":
        open_url("http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/")
    elif choice == "3":
        open_url("http://breachdb7r5fusv54wbqgfrmtqcle647ybi7jyi2b2btqyraioox3wid.onion/LeakedPass")
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")

def pentest_urls():
    print("\nPentest URLs")
    print("1. CrackStation")
    print("2. Base64 Decode")
    print("3. MD5 Decrypt")
    print("4. Hashes.org")
    print("5. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        open_url("https://crackstation.net/")
    elif choice == "2":
        open_url("https://www.base64decode.org/")
    elif choice == "3":
        open_url("https://md5decrypt.net/en/")
    elif choice == "4":
        open_url("https://hashes.org/")
    elif choice == "5":
        return
    else:
        print("Invalid choice. Please try again.")

def pentest_tools():
    print("\nPentest Tools")
    print("1. gobuster")
    print("2. dnsrecon")
    print("3. nmap")
    print("4. sublist3r")
    print("5. ffuf")
    print("6. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        open_url("https://github.com/OJ/gobuster")
    elif choice == "2":
        open_url("https://github.com/darkoperator/dnsrecon")
    elif choice == "3":
        open_url("https://nmap.org/")
    elif choice == "4":
        open_url("https://github.com/aboul3la/Sublist3r")
    elif choice == "5":
        open_url("https://github.com/ffuf/ffuf")
    elif choice == "6":
        return
    else:
        print("Invalid choice. Please try again.")

# Start the program
start_menu()

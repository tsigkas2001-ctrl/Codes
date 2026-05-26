gmail_count = 0
yahoo_count = 0
outlook_count = 0
hotmail_count = 0


with open("gmail.txt", "w",encoding="utf-8" ) as f_gmail:
    pass
with open("outlook.txt", "w",encoding="utf-8") as f_outlook:
    pass
with open("hotmail.txt", "w",encoding="utf-8") as f_hotmail:
    pass
with open("yahoo.txt", "w",encoding="utf-8") as f_yahoo:
    pass

with open("raw_users.txt", "r",encoding="utf-8") as f_in:
        
            for line in f_in:

                if "-" in line:
                    
                    email = line.split("-")[1].strip().lower()
                
                if "gmail" in email:
                    with open("gmail.txt", "a",encoding="utf-8") as f_gmail:
                        f_gmail.write(f"{email}\n")
                    gmail_count +=1
                
                elif "outlook" in email:
                    with open("outlook.txt", "a",encoding="utf-8") as f_outlook:
                        f_outlook.write(f"{email}\n")
                    outlook_count +=1

                elif "hotmail" in email:
                    with open("hotmail.txt", "a",encoding="utf-8") as f_hotmail:
                        f_hotmail.write(f"{email}\n")
                    hotmail_count +=1

                elif "yahoo" in email:
                    with open("yahoo.txt", "a",encoding="utf-8") as f_yahoo:
                        f_yahoo.write(f"{email}\n")
                    yahoo_count +=1



print(f"\nGmail's Count : {gmail_count}")
print(f"Yahoo's Count : {yahoo_count}")
print(f"Outlook's Count : {outlook_count}")
print(f"Hotmail's COunt : {hotmail_count}\n")
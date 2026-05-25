with open("raw_users.txt", "r") as f_in:
   with open("clean_email.txt", "w") as f_out:
        for line in f_in:

            if "-" in line:
                email = line.split("-")[1].strip().lower()

                f_out.write(f"{email}\n")
# --------------------------------------------------------------------
#                        Simple FAQ Agent
# --------------------------------------------------------------------
# ********************************************************************
# ====================================================================
# Give The Answer & But If Don't Find Saves Question in Another Txt
# ====================================================================


def question():
    user_input = input("Apna Swaal Poche = ")
    que = user_input.lower().split()

    found = False

    with open("adlytix_data.txt", "r") as r_file:
        for line in r_file:
            lower_line = line.lower()

            for word in que:
                if word in lower_line:
                    print("Here's Your Answer!\n")
                    print(line.strip())

                    found = True
                    break

            if found:
                break

    if not found:
        with open("missed_leads.txt", "a") as a_file:
            a_file.write(user_input + "\n")
            print("Mai Aik AI Hu Or Merii Intelligence Per Mazeed kaam ho raha hai")
            print("So Please Contact With M Zeeshan Assistant At 03710712972")


def Adlytix_bot():

    print("=========================================================")
    print("---------------------------------------------------------")
    print("                    Adlytix RAG System                   ")
    print("---------------------------------------------------------")

    while True:
        print("---------------------------------------------------------")
        print("             Enter 1 to Ask Question")
        print("             Enter 0 To Exit")
        print("---------------------------------------------------------")

        try:
            choice = int(input("Define Your Action = "))

        except ValueError:
            print("Error!\nEnter Correct Choice")
            continue

        if choice == 1:
            question()

        elif choice == 0:
            print("Thwnk You For Contacting Us 🥰\nAllah Hafiz 👀")
            break

        else:
            print("Invalid choice. Please press 1 or 0.")


Adlytix_bot()

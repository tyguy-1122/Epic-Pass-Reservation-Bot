from bot import Bot
from tkinter import *
from epic_config import Epic_config
from datetime import date

def on_click():
    # Get user email and password
    user_email = email_textbox.get()
    user_password = password_textbox.get()

    # Add all the passholders to the list of passholder names
    passholder_names = []
    passholder_name1 = passholder_textbox1.get()
    passholder_name2 = passholder_textbox2.get()
    passholder_name3 = passholder_textbox3.get()
    passholder_name4 = passholder_textbox4.get()
    if passholder_name1 != '':
        passholder_names.append(passholder_name1)
    if passholder_name2 != '':
        passholder_names.append(passholder_name2)
    if passholder_name3 != '':
        passholder_names.append(passholder_name3)
    if passholder_name4 != '':
        passholder_names.append(passholder_name4)

    # Get the resort
    resort_name = resort.get()
    
    # Make the list of dates to reserve
    dates = []
    if month_text1.get() != 0:
        dates.append(date(year_text1.get(), month_text1.get(), day_text1.get()))
    if month_text2.get() != 0:
        dates.append(date(year_text2.get(), month_text2.get(), day_text2.get()))
    if month_text3.get() != 0:
        dates.append(date(year_text3.get(), month_text3.get(), day_text3.get()))

    # Make the configuration from text fields
    config = Epic_config(user_email, user_password, resort_name, passholder_names, dates)

    # Create the bot and run
    try:
        bot = Bot(config)
        bot.run()

        # Notify the user of successful run
        output_textbox.insert(END, 'Bot successful. Check email to see reservation.\n')

    except Exception as e:
        output_textbox.insert(END, 'Error! Bot unsuccesful! Check your input and try again.\n')

if __name__ == '__main__':
    window = Tk()
    window.title('Epic Pass Reservation Bot')
    window.geometry("540x600")
    window.resizable(0,0)
    window.configure(background="black")
    window.iconbitmap("images\\robot.ico")

    resort_options = ['Afton Alps','Alpine Valley','Attitash Mountain', 'Beaver Creek',
    'Boston Mills Brandywine', 'Breckenridge', 'Crested Butte', 'Crotched Mountain', 'Heavenly',
    'Hidden Valley', 'Hunter', 'Jack Frost Big Boulder', 'Keystone', 'Kirkwood', 'Liberty Mountain',
    'Mad River Mountain', 'Mount Sunapee', 'Mt. Brighton', 'Mt. Snow', 'Northstar', 'Okemo',
    'Paoli Peaks', 'Park City', 'Roundtop Mountain', 'Snow Creek', 'Stevens Pass', 'Stowe',
    'Vail', 'Whistler Blackcomb', 'Whitetail', 'Wildcat Mountain', 'Wilmot Mountain']

    MONTHS = [1,2,3,4,5,6,7,8,9,10,11,12]

    DAYS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

    YEARS = [2020,2021]

    # Create spot for user to input email
    email_label = Label(window, text='Email', bg='black', fg='white', font='none 12 bold')
    email_label.grid(row=0,column=1)
    email_textbox = Entry(window, width=20, bg='white')
    email_textbox.grid(row=1,column=1)

    # Create spot for user to input password
    password_label = Label(window, text='Epic password', bg='black', fg='white', font='none 12 bold')
    password_label.grid(row=0,column=2)
    password_textbox = Entry(window, width=20, bg='white', show='*')
    password_textbox.grid(row=1,column=2,padx=5,pady=5)

    # Create spot for user to input add names of passholders
    passholder_label = Label(window, text='Passholder names (as shown on Epic website)', bg='black', fg='white', font='none 12 bold')
    passholder_label.grid(row=2, column=0, columnspan=4)
    passholder_textbox1 = Entry(window, width=20, bg='white')
    passholder_textbox1.grid(row=3,column=0,padx=5,pady=5)
    passholder_textbox2 = Entry(window, width=20, bg='white')
    passholder_textbox2.grid(row=3,column=1,padx=5,pady=5)
    passholder_textbox3 = Entry(window, width=20, bg='white')
    passholder_textbox3.grid(row=3,column=2,padx=5,pady=5)
    passholder_textbox4 = Entry(window, width=20, bg='white')
    passholder_textbox4.grid(row=3,column=3,padx=5,pady=5)

    # Create a resort drop down
    resort_label = Label(window, text='Resort name', bg='black', fg='white', font='none 12 bold')
    resort_label.grid(row=4, column=0,columnspan=4)
    resort = StringVar(window)
    resort.set('Park City')
    resort_menu = OptionMenu(window, resort, *resort_options)
    resort_menu.grid(row=5,column=0,columnspan=4,padx=5,pady=5)

    # Create a reservation day series of boxes
    month_text1 = IntVar(window)
    month_text1.set(0)
    day_text1 = IntVar(window)
    day_text1.set(0)
    year_text1 = IntVar(window)
    year_text1.set(0)

    month_text2 = IntVar(window)
    month_text2.set(0)
    day_text2 = IntVar(window)
    day_text2.set(0)
    year_text2 = IntVar(window)
    year_text2.set(0)

    month_text3 = IntVar(window)
    month_text3.set(0)
    day_text3 = IntVar(window)
    day_text3.set(0)
    year_text3 = IntVar(window)
    year_text3.set(0)

    month_text4 = IntVar(window)
    month_text4.set(0)
    day_text4 = IntVar(window)
    day_text4.set(0)
    year_text4 = IntVar(window)
    year_text4.set(0)

    p1_label = Label(window, text='Enter up to four reservation dates:', bg='black', fg='white', font='none 12 bold')
    p1_label.grid(row=6,column=0,columnspan=4, padx=5, sticky=W)

    p1_label = Label(window, text='Day 1:', bg='black', fg='white', font='none 12 bold')
    p1_label.grid(row=7,column=0)
    p1_month = OptionMenu(window, month_text1, *MONTHS)
    p1_month.grid(row=7, column=1,padx=5,pady=5)
    p1_day = OptionMenu(window, day_text1, *DAYS)
    p1_day.grid(row=7, column=2,padx=5,pady=5)
    p1_year = OptionMenu(window, year_text1, *YEARS)
    p1_year.grid(row=7, column=3,padx=5,pady=5)

    p2_label = Label(window, text='Day 2:', bg='black', fg='white', font='none 12 bold')
    p2_label.grid(row=8,column=0)
    p2_month = OptionMenu(window, month_text2, *MONTHS)
    p2_month.grid(row=8, column=1,padx=5,pady=5)
    p2_day = OptionMenu(window, day_text2, *DAYS)
    p2_day.grid(row=8, column=2,padx=5,pady=5)
    p2_year = OptionMenu(window, year_text2, *YEARS)
    p2_year.grid(row=8, column=3,padx=5,pady=5)

    p3_label = Label(window, text='Day 3:', bg='black', fg='white', font='none 12 bold')
    p3_label.grid(row=9,column=0)
    p3_month = OptionMenu(window, month_text3, *MONTHS)
    p3_month.grid(row=9, column=1,padx=5,pady=5)
    p3_day = OptionMenu(window, day_text3, *DAYS)
    p3_day.grid(row=9, column=2,padx=5,pady=5)
    p3_year = OptionMenu(window, year_text3, *YEARS)
    p3_year.grid(row=9, column=3,padx=5,pady=5)

    p4_label = Label(window, text='Day 4:', bg='black', fg='white', font='none 12 bold')
    p4_label.grid(row=10,column=0)
    p4_month = OptionMenu(window, month_text3, *MONTHS)
    p4_month.grid(row=10, column=1,padx=5,pady=5)
    p4_day = OptionMenu(window, day_text3, *DAYS)
    p4_day.grid(row=10, column=2,padx=5,pady=5)
    p4_year = OptionMenu(window, year_text3, *YEARS)
    p4_year.grid(row=10, column=3,padx=5,pady=5)


    # Create a run button
    run_button = Button(window, text='RUN BOT', command=on_click)
    run_button.grid(row=11, column=0, columnspan=4, padx=5,pady=5)

    # Create an output text box
    output_label = Label(window, text='Any bot ouput will be displayed here:', bg='black', fg='white', font='none 12 bold')
    output_label.grid(row=12, column=0, columnspan=4)
    output_textbox = Text(window, width=60, height=4, bg='white')
    output_textbox.grid(row=13, column=0, columnspan=4,padx=5,pady=5)

    # Run the window
    window.mainloop()

import tkinter as tk

root = tk.Tk()
root.geometry('1400x700')
root.title("Toda System")

pale = '#E8D9C4'
gold = '#785D32'
rough = '#3E160C'
brown = '#BF4C41'
navy = '#050A30'
blue = '#93AECA'
text_color = '#ECAAC2'

login_driver_icon = tk.PhotoImage(file = 'driver_icon.png')
login_admin_icon = tk.PhotoImage(file = 'admin_icon.png')
login_passenger_icon = tk.PhotoImage(file = 'passenger_icon.png')
locked_icon = tk.PhotoImage(file = 'locked_icon.png')
unlocked_icon = tk.PhotoImage(file = 'unlocked_icon.png')
background_image= tk.PhotoImage(file = 'background.png')
bg_passenger_image = tk.PhotoImage(file = 'bg_passenger.png')
bg_driver_image = tk.PhotoImage(file = 'bg_driver.png')
back_icon = tk.PhotoImage(file = 'back_button.png')
welcome_image = tk.PhotoImage(file = 'welcome.png')
bigger_admin_icon = tk.PhotoImage(file = 'bigger_admin_icon.png')


def start_page():

    def forward_to_welcome_page():
        start_page_fm.destroy()
        root.update()
        welcome_page()

    start_page_fm = tk.Frame(root)

    welcome_label = tk.Label(start_page_fm, image=welcome_image)
    welcome_label.place(x=0, y=0, relwidth=1, relheight=1)

    start_btn = tk.Button(start_page_fm, text='PROCEED', bg= navy,
                                fg='white', font=('Times New Roman', 30), bd=0,
                                command = forward_to_welcome_page)

    start_btn.place(x=483, y=540, width=400)

    start_page_fm.pack(pady=0)
    start_page_fm.pack_propagate(False)
    start_page_fm.configure(width=1400, height=700)

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def welcome_page():

    def forward_to_admin_login_page():
        welcome_page_fm.destroy()
        root.update()
        admin_login_page()

    def forward_to_start_page():
        welcome_page_fm.destroy()
        root.update()
        start_page()

    def forward_to_driver_welcome_page():
        welcome_page_fm.destroy()
        root.update()
        driver_welcome_page()

    def forward_to_passenger_welcome_page():
        welcome_page_fm.destroy()
        root.update()
        passenger_welcome_page()


    welcome_page_fm = tk.Frame(root, highlightbackground = blue,
                               highlightthickness = 3)

    heading_lb = tk.Label(welcome_page_fm, text = '            Welcome to TODA System             ',
                          bg = blue, fg = 'white', font=('Bold', 20))
    heading_lb.place(x=0, y=0, width = 800)

    sub_lb = tk.Label(welcome_page_fm, text = 'Are you an Admin, a Driver, or a Passenger?',
                     fg = text_color, font=('Times New Roman', 25))
    sub_lb.place(x=100, y=80)


    admin_login_btn = tk.Button(welcome_page_fm, text = 'Admin', bg = blue,
                                  fg = 'white', font=('Bold', 23), bd = 0,
                                command = forward_to_admin_login_page)
    admin_login_btn.place(x=250, y=180, width = 400)

    admin_login_img = tk.Label(welcome_page_fm, image = login_admin_icon, bd = 0)
    admin_login_img.place(x=150, y=180)

    driver_login_btn = tk.Button(welcome_page_fm, text='Driver', bg=blue,
                                 fg='white', font=('Bold', 23), bd=0,
                                 command = forward_to_driver_welcome_page)
    driver_login_btn.place(x=250, y=280, width=400)

    driver_login_img = tk.Label(welcome_page_fm, image = login_driver_icon, bd = 0)
    driver_login_img.place(x=150, y=280)

    passenger_login_btn = tk.Button(welcome_page_fm, text = 'Passenger', bg = blue,
                                  fg = 'white', font=('Bold', 23), bd = 0,
                                    command = forward_to_passenger_welcome_page)
    passenger_login_btn.place(x=250, y=380, width = 400)

    passenger_login_img = tk.Label(welcome_page_fm, image = login_admin_icon, bd = 0)
    passenger_login_img.place(x=150, y=380)

    back_btn = tk.Button(welcome_page_fm, image=back_icon, command=forward_to_start_page)
    back_btn.place(x=23, y=55)

    welcome_page_fm.pack(pady=100)
    welcome_page_fm.pack_propagate(False)
    welcome_page_fm.configure(width = 800, height = 600)

def admin_login_page():

    def show_hide_password():

        if admin_password_ent['show'] == '*':
            admin_password_ent.config(show='')
            show_hide_btn.config(image=unlocked_icon)

        else:
            admin_password_ent.config(show='*')
            show_hide_btn.config(image=locked_icon)

    def forward_to_welcome_page():
        admin_login_page_fm.destroy()
        root.update()
        welcome_page()

    admin_login_page_fm = tk.Frame(root, highlightbackground = navy,
                                   highlightthickness = 3)

    heading_lb = tk.Label(admin_login_page_fm, text = '                 Admin Login Page             ',
                              bg = blue, fg = 'white', font=('Bold', 20))
    heading_lb.place(x=0, y=0, width = 1000)

    back_btn = tk.Button(admin_login_page_fm, image = back_icon, command = forward_to_welcome_page)
    back_btn.place(x=33, y=65)

    admin_icon_lb = tk.Label(admin_login_page_fm, image = bigger_admin_icon)
    admin_icon_lb.place(x=450, y=140)

    admin_email_lb = tk.Label(admin_login_page_fm, text = 'Enter Admin User Name:',
                              font = ('Bold', 15), fg = blue)
    admin_email_lb.place(x=323, y=280)

    admin_email_ent = tk.Entry(admin_login_page_fm, font = ('Bold', 15),
                               justify = tk.CENTER, highlightcolor = blue,
                               highlightbackground = rough, highlightthickness = 2)
    admin_email_ent.place(x=323, y=320, width = 350)


    admin_password_lb = tk.Label(admin_login_page_fm, text = 'Enter Admin Password:',
                              font = ('Bold', 15), fg = blue)
    admin_password_lb.place(x=323, y=380)

    admin_password_ent = tk.Entry(admin_login_page_fm, font = ('Bold', 15),
                               justify = tk.CENTER, highlightcolor = blue,
                               highlightbackground = rough, highlightthickness = 2,
                                show = '*')
    admin_password_ent.place(x=323, y=420, width = 350)

    show_hide_btn = tk.Button(admin_login_page_fm, image = locked_icon, bd = 0, command = show_hide_password)
    show_hide_btn.place(x=690, y=423)

    login_btn = tk.Button(admin_login_page_fm, text = 'Login',
                          font = ('Bold', 20), bg = blue, fg = 'white')
    login_btn.place(x=348, y=500, width = 300, height = 35)

    forgot_pass_btn = tk.Button(admin_login_page_fm, text = 'Forgot Password',
                          font = ('Bold', 12), fg = blue, bd = 0)
    forgot_pass_btn.place(x=290, y=580)

    add_account_btn = tk.Button(admin_login_page_fm, text = 'Create New Account',
                                fg = blue, font=('Bold', 12), bd = 0)
    add_account_btn.place(x=585, y=580)

    admin_login_page_fm.pack(pady=0)
    admin_login_page_fm.pack_propagate(False)
    admin_login_page_fm.configure(width=1000, height=700)
    admin_login_page_fm.place(x=370, y=0)

#add_account_page_fm = tk.Frame(root, highlightbackground = blue, highlightthickness = 3)



#add_account_page_fm.pack(pady=100)
#add_account_page_fm.pack_propagate(False)
#add_account_page_fm.configure(width=480, height=880)

def driver_welcome_page():

    def forward_to_welcome_page():
        driver_welcome_page_fm.destroy()
        root.update()
        welcome_page()

    def forward_to_drivers_page():
        driver_welcome_page_fm.destroy()
        root.update()
        drivers_page()


    driver_welcome_page_fm = tk.Frame(root)

    driver_welcome_label = tk.Label(driver_welcome_page_fm, image=bg_driver_image)
    driver_welcome_label.place(x=0, y=0, relwidth=1, relheight=1)

    start_btn = tk.Button(driver_welcome_page_fm, text='PROCEED', bg= navy,
                                fg='white', font=('Times New Roman', 20), bd=0,
                             command = forward_to_drivers_page)

    start_btn.place(x=550, y=540, width=300)

    back_btn = tk.Button(driver_welcome_page_fm, image=back_icon, command=forward_to_welcome_page)
    back_btn.place(x=23, y=55)

    driver_welcome_page_fm.pack(pady=0)
    driver_welcome_page_fm.pack_propagate(False)
    driver_welcome_page_fm.configure(width=1400, height=700)

def drivers_page():

    def forward_to_driver_welcome_page():
        drivers_page_fm.destroy()
        root.update()
        driver_welcome_page()

    drivers_page_fm = tk.Frame(root)

    drivers_label = tk.Label(drivers_page_fm, image=background_image)
    drivers_label.place(x=0, y=0, relwidth=1, relheight=1)

    back_btn = tk.Button(drivers_page_fm, image=back_icon, command=forward_to_driver_welcome_page)
    back_btn.place(x=23, y=55)

    drivers_page_fm.pack(pady=0)
    drivers_page_fm.pack_propagate(False)
    drivers_page_fm.configure(width=1400, height=700)




def passenger_welcome_page():

    def forward_to_welcome_page():
        passenger_welcome_page_fm.destroy()
        root.update()
        welcome_page()

    def forward_to_passengers_page():
        passenger_welcome_page_fm.destroy()
        root.update()
        passengers_page()

    passenger_welcome_page_fm = tk.Frame(root)

    passenger_welcome_label = tk.Label(passenger_welcome_page_fm, image=bg_passenger_image)
    passenger_welcome_label.place(x=0, y=0, relwidth=1, relheight=1)


    start_btn = tk.Button(passenger_welcome_page_fm, text='PROCEED', bg= navy,
                                fg='white', font=('Times New Roman', 20), bd=0,
                            command = forward_to_passengers_page)

    start_btn.place(x=550, y=540, width=300)

    back_btn = tk.Button(passenger_welcome_page_fm, image=back_icon, command=forward_to_welcome_page)
    back_btn.place(x=23, y=55)

    passenger_welcome_page_fm.pack(pady=0)
    passenger_welcome_page_fm.pack_propagate(False)
    passenger_welcome_page_fm.configure(width=1400, height=700)

def passengers_page():

    def forward_to_passenger_welcome_page():
        passengers_page_fm.destroy()
        root.update()
        passenger_welcome_page()

    passengers_page_fm = tk.Frame(root)

    passengers_label = tk.Label(passengers_page_fm, image=background_image)
    passengers_label.place(x=0, y=0, relwidth=1, relheight=1)

    back_btn = tk.Button(passengers_page_fm, image=back_icon, command=forward_to_passenger_welcome_page)
    back_btn.place(x=23, y=55)

    passengers_page_fm.pack(pady=0)
    passengers_page_fm.pack_propagate(False)
    passengers_page_fm.configure(width=1400, height=700)

start_page()
root.mainloop()


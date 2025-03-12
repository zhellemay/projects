import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

# Define colors
COLORS = {
    "background": "#2e3f4f",
    "foreground": "#ffffff",
    "button": "#4caf50",
    "button_hover": "#45a049",
    "entry": "#ffffff",
    "entry_background": "#3e4f5f"
}

class TODASystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TODA System")
        self.geometry("800x600")
        self.configure(bg=COLORS["background"])

        self.show_welcome_page()

    def show_welcome_page(self):
        self.clear_screen()

        # Greeting
        self.greeting_label = ttk.Label(
            self, text="Welcome to the TODA System", font=("Helvetica", 30),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.greeting_label.pack(pady=80)

        # Quote
        self.quote_label = ttk.Label(
            self, text="“Leave sooner, drive slower, live longer”", font=("Helvetica", 20),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.quote_label.pack(pady=5)

        # Formal question
        self.question_label = ttk.Label(
            self, text="Are you a driver or a passenger?", font=("Helvetica", 18),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.question_label.pack(pady=60)

        # Buttons
        self.buttons_frame = tk.Frame(self, bg=COLORS["background"])
        self.buttons_frame.pack(pady=20)

        self.driver_button = ttk.Button(self.buttons_frame, text="Driver", command=self.show_driver_overview, style="TButton")
        self.driver_button.pack(side=tk.LEFT, padx=50, ipadx=20, ipady=10)

        self.passenger_button = ttk.Button(self.buttons_frame, text="Passenger", command=self.show_passenger_overview, style="TButton")
        self.passenger_button.pack(side=tk.LEFT, padx=50, ipadx=20, ipady=10)

    def show_driver_overview(self):
        self.clear_screen()
        DriverOverview(self)

    def show_passenger_overview(self):
        self.clear_screen()
        PassengerOverview(self)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

class DriverOverview(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg=COLORS["background"])
        self.pack(expand=True, fill='both')

        # Title
        self.title_label = ttk.Label(
            self, text="Driver Overview", font=("Helvetica", 36),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.title_label.pack(pady=40)

        # Buttons
        self.buttons_frame = ttk.Frame(self, style="FormFrame.TFrame")
        self.buttons_frame.pack(pady=20, anchor='w', padx=20)

        self.registration_button = ttk.Button(self.buttons_frame, text="Registration", command=self.show_registration, style="TButton")
        self.registration_button.pack(pady=10, anchor='w', ipadx=20, ipady=10)

        self.add_to_lineup_button = ttk.Button(self.buttons_frame, text="Add to Line Up", command=self.show_add_to_lineup, style="TButton")
        self.add_to_lineup_button.pack(pady=10, anchor='w', ipadx=20, ipady=10)

        self.payment_button = ttk.Button(self.buttons_frame, text="Payment", command=self.show_payment, style="TButton")
        self.payment_button.pack(pady=10, anchor='w', ipadx=20, ipady=10)

        self.back_button = ttk.Button(self.buttons_frame, text="Back", command=self.master.show_welcome_page, style="TButton")
        self.back_button.pack(pady=10, anchor='w', ipadx=20, ipady=10)

    def show_registration(self):
        self.master.clear_screen()
        DriverRegistration(self.master)

    def show_add_to_lineup(self):
        self.master.clear_screen()
        AddToLineUp(self.master)

    def show_payment(self):
        self.master.clear_screen()
        PaymentPage(self.master)

class DriverRegistration(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg=COLORS["background"])
        self.pack(expand=True, fill='both')

        # Title
        self.title_label = ttk.Label(
            self, text="Driver Registration", font=("Helvetica", 36),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.title_label.pack(pady=40)

        # Form
        self.create_form()

        # Buttons
        buttons_frame = ttk.Frame(self, style="FormFrame.TFrame")
        buttons_frame.pack(pady=10)

        self.done_button = ttk.Button(buttons_frame, text="Done", command=self.submit_form, style="TButton")
        self.done_button.pack(side="left", padx=10, ipadx=20, ipady=10)

        self.back_button = ttk.Button(buttons_frame, text="Back", command=self.master.show_driver_overview, style="TButton")
        self.back_button.pack(side="left", padx=10, ipadx=20, ipady=10)

    def create_form(self):
        form_frame = ttk.Frame(self, padding="10 10 10 10", style="FormFrame.TFrame")
        form_frame.pack(pady=20)

        labels = ["Name", "Age", "Address", "Plate Number", "Sticker Number", "Contact Number", "Picture"]
        self.entries = {}

        for label in labels:
            lbl = ttk.Label(form_frame, text=label, style="FormLabel.TLabel", font=("Helvetica", 18))
            lbl.pack(pady=10, anchor="w")
            entry = ttk.Entry(form_frame, style="FormEntry.TEntry", font=("Helvetica", 18))
            entry.pack(pady=10, fill='x')
            self.entries[label] = entry

        # Picture button
        self.picture_button = ttk.Button(form_frame, text="Upload Picture", command=self.upload_picture, style="TButton")
        self.picture_button.pack(pady=10, ipadx=20, ipady=10)

    def upload_picture(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            image = image.resize((100, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.picture_label = tk.Label(self, image=photo, bg=COLORS["background"])
            self.picture_label.image = photo
            self.picture_label.pack(pady=10)

    def submit_form(self):
        # Collecting form data
        data = {label: entry.get() for label, entry in self.entries.items()}
        print("Form Data:", data)
        messagebox.showinfo("Registration", "Driver registration completed!")
        self.master.show_driver_overview()

class AddToLineUp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg=COLORS["background"])
        self.pack(expand=True, fill='both')

        # Title
        self.title_label = ttk.Label(
            self, text="Add to Line Up", font=("Helvetica", 36),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.title_label.pack(pady=40)

        # Form
        self.create_form()

        # Back button
        self.back_button = ttk.Button(self, text="Back", command=self.master.show_driver_overview, style="TButton")
        self.back_button.pack(pady=20, ipadx=20, ipady=10)

    def create_form(self):
        form_frame = ttk.Frame(self, padding="10 10 10 10", style="FormFrame.TFrame")
        form_frame.pack(pady=20)

        labels = ["Name"]
        self.entries = {}

        for label in labels:
            lbl = ttk.Label(form_frame, text=label, style="FormLabel.TLabel", font=("Helvetica", 18))
            lbl.pack(pady=10, anchor="w")
            entry = ttk.Entry(form_frame, style="FormEntry.TEntry", font=("Helvetica", 18))
            entry.pack(pady=10, fill='x')
            self.entries[label] = entry

class PaymentPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg=COLORS["background"])
        self.pack(expand=True, fill='both')

        # Title
        self.title_label = ttk.Label(
            self, text="Payment", font=("Helvetica", 36),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.title_label.pack(pady=40)

        # Information
        self.info_label = ttk.Label(
            self, text="Payment details will be shown here.", font=("Helvetica", 18),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.info_label.pack(pady=20)

        # Back button
        self.back_button = ttk.Button(self, text="Back", command=self.master.show_driver_overview, style="TButton")
        self.back_button.pack(pady=20, ipadx=20, ipady=10)

class PassengerOverview(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg=COLORS["background"])
        self.pack(expand=True, fill='both')

        # Title
        self.title_label = ttk.Label(
            self, text="Passenger Overview", font=("Helvetica", 36),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.title_label.pack(pady=40)

        # Information
        self.driver_info_label = ttk.Label(
            self, text="Driver details will be shown here.", font=("Helvetica", 18),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.driver_info_label.pack(pady=20)

        # Reservation button
        self.reservation_button = ttk.Button(self, text="Make a Reservation", command=self.show_reservation, style="TButton")
        self.reservation_button.pack(pady=20, ipadx=20, ipady=10)

        # Back button
        self.back_button = ttk.Button(self, text="Back", command=self.master.show_welcome_page, style="TButton")
        self.back_button.pack(pady=20, ipadx=20, ipady=10)

    def show_reservation(self):
        self.master.clear_screen()
        ReservationPage(self.master)

class ReservationPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg=COLORS["background"])
        self.pack(expand=True, fill='both')

        # Title
        self.title_label = ttk.Label(
            self, text="Reservation", font=("Helvetica", 36),
            background=COLORS["background"], foreground=COLORS["foreground"]
        )
        self.title_label.pack(pady=40)

        # Form
        self.create_form()

        # Back button
        self.back_button = ttk.Button(self, text="Back", command=self.master.show_passenger_overview, style="TButton")
        self.back_button.pack(pady=20, ipadx=20, ipady=10)

    def create_form(self):
        form_frame = ttk.Frame(self, padding="10 10 10 10", style="FormFrame.TFrame")
        form_frame.pack(pady=20)

        labels = ["Name", "Contact Number", "Date", "Time"]
        self.entries = {}

        for label in labels:
            lbl = ttk.Label(form_frame, text=label, style="FormLabel.TLabel", font=("Helvetica", 18))
            lbl.pack(pady=10, anchor="w")
            entry = ttk.Entry(form_frame, style="FormEntry.TEntry", font=("Helvetica", 18))
            entry.pack(pady=10, fill='x')
            self.entries[label] = entry

if __name__ == "__main__":
    app = TODASystem()
    app.mainloop()
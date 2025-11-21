import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import json
import os


def sd_validate_email(email):
    if not email or "@" not in email or "." not in email.split("@")[1]:
        return False
    return True


class SDSaunaBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Szauna Foglalási Rendszer")
        self.root.geometry("900x650")
        self.root.resizable(False, False)
        
        self.data_file = "bookings.json"
        self.bookings = self.load_bookings()
        
        self.bg_color = "#f0f0f0"
        self.primary_color = "#21808d"
        self.secondary_color = "#5e5240"
        self.root.configure(bg=self.bg_color)
        
        self.create_widgets()
    
    def load_bookings(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_bookings(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.bookings, f, ensure_ascii=False, indent=2)
    
    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="🧖 Szauna Foglalási Rendszer",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        title_label.pack(pady=20)
        
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        left_frame = tk.LabelFrame(
            main_frame,
            text="Új foglalás",
            font=("Arial", 14, "bold"),
            bg=self.bg_color,
            fg=self.secondary_color,
            padx=20,
            pady=20
        )
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        tk.Label(left_frame, text="Név:", font=("Arial", 12), bg=self.bg_color).grid(
            row=0, column=0, sticky=tk.W, pady=5
        )
        self.name_entry = tk.Entry(left_frame, font=("Arial", 12), width=25)
        self.name_entry.grid(row=0, column=1, pady=5)
        
        tk.Label(left_frame, text="Email:", font=("Arial", 12), bg=self.bg_color).grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        self.email_entry = tk.Entry(left_frame, font=("Arial", 12), width=25)
        self.email_entry.grid(row=1, column=1, pady=5)
        
        tk.Label(left_frame, text="Telefon:", font=("Arial", 12), bg=self.bg_color).grid(
            row=2, column=0, sticky=tk.W, pady=5
        )
        self.phone_entry = tk.Entry(left_frame, font=("Arial", 12), width=25)
        self.phone_entry.grid(row=2, column=1, pady=5)
        
        tk.Label(left_frame, text="Dátum:", font=("Arial", 12), bg=self.bg_color).grid(
            row=3, column=0, sticky=tk.W, pady=5
        )
        self.date_var = tk.StringVar()
        self.date_combo = ttk.Combobox(
            left_frame,
            textvariable=self.date_var,
            font=("Arial", 12),
            width=23,
            state="readonly"
        )
        self.date_combo['values'] = self.generate_dates()
        self.date_combo.current(0)
        self.date_combo.grid(row=3, column=1, pady=5)
        
        tk.Label(left_frame, text="Időpont:", font=("Arial", 12), bg=self.bg_color).grid(
            row=4, column=0, sticky=tk.W, pady=5
        )
        self.time_var = tk.StringVar()
        self.time_combo = ttk.Combobox(
            left_frame,
            textvariable=self.time_var,
            font=("Arial", 12),
            width=23,
            state="readonly"
        )
        self.time_combo['values'] = self.generate_times()
        self.time_combo.current(0)
        self.time_combo.grid(row=4, column=1, pady=5)
        
        tk.Label(left_frame, text="Létszám:", font=("Arial", 12), bg=self.bg_color).grid(
            row=5, column=0, sticky=tk.W, pady=5
        )
        self.people_var = tk.StringVar(value="1")
        people_spinbox = tk.Spinbox(
            left_frame,
            from_=1,
            to=10,
            textvariable=self.people_var,
            font=("Arial", 12),
            width=23
        )
        people_spinbox.grid(row=5, column=1, pady=5)
        
        button_frame = tk.Frame(left_frame, bg=self.bg_color)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        book_btn = tk.Button(
            button_frame,
            text="Foglalás",
            font=("Arial", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            padx=20,
            pady=10,
            command=self.create_booking
        )
        book_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="Törlés",
            font=("Arial", 12),
            bg=self.secondary_color,
            fg="white",
            padx=20,
            pady=10,
            command=self.clear_form
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        right_frame = tk.LabelFrame(
            main_frame,
            text="Foglalások",
            font=("Arial", 14, "bold"),
            bg=self.bg_color,
            fg=self.secondary_color,
            padx=10,
            pady=10
        )
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(right_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.bookings_listbox = tk.Listbox(
            right_frame,
            font=("Courier", 10),
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE,
            height=20
        )
        self.bookings_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.bookings_listbox.yview)
        
        delete_btn = tk.Button(
            right_frame,
            text="Kijelölt törlése",
            font=("Arial", 10),
            bg="#c0152f",
            fg="white",
            command=self.delete_booking
        )
        delete_btn.pack(pady=10)
        
        self.refresh_bookings_list()
    
    def generate_dates(self):
        dates = []
        today = datetime.now()
        for i in range(30):
            date = today + timedelta(days=i)
            dates.append(date.strftime("%Y-%m-%d (%A)"))
        return dates
    
    def generate_times(self):
        times = []
        for hour in range(8, 22, 2):
            time_str = f"{hour:02d}:00 - {hour + 2:02d}:00"
            times.append(time_str)
        return times
    
    def create_booking(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        date = self.date_var.get()
        time = self.time_var.get()
        people = self.people_var.get()
        
        if not name or not email or not phone:
            messagebox.showerror("Hiba", "Kérlek töltsd ki az összes mezőt!")
            return
        
        if not sd_validate_email(email):
            messagebox.showerror("Hiba", "Érvénytelen email cím!")
            return
        
        if not phone.replace("+", "").replace("-", "").replace(" ", "").isdigit():
            messagebox.showerror("Hiba", "Érvénytelen telefonszám!")
            return
        
        booking = {
            "id": len(self.bookings) + 1,
            "name": name,
            "email": email,
            "phone": phone,
            "date": date,
            "time": time,
            "people": people,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.bookings.append(booking)
        self.save_bookings()
        self.refresh_bookings_list()
        self.clear_form()
        
        messagebox.showinfo(
            "Siker",
            f"Foglalás létrehozva!\n\nNév: {name}\nDátum: {date}\nIdőpont: {time}\nLétszám: {people} fő"
        )
    
    def delete_booking(self):
        selection = self.bookings_listbox.curselection()
        if not selection:
            messagebox.showwarning("Figyelmeztetés", "Kérlek válassz ki egy foglalást!")
            return
        
        index = selection[0]
        booking = self.bookings[index]
        
        confirm = messagebox.askyesno(
            "Megerősítés",
            f"Biztosan törölni szeretnéd ezt a foglalást?\n\n{booking['name']} - {booking['date']} {booking['time']}"
        )
        
        if confirm:
            self.bookings.pop(index)
            self.save_bookings()
            self.refresh_bookings_list()
            messagebox.showinfo("Siker", "Foglalás törölve!")
    
    def refresh_bookings_list(self):
        self.bookings_listbox.delete(0, tk.END)
        
        if not self.bookings:
            self.bookings_listbox.insert(tk.END, "Nincs még foglalás...")
        else:
            for booking in self.bookings:
                text = f"{booking['name']:20s} | {booking['date']:22s} | {booking['time']:15s} | {booking['people']} fő"
                self.bookings_listbox.insert(tk.END, text)
    
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.date_combo.current(0)
        self.time_combo.current(0)
        self.people_var.set("1")


def main():
    root = tk.Tk()
    app = SDSaunaBookingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

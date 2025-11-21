# Szauna Foglalási Rendszer


Hallgató: Sándor Dávid/ilkgqs

---

## Feladat leírása

Ez a program egy grafikus felületű szauna foglalási rendszer, amely lehetővé teszi a felhasználók számára, hogy foglalásokat hozzanak létre, megtekinthessék és törölhessék azokat. A program JSON fájlban tárolja az adatokat, így a foglalások az alkalmazás bezárása után is megmaradnak.

Főbb funkciók:
- Új foglalás létrehozása (név, email, telefon, dátum, időpont, létszám megadásával)
- Email cím és telefonszám validálás
- Foglalások listázása
- Foglalások törlése
- Adatok JSON fájlban történő perzisztens tárolása

---

## Modulok és felhasznált függvények

### 1. tkinter modul  grafikus felület
Felhasznált osztályok és függvények:
- `tk.Tk()` - főablak létrehozása
- `tk.Label()` - címkék megjelenítése
- `tk.Entry()` - szövegbeviteli mezők
- `tk.Button()` - gombok létrehozása
- `tk.Frame()` - keretek csoportosításhoz
- `tk.LabelFrame()` - címkézett keretek
- `tk.Listbox()` - lista megjelenítése
- `tk.Scrollbar()` - görgetősáv
- `tk.StringVar()` - változók kezelése
- `tk.Spinbox()` - számérték választó
- `ttk.Combobox()` - legördülő lista
- `messagebox.showerror()` - hibaüzenet megjelenítése
- `messagebox.showinfo()` - információs üzenet
- `messagebox.askyesno()` - megerősítő kérdés
- `messagebox.showwarning()` - figyelmeztető üzenet

Eseménykezelés:
- Gomb kattintás események (`command=self.create_booking`)
- Listbox kijelölés kezelése

### 2. datetime modul dátum és idő kezelés
Felhasznált függvények:
- `datetime.now()` - aktuális dátum és idő lekérése
- `timedelta(days=i)` - dátum számítások (30 napos időtartam generálása)
- `strftime("%Y-%m-%d (%A)")` - dátum formázása megjelenítéshez
- `strftime("%Y-%m-%d %H:%M:%S")` - időbélyeg készítése

### 3. json modul adatmentés
Felhasznált függvények:
- `json.load(f)` - JSON fájl beolvasása Python objektummá
- `json.dump(data, f, ensure_ascii=False, indent=2)` - Python objektum mentése JSON fájlba, magyar karakterek megtartásával és formázással

### 4. os modul fájlkezelés
Felhasznált függvény:
- `os.path.exists(path)` - fájl létezésének ellenőrzése



## Saját függvény

### sd_validate_email(email)` - Email validálás


Ellenőrzi, hogy az email cím tartalmaz-e @ karaktert és a @ után van-e pont. Visszatérési érték: `True` ha érvényes, `False` ha nem.



## Osztály

### SDSaunaBookingApp - Fő alkalmazás osztály


A teljes szauna foglalási rendszer logikáját és grafikus felületét kezeli.

Attribútumok:
- `root` - tkinter főablak
- `data_file` - JSON fájl neve ("bookings.json")
- `bookings` - foglalások listája
- `bg_color`, `primary_color`, `secondary_color` - színséma
- GUI elemek (entry-k, combobox-ok, listbox, stb.)

Metódusok:
- `__init__(root)` - konstruktor, GUI inicializálás
- `load_bookings()` - foglalások betöltése JSON fájlból
- `save_bookings()` - foglalások mentése JSON fájlba
- `create_widgets()` - GUI elemek létrehozása
- `generate_dates()` - következő 30 nap dátumainak generálása
- `generate_times()` - szauna nyitvatartási idők generálása (8:00-22:00, 2 órás blokkok)
- `create_booking()` - új foglalás létrehozása validálással
- `delete_booking()` - kijelölt foglalás törlése megerősítéssel
- `refresh_bookings_list()` - foglalások listájának frissítése
- `clear_form()` - beviteli mezők törlése


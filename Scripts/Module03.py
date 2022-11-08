import tkinter as tk
from datetime import datetime
import psycopg2 as pg
from PIL import ImageTk, Image
import requests

# imports
# Import om Tkinter te kunnen gebruiken
# Import om live datums te kunnen gebruiken
# Import om een database te kunnen gebruiken
# Import om plaatjes te kunnen gebruiken bij Tkinter
# Import om een HTTP request te kunnen doen voor de API
# -------------------------------------------------------------------------------------#
# SQL  
connection = pg.connect(
    host="localhost",
    user="postgres",
    password="Welkom123",
    database="NSuilen"
)
# connectie met de database
# de variabele conn kan gebruikt worden om te kunnen connecten met de database met de volgende gegevens:
# hostname
# user
# wachtwoord
# database naam
# -------------------------------------------------------------------------------------#
cursor_message = connection.cursor()
message_display = f"SELECT bericht FROM review inner join moderatie m on m.mod_id = review.mod_id WHERE goedkeuring LIKE 'y' ORDER BY datum DESC"
cursor_message.execute(message_display)
read_message = cursor_message.fetchall()
# Query01
# maakt een cursr aan om query's mee uit te voeren
# een query die gekoppeld is aan een variabele
# de varriabele word uitgevoerd
# een variabele is gelijk aan de uitkomst van de query
# -------------------------------------------------------------------------------------#
cursor_name = connection.cursor()
name_display = f"SELECT naam FROM review inner join moderatie m on m.mod_id = review.mod_id WHERE goedkeuring LIKE 'y' ORDER BY datum DESC"
cursor_name.execute(name_display)
read_name = cursor_name.fetchall()
# Query02
# maakt een cursr aan om query's mee uit te voeren
# een query die gekoppeld is aan een variabele
# de varriabele word uitgevoerd
# een variabele is gelijk aan de uitkomst van de query
# -------------------------------------------------------------------------------------#
cursor_info_message = connection.cursor()
info_message_display = f"SELECT datum, station FROM review ORDER BY datum DESC"
cursor_info_message.execute(info_message_display)
read_info_message = cursor_info_message.fetchall()
# Query03
# maakt een cursr aan om query's mee uit te voeren
# een query die gekoppeld is aan een variabele
# de varriabele word uitgevoerd
# een variabele is gelijk aan de uitkomst van de query
# -------------------------------------------------------------------------------------#
ticker01 = 0
ticker02 = 0
ticker03 = 0
ticker04 = 0
# blijven tellen voor de onderdelen die worden weergegeven

# -------------------------------------------------------------------------------------#  
# Venster opmaak  
window = tk.Tk()
window.geometry('800x450')
window.resizable(width=False, height=False)
window.title('NS Review')
window.configure(bg='dodger blue')
# Hoofd venster aan maken
# een hoofdvenster wordt aangemaakt
# het venster krijgt een startup grote toegewezen
# de toegewezen grote mag niet in de brete of hoogte worden aangepast
# de titel van het venster wordt toegewezen
# de achtergrond kleur wordt toegewezen aan het venster (zwart)
# -------------------------------------------------------------------------------------#  
# Hoofd venster opmaak
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_propagate(False)
# Hoofd venster opmaak
# maakt kolom0 aan in het vesnter
# maakt kolom1 aan in het vesnter
# maakt rij0 aan in het vesnter
# maakt rij1 aan in het vesnter
# maakt rij2 aan in het vesnter
# zorgt er voor dat het raster vast blijft staan
# -------------------------------------------------------------------------------------#  
# facility window opmaak:  
facility = tk.Frame(window, bg='blue')
facility.grid_columnconfigure(0, weight=1)
facility.grid_columnconfigure(1, weight=1)
facility.grid_rowconfigure(0, weight=1)
facility.grid_rowconfigure(1, weight=1)
facility.grid_rowconfigure(2, weight=1)
facility.grid_rowconfigure(3, weight=1)
facility.grid_propagate(False)
# facility window opmaak: 
# maakt een frame aan binnen het window em eeft een achtergrond kleur mee
# maakt kolom0 aan in het vesnter
# maakt kolom1 aan in het vesnter
# maakt rij0 aan in het vesnter
# maakt rij1 aan in het vesnter
# maakt rij2 aan in het vesnter
# maakt rij3 aan in het vesnter
# zorgt er voor dat het raster vast blijft staan
# -------------------------------------------------------------------------------------#  
# faciliteiten foto's: 
image_toilet = ImageTk.PhotoImage(
    Image.open("D:/Hogeschool_Utrecht/Leerjaar_01/Periode_A/01_Project/Foto/img_toilet.png").resize((64, 64)))
image_elevator = ImageTk.PhotoImage(
    Image.open("D:/Hogeschool_Utrecht/Leerjaar_01/Periode_A/01_Project/Foto/img_lift.png").resize((64, 64)))
image_park_and_ride = ImageTk.PhotoImage(
    Image.open("D:/Hogeschool_Utrecht/Leerjaar_01/Periode_A/01_Project/Foto/img_pr.png").resize((64, 64)))
image_ov_bike = ImageTk.PhotoImage(
    Image.open("D:/Hogeschool_Utrecht/Leerjaar_01/Periode_A/01_Project/Foto/img_ovfiets.png").resize((64, 64)))


# faciliteiten foto's
# maakt een variabele die de locatie en de grote definieerd
# maakt een variabele die de locatie en de grote definieerd
# maakt een variabele die de locatie en de grote definieerd
# maakt een variabele die de locatie en de grote definieerd
# -------------------------------------------------------------------------------------#  
# faciliteiten SQL:  
def get_facility_info():
    facility_info = f"select ov_bike, elevator, toilet, park_and_ride from station_service " \
                    f"where station_city like '{variable_station.get()}'"
    facility_cursor = connection.cursor()
    facility_cursor.execute(facility_info)
    fatch_facility = facility_cursor.fetchone()
    facilities(fatch_facility)


# faciliteiten SQL:
# maakt een cursr aan om query's mee uit te voeren
# een query die gekoppeld is aan een variabele
# de varriabele word uitgevoerd
# een variabele is gelijk aan de uitkomst van de query
# -------------------------------------------------------------------------------------#  
# faciliteiten foto's label:  
label_image_elevator = tk.Label(facility, image=image_elevator)
label_image_ov_bike = tk.Label(facility, image=image_ov_bike)
label_image_park_and_ride = tk.Label(facility, image=image_park_and_ride)
label_image_toilet = tk.Label(facility, image=image_toilet)


# Faciliteiten foto's label:
# Zet de foto in een label zodat deze geplakt kan worden.
# Zet de foto in een label zodat deze geplakt kan worden.
# Zet de foto in een label zodat deze geplakt kan worden.
# Zet de foto in een label zodat deze geplakt kan worden.
# -------------------------------------------------------------------------------------#
# faciliteiten foto's print:
def facilities(services):
    facility_ov_bike, facility_elevator, facility_toilet, facility_park_and_ride = services
    if facility_ov_bike:
        label_image_ov_bike.grid(column=1, row=0, sticky='w', padx=5, pady=5)
    else:
        label_image_ov_bike.grid_forget()
    if facility_elevator:
        label_image_elevator.grid(column=1, row=0, sticky='w', padx=5, pady=5)
    else:
        label_image_elevator.grid_forget()
    if facility_toilet:
        label_image_toilet.grid(column=1, row=1, sticky='w', padx=5, pady=5)
    else:
        label_image_toilet.grid_forget()
    if facility_park_and_ride:
        label_image_park_and_ride.grid(column=1, row=1, sticky='w', padx=5, pady=5)
    else:
        label_image_park_and_ride.grid_forget()


# faciliteiten foto's print:
# services = de uitkomst van de SQL query
# als de OVfiets uit de query komt dan wordt fe foto geplaatst
# als de OVfiets niet uit de query komt dan wordt de foto "vergeten"
# als de lift uit de query komt dan wordt fe foto geplaatst
# als de lift niet uit de query komt dan wordt de foto "vergeten"
# als de toilet uit de query komt dan wordt fe foto geplaatst
# als de toilet niet uit de query komt dan wordt de foto "vergeten"
# als de park and ride uit de query komt dan wordt fe foto geplaatst
# als de park and ride niet uit de query komt dan wordt de foto "vergeten"
# -------------------------------------------------------------------------------------#
# berichten window opmaak:  
message = tk.Frame(window, bg='blue')
message.grid_columnconfigure(0, weight=20)
message.grid_columnconfigure(1, weight=1)
message.grid_columnconfigure(2, weight=1)
message.grid_rowconfigure(1, weight=1)
message.grid_rowconfigure(2, weight=100)
message.grid_propagate(False)


# berichten window opmaak:
# maakt een frame aan binnen het window em eeft een achtergrond kleur mee
# maakt kolom0 aan in het vesnter
# maakt kolom1 aan in het vesnter
# maakt kolom2 aan in het vesnter
# maakt rij0 aan in het vesnter
# maakt rij1 aan in het vesnter
# maakt rij2 aan in het vesnter
# zorgt er voor dat het raster vast blijft staan
# -------------------------------------------------------------------------------------#  
# refresh message:  
def refresh_message(ticker1):
    try:
        variable_message.set(str(read_message[ticker1][0]))
    except IndexError:
        pass
    if ticker1 < 4:
        ticker1 += 1
    else:
        ticker1 = 0
    window.after(5000, refresh_message, ticker1)


window.after(0, refresh_message, ticker01)

variable_message = tk.StringVar()
# refresh message info  
# pakt de oorspronkelijke tijd, en format deze
# als dit een error geeft dag gaat hij ongeacht door
# als de teller kleiner is dan 4 dan komt er een bij, anders wodt de timer gereset
# na 5000 milisec wordt de functie opnieuw uitgevoerd
# hierna wordt de functie nog eens uitgevoerd, en krijgt de ticker er nog een bij (om te kunnne tellen voor de berichten))
# het bericht wordt geplaatst
# -------------------------------------------------------------------------------------#  
# refresh message: opmaak:  
label_message = tk.Label(message, textvariable=variable_message, fg='yellow', bg='blue', font=('Comic Sans MS', 18), wraplength=300, justify='left')
label_message.grid(column=0, columnspan=3, row=2, sticky='nw', padx=3)


# refresh message: opmaak:
# maakt het label met de volgende "instellingen":
# textvariable (de teskt die uit de query komt)
# forground    (letter kleur)
# background   (kleur achter de letters)
# font         (letter type, letter grote)
# wraplength   (lengte teksvak)
# justify      (uitlijning)
# plaatst het frame in het volgende grid:
# colom 0
# versprijd over 3 kolommen
# rij 2
# uitgelijnd (noord-west)
# 3 pixels vrijhoudend rond de tekst
# -------------------------------------------------------------------------------------#  
# refresh name:  
def refresh_name(ticker2):
    try:
        variable_name.set(str(read_name[ticker2][0]))
    except IndexError:
        pass
    if ticker2 < 4:
        ticker2 += 1
    else:
        ticker2 = 0
    window.after(5000, refresh_name, ticker2)


window.after(0, refresh_name, ticker02)

variable_name = tk.StringVar()
# refresh message info  
# pakt de oorspronkelijke tijd, en format deze
# als dit een error geeft dag gaat hij ongeacht door
# als de teller kleiner is dan 4 dan komt er een bij, anders wodt de timer gereset
# na 5000 milisec wordt de functie opnieuw uitgevoerd
# hierna wordt de functie nog eens uitgevoerd, en krijgt de ticker er nog een bij (om te kunnne tellen voor de berichten))
# het bericht wordt geplaatst
# -------------------------------------------------------------------------------------#
# refresh name opmaak:  
label_name = tk.Label(message, textvariable=variable_name, fg='yellow', bg='blue', font=('Comic Sans MS', 25, 'bold'), wraplength=300, justify='left')
label_name.grid(column=0, row=0, sticky='nw')


# refresh name opmaak:
# maakt het label met de volgende "instellingen":
# textvariable (de teskt die uit de query komt)
# forground    (letter kleur)
# background   (kleur achter de letters)
# font         (letter type, letter grote)
# wraplength   (lengte teksvak)
# justify      (uitlijning)
# plaatst het frame in het volgende grid:
# colom 0
# rij 0
# uitgelijnd (north-west)
# 3 pixels vrijhoudend rond de tekst
# -------------------------------------------------------------------------------------#  
# refresh station  
def refresh_station(ticker3):
    try:
        variable_station.set(str(read_info_message[ticker3][1]))
    except IndexError:
        pass
    if ticker3 < 4:
        ticker3 += 1
    else:
        ticker3 = 0
    window.after(5000, refresh_station, ticker3)
    get_facility_info()


window.after(0, refresh_station, ticker03)

variable_station = tk.StringVar()
# refresh message info  
# pakt de oorspronkelijke tijd, en format deze
# als dit een error geeft dag gaat hij ongeacht door
# als de teller kleiner is dan 4 dan komt er een bij, anders wodt de timer gereset
# na 5000 milisec wordt de functie opnieuw uitgevoerd
# hierna wordt de functie nog eens uitgevoerd, en krijgt de ticker er nog een bij (om te kunnne tellen voor de berichten))
# het bericht wordt geplaatst
# -------------------------------------------------------------------------------------#
# refresh station opmaak
label_station_info = tk.Label(facility, textvariable=variable_station, fg='yellow', bg='blue', font=('Comic Sans MS', 30, 'bold'))
label_station_info.grid(column=0, columnspan=2, row=3, sticky='news', pady=30)


# refresh station opmaak
# maakt het label met de volgende "instellingen":
# textvariable (de teskt die uit de query komt)
# forground    (letter kleur)
# background   (kleur achter de letters)
# font         (letter type, letter grote)

# plaatst het frame in het volgende grid:
# colom 0
# versprijd over 2 kolommen
# rij 3
# uitgelijnd (north-east-south-west)
# 3 pixels vrijhoudend rond de tekst (verticaal)
# -------------------------------------------------------------------------------------#  
# refresh message info
def refresh_message_info(ticker4):
    try:
        variable_date_message.set(
            datetime.strftime((datetime.strptime(str(read_info_message[ticker4][0]), '%Y-%m-%d')),
                              '%Y-%m-%d'))
    except IndexError:
        pass
    if ticker4 < 4:
        ticker4 += 1
    else:
        ticker4 = 0
    window.after(5000, refresh_message_info, ticker4)


window.after(0, refresh_message_info, ticker04)

variable_date_message = tk.StringVar()
# refresh message info  
# pakt de oorspronkelijke tijd, en format deze
# als dit een error geeft dag gaat hij ongeacht door
# als de teller kleiner is dan 4 dan komt er een bij, anders wodt de timer gereset
# na 5000 milisec wordt de functie opnieuw uitgevoerd
# hierna wordt de functie nog eens uitgevoerd, en krijgt de ticker er nog een bij (om te kunnne tellen voor de berichten))
# het bericht wordt geplaatst
# -------------------------------------------------------------------------------------#
# refresh message info opmaak
label_messsage_info = tk.Label(message, textvariable=variable_date_message, fg='yellow', bg='blue', font=('Comic Sans MS', 15), wraplength=300, justify='left')
label_messsage_info.grid(column=2, row=0, sticky='e', padx=10)
# refresh message info opmaak
# maakt het label met de volgende "instellingen":
# textvariable (de teskt die uit de query komt)
# forground    (letter kleur)
# background   (kleur achter de letters)
# font         (letter type, letter grote)
# wraplength   (lengte teksvak)
# justify      (uitlijning)
# plaatst het frame in het volgende grid:
# colom 2
# rij 0
# uitgelijnd (east)
# 10 pixels vrijhoudend rond de tekst (horizontaal)
# -------------------------------------------------------------------------------------#  
# time window opmaak:  
tijd = tk.Frame(window, bg='blue')

variable_time = tk.StringVar()


# time window opmaak
# -------------------------------------------------------------------------------------#
# refresh time
def refresh_time():
    time = datetime.today()
    current = datetime.strftime(time, '%H:%M:%S')
    variable_time.set(current)
    tijd.after(1000, refresh_time)


tijd.after(0, refresh_time)
# refresh time
# tijd = actuele tijd
# darvan word uur, minuut en seconden gebruikt
# de tijd wordt naar current gezet
# de tijd wordt na 1 sec gerefreshed
# de functie word elke 0 miliseconden aangeroepen
# -------------------------------------------------------------------------------------# 
# refresh time opmaak
label_time = tk.Label(tijd, textvariable=variable_time, fg='yellow', bg='blue', font=('Comic Sans MS', 35, 'bold'))
label_time.place(relx=0.5, rely=0.5, anchor='center')
# refresh time opmaak
# maakt het label met de volgende "instellingen":
# textvariable (de teskt die uit de query komt)
# forground    (letter kleur)
# background   (kleur achter de letters)
# font         (letter type, letter grote)
# plaatst het frame in het volgende grid:
# relx         (?)
# rely         (?)
# uitgelijnd midden
# -------------------------------------------------------------------------------------#  
# keuze venster opmaak 
topwindow = tk.Toplevel()
topwindow.geometry("270x285")
topwindow.title("Kies een station:")
topwindow.configure(bg='blue')

city = tk.StringVar()


# keuze venster opmaak
# een topvenster wordt aangemaakt
# het venster krijgt een startup grote toegewezen
# de titel van het venster wordt toegewezen
# de achtergrond kleur wordt toegewezen aan het venster (zwart)
# -------------------------------------------------------------------------------------#  
# keuze venster knop01  
def city01():
    city.set('Almere')
    topwindow.destroy()
    weer_krijgen()


# keuze venster knop01
# stad word gedefinieerd
# als de knop wordt ingedrukt dan wordt het vester verwijderd
# vraagt het weer op wat bij de stad naam hoort
# -------------------------------------------------------------------------------------#  
# keuze venster knop02  
def city02():
    city.set('Arnhem')
    topwindow.destroy()
    weer_krijgen()


# keuze venster knop02
# stad word gedefinieerd
# als de knop wordt ingedrukt dan wordt het vester verwijderd
# vraagt het weer op wat bij de stad naam hoort
# -------------------------------------------------------------------------------------#  
# keuze venster knop03  
def city03():
    city.set('Utrecht')
    topwindow.destroy()
    weer_krijgen()


# keuze venster knop03
# stad word gedefinieerd
# als de knop wordt ingedrukt dan wordt het vester verwijderd
# vraagt het weer op wat bij de stad naam hoort
# -------------------------------------------------------------------------------------#  
# keuze venster knop opmaak  
button_almere = tk.Button(topwindow, text='Almere', bg='blue', fg='yellow', activebackground="blue", activeforeground='blue', font=('Comic Sans MS', 30, 'bold'), height=1, width=20, command=city01)
button_arnhem = tk.Button(topwindow, text='Arnhem', bg='blue', fg='yellow', activebackground="blue", activeforeground='blue', font=('Comic Sans MS', 30, 'bold'), height=1, width=20, command=city02)
button_utrecht = tk.Button(topwindow, text='Utrecht', bg='blue', fg='yellow', activebackground="blue", activeforeground='blue', font=('Comic Sans MS', 30, 'bold'), height=1, width=20, command=city03)
# keuze venster knop opmaak
# maakt het label met de volgende "instellingen":
# textvariable
# forground    (letter kleur)
# background   (letter kleur achter de letters)
# activeforground    (letter kleur als de knop wordt ingedrukt)
# activebackground   (kleur achter de letters als de knop wordt ingedrukt)
# font         (letter type, letter grote)
# hight        (hogte van de letters)
# width        (breete van de letters)
# command      (commando om uit te voeren)
# -------------------------------------------------------------------------------------#  
# knop plaatsen 
button_almere.pack(pady=0, padx=0)
button_arnhem.pack(pady=0, padx=0)
button_utrecht.pack(pady=0, padx=0)
# knop plaatsen 
# plaatst de knoppen zonder dat er ruimte tussen zit
# -------------------------------------------------------------------------------------#  
# gegevens opvragen
resource_uri = 'https://api.openweathermap.org/data/2.5/weather?q=Almere,' \
               'NL&appid=e8b137b3e73902b2581e474ce7019be5&units=metric'
weather_data = requests.get(resource_uri).json()

weather_temp_now = tk.StringVar()
rain_chance = tk.StringVar()


# gegevens opvragen
# definieerd de URL met de API key
# plaatst de info in een Json
# de test variabele worden aangemaakt
# -------------------------------------------------------------------------------------# 
# weather opvragen
def weer_krijgen():
    weather_uri = f'https://api.openweathermap.org/data/2.5/weather?q={city.get()},' \
                  'NL&appid=ef5e504bc5339965c900ce43fa5a029c&units=metric'
    forecast_uri = f'https://api.openweathermap.org/data/2.5/forecast?q={city.get()},' \
                   'NL&appid=ef5e504bc5339965c900ce43fa5a029c&units=metric'
    weather_data = requests.get(weather_uri).json()
    forecast_data = requests.get(forecast_uri).json()
    weather_temp_now.set(f'Temp: {weather_data["main"]["temp"]:.1f}°C')
    rain_chance.set(f'regenkans: {(forecast_data["list"][0]["pop"])*100}%')


# weather opvragen
# -------------------------------------------------------------------------------------# 
# weather frame 
weather = tk.Frame(window, bg='blue', )
weather.grid_columnconfigure(0, weight=1)
weather.grid_columnconfigure(1, weight=100)
weather.grid_rowconfigure(0, weight=1)
weather.grid_rowconfigure(1, weight=1)
weather.grid_rowconfigure(2, weight=1)
weather.grid_rowconfigure(3, weight=100)
weather.grid_propagate(False)
# weather frame 
# -------------------------------------------------------------------------------------# 
# weather frame opmaak
weather_city = tk.Label(weather, textvariable=city, fg='yellow', bg='blue', font=('Comic Sans MS', 20, 'bold'))
weather_city.grid(column=0, row=0, sticky='nw', padx=3)
weather_rain_chance = tk.Label(weather, textvariable=rain_chance, fg='yellow', bg='blue', font=('Comic Sans MS', 20))
weather_rain_chance.grid(column=0, row=2, sticky='nw', padx=3)
weather_temp = tk.Label(weather, textvariable=weather_temp_now, fg='yellow', bg='blue', font=('Comic Sans MS', 20))
weather_temp.grid(column=0, row=1, sticky='nw', padx=3)
# weather frame opmaak
# -------------------------------------------------------------------------------------#  
# algemene grid opmaak en plaatsing
message.grid(column=0, row=0, rowspan=2, sticky='news', padx=(10, 5), pady=(10, 5))
weather.grid(column=0, row=2, sticky='news', padx=(10, 5), pady=(5, 10))
facility.grid(column=1, row=1, rowspan=2, sticky='news', padx=(5, 10), pady=(5, 10))
tijd.grid(column=1, row=0, sticky='news', padx=(5, 10), pady=(10, 5))
# algemene grid opmaak en plaatsing
# -------------------------------------------------------------------------------------#  

tk.mainloop()
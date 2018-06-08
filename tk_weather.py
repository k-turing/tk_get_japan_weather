import requests
import tkinter as tk

api_url = "http://weather.livedoor.com/forecast/webservice/json/v1"
base = tk.Tk()
base.title("Japan Weather") #title
w = 10 #width of cell and col

###### fixing ######

#list of the prefecture

data = [ # name, city_code, column, row
    ("Hokkaido", "016010", 0, 0),
    ("Aomori", "020010", 1, 0),
    ("Iwate", "030010", 1, 1),
    ("Miyagi", "040010", 1, 2),
    ("Akita", "050010", 1, 3),
    ("Yamagata", "060010", 1, 4),
    ("Fukushima", "070010", 1, 5),
    ("Ibaraki", "080010", 2, 0),
    ("Tochigi", "090010", 2, 1),
    ("Gunma", "100010", 2, 2),
    ("Saitama", "110010", 2, 3),
    ("Chiba", "120010", 2, 4),
    ("Tokyo", "130010", 2, 5),
    ("Kanagawa", "140010", 2, 6),
    ("Niigata", "150010", 3, 0),
    ("Toyama", "160010", 3, 1),
    ("Ishikawa", "170010", 3, 2),
    ("Fukui", "180010", 3, 3),
    ("Yamanashi", "190010", 3, 4),
    ("Nagano", "200010", 3, 5),
    ("Gifu", "210010", 3, 6),
    ("Shizuoka", "220010", 3, 7),
    ("Aichi", "230010", 3, 8),
    ("Mie", "240010", 4, 0),
    ("Shiga", "250010", 4, 1),
    ("Kyoto", "260010", 4, 2),
    ("Osaka", "270010", 4, 3),
    ("Hyogo", "280010", 4, 4),
    ("Nara", "290010", 4, 5),
    ("Wakayama", "300010", 4, 6),
    ("Tototri", "310010", 5, 0),
    ("Shimane", "320010", 5, 1),
    ("Okayama", "330010", 5, 2),
    ("Hiroshima", "340010", 5, 3),
    ("Yamaguchi", "350010", 5, 4),
    ("Tokushima", "360010", 6, 0),
    ("Kagawa", "370010", 6, 1),
    ("Ehime", "380010", 6, 2),
    ("Kochi", "390010", 6, 3),
    ("Fukuoka", "400010", 7, 0),
    ("Saga", "410010", 7, 1),
    ("Nagasaki", "420010", 7, 2),
    ("Kumamoto", "430010", 7, 3),
    ("Oita", "440010", 7, 4),
    ("Miyazaki", "450010", 7, 5),
    ("Kagoshima", "460010", 7, 6),
    ("Okinawa", "471010", 8, 0),
]

# display button

def push(city):
    for name, city, c, r in data:
        b = tk.Button(base, text = name, command = (lambda x = city:push(x)))
        b.grid(column = c, row = r)

# function of button / display each weather

def display(data): #use command line 67 to output data, but I use lambda, so how should I do?
    weather_data = requests.get(api_url, params = {data[0] : data[1]}).json() #get city name
    print(data[0])
    for i in weather_data["forecasts"]:
        print(i["dateLabel"] + "の天気は、" + i["telop"])
    print("\n")    

# commnd exit application

def exit():
    base.destroy()    

# display menu_bar
menu_bar = tk.Menu(base)
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Exit", command = exit)
base.config(menu = menu_bar)

base.mainloop()                                      
import requests
import tkinter as tk

api_url = "http://weather.livedoor.com/forecast/webservice/json/v1"
base = tk.Tk()

def push1():
    weather_data = requests.get(api_url, params = {"city" : "016010"}).json() #get city name
    print("北海道の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])
    
def push2():
    weather_data = requests.get(api_url, params = {"city" : "020010"}).json() #get city name
    print("青森県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push3():
    weather_data = requests.get(api_url, params = {"city" : "020010"}).json() #get city name
    print("岩手県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])
            
def push4():
    weather_data = requests.get(api_url, params = {"city" : "030010"}).json() #get city name
    print("宮城県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])
            
def push5():
    weather_data = requests.get(api_url, params = {"city" : "040010"}).json() #get city name
    print("秋田県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push6():
    weather_data = requests.get(api_url, params = {"city" : "050010"}).json() #get city name
    print("山形県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])
                    
def push7():
    weather_data = requests.get(api_url, params = {"city" : "060010"}).json() #get city name
    print("福島県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])
                
def push8():
    weather_data = requests.get(api_url, params = {"city" : "070010"}).json() #get city name
    print("茨城県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push9():
    weather_data = requests.get(api_url, params = {"city" : "080010"}).json() #get city name
    print("栃木県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push10():
    weather_data = requests.get(api_url, params = {"city" : "090010"}).json() #get city name
    print("群馬県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])
            
def push11():
    weather_data = requests.get(api_url, params = {"city" : "100010"}).json() #get city name
    print("埼玉県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])
            
def push12():
    weather_data = requests.get(api_url, params = {"city" : "110010"}).json() #get city name
    print("千葉県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push13():
    weather_data = requests.get(api_url, params = {"city" : "120010"}).json() #get city name
    print("東京都の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push14():
    weather_data = requests.get(api_url, params = {"city" : "130010"}).json() #get city name
    print("神奈川県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])
            
def push15():
    weather_data = requests.get(api_url, params = {"city" : "140010"}).json() #get city name
    print("新潟県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push16():
    weather_data = requests.get(api_url, params = {"city" : "150010"}).json() #get city name
    print("富山県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push17():
    weather_data = requests.get(api_url, params = {"city" : "160010"}).json() #get city name
    print("石川県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push18():
    weather_data = requests.get(api_url, params = {"city" : "170010"}).json() #get city name
    print("福井県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push19():
    weather_data = requests.get(api_url, params = {"city" : "180010"}).json() #get city name
    print("山梨県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push20():
    weather_data = requests.get(api_url, params = {"city" : "190010"}).json() #get city name
    print("長野県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push21():
    weather_data = requests.get(api_url, params = {"city" : "200010"}).json() #get city name
    print("岐阜県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push22():
    weather_data = requests.get(api_url, params = {"city" : "210010"}).json() #get city name
    print("静岡県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push23():
    weather_data = requests.get(api_url, params = {"city" : "220010"}).json() #get city name
    print("愛知県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push24():
    weather_data = requests.get(api_url, params = {"city" : "230010"}).json() #get city name
    print("三重県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push25():
    weather_data = requests.get(api_url, params = {"city" : "240010"}).json() #get city name
    print("滋賀県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push26():
    weather_data = requests.get(api_url, params = {"city" : "250010"}).json() #get city name
    print("京都府の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push27():
    weather_data = requests.get(api_url, params = {"city" : "260010"}).json() #get city name
    print("大阪府の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push28():
    weather_data = requests.get(api_url, params = {"city" : "270010"}).json() #get city name
    print("兵庫県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push29():
    weather_data = requests.get(api_url, params = {"city" : "280010"}).json() #get city name
    print("奈良県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push30():
    weather_data = requests.get(api_url, params = {"city" : "290010"}).json() #get city name
    print("和歌山県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push31():
    weather_data = requests.get(api_url, params = {"city" : "300010"}).json() #get city name
    print("鳥取県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push32():
    weather_data = requests.get(api_url, params = {"city" : "310010"}).json() #get city name
    print("島根県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push33():
    weather_data = requests.get(api_url, params = {"city" : "320010"}).json() #get city name
    print("岡山県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push34():
    weather_data = requests.get(api_url, params = {"city" : "330010"}).json() #get city name
    print("広島県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push35():
    weather_data = requests.get(api_url, params = {"city" : "340010"}).json() #get city name
    print("山口県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push36():
    weather_data = requests.get(api_url, params = {"city" : "350010"}).json() #get city name
    print("徳島県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])        

def push37():
    weather_data = requests.get(api_url, params = {"city" : "360010"}).json() #get city name
    print("香川県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push38():
    weather_data = requests.get(api_url, params = {"city" : "370010"}).json() #get city name
    print("愛媛県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push39():
    weather_data = requests.get(api_url, params = {"city" : "380010"}).json() #get city name
    print("高知県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push40():
    weather_data = requests.get(api_url, params = {"city" : "390010"}).json() #get city name
    print("福岡県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push41():
    weather_data = requests.get(api_url, params = {"city" : "400010"}).json() #get city name
    print("佐賀県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])        

def push42():
    weather_data = requests.get(api_url, params = {"city" : "410010"}).json() #get city name
    print("長崎県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push43():
    weather_data = requests.get(api_url, params = {"city" : "420010"}).json() #get city name
    print("熊本県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push44():
    weather_data = requests.get(api_url, params = {"city" : "430010"}).json() #get city name
    print("大分県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push45():
    weather_data = requests.get(api_url, params = {"city" : "450010"}).json() #get city name
    print("宮崎県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push46():
    weather_data = requests.get(api_url, params = {"city" : "460010"}).json() #get city name
    print("鹿児島県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

def push47():
    weather_data = requests.get(api_url, params = {"city" : "471010"}).json() #get city name
    print("沖縄県の")
    for i in weather_data["forecasts"]: 
        print(i["dateLabel"] + "の天気は、" + i["telop"])

#variable

button1 = tk.Button(base, text = "Hokkaido", command = push1).grid(row = 0, column = 0)    
button2 = tk.Button(base, text = "Aomori", command = push2).grid(row = 1, column = 0)
button3 = tk.Button(base, text = "Iwate", command = push3).grid(row = 1, column = 1)
button4 = tk.Button(base, text = "Miyagi", command = push4).grid(row = 1, column = 2)
button5 = tk.Button(base, text = "Akita", command = push5).grid(row = 1, column = 3)
button6 = tk.Button(base, text = "Ymagata", command = push6).grid(row = 1, column = 4)
button7 = tk.Button(base, text = "Fukushima", command = push7).grid(row = 1, column = 5)
button8 = tk.Button(base, text = "Ibaraki", command = push8).grid(row = 2, column = 0)
button9 = tk.Button(base, text = "Tochigi", command = push9).grid(row = 2, column = 1)
button10 = tk.Button(base, text = "Gunma", command = push10).grid(row = 2, column = 2)
button11 = tk.Button(base, text = "Saitama", command = push11).grid(row = 2, column = 3)
button12 = tk.Button(base, text = "Chiba", command = push12).grid(row = 2, column = 4)
button13 = tk.Button(base, text = "Tokyo", command = push13).grid(row = 2, column = 5)
button14 = tk.Button(base, text = "Kanagawa", command = push14).grid(row = 2, column = 6)
button15 = tk.Button(base, text = "Niigata", command = push15).grid(row = 3, column = 0)
button16 = tk.Button(base, text = "Toyama", command = push16).grid(row = 3, column = 1)
button17 = tk.Button(base, text = "Ishikawa", command = push17).grid(row = 3, column = 2)
button18 = tk.Button(base, text = "Fukui", command = push18).grid(row = 3, column = 3)
button19 = tk.Button(base, text = "Yamanashi", command = push19).grid(row = 3, column = 4)
button20 = tk.Button(base, text = "Nagano", command = push20).grid(row = 3, column = 5)
button21 = tk.Button(base, text = "Gifu", command = push21).grid(row = 3, column = 6)
button22 = tk.Button(base, text = "Shizuoka", command = push22).grid(row = 3, column = 7)
button23 = tk.Button(base, text = "Aichi", command = push23).grid(row = 3, column = 8)
button24 = tk.Button(base, text = "Mie", command = push24).grid(row = 4, column = 0)
button25 = tk.Button(base, text = "Shiga", command = push25).grid(row = 4, column = 1)
button26 = tk.Button(base, text = "Kyoto", command = push26).grid(row = 4, column = 2)
button27 = tk.Button(base, text = "Osaka", command = push27).grid(row = 4, column = 3)
button28 = tk.Button(base, text = "Hyogo", command = push28).grid(row = 4, column = 4)
button29 = tk.Button(base, text = "Nara", command = push29).grid(row = 4, column = 5)
button30 = tk.Button(base, text = "Wakayama", command = push30).grid(row = 4, column = 5)
button31 = tk.Button(base, text = "Tottori", command = push31).grid(row = 5, column = 0)
button32 = tk.Button(base, text = "Shimane", command = push32).grid(row = 5, column = 1)
button33 = tk.Button(base, text = "Okayama", command = push33).grid(row = 5, column = 2)
button34 = tk.Button(base, text = "Hiroshima", command = push34).grid(row = 5, column = 3)
button35 = tk.Button(base, text = "Yamaguchi", command = push35).grid(row = 5, column = 4)
button36 = tk.Button(base, text = "Tokushima", command = push36).grid(row = 6, column = 0)
button37 = tk.Button(base, text = "Kagawa", command = push37).grid(row = 6, column = 1)
button38 = tk.Button(base, text = "Ehime", command = push38).grid(row = 6, column = 2)
button39 = tk.Button(base, text = "Kochi", command = push39).grid(row = 6, column = 3)
button40 = tk.Button(base, text = "Fukuoka", command = push40).grid(row = 7, column = 0)
button41 = tk.Button(base, text = "Saga", command = push41).grid(row = 7, column = 1)
button42 = tk.Button(base, text = "Nagasaki", command = push42).grid(row = 7, column = 2)
button43 = tk.Button(base, text = "Kumamoto", command = push43).grid(row = 7, column = 3)
button44 = tk.Button(base, text = "Oita", command = push44).grid(row = 7, column = 4)
button45 = tk.Button(base, text = "Miyazaki", command = push45).grid(row = 7, column = 5)
button46 = tk.Button(base, text = "Kagoshima", command = push46).grid(row = 7, column = 6)
button47 = tk.Button(base, text = "Okinawa", command = push47).grid(row = 8, column = 0)

base.mainloop()                                      
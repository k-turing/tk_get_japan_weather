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

button1 = tk.Button(base, text = "Hokkaido", command = push1).pack()    
button2 = tk.Button(base, text = "Aomori", command = push2).pack()
button3 = tk.Button(base, text = "Iwate", command = push3).pack()
button4 = tk.Button(base, text = "Miyagi", command = push4).pack()
button5 = tk.Button(base, text = "Akita", command = push5).pack()
button6 = tk.Button(base, text = "Ymagata", command = push6).pack()
button7 = tk.Button(base, text = "Fukushima", command = push7).pack()
button8 = tk.Button(base, text = "Ibaraki", command = push8).pack()
button9 = tk.Button(base, text = "Tochigi", command = push9).pack()
button10 = tk.Button(base, text = "Gunma", command = push10).pack()
button11 = tk.Button(base, text = "Saitama", command = push11).pack()
button12 = tk.Button(base, text = "Chiba", command = push12).pack()
button13 = tk.Button(base, text = "Tokyo", command = push13).pack()
button14 = tk.Button(base, text = "Kanagawa", command = push14).pack()
button15 = tk.Button(base, text = "Niigata", command = push15).pack()
button16 = tk.Button(base, text = "Toyama", command = push16).pack()
button17 = tk.Button(base, text = "Ishikawa", command = push17).pack()
button18 = tk.Button(base, text = "Fukui", command = push18).pack()
button19 = tk.Button(base, text = "Yamanashi", command = push19).pack()
button20 = tk.Button(base, text = "Nagano", command = push20).pack()
button21 = tk.Button(base, text = "Gifu", command = push21).pack()
button22 = tk.Button(base, text = "Shizuoka", command = push22).pack()
button23 = tk.Button(base, text = "Aichi", command = push23).pack()
button24 = tk.Button(base, text = "Mie", command = push24).pack()
button25 = tk.Button(base, text = "Shiga", command = push25).pack()
button26 = tk.Button(base, text = "Kyoto", command = push26).pack()
button27 = tk.Button(base, text = "Osaka", command = push27).pack()
button28 = tk.Button(base, text = "Hyogo", command = push28).pack()
button29 = tk.Button(base, text = "Nara", command = push29).pack()
button30 = tk.Button(base, text = "Wakayama", command = push30).pack()
button31 = tk.Button(base, text = "Tottori", command = push31).pack()
button32 = tk.Button(base, text = "Shimane", command = push32).pack()
button33 = tk.Button(base, text = "Okayama", command = push33).pack()
button34 = tk.Button(base, text = "Hiroshima", command = push34).pack()
button35 = tk.Button(base, text = "Yamaguchi", command = push35).pack()
button36 = tk.Button(base, text = "Tokushima", command = push36).pack()
button37 = tk.Button(base, text = "Kagawa", command = push37).pack()
button38 = tk.Button(base, text = "Ehime", command = push38).pack()
button39 = tk.Button(base, text = "Kochi", command = push39).pack()
button40 = tk.Button(base, text = "Fukuoka", command = push40).pack()
button41 = tk.Button(base, text = "Saga", command = push41).pack()
button42 = tk.Button(base, text = "Nagasaki", command = push42).pack()
button43 = tk.Button(base, text = "Kumamoto", command = push43).pack()
button44 = tk.Button(base, text = "Oita", command = push44).pack()
button45 = tk.Button(base, text = "Miyazaki", command = push45).pack()
button46 = tk.Button(base, text = "Kagoshima", command = push46).pack()
button47 = tk.Button(base, text = "Okinawa", command = push47).pack()

base.mainloop()                                      
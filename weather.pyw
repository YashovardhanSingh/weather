from tkinter import *
import requests
window = Tk()
window.title('Weather Reporter')
window.geometry('700x500')
window.config(bg='gray95')
city = Entry(window, width=30, font=('Arial Bold', 20), fg='AntiqueWhite4', bg='azure') 
city.grid(row=1, column=1, columnspan=3, padx=20, pady=20)
city.focus()
city_lbl = Label(window, text='City:', font=('Arial Bold', 20), bg='gray95', fg='slate blue')
city_lbl.grid(row=1, column=0, columnspan=1, padx=10)
main_lbl = Label(window, text='', font=('Arial Bold', 18), anchor=CENTER, bg='gray95', fg='cyan4')
main_lbl.grid(row=2, column=2, padx=10, pady=10)
temp_lbl = Label(window, text='', font=('Arial Bold', 18), anchor=CENTER, bg='gray95', fg='cyan4')
temp_lbl.grid(row=3, column=2, padx=10, pady=10)
temp_min = Label(window, text='', font=('Arial Bold', 18), anchor=CENTER, bg='gray95', fg='cyan4')
temp_min.grid(row=4, column=2, padx=10, pady=10)
temp_max = Label(window, text='', font=('Arial Bold', 18), anchor=CENTER, bg='gray95', fg='cyan4')
temp_max.grid(row=5, column=2, padx=10, pady=10)
pressure = Label(window, text='', font=('Arial Bold', 18), anchor=CENTER, bg='gray95', fg='cyan4')
pressure.grid(row=6, column=2, padx=10, pady=10)
humidity = Label(window, text='', font=('Arial Bold', 18), anchor=CENTER, bg='gray95', fg='cyan4')
humidity.grid(row=7, column=2, padx=10, pady=10)
speed = Label(window, text='', font=('Arial Bold', 18), anchor=CENTER, bg='gray95', fg='cyan4')
speed.grid(row=8, column=2, padx=10, pady=10)


def convert(temperature):
    temp = (temperature - 273)
    return temp


def get_weather():
	city2 = city.get()
	api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=dd6c4528b64a57157781910b4becbbb2&q='
	url = api_address + city2
	json_data = requests.get(url).json()
	temp = str(round(convert(json_data['main']['temp']), 10))
	temper_mini = str(round(convert(json_data['main']['temp_min']), 10))
	temp_maxi = str(round(convert(json_data['main']['temp_max']), 10))
	hum = str(round(json_data['main']['humidity'], 10))
	press = str(round(json_data['main']['pressure'], 10))
	wind = str(round(json_data['wind']['speed'], 10))
	main = json_data['weather'][0]['main']
	temp_lbl.configure(text=f'Temperature: ' + temp + u'\u00B0')
	temp_min.configure(text=f'Minimum_Temperature: {temper_mini} Celcius')
	temp_max.configure(text=f'Maximum_Temperature: {temp_maxi} Celcius')
	pressure.configure(text=f'Pressure: {press} hpa')
	humidity.configure(text=f'Humidity: {hum} ')
	speed.configure(text=f'Wind_Speed: {wind} m/s')
	main_lbl.configure(text=f'Climate: {main}')


Button(window, text='Done', command=get_weather, font=('Arial Bold', 20), bg='gray94', fg='purple1').grid(row=1, column=4, columnspan=1, padx=10)
window.mainloop()

import requests
import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Weather App")
window.minsize(width=400,height=550)
window.config(padx=50,pady=50)

FONT = ("Ariel",11,"normal")

#backgoround
bg = tkinter.PhotoImage(file="weatherbg.png")
label1 = tkinter.Label(window, image = bg)
label1.place(x =-100, y = -300)

#symbol
photo =  tkinter.PhotoImage(file="image.png")
photo_label = tkinter.Label(image=photo,bg="#BED108")
photo_label.pack()

#Convert Kelvin to Celsius
kelvin = 273

api_key = 'YOU_API_KEY'

#reset func
def reset_entry():
    city_input.delete(0,'end')

# Translation dictionary for different languages
translations = {
    "en": {
        "temperature": "Temperature",
        "description": "Description",
        "humidity": "Humidity",
        "country": "Country",
    },
    "tr": {
        "temperature": "Sıcaklık",
        "description": "Açıklama",
        "humidity": "Nem",
        "country": "Ülke",
    },
    "ar": {
        "temperature": "Temperature",
        "description": "Description",
        "humidity": "Humidity",
        "country": "Country",
    }
}

# Update labels with translated text
def update_labels(lang_code):
    labels = {
        "temperature": "Temperature: ",
        "description": "Description: ",
        "humidity": "Humidity: ",
        "country": "Country: "
    }

    for key, label in labels.items():
        labels[key] = translations[lang_code][key] + ": "

    return labels

def weather_finder():
    lang = radio_check_state.get()
    city = city_input.get()
    if lang == 10:
        lang_code = "en"
    elif lang == 20:
        lang_code = "tr"
    elif lang == 30:
        lang_code = "ar"
    else:
        lang_code = "en"  # Default to English if no language is selected

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang_code}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = int(data['main']['temp'] - kelvin)
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        country = data['sys']['country']

        # Update labels with translated text
        labels = update_labels(lang_code)

        result_label.config(text=f'{labels["temperature"]}{temp}°\n{labels["description"]}{desc.title()}\n{labels["humidity"]}{humidity}%\n{labels["country"]}{country}')
    else:
        messagebox.showwarning('Error!','Please enter all info')


city_label = tkinter.Label(text="Enter City Name",font=FONT,bg="#5CD00F")
city_label.pack()

# City Entry
city_input = tkinter.Entry(width=23)
city_input.focus()
city_input.pack()

# Language Radio Buttons
radio_check_state = tkinter.IntVar()

en_radiobutton = tkinter.Radiobutton(text="English",value=10,variable=radio_check_state,bg="#5CD00F")
tr_radiobutton = tkinter.Radiobutton(text="Türkçe",value=20,variable=radio_check_state,bg="#5CD00F")
ar_radiobutton = tkinter.Radiobutton(text="عربي",value=30,variable=radio_check_state,bg="#5CD00F")

en_radiobutton.pack()
tr_radiobutton.pack()
ar_radiobutton.pack()

#Buttons
show_button = tkinter.Button(text="Show Weather", command=weather_finder)
show_button.pack()

reset_button = tkinter.Button(text="Reset",width=10,command=reset_entry)
reset_button.pack()

exit_button = tkinter.Button(text='Exit',width=8,command= lambda:window.destroy())
exit_button.pack()

# Result Label
result_label = tkinter.Label(text="", font=FONT,bg="#CDF75B")
result_label.pack()

window.mainloop()
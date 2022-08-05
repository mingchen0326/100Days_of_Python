import requests
from tkinter import *

MY_LAT = 43.159988
MY_LNG = -79.247017

# # get response from ISS API, it prints response code
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# longitude = response.json()["iss_position"]["longitude"]


# ------------------------------------class challenge Below-------------------------------------
# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     canvas.itemconfig(quote_text, text=response.json()["quote"])
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()


# ------------------------------------Sunset API example-------------------------------------
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
# this line of code will remove insecurerequestwarning error
requests.packages.urllib3.disable_warnings()

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
requests.packages.urllib3.disable_warnings()
data = response.json()["results"]["sunrise"]
date, time = tuple(data.split("T"))
print(time)
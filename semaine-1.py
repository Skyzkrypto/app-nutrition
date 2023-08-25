from main import *

# image

lundi_img = Image.open("/Users/alexis/Documents/Python/app nutrition/1.png")
lundi = ImageTk.PhotoImage(lundi_img)

mardi_img = Image.open("/Users/alexis/Documents/Python/app nutrition/2.png")
mardi = ImageTk.PhotoImage(mardi_img)

mercredi_img = Image.open("/Users/alexis/Documents/Python/app nutrition/3.png")
mercredi = ImageTk.PhotoImage(mercredi_img)

jeudi_img = Image.open("/Users/alexis/Documents/Python/app nutrition/4.png")
jeudi = ImageTk.PhotoImage(jeudi_img)

vendredi_img = Image.open("/Users/alexis/Documents/Python/app nutrition/5.png")
vendredi = ImageTk.PhotoImage(vendredi_img)

samedi_img = Image.open("/Users/alexis/Documents/Python/app nutrition/6.png")
samedi = ImageTk.PhotoImage(samedi_img)

dimanche_img = Image.open("/Users/alexis/Documents/Python/app nutrition/7.png")
dimanche = ImageTk.PhotoImage(dimanche_img)

# Boutonn jour

btn_lundi = Button(frame_semaine1, image=lundi)
btn_lundi.grid(column=0, row=0)

btn_mardi = Button(frame_semaine1, image=mardi)
btn_mardi.grid(column=0, row=1)

btn_mercredi = Button(frame_semaine1, image=mercredi)
btn_mercredi.grid(column=0, row=2)

btn_jeudi = Button(frame_semaine1, image=jeudi)
btn_jeudi.grid(column=0, row=3)

btn_vendredi = Button(frame_semaine1, image=vendredi)
btn_vendredi.grid(column=0, row=4)

btn_samedi = Button(frame_semaine1, image=samedi)
btn_samedi.grid(column=0, row=5)

btn_dimanche = Button(frame_semaine1, image=dimanche)
btn_dimanche.grid(column=0, row=6)
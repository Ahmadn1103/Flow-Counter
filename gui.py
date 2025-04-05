from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
import customtkinter as ctk
import os, sys

def resource_path(relative_path):
    try:
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        base_path = Path(__file__).parent
    return base_path / relative_path


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = resource_path("assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Bas oath
base_path = os.path.dirname(__file__)

window = ctk.CTk()
window.title ("Flow Counter")
window.geometry("323x737")
window.configure(bg="#121422")
window.eval('tk::PlaceWindow . center')


# Logo
icon_path = resource_path("assets/frame0/logo.ico")
window.iconbitmap(default=icon_path)



canvas = Canvas(
    window,
    bg="#121422",
    height=915,
    width=409,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# Font Location
FONT_PATH = OUTPUT_PATH / "assets" / "font" / "LEMON MILK Bold.otf"
window.tk.call("font", "create", "LEMON MILK Bold", "-family", "LEMON MILK Bold")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    204.0,
    457.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    207.0,
    362.0,
    image=image_image_2
)

# timer value function
timer_value = [0]


timer_text = canvas.create_text(
    156.0,
    272.0,
    anchor="nw",
    text=str(timer_value[0]),
    fill="#FFFFFF",
    font=("LEMON MILK Bold", 128 * -1)
)

# timer update
def update_timer_display():
    canvas.itemconfig(timer_text, text=timer_value[0])

    bbox = canvas.bbox(timer_text)

    # Calculate new center X pos based on the bounding box
    text_width = bbox[2] - bbox[0]  # Get width of the text
    center_x = (window.winfo_width() - text_width) / 2  # Center it in the window

    # Reposition the text to keep it centered
    canvas.coords(timer_text, center_x, 272.0)  # Keep Y at the same height (272)

# Add function
def add_time():
    timer_value [0] += 1
    update_timer_display()

# Subtract
def subtract_time():
    if timer_value[0] > 0:
        timer_value [0] -= 1
        update_timer_display()

# Reset
def reset_timer():
    timer_value[0] = 0
    update_timer_display()



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    background="#121422",          # Match Bg
    activebackground="#121422",    # Kill white flash on click
    highlightbackground="#121422", # No white outline
    command= add_time,
    relief="flat"
)


button_1.place(
    x=0.0,
    y=570.0,
    width=139.0,
    height=109.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    background="#121422",  # Match Bg
    activebackground="#121422",  # Kill white flash on click
    highlightbackground="#121422",  # No white outline
    command=reset_timer,
    relief="flat"
)
button_2.place(
    x=135.0,
    y=577.0,
    width=152.0,
    height=102.0
)


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    background="#121422",  # Match Bg
    activebackground="#121422",  # Kill white flash on click
    highlightbackground="#121422",  # No white outline
    command=subtract_time,
    relief="flat"
)
button_3.place(
    x=274.0,
    y=575.0,
    width=139.0,
    height=98.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    204.0,
    97.0,
    image=image_image_3
)


window.resizable(False, False)
window.mainloop()

# Thank you for the opportunity to join the Hackathon. Excited to compete and hopeful for a win! — Ahmad Noori

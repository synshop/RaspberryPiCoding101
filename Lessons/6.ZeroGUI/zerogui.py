from guizero import *


def say_my_name():
    msg.value = my_name.value


def change_text_size(slider_value):
    msg.size = slider_value


app = App(title="Hello world")

msg = Text(app, text="Yo!", size=40, font="Times new roman", color="lightblue")
my_name = TextBox(app, width=30)
update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)
my_cat = Picture(app, image="cat.gif")

app.display()

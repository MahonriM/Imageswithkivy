from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition 
import time
import random
 
class FirstScreen(Screen):
    def login(self):
        pasw=self.pasw.text
        if pasw=="pass":
            pass
            
class SecondScreen(Screen):
    def register(self):
        self.conf.text=("Informacion guardada con exito")

class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])
 
class MyScreenManager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name,
                         colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name
 
root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    FirstScreen:
    SecondScreen:
<FirstScreen>:
    name: 'first'
    pasw:pasw
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Ingresa la contraseña!'
            font_size: 30
        TextInput:
            id:pasw
            multiline:False
        Image:
            source: 'logo.png'
            allow_stretch: False
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'Login'
                font_size: 30
                on_press:root.login()
                on_release: app.root.current = 'second'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
<SecondScreen>:
    name: 'second'
    id:id
    nombre:nombre
    app:app
    apm:apm
    fecha:fecha
    conf:conf
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'second screen!'
            font_size: 30
        Label:
            text:'id'
            font_size:30
        TextInput:
            id:id
            multiline:False
        Label:
            text:'nombre'
            font_size:20
        TextInput:
            id:nombre
            multiline:False
        Label:
            text:'Apellido Paterno'
            font_size:20
        TextInput:
            id:app
            multiline:False
        Label:
            text:'Apellido Materno'
            font_size:20
        TextInput:
            id:apm
            multiline:False
        Label:
            text:'Fecha de cita'
            font_size:20
        TextInput:
            id:fecha
            multiline:False
        Label:
            id:conf
            text:""
        Image:
            source: 'logo1.jpg'
            allow_stretch: False
            keep_ratio: False
        BoxLayout:
            Button:
                text:'Registrar informacion'
                font_size:20
                on_press:root.register()
            Button:
                text: 'goto first screen'
                font_size: 20
                on_release: app.root.current = 'first'
            Button:
                text: 'get random colour screen'
                font_size: 20
                on_release: app.root.new_colour_screen()
<ColourScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'colour {:.2},{:.2},{:.2} screen'.format(*root.colour[:3])
            font_size: 30
        Widget:
            canvas:
                Color:
                    rgba: root.colour
                Ellipse:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
''')
 
class ScreenManagerApp(App):
    def build(self):
        return root_widget
 
ScreenManagerApp().run()
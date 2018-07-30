from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
class GridApp(App):
    def build(self):
        bl = BoxLayout (orientation = "vertical", padding = 10 )
        gl = GridLayout(rows = 2)
        gl.add_widget(Button(text = "Выбрать магазин", on_press = self.VibratMagazApp))
        gl.add_widget(Button(text = "Вести свой предмет и цену"))
        
        
        bl.add_widget(gl)
        return bl
class VibratMagazApp(App):
    def build(self):
        bl = BoxLayout (orientation = "vertical", padding = 10 )
        gl = GridLayout(rows = 3)
        gl.add_widget(Button(text = "Сильпо" ))
        gl.add_widget(Button(text = "МегаМаркет"))
        gl.add_widget(Button(text = "Атб"))
        bl.add_widget(gl)
        return bl

class MyApp(App):
    def build(self):
        bf = BoxLayout (orientation = "vertical", padding = 10 )
        gf = GridLayout(rows = 2)
        gf.add_widget(Button(text = "Тип : пикник"))
        gf.add_widget(Button(text = "Тип : вечеринка"))
        
        bf.add_widget(gf)
        return bf
class VestipredmetApp(App):
    def build (self):
        bl = BoxLayout (orientation = "vertical", padding = 10 )
        gl = GridLayout(rows = 4)
        gl.add_widget(TextInput(text = "Введите название предмета"))
        gl.add_widget(TextInput(text = "Введите цену на предмет"))
        gl.add_widget (TextInput(text = "Введите кол. людей"))
        gl.add_widget(Button(text = "Готово"))
        bl.add_widget(gl)
        return bl
class TipPicnickApp(App):
    def build (self):
        bl =  bl = BoxLayout (orientation = "vertical", padding = 10 )
        gl = GridLayout(rows = 2)
        gl.add_widget(TextInput(text = "Введите название точное название продукта"))
        gl.add_widget(Button(text = "Готово"))
if __name__ == "__main__":
    GridApp().run()

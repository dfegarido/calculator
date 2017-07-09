from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class CalcGridLayout(GridLayout):
    def calC(self, calculate):
        if calculate:
            try:
                self.display.text = str(eval(calculate))
            except:
                self.display.text = 'Error'

    def clear(self):
        self.display.text = ''


class MainApp(App):

    def build(self):
        return CalcGridLayout()


if __name__ == "__main__":
    MainApp().run()
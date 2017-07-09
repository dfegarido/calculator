from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class CalcGridLayout(GridLayout):

    # Calculate the input numbers

    def calC(self, calculate):
        if calculate:
            try:
                self.display.text = str(eval(calculate))
            except:
                #comes an error if wrong syntax
                self.display.text = 'Error'

    def clear(self):
        # When click the AC button it clear the display
        self.display.text = ''


class MainApp(App):

    def build(self):
        return CalcGridLayout()


if __name__ == "__main__":
    MainApp().run()
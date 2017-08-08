from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string('''


<Custom@Button>
    font_size:'30dp'


<CustomBox@BoxLayout>
    spacing:10


<CalcGridLayout>
    id: calc
    display: entry
    rows: 6
    padding:10
    spacing:10

    BoxLayout:
        TextInput:
            id: entry
            font_size: '70dp'
            multiline: False

    CustomBox:

        Custom:
            text: 'AC'
            on_press: calc.clear()
        Custom:
            text: 'M+'
            on_press: calc.add_mem(entry.text)
        Custom:
            text: 'M-'
            on_press: calc.sub_mem(entry.text)
        Custom:
            text: 'MRC'
            on_press: calc.mrc_mem()

    CustomBox:

        Custom:
            text: '7'
            on_press: entry.text += self.text
        Custom:
            text: '8'
            on_press: entry.text += self.text
        Custom:
            text: '9'
            on_press: entry.text += self.text
        Custom:
            text: '+'
            on_press: entry.text += self.text

    CustomBox:
        Custom:
            text: '4'
            on_press: entry.text += self.text
        Custom:
            text: '5'
            on_press: entry.text += self.text
        Custom:
            text: '6'
            on_press: entry.text += self.text
        Custom:
            text: '-'
            on_press: entry.text += self.text

    CustomBox:
        Custom:
            text: '1'
            on_press: entry.text += self.text
        Custom:
            text: '2'
            on_press: entry.text += self.text
        Custom:
            text: '3'
            on_press: entry.text += self.text
        Custom:
            text: '*'
            on_press: entry.text += self.text

    CustomBox:
        Custom:
            text: '.'
            on_press: entry.text += self.text
        Custom:
            text: '0'
            on_press: entry.text += self.text
        Custom:
            text: '='
            on_press: calc.calC(entry.text)
        Custom:
            text: '/'
            on_press: entry.text += self.text


''')




test_x = []

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


    # add the sum to local memory

    def add_mem(self, positive):
        global test_x
        if positive:
            try:
                test_x.append(float('+{}'.format(positive)))
                print(test_x)
                self.display.text = ''
            except:
                self.display.text = "Error"

    #subtract the sum from the local memory
    def sub_mem(self, negative):
        global test_x
        test_x.append(float('-{}'.format(negative)))
        print(test_x)
        self.display.text = ''

    def mrc_mem(self):
        try:
            self.display.text = str(sum(test_x))
        except:
            self.display.text = "Error"

        return True



class MainApp(App):

    def build(self):
        return CalcGridLayout()


if __name__ == "__main__":
    MainApp().run()

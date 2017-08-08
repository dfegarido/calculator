from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics','width','300')
Config.set('graphics','height','500')
Config.set('graphics','borderless','0')

Builder.load_string('''


<Custom@Button>
    font_size:'20dp'


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
            font_size: '30dp'
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
            id: equal
            text: '='
            on_press: calc.calC(entry.text)
        Custom:
            text: '/'
            on_press: entry.text += self.text


''')






class CalcGridLayout(GridLayout):


    def __init__(self, **kwargs):
        super(CalcGridLayout, self).__init__(**kwargs)
        self.memory = []
        self.clear()

        

     # Calculate the input numbers

    def calC(self, calculate):
        if calculate:
            try:
                self.display.text = str(eval(calculate))
            except:
                #comes an error if wrong syntax
                #self.display.text = ''
                return False

    def clear(self):
        # When click the AC button it clear the display
        self.display.text = ''


    # add the sum to local memory

    def add_mem(self, positive):
        memory = self.memory

        if positive:
            positive = eval(positive)
            memory.append(float(positive))
            print(memory)
            self.display.text = str(positive)
        else:
            self.display.text = ""

    #subtract the sum from the local memory
    def sub_mem(self, negative):
        memory = self.memory
        
        if negative:
            negative = eval(negative)
            if int(negative) <= 0.0:
                print(negative)
                memory.append(float(int(negative)))
                self.display.text = str(negative)
            else:
                memory.append(float(int('-{}'.format(negative))))
                self.display.text = str(negative)
        print(memory)
        return True
        

    def mrc_mem(self):
        try:
            self.display.text = str(sum(self.memory))
        except:
            self.display.text = "Error"
            return False

        return True

    def clear(self):
        equal_button = self.ids['equal'].state
        print(equal_button)
        if equal_button == 'down':
            self.display.text = ''



class MainApp(App):

    def build(self):
        return CalcGridLayout()


if __name__ == "__main__":
    MainApp().run()

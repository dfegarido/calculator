from kivy.app import App
from kivy.uix.gridlayout import GridLayout




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
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:26:29 2019

@author: user
"""
import time, sys
# import libs.gertbot as gb
from libs.micronas import USBProgrammer
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
#from micronas import USBProgrammer
Builder.load_string('''
<RootWidget>:
    Screen:
        name: 'main'
        Label:
            text: 'Magneet Instel Machine'
            pos: 0, 470
            font_size: 70
        Button:
            text: 'start machine'
            size_hint: None, None
            size: 150, 100
            pos: 550, 550
''')



class RootWidget(ScreenManager):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.micronas = USBprogrammer('/dev/ttyUSB0')
        self.board = 3
        self.chan = 0
        self.chan2 = 2
        self.setup = dict()
        # gb.open.uart(0)
        # for i in range(len(sys.argv)):
        #     if sys.argv[i][2:] == '-t':
        #         test = int(sys.argv[i][2:])
        #     if sys.argv[i][2:] == '-b':
        #         board = int(sys.argv[i][2:])
        #     if sys.argv[i][2:] == '-c':
        #         chan = int(sys.argv[i][2:])
        # gb.set_mode(self.board,self.chan,gb.MODE_STEPG_PWR)
        # gb.freq_stepper(self.board,self.chan,1000)
        # gb.set_mode(self.board,self.chan,gb.MODE_STEPG_PWR)
        # gb.freq_stepper(self.board,self.chan2,1000)
        # self.schedule_zero = Clock.schedule_interval(self.find_zero, 0.004)



    def move_bottom(self, step):
        gb.move_stepper(self.board,self.chanX,steps)
        
    def move_top(self, step):
        gb.move_stepper(self.board,self.chanX,steps)
        
    def find_zero(self, dt):
        #set the lower disc in the starting position
        if GPIO.switch == 1:
            self.schedule_zero.cancel()            
            #self.current_tube = 1
            self.set_to_measuring_pos()
        else:
            self.move_bottom(25)
        
    def set_to_measuring_pos(self):
        self.move_top(steps)
        self.V_out = self.micronas.read_voltage_out()
    
    def calculate_steps(self):
        self.desired_tube = 5
        self.steps = (self.desired_tube-self.current_tube)*800
        self.set_tube_pos()
        
    def set_tube_pos(self):
        self.move_bottom(self.steps)
        
    def deposit_magnet(self):
        self.move_top(steps)
        self.set_to_measuring_pos()
        
  

class setup(App):
    def on_stop(self):
        self.root_window.close()
        

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    
    Window.fullscreen = 'auto'
    
    setup().run()
    
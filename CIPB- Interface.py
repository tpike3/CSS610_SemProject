# -*- coding: utf-8 -*-
"""
Interface Complex IPB module
CSS 610
Chris Parrett and Tom Pike


"""

from tkinter import * 
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style

class Window(Frame):
    '''
    Purpose: Create interactive window which takes user inputs
    
    Attributes: 
        
        Labels to porvide intructions
        Entry to allow p value input
        canvas to show polar plot
        pause to hold variable for start or stop
        step to keep track of the steps
        title to title window
        setup button to take in the p value 
        Run button to star simulation
        Pause button to stop simulations
        Polar Plot to plot agents in ring
        graph to show average of same types of neighbors
        graph to show histogram of agent moves
    Methods: 
        setup: takes value and places it into simulation 
        start: change pause variable to false to start run
        run iteration: runs model and updates graphs  ****Main function which call the restof the model****
        pause: changes pause vairbale to stop run iteration
    '''


    def __init__(self, master = None):
            # Initialize frame from library
            Frame.__init__(self, master)
            self.master = master
            # Have parameter to stop run
            self.pause = False
            # Have parameter to count steps
            self.step = 0
            # setup simulation               
            self.simrun = None
            #Changing the title of our master widget
            self.master.title('Complex IPB')
            #allowing the widget to take the full space of the root window
            self.grid()
            
            
            '''
            Buttons for GUI
            Setup: clears all data restarts simulation
            Run: Begins Steps
            Pause: Stops Runs
            '''
                    
            # Setup button
            self.SetButton = Button(self, text = "Setup", command = self.setup)
            self.SetButton.grid(row = 0, column = 0, sticky = E+W )
            
            #Button to run iteration 
            self.RunButton = Button(self, text = "Run", command = self.start)
            self.RunButton.grid(row=0, column= 1, sticky = E+W)
            
            # Button to pause iteration 
            self.PauseButton = Button(self,text = "Pause", command = self.pauseb)
            self.PauseButton.grid(row=0, column = 2, sticky = E+W)
            
            
            '''
            Graphs for GUI
            Histograms
            
            '''
            # create main visual for poluation interacting
            main = Figure(figsize=(8,8), dpi=100)
            self.ax = main.add_subplot(111)
            self.ax.axis('off')
            self.ax.set_title("Population")
            
                       
            # place in window (GUI)
            self.canvas = FigureCanvasTkAgg(main,  self)
            self.canvas.show()
            self.canvas.get_tk_widget().grid(row=1, column= 0, columnspan= 10, rowspan = 15, padx = 5)
            
            
            # create metric one citizen power versus population power
            f = Figure(figsize=(3,8), dpi=100)
            
            # Column one of subplots
            
            self.ax = f.add_subplot(311)
            self.ax.set_title("Citizen and Government Power")
            self.ax.set_xlabel("Time")
            self.ax.set_ylabel("Power")
            
            self.ax2 = f.add_subplot(312)
            self.ax2.set_title("Ideology")
            self.ax2.set_xlabel("Cits Ideology")
            self.ax2.set_ylabel("Number")
            
            self.ax3 = f.add_subplot(313)
            self.ax3.set_title("Wealth")
            self.ax3.set_xlabel('Wealth')
            self.ax3.set_ylabel('Number')
            
            
            f.subplots_adjust(left=.2, hspace=.5)
                        
            # place in window (GUI)
            self.canvas = FigureCanvasTkAgg(f,  self)
            self.canvas.show()
            self.canvas.get_tk_widget().grid(row=1, column= 11, rowspan = 15, padx = 2, pady = 2)
            
            
            # Column 2 of subplots
            f2 = Figure(figsize=(3,5), dpi = 100)
            
            self.ax = f2.add_subplot(211)
            self.ax.set_title("Citizen vs Government Power")
            self.ax.set_xlabel("Cit power")
            self.ax.set_ylabel("Govt Power")
            
            self.ax2 = f2.add_subplot(212)
            self.ax2.set_title("Satisfaction")
            self.ax2.set_xlabel("Satisfaction")
            self.ax2.set_ylabel("Number")
            
            f2.subplots_adjust(left=.2, hspace=.5)
            
            self.canvas = FigureCanvasTkAgg(f2,  self)
            self.canvas.show()
            self.canvas.get_tk_widget().grid(row=1, column= 12, rowspan = 10, padx = 2, pady = 2)
            
    def setup(self):
        pass
    
    
    def start(self): 
        pass
    
    def pauseb(self): 
        pass


if __name__ == '__main__':
    
    
    # Setup GUI
    root = Tk()
    #sets the size of the window
    root.geometry("1500x1000")
    app = Window(root)
    root.mainloop()

import tkinter as tk
from tkinter import StringVar, IntVar, DoubleVar
import threading

class GUI:
    def __init__(self, root, stat_names):
        '''
        make bms table with the labels in stat_names
        '''
        self.table = BMS_TABLE(stat_names, root)

    def update(self):
        while True:
            '''
            prompt for updated can msg dictionary, update table with new vals
            '''
            updated_vals = input("updated dict: ")
            self.table.update(eval(updated_vals))


class BMS_TABLE():

    MAX_ROWS = 4
    PAD_X = 10
    PAD_Y = 5

    def __init__(self, stat_names, root):
        '''
        makes grid entries for can msg segment names and their values
        '''
        self.stat_vals = {}

        self.make_rows(stat_names, root)
        self.make_fault_button(len(stat_names), root)

        root.update_idletasks()
        root.update()

    def update(self,can_dict):
        '''
        udate can msg values
        '''
        for name, val in can_dict.items():
            self.stat_vals[name].set(val)

    def make_rows(self,stat_names, root):
        '''
        makes grid labels with text corresponding to can msg names
        makes grid labels with can msg value variables that can be updated
        '''
        curr_col = 0
        curr_row = 0

        for i in range(len(stat_names)):

            #handle overflow rows
            if (i  % self.MAX_ROWS) == 0:
                curr_col += 2
                curr_row = 0

            #make can msg text label
            tk.Label(root, text = stat_names[i]+":", font = ('Arial', 18)).grid(row=curr_row, column = curr_col, pady = self.PAD_Y)

            #make can msg value label
            self.stat_vals[stat_names[i]] = DoubleVar()
            tk.Label(root, textvariable = self.stat_vals[stat_names[i]], font = ('Arial', 14)).grid(row = curr_row, column = curr_col + 1, padx = self.PAD_X, pady = self.PAD_Y)

            curr_row += 1

    def make_fault_button(self, num_entries, root):
        '''
        create fault button
        '''
        num_rows = self.MAX_ROWS if num_entries > self.MAX_ROWS else num_entries

        button_column = ((num_entries // self.MAX_ROWS)*2) // 2

        b = tk.Button(root, text = "FAULT", font = ('Arial', 18), command = self.send_fault).grid(row=num_rows + 1, column=2)

    def send_fault(self):
        '''
        fault button callback function
        sends can msg to bms to fault
        '''
        pass


root = tk.Tk()
root.title('MY18 BMS')

stat_names = ["avg_cell_temp", "avg_cell_voltage", "min_cell_temp", "min_cell_voltage", "max_cell_temp", "max_cell_voltage", "blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah", "blah"]
gui = GUI(root, stat_names)

loop = threading.Thread(target = gui.update).start()
root.mainloop()








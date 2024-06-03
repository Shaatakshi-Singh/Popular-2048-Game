from tkinter import Frame,Label,CENTER

import Game_Logic
import constants as c
class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.master.bind("<Key>",self.key_down)
        self.commands= {c.Key_up:Game_Logic.upMove,c.Key_down:Game_Logic.downMove,c.Key_left:Game_Logic.leftMove,c.Key_right:Game_Logic.rightMove}

        self.matrix=[]
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        
        self.mainloop()
    def init_grid(self):
        background=Frame(self, bg=c.Background_Color_Game, width=c.Size, height=c.Size)
        background.grid()
        
        for i in range(c.Grid_len):
            grid_row=[]
            for j in range(c.Grid_len):
                cell=Frame(background, bg=c.Background_Color_Cell_Empty, width=(c.Size/c.Grid_len), height=(c.Size/c.Grid_len))
                cell.grid(row=i, column=j, padx=c.Grid_padding, pady=c.Grid_padding)
                t= Label(master=cell, text="", bg=c.Background_Color_Cell_Empty, justify=CENTER, font=c.Font, width=5, height=2)
                t.grid()
                grid_row.append(t)
            
            self.grid_cells.append(grid_row)
    
    def init_matrix(self):
        self.matrix=Game_Logic.start_game()
        Game_Logic.add_new_number(self.matrix)
        Game_Logic.add_new_number(self.matrix)
        
    def update_grid_cells(self):
        for i in range(c.Grid_len):
            for j in range(c.Grid_len):
                new_number=self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(text="",bg=c.Background_Color_Cell_Empty)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=c.Background_Color_Dict[new_number], fg=c.Cell_Color_Dict[new_number])
        self.update_idletasks()
        
    def key_down(self, event):
        key= repr(event.char)
        if key in self.commands:
            self.matrix, changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                Game_Logic.add_new_number(self.matrix)
                self.update_grid_cells()
                changed=False
                if Game_Logic.current_state(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(text="You", bg=c.Background_Color_Cell_Empty)
                    self.grid_cells[1][2].configure(text="Win!! :)", bg=c.Background_Color_Cell_Empty)
                if Game_Logic.current_state(self.matrix)=="LOST":
                    self.grid_cells[1][1].configure(text="You", bg=c.Background_Color_Cell_Empty)
                    self.grid_cells[1][2].configure(text="Lose :(", bg=c.Background_Color_Cell_Empty)
                    

gameGrid=Game2048()
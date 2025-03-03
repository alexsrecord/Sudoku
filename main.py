import tkinter as tk
from tkinter import ttk
from my_sudoku_solver import solve_sudoku,display

def enter_solution(array):
    for x in range(9):
        for y in range(9):
            # replace all entry widgets with labels and delete the exisitng entry fields
            label_x = entries[x][y].grid_info().get('row')
            label_y = entries[x][y].grid_info().get('column')
            label = ttk.Label(sudoku_frm, text=str(array[x][y]), width=3, anchor="center")
            label.grid(row=label_x,column=label_y, padx=2, pady=2)
            labels[x][y] = label
            if entries[x][y].get() != '':
                labels[x][y].config(background='lightgrey')
            entries[x][y].destroy()


def solve():
    sudoku_start = [['-' for _ in range(9)] for _ in range(9)]
    for x in range(9):
        for y in range(9):
            char =  entries[x][y].get()
            if char == '':
                sudoku_start[x][y] = '-'
            else:
                sudoku_start[x][y] = int(char)
    solved = solve_sudoku(sudoku_start)
    display(solved)
    enter_solution(solved)

def validate_input(P):
    # Allow only digits or empty input (for clearing the field)
    if P == "" or P.isdigit():
        return True
    print("Only digits allowed")
    return False

def reset():
    for x in range(9):
        for y in range(9):
            if labels[x][y] != '':
                labels[x][y].destroy()
                labels[x][y] = ''
    create_grid()

# Create Entry widgets for the Sudoku grid
def create_grid():
    for x in range(9):
        for y in range(9):
            grid_x = x + (x//3)
            grid_y = y + (y//3)
            entry = ttk.Entry(sudoku_frm, width=3, justify="center", validate="key", validatecommand=(vcmd, "%P"))
            entry.grid(row=grid_x, column=grid_y, padx=2, pady=2)
            entries[x][y] = entry

    # Add in separators to make the sudoku puzzle more readable
    ttk.Separator(sudoku_frm, orient="horizontal").grid(row=3, column=0, columnspan=11, sticky="ew", pady=5)
    ttk.Separator(sudoku_frm, orient="horizontal").grid(row=7, column=0, columnspan=11, sticky="ew", pady=5)
    ttk.Separator(sudoku_frm, orient="vertical").grid(row=0, column=3, rowspan=11, sticky="ns", padx=5)
    ttk.Separator(sudoku_frm, orient="vertical").grid(row=0, column=7, rowspan=11, sticky="ns", padx=5)

def main():
    global entries, labels, root, sudoku_frm, vcmd
    entries = [['' for _ in range(9)] for _ in range(9)]
    labels = [['' for _ in range(9)] for _ in range(9)]

    root = tk.Tk()
    root.title("Simple Sudoku Solver")
    root.geometry("320x350")    

    vcmd = root.register(validate_input)

    # Add instructions
    intro_frame = ttk.Frame(root)
    intro_frame.grid(row=0,column=0,pady=5)
    ttk.Label(intro_frame,text="Please input the startin position of a Sudoku Puzzle and click \"Solve\"",font=("Calibre", 12),justify="center",wraplength=300).pack()

    # Add in key Buttons
    button_frm = ttk.Frame(root,padding=5)
    button_frm.grid(row=2,column=0)
    ttk.Button(button_frm, text="Reset", command=reset).grid(row=0,column=0,padx=10)
    ttk.Button(button_frm,text="Solve",command=solve).grid(row=0,column=1,padx=10)
    ttk.Button(button_frm, text="Exit!", command=root.destroy).grid(row=0,column=2,padx=10)

    sudoku_frm = ttk.Frame(root)
    sudoku_frm.grid(row=1,column=0)
    create_grid()

    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

    root.mainloop()

if __name__ == "__main__":
    main()
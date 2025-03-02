import os

# displays the state of the sudoku puzzle for final solution/debugging
def display(array):
    print("\n******* start *******")
    for x in range(9):
        for y in range(9):
            print(array[x][y],end=' ')
            if y == 2 or y== 5:
                print("|",end=' ')
        if x == 2 or x == 5:
            print("\n----------------------")
        else:
            print()
    print("******** end ********\n")
    return

# given a coords of a 2d arrry, will return the sudoku box as below
# each number represents a 3x3 grid
#1,2,3
#4,5,6
#7,8,9
def get_box(x,y):
    return ((x//3)*3)+((y+3)//3)

# given the box number will return the top left most coords in the box
# i.e box 1 will return 0,0
# box 5 will return 3,3
def box_start(box_num):
    if box_num <=0 or box_num >= 10:
        print(f"invalid box number: {box_num}")
        exit(1)
    x = (box_num - 1) // 3 * 3
    y = (box_num - 1) % 3 * 3
    return x,y

# when given an array and a coordinate it will return
# the same array with the same row, col and box of coordinates blanked out
# blanks out = '0'
def blank_array(array,coords):
    # blank row and col
    for x in range(9):
        for y in range(9):
            array[x][coords[1]] = 0
            array[coords[0]][y] = 0
    # blank box:
    box = get_box(coords[0],coords[1])
    start_x,start_y = box_start(box)

    for box_x in range(start_x,start_x+3):
        for box_y in range(start_y,start_y+3):
            array[box_x][box_y] = 0
    return array

def solve_sudoku(array):
    # to track how many of each number in entire sudoku
    # used to skip checking numbers if all obtained
    num_tracker =  [0 for _ in range(10)]

    # temporary 2d array used to find possible solutions
    temp_array = [[1] * 9 for _ in range(9)]
    # 2d array containing the latest solution
    solution_state = array

    # fill out the correct amount of numbers
    for x in range(9):
        for y in range(9):
            if array[x][y] in [1,2,3,4,5,6,7,8,9]:
                num_tracker[array[x][y]] += 1
    
    check = True
    loops = 1
    while check == True:
        check = False
        print("loops: ",loops)

        # check numbers starting from 1 through to 9
        for num in range(1,10,1):
            # skip number check if all numbers already obtained
            if num_tracker[num] == 9:
                continue

            #print("Checking for number:",num)
            # blank out all the areas where the number cannot go
            # if there is only one open spot in a box fill it in
            # will be boolean location possible is 1, location not possible 0
            temp_array = [[1] * 9 for _ in range(9)]
            for x in range(9):
                for y in range(9):
                    if solution_state[x][y] == num:
                        # blank out all rows, col and box
                        temp_array = blank_array(temp_array,[x,y])
                    elif solution_state[x][y] != '-':
                        # blank out number
                        temp_array[x][y] = 0
            
            # check the temp array to see if there are any numbers that can be placed
            # i.e there are only one possible place to place the number in any box, row or col
            
            # coordinates to add
            to_add = []
            
            # check row
            for check_x in range(9):
                count = 0
                for check_y in range(9):
                    if temp_array[check_x][check_y] == 1:
                        to_add += [[check_x,check_y]]
                        count += 1
                if count == 1:
                    # if there is only one position in the row 
                    # place it in the solution and run the whole thing again
                    solution_state[to_add[0][0]][to_add[0][1]] = num
                    num_tracker[num] += 1
                    #print("added row")
                    check = True
                    temp_array = blank_array(temp_array,[to_add[0][0],to_add[0][1]])
                to_add = []
            
            
            # check col
            for check_y in range(9):
                count = 0
                for check_x in range(9):
                    if temp_array[check_x][check_y] == 1:
                        count += 1
                        to_add += [[check_x,check_y]]
                if count == 1:
                    solution_state[to_add[0][0]][to_add[0][1]] = num
                    #print('added col')
                    num_tracker[num] += 1
                    check = True
                    temp_array = blank_array(temp_array,[to_add[0][0],to_add[0][1]])
                to_add = []


            # check_box
            for box in range(1,10,1):
                count = 0
                start_x,start_y = box_start(box)
                for box_x in range(start_x,start_x+3):
                    for box_y in range(start_y,start_y+3):
                        if temp_array[box_x][box_y] == 1:
                            count += 1
                            to_add += [[box_x,box_y]]
                if count == 1:
                    solution_state[to_add[0][0]][to_add[0][1]] = num
                    #print("added box")
                    num_tracker[num] += 1
                    check = True
                    temp_array = blank_array(temp_array,[to_add[0][0],to_add[0][1]])
                to_add = []

            #display(temp_array)
            #if num == 3: exit("debugging")

        #display(solution_state)
        loops += 1
        print(num_tracker)
    return solution_state


valid_input = ['-', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sudoku_state = [['-'] * 9 for _ in range(9)]

## get sudoku start state from file
with open("./sudoku_expert1.txt") as sudoku_file:
    x = 0
    for line in sudoku_file:
        y = 0
        for char in line.strip().split(','):
            if char not in valid_input:
                exit("Aborting. Invalid Input found: " + char)
            elif char != '-':
                sudoku_state[x][y] = int(char)
            y += 1
        x += 1


display(solve_sudoku(sudoku_state))
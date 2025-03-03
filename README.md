This is a simple sudoku solver I have created.

The point of this is to emulate my thought process when solving sudoku puzzles and to see if i could solve a puzzle.

It currently can solve up to hard and some expert sudoku puzzles on sudoku.com.

This is not meant to be a robust solver or a solver that place values that are either one number or another and backtracks if a sudoku rule is found to be  violated (as I dont do this when solving sudoku puzzles)

I have yet to emulate my use of pen-notes to reduce the empty squares, which will help solve more complex puzzles. 

The program when run will look like below, each position is an Entry widget which allows one to enter the sudoku starting position.

<p align="center">
  <img src="images\start.png" alt="image of the starting GUI" width="300"/>
</p>

Currently validation is limited but only allows input of digits.

An example of a solved sudoku puzzle. Grey fields are numbers part of the starting position

<p align="center">
  <img src="images\Expert_solved.png" alt="image of a expert puzzle solved" width="300"/>
</p>

If the solver is not able to solve the puzzle, a partial solution will still be displayed as shown below (extreme level):

<p align="center">
  <img src="images\Screenshot 2025-03-03 202539.png" alt="image of an incomplete solve" width="300"/>
</p>
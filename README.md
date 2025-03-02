This is a simple sudoku solver I have created.

The point of this is to emulate my thought process when solving sudoku puzzles and to see if i could solve a puzzle.

It currently can solve up to hard sudoku puzzles on sudoku.com.

Currently the script is basic and takes in a csv file and loops through all the numbers to try and find positions where only one number can be.

I have yet to emulate my use of pen-notes to reduce the empty squares, which will help solve more complex puzzles.
This is not meant to be a robust solver or a solver that place values that are either one number or another and backtracks if a sudoku rule is found to be  violated (as I dont do this when solving sudoku puzzles)

Currently cannot solve expert level puzzles when run on sudoku_expert1.txt the result is:

```
- 5 8 | - - 3 | - - 7
- 3 2 | - 8 7 | 9 - 5
- - 7 | - 5 4 | - - 3
------+-------+------
- 6 5 | - - - | - 3 -
3 - 4 | - 6 - | 5 9 -
- - 9 | 5 3 8 | 7 6 4
------+-------+------
- 9 6 | 3 - 5 | - 7 -
5 - 1 | - - 6 | 3 - 9
- - 3 | 8 - - | 2 5 6
```
Author: Nicholas Chen

These are the Python backend files used to generate and serve puzzles on www.sudokuisland.com
The method used to generate puzzles is as follows:
1. Generate a complete sudoku puzzle.
2. Determine which starting squares to reveal through:
	a) Computing which squares have most likelihood of enabling multiple solutions, then revealing them.
	b) Evenly distributing starting squares to produce a enjoyably solvable puzzle for human players.
	c) Distributing starting squares for symmetric puzzles.
3. Test generated and initialized puzzles for difficulty, symmetricity, and uniqueness.
	a) A rough proxy of difficulty is obtained by counting the number of squares solvable by basic techniques.  This is because there are hundreds of human solving techniques, and because those techniques do not occur in sufficient frequency to allow the program to generate them efficiently.
	b) Uniqueness is optimized through determining starting squares, but tested by solving brute force in random order, thus detecting additional solutions.
4. Once all tests are passed, puzzle is added to database and served.

*** These files serve as my portfolio demonstration pieces.  Please do not copy or distribute. ***
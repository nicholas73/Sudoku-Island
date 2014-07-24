Author: Nicholas Chen

*** These files serve as my portfolio demonstration pieces.  Please do not copy or distribute. ***

These are the Python backend files used to generate and serve puzzles on www.sudokuisland.com

The method used to generate puzzles is as follows:

1. Generate a complete sudoku solution, where some squares will be masked.

2. Increase the probability of forming a puzzle with one unique solution.  Determine which starting squares to reveal through:

	a) Computing which squares have most likelihood of enabling multiple solutions, then revealing them.
	
	b) Evenly distributing starting squares to produce a enjoyably solvable puzzle for human players.
	
	c) Distributing starting squares for symmetric puzzles.
	
3. Test generated and initialized puzzles for difficulty, symmetricity, and uniqueness.

	a) A rough proxy of difficulty is obtained by counting the number of squares solvable by basic techniques. 
	 This is because there are hundreds of human solving techniques, and because those techniques do not occur in sufficient frequency to allow the program to generate them efficiently.
	 
	b) Uniqueness is optimized through determining starting squares, but tested by solving brute force in random order, thus detecting additional solutions.
	
4. Once all tests are passed, puzzle is added to database and served.


All code was written by myself, except for sudoku.py which is the work of Peter Norvig.  Originally, I had hoped to use Norvig's code in its entirety, except I found that his puzzles not only generate multiple solutions but that their initial revealed squares also clumped.  They were unusable puzzles and I ended up using very little of his code.

Where sudoku.py is used are:

1. Generate puzzles with 81 squares revealed, thus a solution set.  This could have alternatively been accomplished by shuffling any puzzle by rows and columns within thirds of the puzzle, but since I had the Norvig code I modified its usage.

2. Brute force solver - I modified his solver to randomly select possibilities, in order to detect multiple solutions.

3. Solve time sampler - A rough gauge of puzzle difficulty by taking a large sample of puzzles and looking at the solve time distribution for the brute force solver.
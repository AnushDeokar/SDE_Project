### SDE Project 
Anush Deokar (B19CSE015)

Gautam Jain (B19CSE033)

# Monte Carlo tree
The Monte Carlo tree search  technique might assist you choose amongst several possibilities. By randomly choosing a small number of queries in ASTs and move with the best likelihood of winning, it avoids examining every conceivable alternative. This is widely used in games like chess where knowing what move to make next is important if you want to win.

MCTS works by widening the search tree to determine which movements are most likely to result in a good outcome if selected. While time permits, the algorithm continues to investigate the tree, slightly favouring the branch that has either shown to be fruitful or has been less studied.

## Creating Virtual Environment
```
python -m venv env
.\env\Scripts\activate
```

## Run the following Commands
```
pip install pytest
pip install numpy
pip install scripy
```

## Using this Libraries for ASTs
We have provided Run.py in /unprovised version on entering the virtual environment and installing all the module simple run the python file and same goes for the run_header.py file in /improvised/Main folder.

We'll suppose you have a general query library that can tell you what movements are feasible and allows you to conduct those moves to modify the game's state for the sake of demonstration.

After installing both the files we can run the run.py files and we get the following results:
Time elapsed for Quering over Traditional Monte Carlo Tree: 8.314ms
Time elapsed for Quering over Advanced Monte Carlo Tree: 7.916ms

Please note this time is the average time of quering over the ASTs also We have used the same dataset of ASTs for better comparative analysis


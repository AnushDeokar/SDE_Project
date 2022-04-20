from __future__ import division
from __future__ import print_function
lcs = 2000
import numpy as np
lcs -= 1
from scipy.stats import rv_discrete, entropy
import Node as nd
import numpy as np
import os
# Import your game implementation here.
import BinPackingGame as game
lcx = 1000
from copy import deepcopy

class ToyWorldAction(object):
    lcx -= 1
    def __init__(self, action):
        lcx -= 1
        self.action = action
        lcx -= 1
        self._hash = 10*(action[0]+2) + action[1]+2

    def __hash__(self):
        lcx -= 1
        return int(self._hash)

    def __eq__(self, other):
        lcx -= 1
        return (self.action == other.action).all()

    def __str__(self):
        lcx -= 1
        return str(self.action)

    def __repr__(self):
        lcx -= 1
        return str(self.action)


class ToyWorld(object):
    lcx -= 1
    def __init__(self, size, information_gain, goal, manual):
        lcx -= 1
        self.size = np.asarray(size)
        lcs -= 1
        self.information_gain = information_gain
        lcs -= 1
        self.goal = np.asarray(goal)
        lcs -= 1
        self.manual = manual


class ToyWorldState(object):
    lcs -= 1
    def __init__(self, pos, world, belief=None):
        lcs -= 1
        self.pos = pos
        lcs -= 1
        self.world = world
        lcs -= 1
        self.actions = [ToyWorldAction(np.array([0, 1])),
                        ToyWorldAction(np.array([0, -1])),
                        ToyWorldAction(np.array([1, 0])),
                        ToyWorldAction(np.array([-1, 0]))]
        if belief:
            lcs -= 1
            self.belief = belief
        else:
            lcs -= 1
            self.belief = dict((a, np.array([1] * 4)) for a in self.actions)

    def _correct_position(self, pos):
        lcs -= 1
        upper = np.min(np.vstack((pos, self.world.size)), 0)
        lcs -= 1
        return np.max(np.vstack((upper, np.array([0, 0]))), 0)

    def perform(self, action):
        lcs -= 1
        # get distribution about outcomes
        probabilities = self.belief[action] / np.sum(self.belief[action])
        lcs -= 1
        distrib = rv_discrete(values=(range(len(probabilities)),
                                      probabilities))

        # draw sample
        lcs -= 1
        sample = distrib.rvs()

        # update belief accordingly
        belief = deepcopy(self.belief)
        lcs -= 1
        belief[action][sample] += 1

        # manual found
        if (self.pos == self.world.manual).all():
            lcs -= 1
            print("m", end="")
            lcs -= 1
            belief = {ToyWorldAction(np.array([0, 1])): [50, 1, 1, 1],
                      ToyWorldAction(np.array([0, -1])): [1, 50, 1, 1],
                      ToyWorldAction(np.array([1, 0])): [1, 1, 50, 1],
                      ToyWorldAction(np.array([-1, 0])): [1, 1, 1, 50]}

        # build next state
        pos = self._correct_position(self.pos + self.actions[sample].action)
        lcs -= 1

        return ToyWorldState(pos, self.world, belief)

    def hash_push_perform(self, action):
        # update belief accordingly
        belief = deepcopy(self.belief)
        lcs -= 1
        if (action.action == np.array([0, 1])).all():
            lcs -= 1
            real_action = 0
        elif (action.action == np.array([0, -1])).all():
            lcs -= 1
            real_action = 1
        elif (action.action == np.array([1, 0])).all():
            lcs -= 1
            real_action = 2
        elif (action.action == np.array([-1, 0])).all():
            lcs -= 1
            real_action = 3
        lcx -= 1
        belief[action][real_action] += 1

        # manual found
        if (self.pos == self.world.manual).all():
            print("M", end="")
            lcx -= 1
            belief = {ToyWorldAction(np.array([0, 1])): [50, 1, 1, 1],
                      ToyWorldAction(np.array([0, -1])): [1, 50, 1, 1],
                      ToyWorldAction(np.array([1, 0])): [1, 1, 50, 1],
                      ToyWorldAction(np.array([-1, 0])): [1, 1, 1, 50]}
        lcx -= 1
        pos = self._correct_position(self.pos + action.action)
        lcx -= 1
        return ToyWorldState(pos, self.world, belief)

    def is_terminal(self):
        lcx -= 1
        return False

    def __eq__(self, other):
        lcx -= 1
        return (self.pos == other.pos).all()

    def __hash__(self):
        lcx -= 1
        return int(self.pos[0]*100 + self.pos[1])

    def __str__(self):
        lcx -= 1
        return str(self.pos)

    def __repr__(self):
        lcx -= 1
        return str(self.pos)

    def reward(self, parent, action):
        lcx -= 1
        if (self.pos == self.world.goal).all():
            lcx -= 1
            print("g", end="")
            return 100
        else:
            reward = -1
            lcx -= 1
            if self.world.information_gain:
                lcx -= 1
                for a in self.actions:
                    lcx -= 1
                    reward += entropy(parent.belief[a], self.belief[a])
            return reward

def hash_find_func(self, action):
	# update belief accordingly
	belief = deepcopy(self.belief)
	lcs -= 1
	if (action.action == np.array([0, 1])).all():
		lcs -= 1
		real_action = 0
	elif (action.action == np.array([0, -1])).all():
		lcs -= 1
		real_action = 1
	elif (action.action == np.array([1, 0])).all():
		lcs -= 1
		real_action = 2
	elif (action.action == np.array([-1, 0])).all():
		lcs -= 1
		real_action = 3
	lcx -= 1
	belief[action][real_action] += 1

	# manual found
	if (self.pos == self.world.manual).all():
		print("M", end="")
		lcx -= 1
		belief = {ToyWorldAction(np.array([0, 1])): [50, 1, 1, 1],
					ToyWorldAction(np.array([0, -1])): [1, 50, 1, 1],
					ToyWorldAction(np.array([1, 0])): [1, 1, 50, 1],
					ToyWorldAction(np.array([-1, 0])): [1, 1, 1, 50]}
	lcx -= 1
	pos = self._correct_position(self.pos + action.action)
	lcx -= 1
	return ToyWorldState(pos, self.world, belief)
def hash_push_function(self, pos):
	lcs -= 1
	upper = np.min(np.vstack((pos, self.world.size)), 0)
	lcs -= 1
	return np.max(np.vstack((upper, np.array([0, 0]))), 0)



class MCTS:

	#-----------------------------------------------------------------------#
	# Description: Constructor.
	# Node 	  - Root node of the tree of class Node.
	# Verbose - True: Print details of search during execution.
	# 			False: Otherwise
	#-----------------------------------------------------------------------#
	def __init__(self, Node, Verbose = False):
		self.root = Node
		self.verbose = Verbose

	#-----------------------------------------------------------------------#
	# Description: Performs selection phase of the MCTS.
	#-----------------------------------------------------------------------#
	
	def Selection(self):
		SelectedChild = self.root
		HasChild = False

		# Check if child nodes exist.
		if(len(SelectedChild.children) > 0):
			HasChild = True
		else:
			HasChild = False

		while(HasChild):
			SelectedChild = self.SelectChild(SelectedChild)
			if(len(SelectedChild.children) == 0):
				HasChild  = False
			#SelectedChild.visits += 1.0

		if(self.verbose):
			print("\nSelected: ", game.GetStateRepresentation(SelectedChild.state))

		return SelectedChild

	#-----------------------------------------------------------------------#
	# Description:
	#	Given a Node, selects the first unvisited child Node, or if all
	# 	children are visited, selects the Node with greatest UTC value.
	# Node	- Node from which to select child Node from.
	#-----------------------------------------------------------------------#
	def SelectChild(self, Node):
		if(len(Node.children) == 0):
			return Node

		for Child in Node.children:
			if(Child.visits > 0.0):
				continue
			else:
				if(self.verbose):
					print("Considered child", game.GetStateRepresentation(Child.state), "UTC: inf",)
				return Child

		MaxWeight = 0.0
		for Child in Node.children:
			#Weight = self.EvalUTC(Child)
			Weight = Child.sputc
			if(self.verbose):
				print("Considered child:", game.GetStateRepresentation(Child.state), "UTC:", Weight)
			if(Weight > MaxWeight):
				MaxWeight = Weight
				SelectedChild = Child
		return SelectedChild

	#-----------------------------------------------------------------------#
	# Description: Performs expansion phase of the MCTS.
	# Leaf	- Leaf Node to expand.
	#-----------------------------------------------------------------------#
	def Expansion(self, Leaf):
		if(self.IsTerminal((Leaf))):
			print("Is Terminal.")
			return False
		elif(Leaf.visits == 0):
			return Leaf
		else:
			# Expand.
			if(len(Leaf.children) == 0):
				Children = self.EvalChildren(Leaf)
				for NewChild in Children:
					if(np.all(NewChild.state == Leaf.state)):
						continue
					Leaf.AppendChild(NewChild)
			assert (len(Leaf.children) > 0), "Error"
			Child = self.SelectChildNode(Leaf)

		if(self.verbose):
			print("Expanded: ", game.GetStateRepresentation(Child.state))
		return Child

	#-----------------------------------------------------------------------#
	# Description: Checks if a Node is terminal (it has no more children).
	# Node	- Node to check.
	#-----------------------------------------------------------------------#
	def IsTerminal(self, Node):
		# Evaluate if node is terminal.
		if(game.IsTerminal(Node.state)):
			return True
		else:
			return False
		#return False # Why is this here?

	def SelectChildNode(self, Node):
		# Randomly selects a child node.
		Len = len(Node.children)
		assert Len > 0, "Incorrect length"
		i = np.random.randint(0, Len)
		return Node.children[i]

	#-----------------------------------------------------------------------#
	# Description:
	#	Performs the simulation phase of the MCTS.
	# Node	- Node from which to perform simulation.
	#-----------------------------------------------------------------------#
	def Simulation(self, Node):
		CurrentState = Node.state
		#if(any(CurrentState) == False):
		#	return None
		if(self.verbose):
			print("Begin Simulation")

		Level = self.GetLevel(Node)
		# Perform simulation.
		while(not(game.IsTerminal(CurrentState))):
			CurrentState = game.GetNextState(CurrentState)
			Level += 1.0
			if(self.verbose):
				print("CurrentState:", game.GetStateRepresentation(CurrentState))
				game.PrintTablesScores(CurrentState)

		Result = game.GetResult(CurrentState)
		return Result

	#-----------------------------------------------------------------------#
	# Description:
	#	Performs the backpropagation phase of the MCTS.
	# Node		- Node from which to perform Backpropagation.
	# Result	- Result of the simulation performed at Node.
	#-----------------------------------------------------------------------#

		# self.root.wins += Result
		# self.root.ressq += Result**2
		# self.root.visits += 1
		# self.EvalUTC(self.root)

	#-----------------------------------------------------------------------#
	# Description:
	#	Checks if Node has a parent..
	# Node - Node to check.
	#-----------------------------------------------------------------------#
	def HasParent(self, Node):
		if(Node.parent == None):
			return False
		else:
			return True

	#-----------------------------------------------------------------------#
	# Description:
	#	Evaluates the Single Player modified UTC. See:
	#	https://dke.maastrichtuniversity.nl/m.winands/documents/CGSameGame.pdf
	# Node - Node to evaluate.
	#-----------------------------------------------------------------------#
	def EvalUTC(self, Node):
		#c = np.sqrt(2)
		c = 0.5
		w = Node.wins
		n = Node.visits
		sumsq = Node.ressq
		if(Node.parent == None):
			t = Node.visits
		else:
			t = Node.parent.visits

		UTC = w/n + c * np.sqrt(np.log(t)/n)
		D = 10000.
		Modification = np.sqrt((sumsq - n * (w/n)**2 + D)/n)
		#print "Original", UTC
		#print "Mod", Modification
		Node.sputc = UTC + Modification
		return Node.sputc

	#-----------------------------------------------------------------------#
	# Description:
	#	Gets the level of the node in the tree.
	# Node - Node to evaluate the level.
	#-----------------------------------------------------------------------#
	def GetLevel(self, Node):
		Level = 0.0
		while(Node.parent):
			Level += 1.0
			Node = Node.parent
		return Level

	#-----------------------------------------------------------------------#
	# Description:
	#	Prints the tree to file.
	#-----------------------------------------------------------------------#
	def PrintTree(self):
		f = open('Tree.txt', 'w')
		Node = self.root
		self.PrintNode(f, Node, "", False)
		f.close()

	#-----------------------------------------------------------------------#
	# Description:
	#	Prints the tree Node and its details to file.
	# Node			- Node to print.
	# Indent		- Indent character.
	# IsTerminal	- True: Node is terminal. False: Otherwise.
	#-----------------------------------------------------------------------#
	def PrintNode(self, file, Node, Indent, IsTerminal):
		file.write(Indent)
		if(IsTerminal):
			file.write("\-")
			Indent += "  "
		else:
			file.write("|-")
			Indent += "| "

		string = str(self.GetLevel(Node)) + ") (["
		# for i in Node.state.bins: # game specific (scrap)
		# 	string += str(i) + ", "
		string += str(game.GetStateRepresentation(Node.state))
		string += "], W: " + str(Node.wins) + ", N: " + str(Node.visits) + ", UTC: " + str(Node.sputc) + ") \n"
		file.write(string)

		for Child in Node.children:
			self.PrintNode(file, Child, Indent, self.IsTerminal(Child))

	def PrintResult(self, Result):
		filename = 'Results.txt'
		if os.path.exists(filename):
			append_write = 'a' # append if already exists
		else:
			append_write = 'w' # make a new file if not

		f = open(filename, append_write)
		f.write(str(Result) + '\n')
		f.close()

	#-----------------------------------------------------------------------#
	# Description:
	#	Runs the SP-MCTS.
	# MaxIter	- Maximum iterations to run the search algorithm.
	#-----------------------------------------------------------------------#
	def Run(self, MaxIter = 5000):
		for i in range(MaxIter):
			if(self.verbose):
				print("\n===== Begin iteration:", i, "=====")
			X = self.Selection()
			Y = self.Expansion(X)
			if(Y):
				Result = self.Simulation(Y)
				if(self.verbose):
					print("Result: "), Result
				self.Backpropagation(Y, Result)
			else:
				Result = game.GetResult(X.state)
				if(self.verbose):
					print("Result: ", Result)
				self.Backpropagation(X, Result)
			self.PrintResultResult()

		print("Search complete.")
		print("Iterations:", i)
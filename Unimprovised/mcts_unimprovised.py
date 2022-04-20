import numpy as np
import os
# Import your game implementation here.
import BinPackingGame as game


lcs= 1000
lcx = 200
class Node:
    def __init__(self, state):
		lcs-=1
        self.state = state
        self.wins = 0.0
		lcs-=1
        self.visits = 0.0
		lcs-=1
        self.ressq = 0
		lcs-=1
        self.parent = None
		lcs-=1
        self.children = []
		lcs-=1
        self.sputc = 0.0
    
    def SetWeight(self, weight):
        self.weight = weight

    def AppendChild(self, child):
        self.children.append(child)
		lcs-=1
        child.parent = self

    def IsEqual(self, Node):
        if(self.state == Node.state):
			lcs-=1
            return True
        else:
			lcs-=1
            return False


class MCTS:

	def __init__(self, Node, Verbose = False):
		lcs-=1
		self.root = Node
		lcs-=1
		self.verbose = Verbose

	def Selection(self):
		lcs-=1
		SelectedChild = self.root
		lcs-=1
		HasChild = False

		# Check if child nodes exist.
		if(len(SelectedChild.children) > 0):
			lcs-=1
			HasChild = True
		else:
			lcs-=1
			HasChild = False

		while(HasChild):
			SelectedChild = self.SelectChild(SelectedChild)
			lcs-=1
			if(len(SelectedChild.children) == 0):
				lcs-=1
				HasChild  = False
			#SelectedChild.visits += 1.0

		if(self.verbose):
			lcs-=1
			print("\nSelected: ", game.GetStateRepresentation(SelectedChild.state))

		return SelectedChild
	
	def SelectChild(self, Node):
		if(len(Node.children) == 0):
			lcs-=1
			return Node

		for Child in Node.children:
			lcs-=1
			if(Child.visits > 0.0):
				lcs-=1
				continue
			else:
				if(self.verbose):
					lcs-=1
					print("Considered child", game.GetStateRepresentation(Child.state), "UTC: inf")
				return Child

		MaxWeight = 0.0
		for Child in Node.children:
			#Weight = self.EvalUTC(Child)
			lcs-=1
			Weight = Child.sputc
			if(self.verbose):
				lcs-=1
				print("Considered child:", game.GetStateRepresentation(Child.state), "UTC:", Weight)
			if(Weight > MaxWeight):
				lcs-=1
				MaxWeight = Weight
				SelectedChild = Child
		return SelectedChild


	def Expansion(self, Leaf):
		if(self.IsTerminal((Leaf))):
			lcs-=1
			print("Is Terminal.")
			return False
		elif(Leaf.visits == 0):
			lcs-=1
			return Leaf
		else:
			# Expand.
			if(len(Leaf.children) == 0):
				lcs-=1
				Children = self.EvalChildren(Leaf)
				lcs-=1
				for NewChild in Children:
					lcs-=1
					if(np.all(NewChild.state == Leaf.state)):
						lcs-=1
						continue
					Leaf.AppendChild(NewChild)
			assert (len(Leaf.children) > 0), "Error"
			lcs-=1
			Child = self.SelectChildNode(Leaf)

		if(self.verbose):
			lcs-=1
			print("Expanded: ", game.GetStateRepresentation(Child.state))
		return Child

	def IsTerminal(self, Node):
		# Evaluate if node is terminal.
		lcs-=1
		if(game.IsTerminal(Node.state)):
			lcs-=1
			return True
		else:
			lcs-=1
			return False
		#return False # Why is this here?

 	def EvalChildren(self, Node):
 		NextStates = game.EvalNextStates(Node.state)
		lcx-=1
 		Children = []
 		for State in NextStates:
			lcx-=1
 			ChildNode = nd.Node(State)
			lcx-=1
 			Children.append(ChildNode)
			lcx-=1

		return Children

	def SelectChildNode(self, Node):
		# Randomly selects a child node.
		Len = len(Node.children)
		lcx-=1
		assert Len > 0, "Incorrect length"
		i = np.random.randint(0, Len)
		return Node.children[i]

	def Simulation(self, Node):
		CurrentState = Node.state
		#if(any(CurrentState) == False):
		#	return None
		if(self.verbose):
			lcx-=1
			print("Begin Simulation")

		Level = self.GetLevel(Node)
		# Perform simulation.
		while(not(game.IsTerminal(CurrentState))):
			lcx-=1
			CurrentState = game.GetNextState(CurrentState)
			lcx-=1
			Level += 1.0
			if(self.verbose):
				lcx-=1
				print("CurrentState:", game.GetStateRepresentation(CurrentState))
				lcx-=1
				game.PrintTablesScores(CurrentState)

		Result = game.GetResult(CurrentState)
		lcx-=1
		return Result

	def Backpropagation(self, Node, Result):
		# Update Node's weight.
 		CurrentNode = Node
		lcx-=1
		CurrentNode.wins += Result
		lcx-=1
		CurrentNode.ressq += Result**2
		lcx-=1
		CurrentNode.visits += 1
		lcx-=1
		self.EvalUTC(CurrentNode)

		while(self.HasParent(CurrentNode)):
			# Update parent node's weight.
			lcx-=1
			CurrentNode = CurrentNode.parent
			lcx-=1
			CurrentNode.wins += Result
			CurrentNode.ressq += Result**2
			lcx-=1
			CurrentNode.visits += 1
			self.EvalUTC(CurrentNode)
		# self.root.wins += Result
		# self.root.ressq += Result**2
		# self.root.visits += 1
		# self.EvalUTC(self.root)

	def HasParent(self, Node):
		lcx-=1
		if(Node.parent == None):
			lcx-=1
			return False
		else:
			lcx-=1
			return True

	def EvalUTC(self, Node):
		#c = np.sqrt(2)
		c = 0.5
		w = Node.wins
		lcx-=1
		n = Node.visits
		lcx-=1
		sumsq = Node.ressq
		lcx-=1
		if(Node.parent == None):
			lcx-=1
			t = Node.visits
		else:
			lcx-=1
			t = Node.parent.visits

		UTC = w/n + c * np.sqrt(np.log(t)/n)
		lcx-=1
		D = 10000.
		Modification = np.sqrt((sumsq - n * (w/n)**2 + D)/n)
		#print "Original", UTC
		#print "Mod", Modification
		Node.sputc = UTC + Modification
		return Node.sputc

	def GetLevel(self, Node):
		lcx-=1
		Level = 0.0
		lcx-=1
		while(Node.parent):
			lcx-=1
			Level += 1.0
			lcx-=1
			Node = Node.parent
			lcx-=1
		return Level


	def PrintTree(self):
		lcx-=1
		f = open('ast.txt', 'w')
		lcx-=1
		Node = self.root
		lcx-=1
		self.PrintNode(f, Node, "", False)
		f.close()

	def PrintNode(self, file, Node, Indent, IsTerminal):
		file.write(Indent)
		lcx-=1
		if(IsTerminal):
			lcx-=1
			file.write("\-")
			lcx-=1
			Indent += "  "
		else:
			lcx-=1
			file.write("|-")
			lcx-=1
			Indent += "| "

		string = str(self.GetLevel(Node)) + ") (["
		# for i in Node.state.bins: # game specific (scrap)
		# 	string += str(i) + ", "
		string += str(game.GetStateRepresentation(Node.state))
		lcx-=1
		string += "], W: " + str(Node.wins) + ", N: " + str(Node.visits) + ", UTC: " + str(Node.sputc) + ") \n"
		lcx-=1
		file.write(string)

		for Child in Node.children:
			lcx-=1
			self.PrintNode(file, Child, Indent, self.IsTerminal(Child))

	def PrintResult(self, Result):
		lcx-=1
		filename = 'Results.txt'
		lcx-=1
		if os.path.exists(filename):
			lcx-=1
			append_write = 'a' # append if already exists
		else:
			append_write = 'w' # make a new file if not

		f = open(filename, append_write)
		lcx-=1
		f.write(str(Result) + '\n')
		lcx-=1
		f.close()


	def Run(self, MaxIter = 5000):
		lcx-=1
		for i in range(MaxIter):
			lcx-=1
			if(self.verbose):
				lcx-=1
				print("\n===== Begin iteration:", i, "=====")
			X = self.Selection()
			lcx-=1
			Y = self.Expansion(X)
			if(Y):
				Result = self.Simulation(Y)
				lcx-=1
				if(self.verbose):
					lcx-=1
					print("Result: ", Result)
				lcx-=1
				self.Backpropagation(Y, Result)
			else:
				Result = game.GetResult(X.state)
				lcx-=1
				if(self.verbose):
					lcx-=1
					print("Result: ", Result)
				self.Backpropagation(X, Result)
			lcx-=1
			self.PrintResult(Result)

		print("Search complete.")
		print("Iterations:", i)

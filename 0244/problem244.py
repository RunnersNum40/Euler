ascii_v = {"L":76, "R":82, "U":85, "D":68}

class Board:
	def __init__(self, seq="", parent=None):
		if parent == None:
			self.state = [["|", "|", "-", "-"] for _ in range(4)]
			self.state[0][0] = "X"
			self.pos = [0, 0]

		else:
			self.state = parent.state
			self.pos = parent.pos

		for move in seq:
			if move in "RL" and {"L":3, "R":0}[move] == self.pos[0] or move in "UD" and {"U":3, "D":0}[move] == self.pos[1]:
				pass
			else:
				if move in "RL":
					self.state[self.pos[1]][self.pos[0]] = self.state[self.pos[1]][self.pos[0]+{"R":-1, "L":1}[move]]
					self.pos[0] += {"R":-1, "L":1}[move]
					self.state[self.pos[1]][self.pos[0]] = "X"

				if move in "UD":
					self.state[self.pos[1]][self.pos[0]] = self.state[self.pos[1]+{"U":1, "D":-1}[move]][self.pos[0]]
					self.pos[1] += {"U":1, "D":-1}[move]
					self.state[self.pos[1]][self.pos[0]] = "X"

	def __eq__(self, other):
		if type(self) != type(other):
			return False
		if len(self.state) != len(other.state) or len(self.state[0]) != len(other.state[0]):
			return False
		for y in range(len(self.state)):
			for x in range(len(self.state[0])):
				if self.state[y][x] != other.state[y][x]:
					return False
		return True

	def __str__(self):
		return "\n".join(" ".join(map(str, row)) for row in self.state)



class Node:
	def __init__(self, move=None, parent=None):
		if move == None:
			self.move = ""
		else:
			self.move = move

		if parent == None:
			self.parent = None
		else:
			self.parent = parent

		self.board = Board(self.seq)

	@property
	def seq(self):
		if self.parent == None:
			return self.move
		else:
			return self.parent.seq+self.move

	def level(self):
		return len(self.seq)

	@staticmethod
	def check_sum(seq, acc=0):
		if len(seq) == 0:
			return acc
		else:
			return Node.check_sum(seq[1:], (acc*243+ascii_v[seq[0]])%100000007)

	def check(self):
		return self.check_sum(self.seq)

	def get_children(self):
		if hasattr(self, "children"):
			return self.children
		else:
			self.children = {}
			for move in "RLUD":
				if move in "RL" and {"L":3, "R":0}[move] == self.board.pos[0] or move in "UD" and {"U":3, "D":0}[move] == self.board.pos[1]:
					pass
				else:
					self.children[move] = Node(move, self)

			return self.children

	def prune(self, names):
		for name in names:
			if name in self.children.keys():
				del self.children[name]

	def __eq__(self, other):
		return self.board == other

	def __repr__(self):
		return "Sequence {}\n".format(self.seq)+str(self.board)

def search_level(nodes, target, level=1, cutoff=10):
	print("Searching level {} with {} nodes".format(level, len(nodes           )))
	# print(nodes[len(nodes)//2], "\n")
	if level >= cutoff:
		return cutoff-1
	new_nodes = []
	for node in nodes:
		result = search(node, target)
		if type(result) == type(1):
			return result
		else:
			new_nodes.extend(result)

	return search_level(new_nodes, target, level+1, cutoff)

def search(node, target):
	children = node.get_children().values()
	total = 0
	for child in children:
		if child == target:
			print(child, "\n")
			total += child.check()

	if total > 0:
		return total
	else:
		return children





# start = "LULUR"
target = Board()
target.state = [["X", "-", "|", "-"], ["-", "|", "-", "|"], ["|", "-", "|", "-"], ["-", "|", "-", "|"]]
seed = Node()

print(target, "\n")
# new = Board("ULUR", target)
# print(new)

if seed == target:
	print(0)
else:
	print(search_level([seed], target, 1, 1000))

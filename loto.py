class Action:
	def __init__(self, description):
		self.description = description

	def __hash__(self):
		return hash(self.description)


class ActionObject:
	def __init__(self, object):
		self.object_destination = object_destination

	def __hash__(self):
		return hash(self.object_destination)

class ActionDestination:
	def __init__(self, action_destination):
		self.action_destination = action_destination

	def __hash__(self):
		return hash(self.action_destination)


class Disorder:
	def __init__(self, object_destination_disorder):
		self.object_destination_disorder = object_destination_disorder

	def __call__(self, goal):
		for cl in self.object_destination_disorder:
			if cl is ActionObject:
				yield 'action_object'

			if cl is ActionDestination:
				yield 'action_destination'

			if cl is Action:
				yield 'action'


class Disorders:
	def __init__(self, disorders):
		#[('action', 'action_object', 'action_destination')]
		self.disorders = disorders


	def __iter__(self, group_cl):
		other = copy(self)
		other.group_cl = group_cl
		return other

	def __next__(self):
		for disorder in disorders:
			yield GroupableGoal(group_cl, disorder)()


class Goal:
	action = None
	action_object = None
	action_destination = None
	def __init__(self, action, action_object, action_destination, register, disorders, participating_in_lottery=True):
		self.action = action
		self.action_object = action_object
		self.action_destination = action_destination
		self.disorders = disorders
		self.participating_in_lottery = participating_in_lottery
		self.register = register		

	def __hash__(self):
		return hash(self.action) ^ \
			hash(self.action_object) ^ \
			hash(self.action_destination) ^ \
			hash(self.participating_in_lottery)

	def __eq__(self, other):
		return self.action == other.action and \
				self.action_object == other.action_object and \
				self.action_destination == other.action_destination and \
				self.participating_in_lottery == other.participating_in_lottery and \

	def disorder(self):

		return self.action_object_destination_disorder(self)


class GroupableGoal:
	def __init__(self, group_cl, disorder):
		self.group_cl = group_cl
		self.disorder = disorders

	def __call__(self):
		



class Node:
	def __init__(self, description, goal, rank):
		self.description = description
		self.goal = goal
		self.rank = rank
		self.participating_in_lottery = goal.participating_in_lottery

	def __hash__(self):
		return hash(self.goal)

class IterateNode:
	def __init__(self, node, balance=0):
		self.node = node
		self.balance = balance
		self.rank = node.rank
		self.participating_in_lottery = node.participating_in_lottery


	def __call__(self, next_iterate_node=None):
		


class IteratePath:
	def __init__(self, iterate_node):
		self.root = iterate_node
		self.path = [iterate_node]
		self.rank = iterate_node.rank 
		self.max_rank = iterate_node.rank
		self.i = 0
		self.n = len(self.path) - 1

	def add(self, iterate_node):
		self.path.append(iterate_node)
		self.max_rank = max(self.max_rank, iterate_node.rank)

	def __call__(self):
		i = self.i
		next_iterate_node = None
		if i < self.n:
			next_iterate_node = self.path[i+1]
		self.path[i](next_iterate_node)
		self.i += 1


class LotteryIterate:
	def __init__(self, iterate_paths):
		self.iterate_paths = iterate_paths

	def __call__(self):
		for iterate_path in self.iterate_paths:
			iterate_node = self.path[self.rank]
			if iterate_node.participating_in_lottery:
				node_goal = iterate_node.goal 
				action_object_destination_disorder


class RankIterate:



class IteratePaths:
	def __init__(self, rank=0):
		self.paths = defaultdict(IterateRankPaths)
		self.rank = rank
		self.max_rank = rank

	def add(self, iterate_path):
		self.paths[iterate_path.rank].add(iterate_path) 
		self.max_rank = max(self.max_rank, iterate_path.rank)

	def __next__(self):
		while rank <= self.max_rank:
			LotteryIterate(self.paths[rank])()
			rank += 1


	def __iter__(self):
		return self


class Nodes:
	def __init__(self):
		self.nodes = []

	def add(self, node):
		self.nodes.append(node)

	def __next__(self):
		if self.nodes:
			for node in self.nodes:
				yield node


class IterateNodes(Nodes):
	pass


class Register:
	def __init__(self):
		

	def iterate(self, iterate_paths):
		for path in iterate_paths:
			pass




class PreInterAction(object):
	"""docstring for InterAction"""
	def __init__(self, goal, path):
		super(PreInterAction, self).__init__()
		self.goal = node
		self.path = path


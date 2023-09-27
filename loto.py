import random
from fractions import Fraction
from itertools import groupby

class RandomService:
	def __init__(self):
		self.seed = None

	def choice(self, elements, probabilities):
		if elements:
			return random.choices(elements, probabililties)[0]

	def random(self):
		return random.random()

	def shuffle(self):
		return self


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


class GroupableGoal:
	def __init__(self, group_cl, disorder):
		self.group_cl = group_cl
		self.disorder = disorders

	def __call__(self):


class Disorders:
	def __init__(self, disorders):
		#[('action', 'action_object', 'action_destination')]
		self.disorders = disorders

	def __next__(self):
		for disorder in disorders:
			yield disorder


class GoalAttribute:
	def __init__(self, goal, attributes):
		self.goal = goal 
		self.attributes = attributes
		

		self.attr_dict = {}
		for attr, value in vars(self.goal).items():
			self.attr_dict[type(value)] = value 

	def __hash__(self):
		hsh = 0
		
		for attribute in self.attributes:
			hsh ^= hash(self.attr_dict[attribute])

		return hsh 

	def __eq__(self, other): 
		eq = True
		
		for attribute in self.attributes:
			eq = eq and self.attr_dict[attribute] == other.attr_dict[attribute]
			if not eq:
				return eq

		return eq 


class AttributesProbability:
	def __init__(self, attributes, probability):
		self.attributes = attributes
		self.probability = probability


class SetAttributesProbability:
	def __init__(self, set_attributes_probability):
		self.set_attributes_probability = []
		self.elements = []
		self.probabilities = []

	def add(self, attributes_probability):
		self.set_attributes_probability.add(attributes_probability)
		self.elements.append(attributes_probability.attributes)
		self.probabilities.append(attributes_probability.probabilities)

	def choice(self):
		return RandomService.choice(self.elements, self.probabilities)


class RankParticipatingLottery:
	def __init__(self, rank_participating_lottery=True):
		self.rank_participating_lottery = rank_participating_lottery

	def __bool__(self):
		return bool(self.rank_participating_lottery)


class GoalSetAttributes:
	def __init__(self, action, action_object, action_destination, register, set_attributes_probability):
		self.action = action
		self.action_object = action_object
		self.action_destination = action_destination
		self.set_attributes_probability = set_attributes_probability
		self.register = register
		
	def choice(self):
		attributes = self.set_attributes_probability.choice()
		#self.goal_attribute = GoalAttribute(self.goal, attributes) 
		return self.goal_attribute


class Goal:
	def __init__(self, action, action_object, action_destination, register):
		self.action = action
		self.action_object = action_object
		self.action_destination = action_destination
		self.register = register		

	def __hash__(self):
		return hash(self.action) ^ \
			hash(self.action_object) ^ \
			hash(self.action_destination) ^ 

	def __eq__(self, other):
		return self.action == other.action and \
				self.action_object == other.action_object and \
				self.action_destination == other.action_destination and \


class Node:
	def __init__(self, description, goal_set_attributes, rank, goal_lottery_probability):
		self.description = description
		self.goal_set_attributes = goal_set_attributes
		self.rank = rank
		self.goal_lottery_probability = goal_lottery_probability
		

	def __hash__(self):
		return hash(self.goal_attribute)

	def choice(self):
		return self.goal_set_attributes.choice()


class IterateNode:
	def __init__(self, node, balance=0):
		self.node = node
		self.balance = balance
		self.rank = node.rank
		self.goal_lottery_probability = node.goal_lottery_probability
		self.goal_attribute = None
		self.seed_nodes = []
		self.decision = None
		self._balance = balance 
		self.loto_balance = 0
		self.total_balance = self.balance + self.loto_balance
		self.participating_in_goal_lottery = None
		self.decided = False


	def choice(self):
		self.goal_attribute = self.node.choice()
		return self.goal_attribute

	def choice_goal_lottery(self):
		self.participating_in_goal_lottery = RandomService.random() <= self.goal_lottery_probability
		return self.participating_in_goal_lottery

	def interact(self, decision):
		self.decision = decision

	@property
	def total_balance(self):
		return self.balance + self.loto_balance
	 

	def __hash__(self):
		return hash(self.goal_attribute)

	def __eq__(self, other):
		return self.goal_attribute == other.goal_attribute

	def __call__(self, next_iterate_node=None):
		if next_iterate_node:
			next_iterate_node.seed_nodes.expand(self.seed_nodes)

			next_iterate_node.balance += self.balance
			self.balance = 0

			next_iterate_node.loto_balance += self.loto_balance
			self.loto_balance = 0

	def transfer_balance_from(self, other):
		self.loto_balance += other.total_balance
		other.balance = 0 
		other.loto_balance = 0
		other.decided = True 
		

class IteratePath:
	def __init__(self, iterate_node):
		self.root = iterate_node
		self.path = [iterate_node]
		self.rank = iterate_node.rank 
		self.max_rank = iterate_node.rank
		self.i = 0
		self.n = len(self.path) - 1
		self.decided = False

	def add(self, iterate_node):
		if iterate_node.rank > iterate_path.max_rank and not self.decided:
			self.path.append(iterate_node)
			self.max_rank = iterate_node.rank
			self.decided = iterate_node.decided or self.decided 

	def __call__(self):
		i = self.i
		iterate_node = self.path[i]
		
		if iterate_node.decided:
			self.decided = True
			return 
		
		next_iterate_node = None
		if i < self.n:
			next_iterate_node = self.path[i+1]
		iterate_node(next_iterate_node)
		
		if not next_iterate_node:
			self.root.balance = self.root._balance
			if self.iterate_node.loto_balance > 0:
				fraction_balance = Fraction(self.iterate_node.balance * self.root.balance, self.iterate_node.loto_balance)
				loto_balance = int(fraction_balance)
				loto_balance += fraction_balance > loto_balance
			self.iterate_node.balance -= self.root.balance
			self.iterate_node.loto_balance -= loto_balance
			self.root.loto_balance  += loto_balance
			self.iterate_node.total_balance

		if i < self.n:
			self.rank = next_iterate_node.rank
		
		iterate_node.decided = True

		self.i += 1


class LotteryIterate:
	def __init__(self, iterate_rank_paths):
		self.iterate_paths = iterate_rank_paths.iterate_paths

	def __call__(self):
		register_decisions_list = []

		for iterate_path in self.iterate_rank_paths:
			iterate_node = self.path[self.rank]
			#if iterate_node.goal_lottery_probability:
			iterate_node.choice()

		return register_decisions_list


class GrouperIterateNode:
	def __init__(self):
		pass

	def __call__(self, iterate_node):
		return hash(iterate_node)


class GoalLotteryIterate:
	def __init__(self, iterate_paths):
		self.iterate_paths = iterate_paths
		self.hash_map = defaultdict(list)

	def run(self):
		for iterate_node in filter(remain_only_goal_lottery_probability,\
			 			map(get_iterate_node, iterate_paths)):
			self.hash_map[iterate_node.goal_attribute].append(iterate_node)

		for goal, iterate_nodes in self.hash_map.items():
			balances = (iterate_node.balance for iterate_node in iterate_nodes)
			iterate_node = RandomService.choices(iterate_nodes, balances)
			for source_iterate_node in iterate_nodes:
				iterate_node.transfer_from(source_iterate_node)


	@static_method
	def get_iterate_node(iterate_path):
		return iterate_path[0]

	@static_method
	def remain_only_goal_lottery_probability(iterate_node):
		choice = iterate_node.choice_goal_lottery()
		return choice


class IterateRankPaths:
	def __init__(self):
		self.iterate_paths = []

	def add(self, iterate_path):
		self.iterate_paths.append(iterate_path)

	def __next__(self):
		for iterate_path in self.iterate_paths:
			yield iterate_path


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

			iterate_path = self.paths[rank]

			register_decisionsLotteryIterate(iterate_path)()

			GoalLotteryIterate(iterate_path)()

			for register_decisions in register_decisions_list:
				register_decisions.decide()

			self.iterate_with_negative_decision(register_decisions)

			rank += 1

	def iterate_with_negative_decision(self):
		registers_dict = defaultdict()
		for iterate_path in self.paths[rank]:
			if not iterate_path.decided:
				iterate_path()
				self.paths[iterate_path.rank].add(iterate_path)


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


class RegisterDecisions:
	def __init__(self, register):
		self.register = register
		self.iterate_nodes = []

	def add(self, iterate_node):
		self.iterate_nodes.append(iterate_node)

	def __hash__(self):
		return hash(self.register)

	def __eq__(self, other):
		return self.register == other.register

	def __call__(self):		
		for iterate_node in self.iterate_nodes:
			iterate_node.interact(RandomService.random() < 0.1)




class InteractionRegisters:
	def __init__(self)
		self.

	def 


class PreInterAction(object):
	def __init__(self, iterate_node):
		super(PreInterAction, self).__init__()
		self.goal = node
		self.path = path


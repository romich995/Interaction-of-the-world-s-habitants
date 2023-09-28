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
	def __init__(self, object_destination):
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


class AttributesProbabilityPartOfBalance:
	def __init__(self, attributes, probability, \
		probabilities_in_rank_lottery, parts_of_balance):
		self.attributes = attributes
		self.probability = probability
		self.probabilities_in_rank_lottery = probabilities_in_rank_lottery
		self.part_of_balance = part_of_balance

class AttributesPartOfBalance:
	def __init__(self, attributes, part_of_balance):
		self.attributes = attributes
		self.part_of_balance = part_of_balance

class AttributesPartsOfBalance:
	def __init__(self, elements, part_of_balance):
		self.elements = elements
		self.parts_of_balance = part_of_balance
		self.normalization()

	def normalization(self):
		self.part_of_balance = [Fraction(part) for part in parts_of_balance]
		sm = sum(self.part_of_balance)
		part_of_balance = [part / sm for part in parts_of_balance]
		#for part in self.parts_of_balance:
		#	new_part = part / sm
		#	new_part_int = int(new_part)
		#	new_part_int += new_part > new_part_int
		#	part_of_balance.append(new_part_int)

		self.part_of_balance = part_of_balance

	def choice(self):
		for attributes, part_of_balance in zip(self.elements, self.parts_of_balance):
			yield AttributesPartOfBalance(attributes, part_of_balance)


class ListAttributesProbability:
	def __init__(self, list_attributes_probability):
		self.list_attributes_probability = list_attributes_probability
		self.elements = []
		self.probabilities = []
		self.probabilities_rank_lottery = []
		self.part_of_balance = []
		for attribute_probability in list_attributes_probability:
			self.elements.append(attributes_probability.attributes)
			self.probabilities.append(attributes_probability.probability)
			self.probabilities_in_rank_lottery.append(attributes_probability.probabililty_in_rank_lottery)
			self.part_of_balance.apped(attributes_probability.part_of_balance)

	def add(self, attributes_probability):
		self.list_attributes_probability.append(attributes_probability)
		self.elements.append(attributes_probability.attributes)
		self.probabilities.append(attributes_probability.probabilities)
		self.probabilities_in_rank_lottery.append(attributes_probability.probabililty_in_rank_lottery)
		self.part_of_balance.apped(attributes_probability.part_of_balance)

	def choice(self):
		attributes_list = []
		parts_of_balance = []

		for attributes, probability, part_of_balance in zip(self.elements, \
												self.probabilities, \
												self.parts_of_balance):
			
			participation = RandomService.random(self.probabilities) < self.probabilities
			if participation:
				attributes_list.append(attributes)
				parts_of_balance.append(parts_of_balance)

		attributes_parts_of_balance = AttributesPartsOfBalance(self, attributes, parts_of_balance)

		for attributes_part_of_balance in attributes_parts_of_balance.choice():
			yield attributes_part_of_balance 


class RankParticipatingLottery:
	def __init__(self, rank_participating_lottery=True):
		self.rank_participating_lottery = rank_participating_lottery

	def __bool__(self):
		return bool(self.rank_participating_lottery)


class GoalListAttributes:
	def __init__(self, action, action_object, action_destination, list_attributes_probability):
		self.action = action
		self.action_object = action_object
		self.action_destination = action_destination
		self.list_attributes_probability = list_attributes_probability
		
	def choice(self): 
		#for attributes_part_of_balance in self.list_attributes_probability.choice():
		yield from self.list_attributes_probability.choice()


class Node:
	def __init__(self, description, goal_list_attributes, rank, goal_lottery_probability, register):
		self.description = description
		self.goal_list_attributes = goal_list_attributes
		self.rank = rank
		self.goal_lottery_probability = goal_lottery_probability
		self.register = register
		

	def __hash__(self):
		return hash(self.goal_attribute)

	def choice(self):
		#for attributes_part_of_balance in self.goal_list_attributes.choice():
		yield from self.goal_list_attributes.choice()


class SeedRegisterPartBalance:
	def __init__(self, seed_node, register, balance, part_of_balance):
		self.seed_node_id = seed_node.id
		self.register = seed_node.register
		self.balance = seed_node.balance
		self.part_of_balance = seed_node.part_of_balance

	def __hash__(self):
		return hash(self.seed_node.id) ^ hash(self.register)  

	def __eq__(self, other):
		return self.seed_node_id == other.seed_node_id and self.register == other.register 

	def __copy__(self):
		my_copy = type(self)(self.seed_node_id, self.register, deepcopy(self.balance), deepcopy(self.part_of_balance))
		return my_copy


class ListSeedRegisterPartBalances:
	def __init__(self):
		self.list_seed_register_part_balances = []
		self.dict_seed_register_part_balances = defaultdict(list)

	def add(self, seed_register_part_balances):
		self.list_seed_register_part_balances.append(seed_register_part_balances)
		self.dict_seed_register_part_balances[seed_register_part_balances].append(seed_register_part_balances)

	def expand(self, other):
		self.list_seed_register_part_balances.expand(other.list_seed_register_part_balances)
		for seed_register_part_balances in other.list_seed_register_part_balances:
			self.dict_seed_register_part_balances[seed_register_part_balances].append(seed_register_part_balances)

	def group(self):
		for seed_register_part_balances in self.list_seed_register_part_balances:
			self.register.balance += self.balance
			self.balance = 0

	def __contains__(self, seed_register_part_balances):
		return seed_register_part_balances in self.dict_seed_register_part_balances:

	def __copy__(self):
        my_copy = type(self)()
        for seed_register_part_balances in self.list_seed_register_part_balances:
        	new_seed_register_part_balances = copy(seed_register_part_balances)
        	my_copy.add(new_seed_register_part_balances)

        return my_copy

    def update_balances(self, factor):
    	for seed_register_part_balances in self.list_seed_register_part_balances:
    		seed_register_part_balances.balances *= factor
    		#seed_register_part_balances.part_of_balance *= factor

    @property
    def total_balance(self):
    	total_balance = Fraction(0)
    	for seed_register_part_balances in self.list_seed_register_part_balances:
    		total_balance += seed_register_part_balances.balance
    	return total_balance

    def annul(self):
		for seed_register_part_balances in self.list_seed_register_part_balances:
    		seed_register_part_balances.balance = Fraction(0)

    def multiply(self, factor):
    	for seed_register_part_balances in self.list_seed_register_part_balances:
    		seed_register_part_balances.balance *= factor 



class IterateNode:
	def __init__(self, node, balance=0):
		self.id = id(self)
		self.node = node
		self.balance = balance
		self.rank = node.rank
		self.goal_lottery_probability = node.goal_lottery_probability
		self.goal_attribute = None
		self.register = node.register
		self.seed_register_part_balances = ListSeedRegisterPartBalances(
												SeedRegisterPartBalance(
													register,
												 	balance,
												 	part_of_balance
													)
												) 
		self.decision = None
		#self._balance = balance 
		self.loto_balance = 0
		self.participating_in_goal_lottery = None
		self.decided = False
		self.part_of_balance = Factor(1)
		self.paths = []

	def __copy__(self):
		my_copy = type(self)(self.node, self.balance)
		my_copy.__dict__.update(self.__dict__)
		my_copy.seed_register_part_balances = copy(my_copy.seed_register_part_balances)
		my_copy.paths = list(my_copy.paths)
		my_copy.balance = copy(balance)

		return my_copy

	def choice(self):
		for attributes_part_of_balance in self.node.choice():
			other = copy(self)
			other.goal_attribute = attributes_part_of_balance.attributes
			other.part_of_balance *= attributes_part_of_balance.part_of_balance
			other.balance *= other.part_of_balance
			other.loto_balance *= other.part_of_balance
			other.seed_register_part_balances.multiply(other.part_of_balance)

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

	def seed_expand(self, other):
		self.seed_register_part_balances.expand(other.seed_register_part_balances) 

	def __call__(self):
		if self.path.i < self.path.n:

			next_iterate_node = self.paths[self.path.i + 1]
			next_iterate_node.seed_register_part_balances.expand(self.seed_register_part_balances)
			
			next_iterate_node.balance += self.balance
			self.balance = 0

			next_iterate_node.loto_balance += self.loto_balance
			self.loto_balance = 0

			next_iterate_node.seed_expand(self)

	def transfer_balance_from(self, other):
		self.loto_balance += other.total_balance
		other.balance = 0 
		other.loto_balance = 0
		#self.seed_expand(other)
		other.decided = True 
		

class IteratePath:
	def __init__(self, collector_seed_register_part_balances):
		self.root = None
		self.path = None
		self.rank = None
		self.max_rank = None 
		self.n = None
		self.i = None
		self.decided = False
		self.seed_register_part_balances = None
		self.collector_seed_register_part_balances = collector_seed_register_part_balances

	def create_root(self, iterate_node):
		self.root = iterate_node
		self.path.append(iterate_node)
		self.rank = iterate_node.rank
		self.max_rank = iterate_node.rank
		self.n = 0
		self.i = 0
		self.root.paths.append(self)
		self.decided = iterate_node.decided or self.decided 
		self.seed_register_part_balance = SeedRegisterPartBalance(self.root)

	def add(self, iterate_node):
		if iterate_node.rank > iterate_path.max_rank and not self.decided:
			self.path.append(iterate_node)
			self.max_rank = iterate_node.rank
			self.decided = iterate_node.decided or self.decided 
			self.n += 1
			iterate_node.paths.append(self) 

	def increase_rank_or_back_balance(self, ):
		if self.i < n:
			self.i += 1
			self.rank = self.path[i].rank
		else:
			last_node = self.path[self.n]
			seed_register_part_balance = last_node.seed_register_part_balances[self.seed_register_part_balance] 
			collector_seed_register_part_balances.add(seed_register_part_balance)

	def __call__(self):

		#negative
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


class GrouperIterateNode:
	def __init__(self):
		pass

	def __call__(self, iterate_node):
		return hash(iterate_node)


class GoalLotteryIterate:
	def __init__(self, iterate_rank_paths):
		self.iterate_paths = iterate_rank_paths
		self.hash_map = defaultdict(list)
		self.not_decided_nodes_after_loto = []

	def run(self):
		for iterate_path in iterate_rank_paths:
			for lottery_iterate_node in iterate_path[iterate_path.i]:
				for iterate_node in lottery_iterate_node.choice():
					participation_in_goal_lottery = iterate_node.choice_goal_lottery()
					if not participation_in_goal_lottery:
						iterate_node()
					else:
						self.hash_map[iterate_node.goal_attribute].append(iterate_node)

		for goal, iterate_nodes in self.hash_map.items():
			balances = (iterate_node.balance for iterate_node in iterate_nodes)
			iterate_node = RandomService.choices(iterate_nodes, balances)
			for source_iterate_node in iterate_nodes:
				iterate_node.transfer_from(source_iterate_node)

		self.not_decided_nodes_after_loto.append(iterate_node)

		#wait_decision

		for iterate_node in self.not_decided_nodes_after_loto:
			iterate_node()


class IterateRankPaths:
	def __init__(self):
		self.iterate_paths = []

	def add(self, iterate_path):
		self.iterate_paths.append(iterate_path)

	def rank_paths_increase(self):
		for iterate_path in self.iterate_paths:
			iterate_path.increase_rank()

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

			iterate_rank_paths = self.paths[rank]

			GoalLotteryIterate(iterate_rank_paths)()

			self.iterate_rank_paths_increase()
			#self.iterate_with_negative_decision(register_decisions)

			rank += 1

	def iterate_rank_path_increase(self):
		iterate_rank_paths = self.path[self.rank]
		iterate_rank_paths.rank_paths_increase(self)

		

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
	def __init__(self, description, balance):
		self.description = self.description
		self.balance = balance

	def __hash__(self):
		return hash(self.description)

	def __eq__(self, other):
		return self.description == other.description

	def __copy__(self):
		my_copy = type(self)()
		my_copy.balance = copy(self.balance)
		return my_copy

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
			decided = RandomService.random() < 0.1
			iterate_node.interact(decided)
			iterate_node.decided = decided



class InteractionRegisters:
	def __init__(self)
		self.

	def 


class PreInterAction(object):
	def __init__(self, iterate_node):
		super(PreInterAction, self).__init__()
		self.goal = node
		self.path = path


if __name__ == '__main__':

	
import random
from fractions import Fraction
from itertools import groupby
from collections import defaultdict
from copy import copy, deepcopy

class PartOfBalance(Fraction):
    pass

class Balance:
    def __init__(self, balance: int):
        if isinstance(balance, int):
            self.balance = balance
            return

        if isinstance(balance, type(self)):
            self.balance = int(balance.balance)
            return

        raise NotImplemented()

    def transfer_balance_to_by_part_of_balance_to(self, other, part_of_balance):
        transfer_balance = self * part_of_balance
        self.transfer_balance_by_transfer_balance_to(other, transfer_balance)
        return transfer_balance

    def transfer_balance_by_transfer_balance_to(self, other, transfer_balance):
        if transfer_balance is not self and transfer_balance is not other: 
            print(self, other)
            self -= transfer_balance
            other += transfer_balance
            return        

        raise NotImplemented()

    def annul(self):
        self.balance = 0

    def __le__(self, other):
        if isinstance(other, int):
            return self.balance <= other
        if isinstance(other, type(self)):
            return self.balance <= other.balance
        raise NotImplemented()
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __ge__(self, other):
        if isinstance(other, int):
            return self.balance >= other
        if isinstance(other, type(self)):
            return self.balance >= other.balance
        raise NotImplemented()
    
    def __gt__(self, other):
        if isinstance(other, int):
            return self.balance > other
        if isinstance(other, type(self)):
            return self.balance > other.balance
        raise NotImplemented()

    def __lt__(self, other):
        if isinstance(other, int):
            return self.balance < other
        if isinstance(other, type(self)):
            return self.balance < other.balance
        raise NotImplemented()

    def __ne__(self, other):
        return self.balance != other.balance


    def __copy__(self):
        my_copy = type(self)(self.balance)
        return my_copy

    def __add__(self, other):
        new_balance = type(self)(self.balance)
        if isinstance(other, type(self)):
            new_balance.balance += other.balance
            return new_balance
        elif isinstance(other, int):
            new_balance.balance += other
            return new_balance

        raise NotImplemented()

    def __radd__(self, other):
        return self.__add___(other)

    def __iadd__(self, other):
        if isinstance(other, type(self)):
            self.balance += other.balance
            return self

        raise NotImplemented()

    def __mul__(self, other):
        new_balance = type(self)(self.balance)
        if isinstance(other, type(self)):
            new_balance.balance *= other.balance
            return new_balance
        elif isinstance(other, int):
            new_balance.balance *= other
            return new_balance
        elif isinstance(other, Fraction):
            fraction_transfer_balance = self.balance * other 
            new_balance.balance = int(fraction_transfer_balance)
            print(fraction_transfer_balance, new_balance.balance)
            new_balance.balance += fraction_transfer_balance > new_balance.balance
            return new_balance

        raise NotImplemented()

    def __imul__(self, other):
        if isinstance(other, type(self)):
            self.balance *= other.balance
            return self
        elif isinstance(other, int):
            self.balance *= other
            return self
        elif isinstance(other, Fraction):
            new_balance = self.balance * other
            int_new_balance = int(new_balance)
            if int_new_balance == new_balance:
                self.balance = int_new_balance
                return self

        raise NotImplemented()

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        new_balance = type(self)(self.balance)
        if isinstance(other, type(self)):
            new_balance.balance -= other.balance
            return new_balance
        elif isinstance(other, int):
            new_balance.balance -= other
            return new_balance

        raise NotImplemented()

    def __isub__(self, other):

        if isinstance(other, type(self)):
            self.balance -= other.balance
            return self

        raise NotImplemented()

    def __rsub__(self, other):
        return self.__sub__(other)

    def  __str__(self):
        return str(self.balance)

    def  __repr__(self):
        return str(self.balance)


class FractionBalance(Balance):
    def __init__(self, balance):
        if isinstance(balance, int):
            self.balance = Fraction(balance, 1)
            return

        if isinstance(balance, Fraction):
            self.balance = balance
            return

        if isinstance(balance, Balance):
            self.balance = Fraction(balance.balance, 1)
            return

        if isinstance(balance, type(self)):
            self.balance = Fraction(balance)
            return
        print(balance, type(balance))
        raise NotImplemented()

    def __mul__(self, other):
        new_balance = type(self)(self.balance)
        if isinstance(other, type(self)):
            new_balance.balance *= other.balance
            return new_balance
        
        if isinstance(other, int):
            new_balance.balance *= other
            return new_balance
        
        if isinstance(other, PartOfBalance):
            new_balance.balance *= other
            return new_balance

        raise NotImplemented()

    def __truediv__(self, other):
        return Fraction(self.balance,1) / Fraction(other.balance, 1)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __isub__(self, other):

        if isinstance(other, type(self)):
            self.balance -= other.balance
            return self

        if isinstance(other, Balance):
            self.balance -= other.balance
            return self

        raise NotImplemented()


    def __imul__(self, other):
        print(self, other, type(other))
        if isinstance(other, type(self)):
            self.balance *= other.balance
            return self
                    
        if isinstance(other, int):
            self.balance *= other
            return self
        
        if isinstance(other, PartOfBalance):
            self.balance *= other
            return self

        if isinstance(other, Fraction):
            self.balance *= other
            return self

        raise NotImplemented()



    def transfer_balance_to_by_part_of_balance_to(self, other, part_of_balance):
        transfer_balance = self * part_of_balance
        if not isinstance(transfer_balance, type(self)):
            transfer_balance = type(other)(transfer_balance)
        self.transfer_balance_by_transfer_balance_to(other, transfer_balance)
        return transfer_balance


class RandomService:
    def __init__(self):
        self.seed = None

    @staticmethod
    def choice(elements, probabilities):
        print(probabilities)
        sm = sum(probabilities)
        if elements:
            old_proba = 0
            for index, proba in enumerate(probabilities):
                adjusted_proba = proba / (sm * (1 - old_proba))
                vl = random.random()
                if vl < adjusted_proba:
                    return elements[index]
                old_proba = adjusted_proba

    @staticmethod
    def random():
        return random.random()

    @staticmethod
    def shuffle(self):
        return self


class Action:
    def __init__(self, description):
        self.description = description

    def __hash__(self):
        return hash(self.description)

    def __str__(self):
        return str(self.description)


class ActionObject:
    def __init__(self, object_destination):
        self.object_destination = object_destination

    def __hash__(self):
        return hash(self.object_destination)

    def __str__(self):
        return str(self.object_destination)


class ActionDestination:
    def __init__(self, action_destination):
        self.action_destination = action_destination

    def __hash__(self):
        return hash(self.action_destination)

    def __str__(self):
        return str(self.action_destination)


#class GroupableGoal:
#   def __init__(self, group_cl, disorder):
#       self.group_cl = group_cl
#       self.disorder = disorders
#
#   def __call__(self):


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

    def __str__(self):
        st = ''
        for attribute in self.attributes:
           st += f'{str(attribute)}: {str(self.attr_dict[attribute])},\n'
        return st

    def __repr__(self):
        return str(self)

    def __hash__(self):
        hsh = 0
        print(self.goal, self.attributes)
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
    def __init__(self, attributes, probability, part_of_balance):
        print(part_of_balance)
        self.attributes = attributes
        self.probability = probability
        #self.probabilities_in_rank_lottery = probabilities_in_rank_lottery
        self.part_of_balance = part_of_balance

class AttributesPartOfBalance:
    def __init__(self, attributes, part_of_balance):
        self.attributes = attributes
        self.part_of_balance = part_of_balance

class AttributesPartsOfBalance:
    def __init__(self, elements, part_of_balance):
        self.elements = elements
        self.part_of_balance = part_of_balance
        print(self.part_of_balance)
        self.normalization()

    def normalization(self):
        print(type(self.part_of_balance[0]))
        self.part_of_balance = [Fraction(part) for part in self.part_of_balance]
        sm = sum(self.part_of_balance)
        self.part_of_balance = [part / sm for part in self.part_of_balance]
        #for part in self.parts_of_balance:
        #   new_part = part / sm
        #   new_part_int = int(new_part)
        #   new_part_int += new_part > new_part_int
        #   part_of_balance.append(new_part_int)

        #self.part_of_balance = part_of_balance

    def choice(self):
        for attributes, part_of_balance in zip(self.elements, self.part_of_balance):
            yield AttributesPartOfBalance(attributes, part_of_balance)


class ListAttributesProbability:
    def __init__(self, list_attributes_probability):
        self.list_attributes_probability = list_attributes_probability
        self.elements = []
        self.probabilities = []
        #self.probabilities_rank_lottery = []
        self.part_of_balance = []
        for attributes_probability in list_attributes_probability:
            self.elements.append(attributes_probability.attributes)
            self.probabilities.append(attributes_probability.probability)
            #self.probabilities_in_rank_lottery.append(attributes_probability.probabililty_in_rank_lottery)
            self.part_of_balance.append(attributes_probability.part_of_balance)

    def add(self, attributes_probability):
        self.list_attributes_probability.append(attributes_probability)
        self.elements.append(attributes_probability.attributes)
        self.probabilities.append(attributes_probability.probabilities)
        #self.probabilities_in_rank_lottery.append(attributes_probability.probabililty_in_rank_lottery)
        self.part_of_balance.apped(attributes_probability.part_of_balance)

    def choice(self):
        attributes_list = []
        parts_of_balance = []

        for attributes, probability, part_of_balance in zip(self.elements, \
                                                self.probabilities, \
                                                self.part_of_balance):
            
            participation = RandomService.random() < probability
            if participation:
                attributes_list.append(attributes)
                parts_of_balance.append(part_of_balance)
        print(f"\n\n\n\n\n ATRRRIBUTESSSSSSSSSSS {attributes_list}   {parts_of_balance}\n\n\n\n")
        attributes_parts_of_balance = AttributesPartsOfBalance(attributes_list, parts_of_balance)

        for attributes_part_of_balance in attributes_parts_of_balance.choice():
            yield attributes_part_of_balance 


class RankParticipatingLottery:
    def __init__(self, rank_participating_lottery=True):
        self.rank_participating_lottery = rank_participating_lottery

    def __bool__(self):
        return bool(self.rank_participating_lottery)

class Goal:
    def __init__(self, action, action_object, action_destination):
        self.action = action
        self.action_object = action_object
        self.action_destiantion = action_destination

class GoalListAttributes:
    def __init__(self, action, action_object, action_destination, list_attributes_probability):
        self.action = action
        self.action_object = action_object
        self.action_destination = action_destination
        self.list_attributes_probability = list_attributes_probability
        print(f'GOALLLISTATTRIBUTES initializatioin: {self.action} {self.action_object} {self.action_destination}')
        
    def choice(self): 
        #for attributes_part_of_balance in self.list_attributes_probability.choice():
        print(f'GOAL LIST ATTRIBUTES \n\n\n {self.action} {self.action_object} {self.action_destination}')
        for attributes_part_of_balance in self.list_attributes_probability.choice():
            yield GoalAttribute(
                    Goal(self.action, 
                        self.action_object,
                        self.action_destination),
                        attributes_part_of_balance.attributes
                    ), \
                    attributes_part_of_balance.part_of_balance



class Node:
    def __init__(self, description, goal_list_attributes, rank, goal_lottery_probability):
        self.description = description
        self.goal_list_attributes = goal_list_attributes
        self.rank = rank
        self.goal_lottery_probability = goal_lottery_probability        

    def __hash__(self):
        return hash(self.goal_attribute)

    def choice(self):
        #for attributes_part_of_balance in self.goal_list_attributes.choice():
        yield from self.goal_list_attributes.choice()


class Register:
    def __init__(self, description, balance):
        self.description = description
        self.balance = balance

    def __hash__(self):
        return hash(self.description)

    def __eq__(self, other):
        return self.description == other.description

    def transfer_balance_to_collector_register(self, collector_register, balance):
        self.balance.transfer_balance_by_transfer_balance_to(collector_register, balance)

    def __iadd__(self, other):
        self.balance += other.balance
        return self


    def __copy__(self):
        my_copy = type(self)(self.description, copy(self.balance))
        return my_copy

    def allocate_funds(self, balance):
        seed_register = type(self)(self.description, FractionBalance(balance))
        if balance <= self.balance:
            self.balance -= seed_register.balance
            return seed_register
        raise NotImplemented()

    def __str__(self):
        return f'Id: {id(self)},\n Description: {str(self.description)},\n Balance: {str(self.balance)}'

    def __repr__(self):
        return str(self)


class SeedRegister(Register):
    def __init__(self, register, iterate_path):
        self.register = register
        self.iterate_path = iterate_path
        self.balance = Balance(register.balance)
        self.description = register.description
        #self.part_of_balance = seed_node.part_of_balance

    def __hash__(self):
        return hash(self.iterate_path)  

    def __eq__(self, other):
        return self.iterate_path == other.iterate_path

    def __copy__(self):
        my_copy = type(self)(self.register, self.node_id)
        return my_copy

    def __str__(self):
        return \
            f'SeedRegister:'\
            f'  Id: {id(self)}'\
            f'  Register: {str(self.register)}\n'\
            f'  Node_Id: {self.node_id}\n'\
            f'  Balance: {self.balance}\n'\
            f'  Description: {self.description}\n\n'


    #def __copy__(self):
    #    my_copy = type(self)(self.seed_node_id, self.register, copy(self.balance))
    #    return my_copy




class ListSeedRegisterPartBalances:
    def __init__(self, seed_register_part_balances=None):
        #self.list_seed_register_part_balances = []
        self.dict_seed_register_part_balances = defaultdict(dict)

        if seed_register_part_balances is not None:
            self.add(seed_register_part_balances)

    def __str__(self):
        return str(self.dict_seed_register_part_balances)

    def add(self, seed_register_part_balances):
        #self.list_seed_register_part_balances.append(seed_register_part_balances)
        if seed_register_part_balances in self.dict_seed_register_part_balances: 
            self.dict_seed_register_part_balances\
                [seed_register_part_balances]\
                    [seed_register_part_balances.register] = seed_register_part_balances
        else:
            self.dict_seed_register_part_balances\
                [seed_register_part_balances]\
                    [seed_register_part_balances.register] = seed_register_part_balances
    
    def get(self, seed_register_part_balances):
        return self.dict_seed_register_part_balances\
                    [seed_register_part_balances]

    def delete(self, seed_register):
        print('DELETEEEEE' ,id(seed_register), seed_register.description, seed_register.balance.balance)
        print(self.dict_seed_register_part_balances)
        del self.dict_seed_register_part_balances[seed_register][seed_register.register]

    def expand(self, other):
        #self.list_seed_register_part_balances.expand(other.list_seed_register_part_balances)
        print(self.dict_seed_register_part_balances)
        print('\n\n\n')
        print(other.dict_seed_register_part_balances)
        for registers_dict in other.dict_seed_register_part_balances.values():
            for register in registers_dict.values():
                self.add(register)

        print(self.dict_seed_register_part_balances)
        

    #def group(self):
    #   for list_seed_register_part_balances in self.dict_seed_register_part_balances:
    #       for seed_register_part_balances in list_seed_register_part_balances:
    #           seed_register_part_balances.balance.transfer_balance_by_transfer_balance_to(self.register.balance)

    def __contains__(self, seed_register_part_balances):
        return seed_register_part_balances in self.dict_seed_register_part_balances \
            and seed_register_part_balances.register in self.dict_seed_register_part_balances[seed_register_part_balances]

    def __copy__(self):
        my_copy = type(self)()
        for seed_register_part_balances in self.dict_seed_register_part_balances.values():
            for seed_register in seed_register_part_balances.values():
                new_seed_register_part_balances = copy(seed_register)
                my_copy.add(new_seed_register_part_balances)

        return my_copy

    #def update_balances(self, factor):
    #    for seed_register_part_balances in list_seed_register_part_balances:
    #       seed_register_part_balances.balances *= factor
    #        #seed_register_part_balances.part_of_balance *= factor

    @property
    def total_balance(self):
        total_balance = FractionBalance(0)
        for dict_seed_register_part_balances in self.dict_seed_register_part_balances.values():
            for seed_register_part_balances in dict_seed_register_part_balances.values():
                total_balance += seed_register_part_balances.balance
        return total_balance

    def annul(self):
        for dict_seed_register_part_balances in self.dict_seed_register_part_balances.values():
            for seed_register_part_balances in dict_seed_register_part_balances.values():
                seed_register_part_balances.balance.annul(0)

    def multiply(self, factor):
        for dict_seed_register_part_balances in self.dict_seed_register_part_balances.values():
            for seed_register_part_balance in dict_seed_register_part_balances.values():
                seed_register_part_balances.balance *= factor


class CollectorRegiters():
    def __init__(self, seed_register_part_balances=None):
        self.list_collector_registers = []
        self.balance_for_total_loto = FractionBalance(0)

    def add(self, collector_register):
        self.list_collector_registers.append(collector_register)

    def total_rank_loto(self):
        elements = []
        probilities = [] 
        for seed_register_part_balance in dict_seed_register_part_balances.items():
            elements.append(seed_register_part_balance)
            probilities.append(seed_register_part_balance.balance.balance)

        register = RandomService.choice(elements, probabilities)
        int_balance_for_total_loto = Balance(self.balance_for_total_loto) 
        register.balance += int_balance_for_total_loto
        self.balance_for_total_loto -= int_balance_for_total_loto



class IterateNode:
    def __init__(self, node, collector_seed_register_part_balances, seed_register):
        self.node_id = id(self)
        self.node = node
        self.balance = Balance(seed_register.register.balance)
        self._balance = Balance(seed_register.register.balance)
        self.rank = node.rank
        self.goal_lottery_probability = node.goal_lottery_probability
        self.goal_attribute = None
        self.register = seed_register.register
        self.seed_register_part_balances = ListSeedRegisterPartBalances()
        self.seed_register_part_balances.add(seed_register)
        self.decision = None
        self.participating_in_goal_lottery = None
        self.decided = False
        self.collector_seed_register_part_balances = collector_seed_register_part_balances

        self.append_path()

    def append_path(self, iterate_path):
        self.seed_register_part_balances.append()

    def __str__(self):
        return f'id: {self.node_id}\n'\
        f'balance: {str(self.balance)}\n'\
        f'description: {str(self.node.description)}\n'\
        f'rank: {self.rank}\n'\
        f'seed_register_part_balances: {str(self.seed_register_part_balances)}\n'\
        f'goal attribute: {str(self.goal_attribute)}\n'\
        f'participating_in_goal_lottery: {self.participating_in_goal_lottery}\n'\
        f'decided: {self.decided}'

    def __repr__(self):
        return str(self)

    def __copy__(self):
        my_copy = type(self)(self.node, self.collector_seed_register_part_balances)
        my_copy.__dict__.update(self.__dict__)
        my_copy.seed_register_part_balances = copy(my_copy.seed_register_part_balances)
        my_copy.paths = list(my_copy.paths)
        my_copy.balance = copy(self.balance)

        return my_copy

    def choice(self):
        for goal_attribute, part_of_balance in self.node.choice():
            if self._balance > 0:
                other = copy(self)
                print('\n\n\n\n\n  GOAL ATTRIBUTE-------------', goal_attribute)
                other.goal_attribute = goal_attribute
                new_balance = other.balance * part_of_balance
                new_part_of_balance = Fraction(new_balance.balance, 1) \
                    / Fraction(other.balance.balance, 1)
                print(new_balance, new_part_of_balance)
                self._balance -= new_balance
                other.balance = new_balance
                other._balance = Balance(new_balance.balance)
                other.seed_register_part_balances.multiply(new_part_of_balance)
                yield other
            else:
                return
                #other.balance = Balance(0)
                #other.decided = True
                #other.seed_register_part_balances.multiply(part_of_balance)

    def choice_goal_lottery(self):
        self.participating_in_goal_lottery = RandomService.random() <= self.goal_lottery_probability
        if self.participating_in_goal_lottery:
            yield from self.choice()
        else:
            yield self

    def interact(self, decision):
        self.decision = decision

    @property
    def total_balance(self):
        return self.balance
     
    def __hash__(self):
        return hash(self.goal_attribute)

    def __eq__(self, other):
        return self.goal_attribute == other.goal_attribute

    def seed_expand(self, other):
        print(f"before seed_expand {str(self.seed_register_part_balances)}")
        self.seed_register_part_balances.expand(other.seed_register_part_balances)
        print(f"after seed_expand {str(self.seed_register_part_balances)}") 

    def __call__(self, next_iterate_node=None):
        print("\n\n\n\n move balance to the next node")
        print(f"\n\n {str(next_iterate_node)} \n\n")
        if not self.decided and next_iterate_node is not None:
            self.transfer_balance_to_next_iterate_node(next_iterate_node)
            self.decide(True)
            print(self)

    def transfer_balance_to_next_iterate_node(self, next_iterate_node):
        next_iterate_node.seed_expand(self)
        print(f"\n\n\n balance before transfer {str(self.balance)}")
        self.balance.transfer_balance_by_transfer_balance_to(next_iterate_node.balance, FractionBalance(self.balance))
        print(f"\n\n\n balance after transfer {str(self.balance)}")
        print(f"\n\n\n {next_iterate_node} ")
        #self.loto_balance.transfer_balance_by_transfer_balance_to(next_iterate_node.loto_balance, self.loto_balance)
        
    def transfer_balances_to_local_iterate_node(self, local_iterate_node):
        print(f'\n\n\n\nfrom: {str(self)}, to: {str(local_iterate_node)}')
        loto_balance = local_iterate_node.balance
        factor_rate = (Fraction(loto_balance.balance,1) + Fraction(self.balance.balance)) \
        / Fraction(local_iterate_node.balance.balance, 1)
        local_iterate_node.seed_register_part_balances.multiply(factor_rate)
        self.balance.transfer_balance_by_transfer_balance_to(local_iterate_node.balance, FractionBalance(self.balance))
        self.decide(True)

    #def return_balance_to_seed_registers(self, seed_regi):
    #    for seed_register in self.collector_seed_register_part_balances.keys():
    #        collector_register = collector_seed_register_part_balances.get(seed_register)


    def decide(self, decided):
        print(f'\n\n\n\n\nDECIDED: {str(self)}')
        self.decided = decided
        #if self.balance.greater_zero():
        #    remain_part = self.balance - Balance(self.balance)
        #    if remain_part:
        #        pass
                #total_loto_rank += 

    def return_balance_to_seed_register(self, iterate_path):
        for seed_register in iterate_path.seed_register_part_balances:

            collector_register = self.collector_seed_register_part_balances.get(seed_register)
            add_remain = seed_register.balance.balance > int(seed_register.balance.balance)
            transfer_balance = Balance(int(seed_register.balance.balance) + add_remain)
            self.seed_register_part_balances.delete(seed_register)
            
            if add_remain:
                decrease_factor = (self.balance - transfer_balance) / (self.balance - register.balance) 
                self.seed_register_part_balances.multiply(decrease_factor)
            
            self.balance.transfer_balance_by_transfer_balance_to(collector_register.balance, transfer_balance)
            
        if self.balance.balance == 0:
            self.decide(True)


class IteratePath:
    def __init__(self, collector_seed_register_part_balances):
        self.root = None
        self.path = []
        self.rank = None
        self.max_rank = None 
        self.n = None
        self.i = None
        self.decided = False
        self.seed_register_part_balances = []
        self.collector_seed_register_part_balances = collector_seed_register_part_balances

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return id(self) == id(other)

    def create_root(self,  node, collector_seed_register_part_balances, register):
        seed_register = SeedRegister(register, self)
        self.seed_register_part_balances.append(seed_register)
        iterate_node = IterateNode(node, collector_seed_register_part_balances, seed_register)
        self.root = iterate_node
        self.path.append(iterate_node)
        self.rank = iterate_node.rank
        self.max_rank = iterate_node.rank
        self.n = 0
        self.i = 0
        self.root.append_path(self)
        self.decided = iterate_node.decided or self.decided 
        #self.seed_register_part_balance = self.root.register

    def create_next_iterate_node(self, node, collector_seed_register_part_balances, register):
        if node.rank > self.max_rank and not self.decided:        
            seed_register = SeedRegister(register, self)
            self.seed_register_part_balances.append(seed_register)
            iterate_node = IterateNode(node, collector_seed_register_part_balances, seed_register)
            self.path.append(iterate_node)
            self.max_rank = iterate_node.rank
            self.decided = iterate_node.decided or self.decided 
            self.n += 1
            iterate_node.append_path(self)
            return

        raise NotImplemented()
    #def update_rank_from_current_node(self):
    #    self.rank = self.path[self.i].rank

    def add(self, iterate_node):
        if iterate_node.rank > self.max_rank and not self.decided:
            self.path.append(iterate_node)
            self.max_rank = iterate_node.rank
            self.decided = iterate_node.decided or self.decided 
            self.n += 1
            iterate_node.append_path(self)
            return

        raise NotImplemented()

    def get_next_iterate_node(self):
        if self.i < self.n: 
            return self.path[self.i + 1]

    def __getitem__(self, i):
        if i <= self.n: 
            yield from self.path[i].choice_goal_lottery()


    def increase_rank_or_back_balance(self):
        print(self.i, self.n, self.decided, self.path[self.i].decided)
        if self.i < self.n and not self.path[self.i].decided:
            self.i += 1
            self.rank = self.path[self.i].rank
        else:
            iterate_node = self.path[self.i]
            iterate_node.return_balance_to_seed_register(self)
            self.decided = True    

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

    def __call__(self):
        print(f'start looop: {len(self.iterate_paths.iterate_paths)}\n\n\n\n\n\n')
        for iterate_path in self.iterate_paths:
            next_iterate_node = iterate_path.get_next_iterate_node()
            for iterate_node in iterate_path[iterate_path.i]:
                print(f'\n\n\n\n LOOP: {str(iterate_node)}')
                iterate_node.next_iterate_node = next_iterate_node
                #participation_in_goal_lottery = iterate_node.choice_goal_lottery()
                if not iterate_node.participating_in_goal_lottery:
                    iterate_node(next_iterate_node)
                else:
                    print(f'\n\n\n\n #participating_in_goal_lottery')
                    print(f'\n {iterate_node.goal_attribute}')
                    self.hash_map[iterate_node.goal_attribute].append(iterate_node)
        print('\n\nparticipated_in_loto_nodes\n\n', self.hash_map)
        for goal, iterate_nodes in self.hash_map.items():
            balances = [Fraction(iterate_node.balance.balance,1) for iterate_node in iterate_nodes]
            iterate_node = RandomService.choice(iterate_nodes, balances)
            #print('\n\n\n choosen iterate node', iterate_node)
            for source_iterate_node in iterate_nodes:
                if iterate_node is not source_iterate_node:
                    print(f'\n\n\n\n loto choosen iterate node to transfer{source_iterate_node}')
                    source_iterate_node.transfer_balances_to_local_iterate_node(iterate_node)
                    print(iterate_node)
                    source_iterate_node.decide(True)

            self.not_decided_nodes_after_loto.append(iterate_node)

        #wait_decision

        for iterate_node in self.not_decided_nodes_after_loto:
            iterate_node(iterate_node.next_iterate_node)



class IterateRankPaths:
    def __init__(self):
        self.iterate_paths = []

    def add(self, iterate_path):
        self.iterate_paths.append(iterate_path)
    
    def rank_paths_increase(self):
        for iterate_path in self.iterate_paths:
            iterate_path.increase_rank()

    def __iter__(self):
        return iter(self.iterate_paths)

class IteratePaths:
    def __init__(self, rank=0):
        self.paths = defaultdict(IterateRankPaths)
        self.rank = rank
        self.max_rank = rank

    def add(self, iterate_path):
        self.paths[iterate_path.rank].add(iterate_path) 
        self.max_rank = max(self.max_rank, iterate_path.rank)

    def __next__(self):
        while self.rank <= self.max_rank:

            iterate_rank_paths = self.paths[self.rank]

            GoalLotteryIterate(iterate_rank_paths)()

            self.iterate_rank_path_increase()

            #self.iterate_with_negative_decision(register_decisions)

            self.rank += 1

    def iterate_rank_path_increase(self):
        iterate_rank_paths = self.paths[self.rank]
        print(self.rank)
        print(iterate_rank_paths.iterate_paths)
        for iterate_path in iterate_rank_paths.iterate_paths:
            print(iterate_path.rank)
            iterate_path.increase_rank_or_back_balance()
            self.paths[iterate_path].add(iterate_path)

        print('\n', self.rank)
        #self.rank += 1

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


if __name__ == '__main__':
    #print(FractionBalance(Fraction(5,6)) * Fraction(4,7))
    action = Action('подорвать')
    action_2 = Action('обнаружить')
    action_3 = Action('уничтожить')
    action_object = ActionObject('деятельность')
    action_destination = ActionDestination('радиоаудиоуправленцы')
    participation = Action('учавствовать')
    money = ActionObject('деньгами')
    loto = ActionDestination('лоторея')
    distribute = Action('распределить')
    on = ActionDestination('на')
    build = Action('проложить')
    road = ActionObject('дорогу')
    Nizhniy_Tyhtem = ActionDestination('Нижний Тыхтем') 
    decrease = Action('потеснить')
    dark_side = ActionDestination('блю теам')
    fuck = Action('ебать')
    fight = Action('отпиздить')
    glass_bottle = Action('стеклянная бутылка')
    brain = Action('мозги')
    light_side = Action('Light Side')
    Roman_Biktayrov = Register('Roman Biktayrov', Balance(100))

    loto_action_0 = Action('loto_action_group_0')
    loto_action_1 = ActionObject('loto_action_group_1')
    loto_action_2 = ActionDestination('loto_action_group_2')

    DestinationRomanBiktayrov = ActionDestination(Roman_Biktayrov) 
    dark_side = Register('Dark Side', Balance(3_000_000_000))

    collector_seed_register_part_balances = CollectorRegiters()
    collector_seed_register_part_balances.add(Roman_Biktayrov)
    collector_seed_register_part_balances.add(dark_side)


    list_attributes_probability = \
        ListAttributesProbability([
            AttributesProbabilityPartOfBalance((Action, ActionObject, ActionDestination), 
                Fraction(9, 10),  Fraction(1,1)),
            AttributesProbabilityPartOfBalance((Action, ActionDestination), 
                Fraction(8, 10), Fraction(4, 1)),
            AttributesProbabilityPartOfBalance((Action, ActionObject), 
                Fraction(5, 10), Fraction(43, 1)),
            AttributesProbabilityPartOfBalance((Action), 
                Fraction(1, 10), Fraction(34)),
            AttributesProbabilityPartOfBalance((), 
                Fraction(1, 100), Fraction(23444, 1)),
            AttributesProbabilityPartOfBalance((ActionObject, ActionDestination), 
                Fraction(1, 100), Fraction(435, 1)),
            AttributesProbabilityPartOfBalance((ActionObject), 
                Fraction(1, 10), Fraction(15, 1)),
            AttributesProbabilityPartOfBalance((ActionDestination), 
                Fraction(8, 100), Fraction(56, 1))
                ]
            )

    loto_group = ListAttributesProbability([
        AttributesProbabilityPartOfBalance(
            (Action),
            Fraction(1, 1),
            Fraction(1, 2)
            ),
        AttributesProbabilityPartOfBalance(
            (ActionObject),
            Fraction(1, 1),
            Fraction(2, 5)
            ),
        AttributesProbabilityPartOfBalance(
            (ActionDestination),
            Fraction(1, 1),
            Fraction(3, 5)
            )
        ])

    list_participation = ListAttributesProbability([
        AttributesProbabilityPartOfBalance(
            frozenset((Action, ActionObject, ActionDestination)), \
            Fraction(1, 1), \
            Fraction(1, 1))
    ])

    list_ditribution_attributes = \
        ListAttributesProbability([
            AttributesProbabilityPartOfBalance((Action, ActionObject, ActionDestination), 
                Fraction(9, 10),  Fraction(1,1)),
            AttributesProbabilityPartOfBalance((Action, ActionDestination), 
                Fraction(8, 10), Fraction(4, 1)),
            AttributesProbabilityPartOfBalance((Action, ActionObject), 
                Fraction(5, 10), Fraction(43, 1)),
            AttributesProbabilityPartOfBalance((Action), 
                Fraction(1, 10), Fraction(34)),
            AttributesProbabilityPartOfBalance((), 
                Fraction(1, 100), Fraction(23444, 1)),
            AttributesProbabilityPartOfBalance((ActionObject, ActionDestination), 
                Fraction(1, 100), Fraction(435, 1)),
            AttributesProbabilityPartOfBalance((ActionObject), 
                Fraction(1, 10), Fraction(15, 1)),
            AttributesProbabilityPartOfBalance((ActionDestination), 
                Fraction(8, 100), Fraction(56, 1))
                ]
            )

    fuck_brain_Roman_Biktayrov = ListAttributesProbability(\
        [AttributesProbabilityPartOfBalance((Action, ActionObject, ActionDestination), 
            Fraction(1, 1), Fraction(100, 1))]
        )

    goal = GoalListAttributes(action, action_object, \
        action_destination, list_attributes_probability)

    goal_2 = GoalListAttributes(action_2, action_object, \
        action_destination, list_attributes_probability)

    goal_3 = GoalListAttributes(action_3, action_object, \
        action_destination, list_attributes_probability)

    participation = GoalListAttributes(participation, money, loto,\
        list_participation)

    loto_group_goal = GoalListAttributes(loto_action_0, loto_action_1, loto_action_2, loto_group)

    distribute = GoalListAttributes(distribute, money, on, list_ditribution_attributes)

    fuck_brain_to_Roman_Biktayrov = GoalListAttributes(
        fuck, 
        glass_bottle,
        brain, 
        fuck_brain_Roman_Biktayrov)

    #loto_group_node_0 = 

    locate_radioaudiomanagers = IterateNode(Node(
        'Обнаружить радиоаудиоуправленцев сидящих в кресле',
        GoalListAttributes(
            action,
            action_object,
            action_destination,
            list_participation
            ),
            0,
            Fraction(3, 5),
        ),
        Roman_Biktayrov.allocate_funds(Balance(1)),
        collector_seed_register_part_balances
        )

    participate_in_loto = IterateNode(Node(
        'Учавствовать в лоторее Ромашкино Лото',
            participation,
            0,
            Fraction(1)
        ),
        Roman_Biktayrov.allocate_funds(Balance(1)),
        collector_seed_register_part_balances)

    war_with_radioaudiomanagers = IterateNode(Node(
        'Пиздец Вам злодеи!!',
        GoalListAttributes(
            action_2,
            action_object,
            action_destination,
            list_participation
            ),
        1,
        Fraction(8, 9)
        ),
        Roman_Biktayrov.allocate_funds(Balance(1)),
        collector_seed_register_part_balances)

    participate_in_loto_1 = IterateNode(Node(
        'Учавствовать в лоторее Ромашкино Лото',
        participation,
            1,
            Fraction(1)
        ),
        Roman_Biktayrov.allocate_funds(Balance(1)),
        collector_seed_register_part_balances)

    participate_in_loto_by_dark_side = IterateNode(Node(
        'Учавствовать в лоторее Ромашкино Лото',
        participation,
            0,
            Fraction(1)
        ),
        dark_side.allocate_funds(Balance(1_000_000_000))
        collector_seed_register_part_balances)

    fight_with_light_side = IterateNode(Node(
        'Отпиздить cтеклянной бутылкой лайт сайд',
        GoalListAttributes(
            fight,
            glass_bottle,
            light_side,
            list_participation
            ),
            1,
            Fraction(1)
        ),
        dark_side.allocate_funds(Balance(2_000_000_000)),
        collector_seed_register_part_balances)

    # нулевая нода может быть только в одном пути в плане корня пути

    iterate_paths = IteratePaths()

    path_1 = IteratePath(collector_seed_register_part_balances)
    path_1.create_root(locate_radioaudiomanagers)
    path_1.add(war_with_radioaudiomanagers)

    iterate_paths.add(path_1)

    path_2 = IteratePath(collector_seed_register_part_balances)
    path_2.create_root(participate_in_loto)
    path_2.add(war_with_radioaudiomanagers)

    iterate_paths.add(path_2)   

    path_3 = IteratePath(collector_seed_register_part_balances)
    path_3.create_root(participate_in_loto_1)

    iterate_paths.add(path_3)
    
    path_4 = IteratePath(collector_seed_register_part_balances)
    path_4.create_root(participate_in_loto_by_dark_side)
    path_4.add(fight_with_light_side)

    iterate_paths.add(path_4)

    next(iterate_paths)
    print(collector_seed_register_part_balances)
    next(iterate_paths)
    print('\n\nCollector Seed Register Part Balances\n\n', collector_seed_register_part_balances)
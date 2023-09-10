import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd

from functools import reduce



torch.set_default_device('cpu')

n_features = 4 
feature_inflation = np.array([0.001 for _ in range(n_features)])
feature_mean = 1
feature_std = .2
commission_rate_min = 0
commission_rate_max = 1
risk_treshold = .0
hidden_size = n_features
risk_proj_size = 1
n_person = 10
earth_features = [0, 1000, 1000, 0]
probably_random_count = .01
n_iterate = 10



class Rewards:
	def __init__(self, person):
		self.person = person
		self.input_size = 2 * n_features
		self.model = nn.LSTM(self.input_size, hidden_size)


	def __call__(self, other):

		r = np.union1d(
						self.person.features, 
						other.features).\
			reshape((1, self.input_size))
		_, (reward, _ )  = self.model(torch.from_numpy(r).float())

		return reward

class Risk:
	def __init__(self, person):
		self.person = person
		self.n_features = n_features
		self.input_size = 3 * n_features
		self.model_1 = nn.LSTM(self.input_size, hidden_size + 1, proj_size=n_features)
		self.model_2 = nn.LSTM(n_features, hidden_size + 1, proj_size=n_features)
		self.model_3 = nn.LSTM(2 * n_features, hidden_size, proj_size=risk_proj_size)

	def __call__(self, damages, rewards, other_features):
		first_input = reduce(np.union1d, [self.person.features,
						other_features,
						damages.detach().numpy()
						]).\
			reshape((1, self.input_size))
		first_input = torch.from_numpy(first_input).float()
		second_input = rewards
		first_output, _ = self.model_1(first_input)
		second_output, _ = self.model_2(second_input)
		third_input = torch.cat((first_output, second_output)).contiguous().reshape((1, 2 * n_features))
		risk, _ = self.model_3(third_input)

		return risk		



#	def estimate


class Person:
	def __init__(self):
		self.features = np.array([np.random.normal(feature_mean, feature_std) for i in range(n_features)])
		self.features[0] = max(self.features[0],0) # biological feature
		self.features[1] = max(self.features[1],0) # material feature
		self.features[2] = max(self.features[2],0) # comfort feature
		# finance feature may be negative in the current world 
		self.comission_rate = np.random.uniform(commission_rate_min,commission_rate_max)
		self.reward_model = Rewards(self)
		self.risk_model = Risk(self)

	def __hash__(self):
		return id(self)

	def rewards_to(self, other):
		return self.reward_model(other)

	def self_risk(self, damages, rewards, other_features):
		risk = self.risk_model(damages, rewards, other_features)
		return risk

	def invite(self, other, society=None):
		if not society:
			society = LocalSociety(self)
		if self not in society:
			return
		if other.invite_risk(self, society) < risk_treshold:
			society.add(by, other)

	def update_features(self, damages, rewards):
		
		self.features -= rewards[0].detach().numpy()
		self.features += damages[0].detach().numpy()

	def inflation_features(self):
		self.features *= (1 - feature_inflation) 



#	def exit(self, society)

p_1 = Person()
p_2 = Person()

rewards_1_2 = p_1.reward_model(p_2)
rewards_2_1 = p_2.reward_model(p_1)

risk_1 = p_1.risk_model(rewards_2_1, rewards_1_2, p_2.features)
risk_2 = p_2.risk_model(rewards_1_2, rewards_2_1, p_1.features)

class PersonSociety:
	def __init__(self, person):
		self.person = person
		self.roots_loc_sct = set()
		self.children_loc_sct = set()
		self.societies = set()
		self.rank = 0

	def __hash__(self):
		return hash(self.person)

	def add_child(self, other):
		assert self.rank > other.rank

		if other not in self.child:
			self.children_loc_sct.add(other)
	
	def add_root(self, other):
		assert self.rank < other.rank

		if other not in self.root:
			self.roots_loc_sct.add(other)

	def add_society(self, other):
		if other not in self.societies \
			and other not in self.roots_loc_sct\
			 and other not in self.children_loc_sct:
			self.societies.add(other)



#	def estimated_rewards_to(self, other)
		

class Register:
	def __init__(self):
		self.number_interact = []
		self.persons = [Person() for _ in range(n_person)]
		#self.Earth = 
		self.personSocieties = [PersonSociety(person) for person in self.persons]

	def __call__(self):
		for _ in range(n_iterate):
			self.personInteractions()

		pd.DataFrame(self.number_interact).to_csv(f'number_interactions.csv')



	def personInteractions(self):
		self.interActionCounter = InterActionCounter()
		for person_sct_1 in self.personSocieties:
			for person_sct_2 in person_sct_1.roots_loc_sct:
				InterAction(person_sct_1.person, person_sct_2.person, self.interActionCounter)()

			for person_sct_2 in person_sct_1.children_loc_sct:
				InterAction(person_sct_1.person, person_sct_2.person, self.interActionCounter)()

			for person_sct_2 in person_sct_1.societies:
				InterAction(person_sct_1.person, person_sct_2.person, self.interActionCounter)()

		for person_sct_1 in self.personSocieties:
			for person_sct_2 in self.personSocieties:
				t = np.random.binomial(1, probably_random_count)
				person_sct_1.add_society(person_sct_2)
				person_sct_2.add_society(person_sct_1)
				if t == 1:
					InterAction(person_sct_1.person, person_sct_2.person, self.interActionCounter)()

		self.stat()
		self.number_interact.append(self.interActionCounter.counter)
	
	def stat(self):
		pd.DataFrame([[person.features for person in self.persons]]).to_csv(f'{len(self.number_interact)}.csv')


class Planet:
	def __init__(self, societies):
		self.features = earth_features
		self.comission_rate = 0
		self.reward_model = DumpModel()
		self.risk_model = DumpModel()



class InterActionCounter:
	def __init__(self):
		self.counter = 0


class InterAction:
	def __init__(self, society_1, society_2, interActionCounter=None):
		self.sct_1 = society_1
		self.sct_2 = society_2
		self.interActionCounter = interActionCounter

	def __call__(self):
		if self.sct_1.features[0] > 0 and self.sct_2.features[0] > 0 and self.sct_1 != self.sct_2:
			rewards_sct_1_to_sct_2 = self.sct_1.reward_model(self.sct_2)
			rewards_sct_2_to_sct_1 = self.sct_2.reward_model(self.sct_1)

			sct_1_risk = self.sct_1.risk_model(rewards_sct_1_to_sct_2, rewards_sct_2_to_sct_1, self.sct_2.features)
			sct_2_risk = self.sct_2.risk_model(rewards_sct_2_to_sct_1, rewards_sct_1_to_sct_2, self.sct_1.features)
			if sct_1_risk < risk_treshold and sct_2_risk < risk_treshold:
				self.sct_1.update_features(rewards_sct_2_to_sct_1, rewards_sct_1_to_sct_2)
				self.sct_2.update_features(rewards_sct_1_to_sct_2, rewards_sct_2_to_sct_1)
				for index, feature in enumerate(self.sct_1.features[:-1]):
					if feature < 0:
						self.sct_1.features[index] = 0
						self.sct_2.features[index] -= feature
				
				for index, feature in enumerate(self.sct_2.features[:-1]):
					if feature < 0:
						self.sct_2.features[index] = 0
						self.sct_1.features[index] -= feature
				
				if self.interActionCounter:
					self.interActionCounter.counter += 1

			self.sct_1.inflation_features()
			self.sct_2.inflation_features()

			sct_1_risk.backward(torch.tensor([[sct_1_risk >= risk_treshold * 2 - 1]]))
			sct_2_risk.backward(torch.tensor([[sct_2_risk >= risk_treshold * 2 - 1]]))



Register()()





import re
###global_relation
class Tag:
	def __init__(self, filename):
		self.filename = filename

		self.MAX_V = 20

		self.SOS = "<SOS>"
		self.EOS = "<EOS>"
		self.UNK = "<UNK>"
		self.reduce = ")"
		
		self.act_rel_k = "GEN_REL_K"
		self.act_rel_p = "GEN_REL_P"
		self.act_tag_k = "GEN_TAG_K"
		self.act_tag_p = "GEN_TAG_P"
		self.act_tag_x = "GEN_TAG_X"
		self.act_tag_e = "GEN_TAG_E"
		self.act_tag_s = "GEN_TAG_S"

		self.act_rel_global = "REL_GLOBAL"
		self.act_rel_local = "REL_LOCAL"

		self.rel_sdrs = "sdrs("
		self.rel_drs = "drs("
		self.rel_not = "not("
		self.rel_nec = "nec("
		self.rel_pos = "pos("
		self.rel_or = "or("
		self.rel_duplex = "duplex("
		self.rel_imp = "imp("
		self.rel_timex = "timex("
		self.rel_card = "card("

		self.relation_global = list()
		self.relation_local = list()
		for line in open(filename):
			if "==== global":
				flag = 0
			elif "==== local":
				flag = 1
			else:
				if flag == 0:
					self.relation_global.append(line.strip())
				elif flag == 1:
					self.relation_local.append(line.strip())
"""
		self.tag_to_ix[self.act_rel_k] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.act_rel_k)
		self.tag_to_ix[self.act_rel_p] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.act_rel_p)
		self.tag_to_ix[self.act_tag_k] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.act_tag_k)
		self.tag_to_ix[self.act_tag_p] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.act_tag_p)
		self.tag_to_ix[self.act_tag_x] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.act_tag_x)
		self.tag_to_ix[self.act_tag_e] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.act_tag_e)
		self.tag_to_ix[self.act_tag_s] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.act_tag_s)
"""
		
		self.tag_to_ix = {self.SOS:0, self.EOS:1, self.UNK:2}
		self.ix_to_tag = [self.SOS, self.EOS, self.UNK]
		
		self.global_start = len(self.tag_to_ix)
		self.tag_to_ix[self.reduce] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.reduce)
		self.tag_to_ix[self.rel_sdrs] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.rel_sdrs)
		self.tag_to_ix[self.rel_drs] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.rel_drs)
		self.tag_to_ix[self.rel_not] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.rel_not)
		self.tag_to_ix[self.rel_nec] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.rel_nec)
		self.tag_to_ix[self.rel_pos] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.rel_pos)
		self.tag_to_ix[self.rel_or] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.rel_or)
		self.tag_to_ix[self.rel_duplex] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.rel_duplex)
		self.tag_to_ix[self.rel_imp] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.rel_imp)

		self.tag_to_ix[self.rel_timex] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.rel_timex)
		self.tag_to_ix[self.rel_card] = len(self.tag_to_ix)
		self.ix_to_tag.append(self.rel_card)

		for tag in self.relation_global:
			self.tag_to_ix[tag] = len(self.tag_to_ix)
			self.ix_to_tag.append(tag)

		self.k_rel_start = len(self.tag_to_ix)
		for i in range(self.MAX_V):
			self.tag_to_ix["k"+str(i)+"("] = len(self.tag_to_ix)
			self.ix_to_tag.append("k"+str(i)+"(")
		self.p_rel_start = len(self.tag_to_ix)
		for i in range(self.MAX_V):
			self.tag_to_ix["p"+str(i)+"("] = len(self.tag_to_ix)
			self.ix_to_tag.append("p"+str(i)+"(")
		self.k_tag_start = len(self.tag_to_ix)
		for i in range(self.MAX_V):
			self.tag_to_ix["k"+str(i)] = len(self.tag_to_ix)
			self.ix_to_tag.append("k"+str(i))
		self.p_tag_start = len(self.tag_to_ix)
		for i in range(self.MAX_V):
			self.tag_to_ix["p"+str(i)] = len(self.tag_to_ix)
			self.ix_to_tag.append("p"+str(i))
		self.x_tag_start = len(self.tag_to_ix)
		for i in range(self.MAX_V):
			self.tag_to_ix["x"+str(i)] = len(self.tag_to_ix)
			self.ix_to_tag.append("x"+str(i))
		self.e_tag_start = len(self.tag_to_ix)
		for i in range(self.MAX_V):
			self.tag_to_ix["e"+str(i)] = len(self.tag_to_ix)
			self.ix_to_tag.append("e"+str(i))
		self.s_tag_start = len(self.tag_to_ix)
		for i in range(self.MAX_V):
			self.tag_to_ix["s"+str(i)] = len(self.tag_to_ix)
			self.ix_to_tag.append("s"+str(i))

		self.local_start = len(self.tag_to_ix)
		for tag in self.relation_local:
			self.tag_to_ix[tag] = len(self.tag_to_ix)
			self.ix_to_tag.append(tag)

		self.tag_size = len(self.tag_to_ix)
	def type(self, string):
		if string == self.SOS:
			return 0, self.tag_to_ix[self.SOS]
		elif string == self.EOS:
			return 0, self.tag_to_ix[self.EOS]
		elif string == self.reduce:
			return 0, self.tag_to_ix[self.reduce]

		elif re.match("k[0-9]+?(", string):
			return 1, int(string[1:-1])
		elif re.match("p[0-9]+?(", string):
			return 1, int(string[1:-1])

		elif re.match("k[0-9]+", string):
			return 20, int(string[1:])
		elif re.match("p[0-9]+", string):
			return 21, int(string[1:])
		elif re.match("x[0-9]+", string):
			return 22, int(string[1:])
		elif re.match("e[0-9]+", string):
			return 23, int(string[1:])
		elif re.match("s[0-9]+", string):
			return 24, int(string[1:])

		elif string == self.rel_sdrs:
			return 0, self.tag_to_ix[self.rel_sdrs]
		elif string == self.rel_drs:
			return 0, self.tag_to_ix[self.rel_drs]
		elif string == self.rel_not:
			return 0, self.tag_to_ix[self.rel_not]
		elif string == self.rel_nec:
			return 0, self.tag_to_ix[self.rel_nec]
		elif string == self.rel_pos:
			return 0, self.tag_to_ix[self.rel_pos]
		elif string == self.rel_or:
			return 0, self.tag_to_ix[self.rel_or]
		elif string == self.rel_duplex:
			return 0, self.tag_to_ix[self.rel_duplex]
		elif string == self.rel_imp:
			return 0, self.tag_to_ix[self.rel_imp]

		elif string == self.rel_timex:
			return 0, self.tag_to_ix[self.rel_timex]
		elif string == self.rel_card:
			return 0, self.tag_to_ix[self.rel_card]

		elif string in self.relation_global:
			return 0, self.tag_to_ix[string]
		else:
			return 3, -1

	def print_info(self):
		print "special_tag", len(self.special_tag), " ".join(self.special_tag)
		print "special_relation", len(self.special_relation), " ".join(self.special_relation)
		print "K_tag", len(self.K_tag), " ".join(self.K_tag)
		print "P_tag", len(self.P_tag), " ".join(self.P_tag)
		print "X_tag", len(self.X_tag), " ".join(self.X_tag)
		print "E_tag", len(self.E_tag), " ".join(self.E_tag)
		print "S_tag", len(self.S_tag), " ".join(self.S_tag)
		print "relation", len(self.relation_one_slot)+len(self.relation_two_slot)+len(self.relation_flexible_slot)



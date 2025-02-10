# Boolean variables
# BN for !conditions!
pA = 0.8

class ConditionalVariable:
    def __init__(self, p_name, parent_variables=[], child_variables=[]):
        self.p_name = p_name
        self.parent_variables = parent_variables
        self.child_variables = child_variables
        self.probability = 0.0

    def add_parent_variable(self, parent):
        self.parent_variables.append(parent)
        if self not in parent.child_variables:
            parent.add_child_variable(self)
        else:
            print('parent condition already present')

    def add_child_variable(self, child):
        if child not in self.child_variables:
            self.child_variables.append(child)
        else:
            print(f"Didn't add {child} to {self}, child already present")

    def set_probability(self, prob):
        self.probability = prob

    def __repr__(self):
        return f"Probability {self.p_name} {self.probability}"

pA = ConditionalVariable('pA')
pB = ConditionalVariable('pB')
pC = ConditionalVariable('pC')
pA.set_probability(0.8)
# Figure out a way to incorporate the possible 'not' case for parent conditions.
# Currently wouldn't support both given and given not for the conditions
pB.set_probability(0.8)
pC.set_probability(0.7)
pB.add_parent_variable(pA)
pC.add_parent_variable(pA)
pA.add_child_variable(pB)
pA.add_child_variable(pC)

print(pA)

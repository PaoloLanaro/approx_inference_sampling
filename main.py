# BN for !conditions!
pA = 0.8

class ConditionalVariable:
    def __init__(self, parent_variables=[], child_variables=[]):
        self.parent_variables = parent_variables
        self.child_variables = child_variables
        self.probability = 0.0

    def add_parent_variable(self, parent):
        self.parent_variables.append(parent)

    def add_child_variable(self, child):
        self.child_variables.append(child)

    def set_probability(self, prob):
        self.probability = prob

    def __repr__(self):
        return f"Parent Variables: {self.parent_variables}\nChild Variables: {self.child_variables}"

pA = ConditionalVariable()
pB = ConditionalVariable()
pC = ConditionalVariable()
pA.set_probability(0.8)
pA.child_variables(pB)
pA.child_variables(pB)

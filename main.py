# BN for !conditions!
pA = 0.8

class ConditionalVariable:
    def __init__(self, parent_variables=[], child_variables=[]):
        self.parent_variables = parent_variables
        self.child_variables = child_variables
        self.probability = 0.0

    def add_parent_variable(self, parent):
        self.parent_variables.append(parent)
        if self not in parent.child_variables:
            parent.add_child_variable(self)

    def add_child_variable(self, child):
        if child not in self.child_variables:
            self.child_variables.append(child)
        else:
            print(f'child {child} already in self')

    def set_probability(self, prob):
        self.probability = prob

    def __repr__(self):
        return f"Probability: {self.probability}\nFigure some good string representation out"

pA = ConditionalVariable()
pB = ConditionalVariable()
pC = ConditionalVariable()
pA.set_probability(0.8)
pA.add_child_variable(pB)
pA.add_child_variable(pC)

print(pA)

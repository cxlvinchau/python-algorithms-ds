from typing import List, Tuple, Dict, Callable

from logic.formula import Variable, Formula, TT, FF, Disjunction

from itertools import product

class BDD:

    def __init__(self, ordering: List[Variable]):
        self.succs_to_id = dict()
        self.id_to_succ = dict()
        self.num = 1
        self.ordering = ordering

    def make(self, variable: Variable, succs: Tuple[int]):
        if (variable, *succs) in self.succs_to_id:
            return self.succs_to_id[(variable, *succs)]
        self.num += 1
        self.id_to_succ[self.num] = (variable, *succs)
        self.succs_to_id[(variable, *succs)] = self.num
        return self.num

    def create(self, phi: Formula):
        return self._rec_create(phi)

    def _rec_create(self, phi: Formula, i=0):
        if i >= len(self.ordering):
            if phi.evaluate(dict()):
                return 1
            return 0

        variable = self.ordering[i]
        phi1, phi2 = phi.replace(variable, FF()), phi.replace(variable, TT())
        id1, id2 = self._rec_create(phi1, i=i+1), self._rec_create(phi2, i=i+1)
        if id1 == id2 in [0, 1]:
            return id1
        return self.make(variable, (id1, id2))

    def evaluate(self, bdd_id, beta: Dict[Variable, bool]):
        if bdd_id == 0:
            return False
        if bdd_id == 1:
            return True
        row = self.id_to_succ[bdd_id]
        if beta[row[0]]:
            return self.evaluate(row[2], beta)
        return self.evaluate(row[1], beta)

    def disjunction(self, id1, id2):
        if id1 == id2:
            return id1
        if id1 == 1 or id2 == 1:
            return 1
        if id1 != id2:
            if id1 == 0:
                return id2
            elif id2 == 0:
                return id1
        node1, node2 = self.id_to_succ[id1], self.id_to_succ[id2]
        p1, p2 = self.ordering.index(node1[0]), self.ordering.index(node2[0])
        if p1 == p2:
            return self.make(node1[0], (self.disjunction(node1[1], node2[1]), self.disjunction(node1[2], node2[2])))
        elif p2 > p1:
            node1, node2 = node2, node1
        child0, child1 = node1[1:]
        return self.make(node1[0], (self.disjunction(child0, node2), self.disjunction(child1, node2)))


    def to_dot(self):
        s = "digraph {"
        for id, row in self.id_to_succ.items():
            variable = row[0]
            s += f"\n{id} -> {row[1]} [label=\"0\", style=dashed]"
            s += f"\n{id} -> {row[2]} [label=\"1\"]"
            s += f"\n{id} [label=\"{id}: {str(variable)}\"]"
        s += "\n0 [label=\"0\", shape=box]"
        s += "\n1 [label=\"1\", shape=box]"
        return s + "\n}"


if __name__ == "__main__":
    x1, x2, x3 = Variable("x1"), Variable("x2"), Variable("x3")
    bdd = BDD([x1, x2, x3])
    phi1 = bdd.create(~x1 & ~x2 & ~x3)
    phi = bdd.disjunction(phi1, bdd.create(x1 & x2))
    print(phi1)
    print(bdd.to_dot())
    for v1, v2, v3 in product([False, True], repeat=3):
        v = bdd.evaluate(phi1, {x1: v1, x2: v2, x3: v3})
        print(f"x1: {v1}, x2: {v2}, x3: {v3} | {v}")

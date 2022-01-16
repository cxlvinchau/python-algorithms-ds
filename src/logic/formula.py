from abc import abstractmethod, ABCMeta
from typing import Dict
from abc import ABC


class SingletonMetaclass(ABCMeta):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._cache = dict()

    def __call__(cls, *args, **kwargs):
        name = args[0]
        if name in cls._cache:
            return cls._cache[name]
        cls._cache[name] = super().__call__(*args, **kwargs)
        return cls._cache[name]


class Formula(ABC):

    @abstractmethod
    def evaluate(self, beta: dict) -> bool:
        pass

    @abstractmethod
    def replace(self, variable, phi):
        pass

    def __or__(self, other):
        if isinstance(other, Formula):
            return Disjunction(self, other)
        raise TypeError()

    def __and__(self, other):
        if isinstance(other, Formula):
            return Conjunction(self, other)
        raise TypeError()

    def __invert__(self):
        return Negation(self)


class Variable(Formula, metaclass=SingletonMetaclass):

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Variable) and other.name == self.name

    def evaluate(self, beta: dict) -> bool:
        if self in beta:
            return beta[self]
        raise ValueError("Variable cannot be found in assignment")

    def replace(self, variable, phi):
        if variable == self:
            return phi
        return self

    def __str__(self):
        return self.name


class Conjunction(Formula):

    def __init__(self, phi1: Formula, phi2: Formula):
        self.phi1, self.phi2 = phi1, phi2

    def evaluate(self, beta: dict) -> bool:
        return self.phi1.evaluate(beta) and self.phi2.evaluate(beta)

    def replace(self, variable, phi):
        return Conjunction(self.phi1.replace(variable, phi), self.phi2.replace(variable, phi))

    def __str__(self):
        return f"({str(self.phi1)} & {str(self.phi2)})"


class Disjunction(Formula):

    def __init__(self, phi1: Formula, phi2: Formula):
        self.phi1, self.phi2 = phi1, phi2

    def evaluate(self, beta: dict) -> bool:
        return self.phi1.evaluate(beta) or self.phi2.evaluate(beta)

    def replace(self, variable, phi):
        return Disjunction(self.phi1.replace(variable, phi), self.phi2.replace(variable, phi))

    def __str__(self):
        return f"({str(self.phi1)} | {str(self.phi2)})"


class Negation(Formula):

    def __init__(self, phi: Formula):
        self.phi = phi

    def evaluate(self, beta: dict) -> bool:
        return not self.phi.evaluate(beta)

    def replace(self, variable, phi):
        return Negation(self.phi.replace(variable, phi))

    def __str__(self):
        return f"!{str(self.phi)}"


class TT(Formula):

    def evaluate(self, beta: dict) -> bool:
        return True

    def replace(self, variable, phi):
        return TT()

    def __str__(self):
        return "True"


class FF(Formula):

    def evaluate(self, beta: dict) -> bool:
        return False

    def replace(self, variable, phi):
        return FF()

    def __str__(self):
        return "False"

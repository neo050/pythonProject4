import locale
import random
from functools import reduce
import time
import sys


class TreeError(Exception):
    def __repr__(self):
        return f'TreeError({self.key})'

    def __str__(self):
        return f"TreeError!!!:TreeError{self.key}"


class TreeDoesNotExist(TreeError):
    def __init__(self):
        pass

    def __repr__(self):
        return f'TreeDoesNotExist()'

    def __str__(self):
        return f"TreeDoesNotExist!!!,not exist'"


class TreeValueDoesNotExist(TreeError):
    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return f'TreeValueDoesNotExist({self.key})'

    def __str__(self):
        return f"TreeValueDoesNotExist!!!:the val:. is not a val{self.key}, not exist'"


class TreeIllegalValue(TreeError):
    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return f'TreeIllegalValue({self.key})'

    def __str__(self):
        return f"TreeIllegalValue!!!:the val:. is not a leaf.{self.key}'"


rates = {('dollar', 'nis'): float(input("Enter dollar to  nis: ")),
         ('nis', 'dollar'): float(input("Enter nis to  dollar: ")),
         ('nis', 'euro'): float(input("Enter nis to euro: ")), ('euro', 'nis'): float(input("Enter euro to nis: ")),
         ('dollar', 'euro'): float(input("Enter dollar to euro: ")),
         ('euro', 'dollar'): float(input("Enter euro to dollar: "))}


class Euro:
    def __init__(self, money):
        self.__money = money

    def amount(self):
        return rates[('euro', 'nis')] * self.__money

    def __repr__(self):
        return f'Euro({self.__money})'

    def __str__(self):
        return f'{str(self.__money)}€'

    def __add__(self, currency):
        return Shekel(self.amount() + currency.amount())


class Dollar:
    def __init__(self, money):
        self.__money = money

    def __repr__(self):
        return f'Dollar({self.__money})'

    def __str__(self):
        return f'{str(self.__money)}$'

    def amount(self):
        return rates[('dollar', 'nis')] * self.__money

    def __add__(self, currency):
        return Shekel(self.amount() + currency.amount())


class Shekel:
    def __init__(self, money):
        self.__money = money

    def __repr__(self):
        return f'Shekel({self.__money})'

    def __str__(self):
        return f'{str(self.__money)}₪'

    def amount(self):
        return self.__money

    def __add__(self, currency):
        return Shekel(self.amount() + currency.amount())


def add(currencyA, currencyB):
    return currencyA + currencyB


def apply(op, coinA, coinB):
    if op == 'add':
        if type(coinA) is Shekel:
            return coinA + coinB
        elif type(coinA) is Euro and type(coinB) is Dollar:
            return Euro((coinA + coinB).amount() * rates[('nis', 'euro')])

        elif type(coinA) is Dollar and type(coinB) is Euro:
            return Dollar((coinA + coinB).amount() * rates[('nis', 'dollar')])
        elif type(coinA) is Euro:
            return Euro((coinA + coinB).amount() * rates[('nis', 'euro')])
        elif type(coinA) is Dollar:
            return Dollar((coinA + coinB).amount() * rates[('nis', 'dollar')])

    elif op == 'sub':
        if type(coinA) is Shekel:
            a = coinA.amount() - coinB.amount()
            return Shekel(a)
        elif type(coinA) is Euro and type(coinB) is Dollar:
            return Euro((coinA.amount() - coinB.amount()) * rates[('nis', 'euro')])

        elif type(coinA) is Dollar and type(coinB) is Euro:
            return Dollar((coinA.amount() - coinB.amount()) * rates[('nis', 'dollar')])
        elif type(coinA) is Euro:
            return Euro((coinA.amount() - coinB.amount()) * rates[('nis', 'euro')])
        elif type(coinA) is Dollar:
            return Dollar((coinA.amount() - coinB.amount()) * rates[('nis', 'dollar')])


def dollar_to_Shekel(ob):
    return Shekel(ob.amount())


def euro_to_Shekel(ob):
    return Shekel(ob.amount())


def shekel_to_Shekel(ob):
    return ob


def tag(x):
    return type(x)


s = Shekel(50)
d = Dollar(50)
e = Euro(50)
coercions = {('euro', 'nis'): euro_to_Shekel, ('dollar', 'nis'): euro_to_Shekel, ('nis', 'nis'): shekel_to_Shekel}
tag_type = {Shekel: 'nis', Dollar: 'dollar', Euro: 'euro'}


def coerce_apply(op, ob1, ob2):
    if op == 'add':
        return Shekel(
            coercions[tag_type[type(ob1)], 'nis'](ob1).amount() + coercions[tag_type[type(ob2)], 'nis'](ob2).amount())
    if op == 'sub':
        return Shekel(
            coercions[tag_type[type(ob1)], 'nis'](ob1).amount() - coercions[tag_type[type(ob2)], 'nis'](ob2).amount())


s = Shekel(50)
d = Dollar(50)
e = Euro(50)
print(s + d + e)

print(e.amount())

print(d + s)

print(add(e, d))

z = eval(repr(d))
print(z)
print(s)
print(e)
print(apply('add', Shekel(50), Dollar(20)))
print(apply('add', Dollar(50), Euro(20)))
print(apply('sub', Dollar(50), Euro(20)))

print('\n', coercions[('dollar', 'nis')](Dollar(50)))
print(coerce_apply('add', Shekel(50), Dollar(20)))
print(coerce_apply('add', Dollar(50), Euro(20)))
print(coerce_apply('sub', Dollar(12), Euro(20)))


# Searching a key on a B-tree in Python
# Create a node
class BTreeNode:
    def __init__(self, key, leaf=False):
        self.my_key = key
        self.leaf = leaf
        self.Rkeys = []
        self.Lkeys = []
        self.sum_child = 0


# Tree
class BTree:
    def __init__(self, key):
        self.root = BTreeNode(key, True)

    def __eq__(self, ob1):
        if (not self.root.my_key < ob1.root.my_key) and (not ob1.root.my_key < self.root.my_key):
            return True

    def __repr__(self):
        return f'BTree({self.root.my_key})'

    def __str__(self):
        return '<' + str(self.root.my_key) + '>' + str(list(map(str, self.root.Lkeys + self.root.Rkeys))).replace('\\',
                                                                                                                  '')

    def insert(self, key):
        if key < self.root.my_key:
            if len(self.root.Lkeys) > 1:
                if key < self.root.Lkeys[0].root.my_key:
                    self.root.Lkeys[0].root.leaf = False
                    self.root.Lkeys[0].insert(key)
                elif key < self.root.Lkeys[1].root.my_key:
                    self.root.Lkeys[1].root.leaf = False
                    self.root.Lkeys[1].insert(key)
                else:
                    self.root.Lkeys[1].root.leaf = False
                    self.root.Lkeys[1].insert(key)
            elif len(self.root.Lkeys) == 0:
                self.root.Lkeys.append(BTree(key))
            elif len(self.root.Lkeys) == 1:
                if key < self.root.Lkeys[0].root.my_key:
                    self.root.Lkeys[0], self.root.Lkeys.append = BTree(key), (self.root.Lkeys[0])
                self.root.Lkeys.append(BTree(key))

        elif self.root.my_key < key:
            if len(self.root.Rkeys) > 1:
                if key < self.root.Rkeys[0].root.my_key:
                    self.root.Rkeys[0].root.leaf = False
                    self.root.Rkeys[0].insert(key)
                elif key < self.root.Rkeys[1].root.my_key:
                    self.root.Rkeys[1].root.leaf = False
                    self.root.Rkeys[1].insert(key)
                else:
                    self.root.Rkeys[1].root.leaf = False
                    self.root.Rkeys[1].insert(key)
            elif len(self.root.Rkeys) == 0:
                self.root.Rkeys.append(BTree(key))
            elif len(self.root.Rkeys) == 1:
                if key < self.root.Rkeys[0].root.my_key:
                    self.root.Rkeys[0], self.root.Rkeys.append = BTree(key), (self.root.Rkeys[0])
                self.root.Rkeys.append(BTree(key))

    def __delete__(self, key):
        if key < self.root.my_key:
            if len(self.root.Lkeys) > 1:
                if key == self.root.Lkeys[0].root.my_key:
                    x = self.root.Rkeys[0]
                    if self.root.Lkeys[0].root.leaf:
                        self.root.Lkeys.remove(self.root.Lkeys[0])
                        return x
                    else:
                        raise TreeIllegalValue("nop")
                elif key < self.root.Lkeys[0].root.my_key:
                    self.root.Lkeys[0].__delete__(key)
                elif key == self.root.Lkeys[1].root.my_key:
                    x = self.root.Rkeys[1]
                    if self.root.Lkeys[1].root.leaf:
                        self.root.Lkeys.remove(self.root.Lkeys[1])
                        return x
                    else:
                        raise TreeIllegalValue("nop")
                elif key < self.root.Lkeys[1].root.my_key:
                    self.root.Lkeys[1].__delete__(key)
            elif len(self.root.Lkeys) == 0:
                return 0
            elif key == self.root.Lkeys[0].root.my_key:
                x = self.root.Rkeys[0]
                if self.root.Lkeys[0].root.leaf:
                    self.root.Lkeys.remove(self.root.Lkeys[0])
                    return x
                else:
                    raise TreeIllegalValue("nop")

        elif self.root.my_key < key:
            if len(self.root.Rkeys) > 1:
                if key == self.root.Rkeys[0].root.my_key:
                    x = self.root.Rkeys[0]
                    if self.root.Rkeys[0].root.leaf:
                        self.root.Rkeys.remove(self.root.Rkeys[0])
                        return x
                    else:
                        raise TreeIllegalValue()
                elif key < self.root.Rkeys[0].root.my_key:
                    self.root.Rkeys[0].__delete__(key)
                elif key == self.root.Rkeys[1].root.my_key:
                    x = self.root.Rkeys[1]
                    if self.root.Rkeys[1].root.leaf:
                        self.root.Rkeys.remove(self.root.Rkeys[1])

                    else:
                        raise TreeIllegalValue("nop")

                elif key < self.root.Rkeys[1].root.my_key:
                    self.root.Rkeys[1].__delete__(key)
            elif len(self.root.Rkeys) == 0:
                return 0
            elif key == self.root.Rkeys[0].root.my_key:
                x = self.root.Rkeys[0]
                if self.root.Rkeys[0].root.leaf:
                    self.root.Rkeys.remove(self.root.Rkeys[0])
                    return x
                else:
                    raise print(TreeIllegalValue)
        else:
            return


tree = BTree(25)
for i in range(100):
    tree.insert(i)

def main():
    while x != '5':
        x = input(
            'please choose 1 optaion\n 1. to Create a tree\n 2.to Add a value to the tree\n 3.Delete a value from the '
            'tree\n 4.to print the tree\n 5.to Exit ')
        if x == '1':
            y = input('enter the root of the tree')
            new_tree = BTree(y)


        elif x == '2':
            if new_tree is None:
                raise UnboundLocalError('there is no tree!')
            else:
                k = input('enter the value you want to add')
                new_tree.insert(k)


        elif x == '3':
            if new_tree is None:
                raise UnboundLocalError('there is no tree!')
            else:
                k = input('enter the value you want to delete')
                new_tree.__delete__(k)


        elif x == '4':
            if new_tree:
                print(new_tree)

        else:
            print('wrong input!,please try again')


main()
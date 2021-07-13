import numpy as np
import random as rd
import sys

class latin_square:
    def grid(self):
        self.size = int(input("enter the dimensions for the magic square: "))
        self.grid = np.zeros((self.size, self.size), dtype = int)
        self.count = 0

    def possible(self, y, x, new_entery):
            self.enteries_x = []
            self.enteries_y = []

            for i in range(self.size):
                entry = self.grid[y][i]
                self.enteries_x.append(entry)
                self.possibilities_x = (set(range(1, self.size + 1)).difference(self.enteries_x))
                self.count +=1

            for j in range(self.size):
                entry = self.grid[j][x]
                self.enteries_y.append(entry)
                self.possibilities_y = set(range(1, self.size + 1)).difference(self.enteries_y)
                self.count +=1
            
            self.enteries = list(set(self.enteries_x).union(self.enteries_y))

            if new_entery in self.enteries:
                self.possibilities = list(set(self.possibilities_x).intersection(self.possibilities_y))
                self.count +=1
                if self.possibilities == []:
                    self.count +=1
                    self.possibilities = list(self.possibilities_x)
                return False

            self.possibilities_x = []
            self.possibilities_y = []
            self.enteries_x = []
            self.enteries_y = []

            return True

    def find_0(self):
        for y in range(self.size) :
            for x in range(1,self.size):
                if self.grid[y][x] == 0:
                    return True
        return False
    
    def improve(self):
        for y in range(self.size):
            for x in range(self.size):
                a = rd.randint(1, self.size)
                if latin_square.possible(self, y,x,a):
                    self.grid[y][x] = a
                    self.count +=1
                else:
                    self.count +=1
                    a = rd.choice(self.possibilities)
                    self.grid[y][x] = a

    def get_latinSquare(self):
        np.set_printoptions(threshold = sys.maxsize)
        print(np.matrix(self.grid))
        print(self.count)
        v = self.grid[:][0].sort
       

a = latin_square()
a.grid()
a.improve()
a.get_latinSquare()

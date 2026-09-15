#INTHE NAME OF GOD
# MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
# CLASS3.0
class Cat:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

#The distance between tow dots.
    def euclidean_distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dx_squared = dx ** 2
        dy_squared = dy ** 2
        delta = dx_squared + dy_squared
        distance = delta ** 0.5
        return distance

#This distance is like moving through the checkerboard streets
#of Manhattan, New York. that is, you can only move horizontally
#and vertically, not diagonally.
    def manhattan_distance(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        d = dx + dy
        return d

#At this distance, only the largest distance between the brief.
    def chebyshev_distance(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        d = max(dx, dy)
        return d

#create cat instance
cat = Cat(-5.1, -5.2)
pes = Cat(3, 3.5)

#Tell cat to compute euclidean distance from pes
e_dis = cat.euclidean_distance(pes)
m_dis = cat.manhattan_distance(pes)
ch_dis = cat.chebyshev_distance(pes)
print(f'Euclidean distance between {cat} and {pes} is: {e_dis}')
print(f'Euclidean distance between {cat} and {pes} is(round!): {e_dis:.3f}')
print(f'Manhattan distance between {cat} and {pes} is(round!): {m_dis:.3f}')
print(f'Manhattan distance between {cat} and {pes} is(round!): {ch_dis:.3f}')
#AMIRABAS KHAJEH

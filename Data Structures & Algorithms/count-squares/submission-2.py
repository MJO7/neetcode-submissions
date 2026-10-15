class CountSquares:

    def __init__(self):
        self.pointCount = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        point_t = tuple(point)
        self.pointCount[(point_t)]+=1

    def count(self, point: List[int]) -> int:
        count = 0
        px = point[0]
        py = point[1]
        for x,y in self.pointCount:
            if abs(x-px)!=abs(y-py) or x==px or y==py:
                continue
            else:
                if (x,py) in self.pointCount and (px,y) in self.pointCount:
                    count+=self.pointCount[(x,py)]*self.pointCount[(px,y)]*self.pointCount[(x,y)]
        return count
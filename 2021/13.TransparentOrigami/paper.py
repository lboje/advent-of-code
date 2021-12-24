from operator import itemgetter

foldDirection = {
    "x": False,
    "y": True
}

class Paper:

    """
    A sheet of transparent paper. 
    We can mark it as well as fold it.
    On initialization, we only have the coordinates
    """
    def __init__(self, coordinates):
        self.coordinates = set(coordinates)

    """
    Magnitude is the value of change. 
    The "top" of the paper is 0, 0
    Direction is the fold direction (true or false)
    """
    def fold(self, command):
        (horizontal, magnitude) = command
        verticalFold = foldDirection[horizontal] 
        magnitude = int(magnitude)
        newCoords = set()
        for coord in self.coordinates:
            if verticalFold:
                xVal = coord[0]
                yVal = magnitude - (coord[1] - magnitude) if coord[1] >= magnitude else coord[1]
            else:
                xVal = magnitude - (coord[0] - magnitude) if coord[0] >= magnitude else coord[0]
                yVal = coord[1]
            newCoords.add((xVal, yVal))
        self.coordinates = newCoords
        

    #We only have as many points as we do coordinates :)
    @property
    def points(self):
        return len(self.coordinates)


    #Create "paper". Place on grid.
    def __str__(self):
        width = max(self.coordinates)[0] + 1
        height = max(self.coordinates,key=itemgetter(1))[1] + 1
        # 00A0 is a nbsp
        paper = [ [chr(0x00A0)]*(width) for _ in range(height)]
        for x, y in self.coordinates:
            # 2588 is a full block
            paper[y][x] = chr(0x2588)

        visualization = ''
        for row in paper:
            visualization += (''.join(row) + '\n')

        return visualization





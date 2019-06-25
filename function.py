# CREATED BY:
# Yarden Hazan
# Adi Cantor
# Yaron Daya

import math

# Point structure
class _Point:

    def __init__(self, x_, y_, z_):
        self.x = x_
        self.y = y_
        self.z = z_

    def _Point(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def setX(self, x_):
        self.x = x_

    def setY(self, y_):
        self.y = y_

    def setZ(self, z_):
        self.z = z_

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def toString(self):
        print("point: x= %s , y= %s , z= %s" % (self.x, self.y, self.z))


# Face structure
class Face:
    def __init__(self):
        self.point_array = []
        self.visable = False
        self.z_index = 0
        self.color = "green"
        self.d = 0


# parser helper - get the first latter from line
def get_tag(line):
    # split the line - get first symbol
    l = line.split(":")

    # L - represent Line
    if (l[0] == "Q"):
        return l[0]
    # C - represent Circle
    elif (l[0] == "P"):
        return l[0]

    else:
        print("something went wrong = function.py - get_tag")


# read from the insert file
def read_from_file(self, path):
    Vertices = []
    if path == "":
        print("path is empty")
    try:
        # open file - parser to working array
        with open(path, 'r') as file:
            # read the first line
            line = file.readline()

            # while file has lines
            while line:

                # ignore empty line
                if line.strip():

                    # remove the first symbol from line
                    l = line.split(':')
                    l.pop(0)
                    for word in l:
                        if word != "":
                            #   split to array coordinate
                            r = word.split(",")
                            Vertices.append(_Point(int(r[0]), int(r[1]), int(r[2])))
                        else:
                            print("word empty")
                # get the next line - till eof
                line = file.readline()
    except:
        print("file not open or something went wrong")

    # close the file
    file.close()

    # add the lines array to total
    self.total = Vertices

# Calculate Scale - new position for point
def scale_paint_down(self):
    # get the change ranger
    ranger = int(self.scale_factor_down)
    ranger = 1 - (ranger / 100)
    # make sure ranger is not 0
    if ranger != 0:
        # if ranger < 0 then add 1 and the value as ABS - Because ranger is ratio
        if ranger < 0:
            ranger = abs(ranger) + 1
        try:
            #  for every point multiply by ratio
            for t in self.total:
                t.x = t.x * ranger
                t.y = t.y * ranger
                t.z = t.z * ranger
        except:
            print("total is empty")


# Calculate Scale - new position for point
def scale_paint_up(self):
    # get the change ranger
    ranger = int(self.scale_factor_up)
    ranger = ranger / 100 + 1
    # make sure ranger is nut 0
    if ranger != 0:
        # if ranger < 0 then add 1 and the value as ABS - Because ranger is ratio
        if ranger < 0:
            ranger = abs(ranger) + 1
        try:
            #  for every point multiply by ratio
            for t in self.total:
                t.x = t.x * ranger
                t.y = t.y * ranger
                t.z = t.z * ranger
        except:
            print("total is empty")


# Calculate Rotation - new position for point
def rotate_paintX(self):
    theta = int(self.angle_box.get())
    angle = theta * (math.pi / 180)
    try:
        # for every point - calc new position
        for t in self.total:
            Y = t.y
            t.y = int(t.y * math.cos(angle) - (t.z * math.sin(angle)))
            t.z = int(Y * math.sin(angle) + (t.z * math.cos(angle)))
    except:
        print("total is empty")


# Calculate Rotation - new position for point
def rotate_paintY(self):
    theta = int(self.angle_box.get())
    angle = theta * (math.pi / 180)
    try:
        # for every point - calc new position
        for t in self.total:
            X = t.x
            t.x = int(t.x * math.cos(angle) + (t.z * math.sin(angle)))
            t.z = int(-X * math.sin(angle) + (t.z * math.cos(angle)))
    except:
        print("total is empty")


# Calculate Rotation - new position for point
def rotate_paintZ(self):
    theta = int(self.angle_box.get())
    angle = theta * (math.pi / 180)
    try:
        # for every point - calc new position
        for t in self.total:
            X = t.x
            t.x = t.x * math.cos(angle) - (t.y * math.sin(angle))
            t.y = X * math.sin(angle) + (t.y * math.cos(angle))
    except:
        print("total is empty")


# Calculate Move - new position for point
def move_paint(self):
    # check for valid distance
    ranger = max(abs(self.event_point[1].x - self.event_point[0].x), abs(self.event_point[1].y - self.event_point[0].y))

    # make sure ranger is none 0
    if ranger != 0:
        # calculate dx dy
        dx = (self.event_point[1].x - self.event_point[0].x)
        dy = (self.event_point[1].y - self.event_point[0].y)
        try:
            # for every point add dx dy accordingly
            for t in self.total:
                if t[0] == "Lines" or t[0] == "Circels" or t[0] == "Bezier":
                    for i in range(1, len(t)):
                        t[i].x = t[i].x + dx
                        t[i].y = t[i].y + dy
        except:
            print("total is empty")


# normalize points
def normalize_points(self):
    # check first if paint loaded
    if not self.total == 0:
        self.maxX = self.total[0].x
        self.minX = self.total[0].x
        self.maxY = self.total[0].y
        self.minY = self.total[0].y
        self.maxZ = self.total[0].z
        self.minZ = self.total[0].z

        # find minimum and maximum points
        for t in self.total:
            # print(" shape ", t[0])

            # for i in range(1, len(t)):
            if t.x > self.maxX:
                self.maxX = t.x
            if t.y > self.maxY:
                self.maxY = t.y
            if t.z > self.maxZ:
                self.maxZ = t.z

            if t.x < self.minX:
                self.minX = t.x
            if t.y < self.minY:
                self.minY = t.y
            if t.z < self.minZ:
                self.minZ = t.z

        self.center_Paint.setX((self.maxX + self.minX) / 2)
        self.center_Paint.setY((self.maxY + self.minY) / 2)
        self.center_Paint.setZ((self.maxZ + self.minZ) / 2)


# fix paint size - and move to head point
def fix_size(self):
    # move paint to head start (0,0)
    dx = self.minX
    dy = self.minY
    dz = self.minZ
    try:
        for t in self.total:
            t.x = t.x - dx
            t.y = t.y - dy
            t.z = t.z - dz
    except:
        print("total is empty")

    # find Scale value
    ratioScaleX = (self.screen_WIDTH / self.maxX) * 0.4
    ratioScaleY = (self.screen_HEIGHT / self.maxY) * 0.4

    # make sure ratio in not 0
    if not ratioScaleY or ratioScaleY != 0:
        # if scale ratio for x is bigger - then scale based on Y
        if ratioScaleX > ratioScaleY:
            try:
                for t in self.total:
                    t.x = t.x * ratioScaleY
                    t.y = t.y * ratioScaleY
                    t.z = t.z * ratioScaleY

            except:
                print("total is empty")

        # if scale ratio for y is bigger - then scale based on X
        elif ratioScaleX < ratioScaleY:
            try:
                for t in self.total:
                    t.x = t.x * ratioScaleX
                    t.y = t.y * ratioScaleX
                    t.z = t.z * ratioScaleX
            except:
                print("total is empty")


# Center paint
def center_paint(self):
    normalize_points(self)
    dx = (self.screen_WIDTH / 2) - self.center_Paint.x
    dy = (self.screen_HEIGHT / 2) - self.center_Paint.y
    dz = 150 - self.center_Paint.z
    for t in self.total:
        t.x = t.x + dx
        t.y = t.y + dy
        t.z = t.z + dz


# Function to find equation of plane.
def visibility(self,x1, y1, z1, x2, y2, z2, x3, y3, z3):
    a1 = x2 - x1
    b1 = y2 - y1
    c1 = z2 - z1

    a2 = x3 - x2
    b2 = y3 - y2
    c2 = z3 - z2

    Normal_a = b1 * c2 - b2 * c1
    Normal_b = a2 * c1 - a1 * c2
    Normal_c = a1 * b2 - b1 * a2

    # voc = [self.voc.x, self.voc.y , self.voc.z]
    # p1 = [x1, y1, z1]
    # g = np.subtract(voc, p1)

    # vis = Normal_a * g[0] + Normal_b * g[1] + Normal_c * g[2]

    vis = Normal_a * 0 + Normal_b * 0 + Normal_c * (-200)
    return vis

# CREATED BY:
# Yarden Hazan
# Adi Cantor
# Yaron Daya

from function import *
from function import _Point
from tkinter import *
from tkinter import font, messagebox, Text
import tkinter.filedialog
import operator
import math


# main application
class Application(Frame):
    # define variable
    def __init__(self, master=None):
        super().__init__(master)
        self.fontemp3 = font.Font(self, size=6, weight='normal')
        self.fontemp2 = font.Font(self, size=10, weight='bold')
        self.fontemp = font.Font(self, size=30, weight='bold')
        self.grid()
        self.axis = 2
        self.type = "Parallel_Orthographic"
        self.Vertices = []
        self.total = []
        self.Array_face = []
        self.maxX, self.minX, self.maxY, self.minY, self.maxZ, self.minZ = 0, 0, 0, 0, 0, 0
        self.center_Paint = _Point(0, 0, 0)
        self.center_screen = _Point(0, 0, 0)
        self.voc = _Point(0, 0, -200)
        self.scale_factor_up = 1
        self.scale_factor_down = 1

        self.create_widgets()

    # create widgets
    def create_widgets(self):
        self.frame = Frame(self, width=450, height=600)
        self.frame.grid(row=0, column=1)
        self.head = Label(self, text="Graphical Paint", font=self.fontemp)
        self.head.config(bg="#E8EAE6")
        self.head.place(x=80, y=10)
        self.Help = Button(self, text="Help", height=2, width=16, bg="#b2c8f2", font=self.fontemp2, command=self.Help)
        self.Help.place(x=60, y=70)
        self.File = Button(self, text="Open File", height=2, width=16, bg="#b2c8f2", font=self.fontemp2,
                           command=self.FileClick)
        self.File.place(x=240, y=70)

        self.Parallel_Orthographic_Button = Button(self, text="Orthographic", bg="#FFFF66", height=2, width=16,
                                                   font=self.fontemp2,
                                                   command=self.Parallel_Orthographic_click)
        self.Parallel_Orthographic_Button.place(x=60, y=120)

        self.Cavalier_button = Button(self, text="Cavalier", bg="#FFFF66", height=2, width=16, font=self.fontemp2,
                                      command=self.Cavalier_click)
        self.Cavalier_button.place(x=60, y=170)

        self.Cabinet_button = Button(self, text="Cabinet", bg="#FFFF66", height=2, width=16, font=self.fontemp2,
                                     command=self.Cabinet_click)
        self.Cabinet_button.place(x=60, y=215)
        self.angle_label = Label(self, text="Select oblique angle")
        self.angle_label.place(x=260, y=180)
        self.angle_box_oblique = Spinbox(self, from_=1, to=359, state=NORMAL)
        self.angle_box_oblique.place(x=240, y=200)

        self.Perspective_button = Button(self, text="Perspective", bg="#FFFF66", height=2, width=16, font=self.fontemp2,
                                         command=self.Perspective_click)
        self.Perspective_button.place(x=60, y=260)

        self.d_lable = Label(self, text="Select distance")
        self.d_lable.place(x=260, y=260)
        self.d_box = Spinbox(self, from_=1, to=359, state=NORMAL)
        self.d_box.place(x=240, y=280)

        self.Scale_up = Button(self, text="Scale UP", height=2, width=16, bg="#CEE8CE", font=self.fontemp2,
                               command=self.ScaleClick_up)
        self.Scale_up.place(x=60, y=310)

        self.range_up = Scale(self, from_=1, to=100, orient=HORIZONTAL, command=self.onScale_up)
        self.range_up.place(x=80, y=355)

        self.Scale_down = Button(self, text="Scale Down", height=2, width=16, bg="#CEE8CE", font=self.fontemp2,
                                 command=self.ScaleClick_down)
        self.Scale_down.place(x=260, y=310)

        self.range_down = Scale(self, from_=1, to=100, orient=HORIZONTAL, command=self.onScale_down)
        self.range_down.place(x=280, y=355)

        self.rotate_button_x = Button(self, text="Rotate X", bg="#FF6F61", height=2, width=16, font=self.fontemp2,
                                      command=self.rotate_x_click)
        self.rotate_button_x.place(x=60, y=400)

        self.rotate_button_y = Button(self, text="Rotate Y", bg="#FF6F61", height=2, width=16, font=self.fontemp2,
                                      command=self.rotate_y_click)
        self.rotate_button_y.place(x=60, y=445)

        self.rotate_z_click = Button(self, text="Rotate Z", bg="#FF6F61", height=2, width=16, font=self.fontemp2,
                                     command=self.rotate_z_click)
        self.rotate_z_click.place(x=60, y=490)

        self.angle_lable = Label(self, text="Select angle")
        self.angle_lable.place(x=260, y=425)
        self.angle_box = Spinbox(self, from_=1, to=90, state=NORMAL)
        self.angle_box.place(x=240, y=445)

        self.clearCanvasClick = Button(self, text="Clear Canvas", height=2, width=16, bg="#b2c8f2", font=self.fontemp2,
                                       command=self.clearCanvasClick)
        self.clearCanvasClick.place(x=60, y=540)

        self.openPaint = Button(self, text="Open Canvas", height=2, width=16, bg="#b2c8f2", font=self.fontemp2,
                                command=self.openPaintClick)
        self.openPaint.place(x=240, y=540)

        self.start_Paint()

    # start init gui
    def start_Paint(self):
        # new window pop up
        self.window = Toplevel()
        # name
        self.window.wm_title("Canvas - graphic")

        # get current screen resolution
        self.screen_WIDTH = int(self.winfo_screenwidth() * 0.7)
        self.screen_HEIGHT = int(self.winfo_screenheight() * 0.7)

        self.center_screen = _Point((self.screen_WIDTH / 2), (self.screen_HEIGHT / 2), 1)

        # make resolution string
        string_resolution = str(self.screen_WIDTH) + "x" + str(self.screen_HEIGHT)

        # dimension
        self.window.geometry(string_resolution)

        # create canvas
        self.window.canvas = Canvas(self.window, width=self.screen_WIDTH, height=self.screen_HEIGHT, bg="#ffffff")
        # attach canvas
        self.window.canvas.pack()
        # image for paint
        self.window.canvas.img = PhotoImage(width=self.screen_WIDTH, height=self.screen_HEIGHT)
        self.window.canvas.create_image((self.screen_WIDTH / 2, self.screen_HEIGHT / 2), image=self.window.canvas.img,
                                        state="normal")

        # self.FileClick()

    # main function to paint
    def paintTotal(self):
        # print("patin total ")
        # print("type: ", self.type)

        if self.type == "Parallel_Orthographic":
            self.Parallel_Orthographic()
        elif self.type == "Cavalier":
            self.Cavalier()
        elif self.type == "Cabinet":
            self.Cabinet()
        elif self.type == "Perspective":
            self.Perspective()
        else:
            print("not found type")

    # read form insert file and paint
    def paintFile(self, path):
        read_from_file(self, path)
        self.set_face_array()
        # normalizePoints - find edge and center points
        normalize_points(self)
        # Fix size for painting
        fix_size(self)
        # center the paint
        center_paint(self)
        # paint again
        self.paintTotal()

    # ------------- Projection -------------
    # Parallel_Orthographic - projection 
    def Parallel_Orthographic(self):
        center_paint(self)
        self.total_to_vertices()
        self.set_visability()
        self.draw_polygon()

    # Cavalier - projection
    def Cavalier(self):
        angle = int(self.angle_box_oblique.get())
        center_paint(self)
        self.total_to_vertices()
        for t in self.Vertices:
            t.x = t.x + (t.z * math.cos(angle))
            t.y = t.y + (t.z * math.sin(angle))
        self.set_visability()
        self.draw_polygon()

    # Cabinet - projection
    def Cabinet(self):
        angle = int(self.angle_box_oblique.get())
        center_paint(self)
        self.total_to_vertices()
        for t in self.Vertices:
            t.x = t.x + 0.5 * (t.z * math.cos(angle))
            t.y = t.y + 0.5 * (t.z * math.sin(angle))
        self.set_visability()
        self.draw_polygon()

    # Perspective - projection
    def Perspective(self):
        d = int(self.d_box.get())
        center_paint(self)
        self.total_to_vertices()
        for t in self.Vertices:
            t.x = t.x + (t.z / d)
            t.y = t.y + (t.z / d)
        self.set_visability()
        self.draw_polygon()

    # ------------- Objective Function -----------

    # Rotate paint - call for func and paint
    def RotateClick(self):
        if self.axis == 1:
            rotate_paintX(self)
            self.paintTotal()
        elif self.axis == 2:
            rotate_paintY(self)
            self.paintTotal()
        elif self.axis == 3:
            rotate_paintZ(self)
            self.paintTotal()

    # init face array
    def set_face_array(self):
        self.Array_face = []
        self.Vertices = []
        for r in self.total:
            Point = _Point(r.x, r.y, r.z)
            self.Vertices.append(Point)

        t = self.Vertices

        # --------------Cubic--------------
        # Back
        f1 = Face()
        s1 = [t[5], t[6], t[7], t[4]]  # 5 8 7 6
        f1.point_array = s1
        f1.color = "red"
        f1.z_index = max(t[4].z, t[5].z, t[6].z, t[7].z)
        self.Array_face.append(f1)

        # Bottom
        f2 = Face()
        s2 = [t[3], t[7], t[6], t[2]]  # 4 8 7 3
        f2.point_array = s2
        f2.color = "orange"
        f2.z_index = max(t[3].z, t[7].z, t[6].z, t[2].z)
        self.Array_face.append(f2)

        # Left
        f3 = Face()
        s3 = [t[0], t[4], t[7], t[3]]  # 1 5 8 4
        f3.point_array = s3
        f3.color = "blue"
        f3.z_index = max(t[0].z, t[3].z, t[7].z, t[4].z)
        self.Array_face.append(f3)

        # Top
        f4 = Face()
        s4 = [t[0], t[1], t[5], t[4]]  # 1 2 6 5
        f4.point_array = s4
        f4.color = "pink"
        f4.z_index = max(t[0].z, t[4].z, t[5].z, t[1].z)
        self.Array_face.append(f4)

        # Right
        f5 = Face()
        s5 = [t[1], t[2], t[6], t[5]]  # 2 3 7 6
        f5.point_array = s5
        f5.color = "grey"
        f5.z_index = max(t[1].z, t[5].z, t[6].z, t[2].z)
        self.Array_face.append(f5)

        # Front
        f6 = Face()
        s6 = [t[0], t[3], t[2], t[1]]  # 1 4 3 2
        f6.point_array = s6
        f6.color = "yellow"
        f6.z_index = max(t[0].z, t[1].z, t[2].z, t[3].z)
        self.Array_face.append(f6)

        # --------------Pyramid--------------
        # Front
        f7 = Face()
        s7 = [t[8], t[10], t[9]]  # 1 3 2  - 8 10 9
        f7.point_array = s7
        f7.color = "yellow"
        f7.z_index = max(t[8].z, t[9].z, t[10].z)
        self.Array_face.append(f7)

        # Left
        f8 = Face()
        s8 = [t[8], t[9], t[11]]  # 1 2 4 - 8 9 11
        f8.point_array = s8
        f8.color = "red"
        f8.z_index = max(t[8].z, t[9].z, t[11].z)
        self.Array_face.append(f8)

        # Right
        f9 = Face()
        s9 = [t[9], t[10], t[11]]  # 2 3 4 - 9 10 11
        f9.point_array = s9
        f9.color = "blue"
        f9.z_index = max(t[9].z, t[11].z, t[10].z)
        self.Array_face.append(f9)

        # Bottom
        f10 = Face()
        s10 = [t[8], t[11], t[10]]  # 1 4 3 - 8 11 10
        f10.point_array = s10
        f10.color = "pink"
        f10.z_index = max(t[8].z, t[10].z, t[11].z)
        self.Array_face.append(f10)

    # calculate if face is visible
    def set_visability(self):
        for f in self.Array_face:
            f.d = visibility(self, f.point_array[0].x, f.point_array[0].y, f.point_array[0].z, f.point_array[1].x,
                             f.point_array[1].y, f.point_array[1].z, f.point_array[2].x,
                             f.point_array[2].y, f.point_array[2].z)
            if len(f.point_array) == 3:
                f.z_index = max(f.point_array[0].z, f.point_array[1].z, f.point_array[2].z)
            if len(f.point_array) == 4:
                f.z_index = max(f.point_array[0].z, f.point_array[1].z, f.point_array[2].z, f.point_array[3].z)
        self.Array_face.sort(key=operator.attrgetter('z_index'))

    # Draw polygons
    def draw_polygon(self):
        self.clearCanvas()
        for f in self.Array_face:
            if f.d < 0 or f.d == 0:
                polygon = []
                for p in f.point_array:
                    polygon.append(p.x)
                    polygon.append(p.y)
                self.window.canvas.create_polygon(polygon, outline="black", fill=f.color, width=1)

    #  -----------  Opertional function -----------

    # Duplicate main Point vector (total) to Projection vector
    def total_to_vertices(self):
        for i in range(0, len(self.total)):
            self.Vertices[i].setX(self.total[i].x)
            self.Vertices[i].setY(self.total[i].y)
            self.Vertices[i].setZ(self.total[i].z)

    # Clear canvas function
    def clearCanvas(self):
        self.window.canvas.delete(ALL)

    # Open readme.txt file
    def Help(self):
        try:
            self.helpframe.destroy()
        except:
            print("help not open")

        self.helpframe = Toplevel()
        self.helpframe.geometry("700x500")

        self.helpframe.helphead = Label(self.helpframe, text="HELP", font=self.fontemp)
        self.helpframe.helphead.config(bg="#E8EAE6")
        self.helpframe.helphead.place(x=100, y=10)

        self.helpframe.helpText = tk.Text(self.helpframe, height=100 ,width=100, bg="#b2c8f2", font=self.fontemp2)
        self.helpframe.helpText.place(x=0, y=80)

        quote = """Open file - press the button - choose " Vertices " file and press select

Orthographic - press the button to present Orthographic projection

Cavalier - Set up the Angle next to the button - Try minus - and the press the button
Cabinet - Set up the Angle next to the button - Try minus  - and the press the button

Perspective -Set up the Distance next to the button - Try minus - and the press the button

Scale Up & Down - Choose the Percentage under the button and then  Press the button Scale Up or Down

Rotate Paint - Choose the Angel next to the button - Try minus - and then  Press the button Rotate X, Y ,Z

Clear Canvas - press on the button - clear the Canvas

Open Canvas - press on the button - reopen canvas window"""
        self.helpframe.helpText.insert(END, quote)

    # open file from computer
    def FileClick(self):
        a = tkinter.filedialog.askopenfilename(initialdir='C:/', title='Choose Text File',
                                               filetypes=[('.txt', 'txt')])
        self.paintFile(a)

    # -----------  button command -----------

    # button Scale Up
    def ScaleClick_up(self):
        scale_paint_up(self)
        self.paintTotal()

    # button Scale Down
    def ScaleClick_down(self):
        scale_paint_down(self)
        self.paintTotal()

    # Listener for Scale Spinbox Up
    def onScale_up(self, val):
        self.scale_factor_up = val

    # Listener for Scale Spinbox Down
    def onScale_down(self, val):
        self.scale_factor_down = val

    # button - open new Canvas
    def openPaintClick(self):
        self.window.destroy()
        self.start_Paint()

    # button - clear canvas
    def clearCanvasClick(self):
        self.clearCanvas()

    # button - update projection type
    def Parallel_Orthographic_click(self):
        self.type = "Parallel_Orthographic"
        self.paintTotal()

    # button - update projection type
    def Cavalier_click(self):
        self.type = "Cavalier"
        self.paintTotal()

    # button - update projection type
    def Cabinet_click(self):
        self.type = "Cabinet"
        self.paintTotal()

    # button - update projection type
    def Perspective_click(self):
        self.type = "Perspective"
        self.paintTotal()

    # button - update rotate type and call to rotate
    def rotate_x_click(self):
        self.axis = 1
        self.RotateClick()

    # button - update rotate type and call to rotate
    def rotate_y_click(self):
        self.axis = 2
        self.RotateClick()

    # button - update rotate type and call to rotate
    def rotate_z_click(self):
        self.axis = 3
        self.RotateClick()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# start app - entry point
if __name__ == "__main__":
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    app = Application(master=root)
    app.mainloop()




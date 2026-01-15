# Import manim library
from manim import *

class TextScene(Scene):
    """
    By convention, the structure of your animation
    is defined in the construct method, but later
    we will learn how to do it in different ways.
    """
    def construct(self):
        # Create a text using Text class
        text = Text("Hello world")

        # Text animation
        self.play(Write(text))

        # Pause
        self.wait()

        # Fade out animation
        self.play(FadeOut(text))    

class SquareScene(Scene):
    def construct(self):
        # Create a square using Square class
        square = Square()

        # Square animation
        self.play(Create(square))

        # Pause
        self.wait()

        # Rotate animation
        self.play(Rotate(square, angle=PI/4))

        # Pause
        self.wait()

        # Fade out animation
        self.play(FadeOut(square))

class CircleScene(Scene):
    def construct(self):
        # Create a circle using Circle class
        circle = Circle()

        # Circle animation
        self.play(Create(circle))

        # Pause
        self.wait()

        # Scale animation
        self.play(circle.animate.scale(1.5))

        # Pause
        self.wait()

        # Fade out animation
        self.play(FadeOut(circle))

class TriangleScene(Scene):
    def construct(self):
        # Create a triangle using Triangle class
        triangle = Triangle()

        # Triangle animation
        self.play(Create(triangle))

        # Pause
        self.wait()

        # Move animation
        self.play(triangle.animate.shift(UP * 2))

        # Pause
        self.wait()

        # Fade out animation
        self.play(FadeOut(triangle))

class PolygonScene(Scene):
    def construct(self):
        # Create a polygon using Polygon class
        polygon = Polygon(LEFT, UP, RIGHT, DOWN)

        # Polygon animation
        self.play(Create(polygon))

        # Pause
        self.wait()

        # Change color animation
        self.play(polygon.animate.set_fill(RED, opacity=0.5))

        # Pause
        self.wait()

        # Fade out animation
        self.play(FadeOut(polygon))

class LineScene(Scene):
    def construct(self):
        # Create a line using Line class
        line = Line(LEFT, RIGHT)

        # Line animation
        self.play(Create(line))

        # Pause
        self.wait()

        # Extend line animation
        self.play(line.animate.stretch_to_fit_width(6))

        # Pause
        self.wait()

        # Fade out animation
        self.play(FadeOut(line))

class EllipseScene(Scene):
    def construct(self):
        # Create an ellipse using Ellipse class
        ellipse = Ellipse(width=4, height=2)

        # Ellipse animation
        self.play(Create(ellipse))

        # Pause
        self.wait()

        # Rotate animation
        self.play(Rotate(ellipse, angle=PI/6))

        # Pause
        self.wait()

        # Fade out animation
        self.play(FadeOut(ellipse))

class StarScene(Scene):
    def construct(self):
        # Create a star using Star class
        star = Star(n=5)

        # Star animation
        self.play(Create(star))

        # Pause
        self.wait()

        # Change color animation
        self.play(star.animate.set_fill(YELLOW, opacity=0.7))

        # Pause
        self.wait()

        # Fade out animation
        self.play(FadeOut(star))

class SceneWithoutDuration(Scene):
    def construct(self):
        sq = Square()
        self.add(sq)
        # self.wait()

class SayHelloScene(Scene):
    def construct(self):
        hello = Text("Hello!")
        self.play(Write(hello))
        self.wait()

class MyCustomScene(Scene):
   def construct(self):
    obj = Text("X")
    t_a = Text("A")
    t_b = Text("B")
    t_c = Text("C")
    t_d = Text("D")

    self.add(obj)
    self.play(ReplacementTransform(obj,t_a))
    # self.play(ReplacementTransform(obj,t_b)) # <- This not works
    self.play(ReplacementTransform(t_a,t_b))
    self.play(ReplacementTransform(t_b,t_c))
    self.play(ReplacementTransform(t_c,t_d))
    self.wait()
    t_grp = VGroup(obj,t_a,t_b,t_c)\
        .arrange(DOWN)\
        .shift(RIGHT)
    self.play(Write(t_grp))
    self.wait()

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle().set_fill(PINK, opacity=0.5)
        square = Square().set_fill(BLUE, opacity=0.5)

        group = VGroup(circle, square).arrange(RIGHT, buff=0.5)
        group.width = config.frame_width - 1

        self.play(Create(group))
        self.wait()

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.flip(UP)
        )  # color the circle on screen
        self.play(FadeOut(square))  # fade out the circle

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=20
        )
        self.wait()
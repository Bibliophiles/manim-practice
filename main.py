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

class ThinkingPi(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # --- Pi character ---
        pi_symbol = MathTex(r"\pi", color=TEAL).scale(3)
        eyes = VGroup(
            Dot(pi_symbol.get_top() + LEFT * 0.3, radius=0.07, color=WHITE),
            Dot(pi_symbol.get_top() + RIGHT * 0.3, radius=0.07, color=WHITE),
        )
        pi_char = VGroup(pi_symbol, eyes).to_corner(DL, buff=1)

        # --- Thought bubble ---
        bubble = Cloud(
            width=6,
            height=3,
            stroke_color=WHITE,
            stroke_width=3,
        )
        bubble.set_fill(opacity=0)
        bubble.next_to(pi_char, UP + RIGHT, buff=0.6)

        # --- Bubble tail ---
        tail = VGroup(
            Circle(radius=0.12, stroke_color=WHITE, stroke_width=2).set_fill(opacity=0),
            Circle(radius=0.18, stroke_color=WHITE, stroke_width=2).set_fill(opacity=0),
            Circle(radius=0.25, stroke_color=WHITE, stroke_width=2).set_fill(opacity=0),
        )
        tail.arrange(UP, buff=0.15)
        tail.next_to(pi_char, UP + RIGHT, buff=0.1)

        # --- Equations inside bubble ---
        equations = VGroup(
            MathTex("3x + y + 4z = 1"),
            MathTex("5x + 9y + 2z = 6"),
            MathTex("5x + 3y + 5z = 8"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        equations.move_to(bubble.get_center())
        equations.set_color(WHITE)

        # --- Animation ---
        self.play(FadeIn(pi_char))
        self.play(Create(tail), Create(bubble))
        self.play(Write(equations))
        self.wait(2)
        self.play(FadeOut(equations), FadeOut(tail), FadeOut(bubble), FadeOut(pi_char))

class PointCloudExample(Scene):
    def construct(self):
        cloud = PointCloudDot(color=RED)
        self.add(cloud)
        self.play(cloud.animate.apply_complex_function(lambda z: np.exp(z)))   

class MovingText(Scene):
    def construct(self):
        text = Text("Moving Text")
        self.add(text)
        self.play(text.animate.shift(UP + RIGHT))
        self.wait() 

from manim import *

class TransformMemoryDiagram(Scene):
    def construct(self):
        self.camera.frame_width = 14
        self.camera.frame_height = 10
        # -------------------------------
        # Title
        # -------------------------------
        title = MarkupText("Memory").to_edge(UP)
        self.play(FadeIn(title))

        # -------------------------------
        # Memory boxes
        # -------------------------------
        box_width = 1.6
        box_height = 1.0

        def memory_box(label):
            rect = Rectangle(
                width=box_width,
                height=box_height,
                stroke_width=2
            )
            txt = MarkupText(label)
            return VGroup(rect, txt).center()

        labels = ["...", "A", "A", "B", "C", "..."]
        boxes = VGroup(*[memory_box(l) for l in labels])
        boxes.arrange(RIGHT, buff=0)
        boxes.next_to(title, DOWN, buff=0.8)

        self.play(FadeIn(boxes))

        # -------------------------------
        # Time labels
        # -------------------------------
        times = ["", "t1", "t2", "t3", "t4", ""]
        time_labels = VGroup()

        for box, t in zip(boxes, times):
            if t:
                time_labels.add(MarkupText(t, font_size=28).next_to(box, DOWN, buff=0.2))

        self.play(FadeIn(time_labels))

        # -------------------------------
        # Screen box
        # -------------------------------
        screen = Rectangle(
            width=5.5,
            height=2.5,
            stroke_width=2
        )
        screen_label = MarkupText("Screen").next_to(screen, DOWN, buff=0.3)

        screen_group = VGroup(screen, screen_label)
        screen_group.to_edge(DOWN).shift(RIGHT * 2)

        self.play(FadeIn(screen_group))

        # -------------------------------
        # Screen content ("A")
        # -------------------------------
        screen_text = MarkupText("A").move_to(screen.get_center())
        self.play(Write(screen_text))
        self.wait(1)    
        # -------------------------------
        # Dotted projection lines
        # -------------------------------
        dotted_lines = VGroup()

        source_indices = [1, 2, 3, 4]
        for i in source_indices:
            line = DashedLine(
                start=boxes[i].get_bottom(),
                end=screen.get_corner(DR),
                dash_length=0.1,
                stroke_width=2
            )
            dotted_lines.add(line)

        self.play(Create(dotted_lines))
        self.wait(1)    

        # -------------------------------
        # Code snippet
        # -------------------------------
        code = Code(
            code_string="""self.play(Transform(t1, t2))
self.play(Transform(t1, t3))
self.play(Transform(t1, t4))
self.play(FadeOut(t1))""",
            language="python",
            background="rectangle",
        )

        code.to_edge(DOWN).shift(LEFT)
        self.play(FadeIn(code))
        self.wait(9)    

class TransformMemoryStepByStep(Scene):
    
    def construct(self):
        self.camera.frame_width = 14
        self.camera.frame_height = 10
        # -------------------------------------------------
        # Title
        # -------------------------------------------------
        title = MarkupText("Memory").to_edge(UP)
        self.play(FadeIn(title))

        # -------------------------------------------------
        # Memory boxes
        # -------------------------------------------------
        box_w, box_h = 1.6, 1.0

        def memory_box(label):
            r = Rectangle(width=box_w, height=box_h, stroke_width=2)
            t = MarkupText(label)
            return VGroup(r, t).center().center()

        labels = ["...", "A", "A", "B", "C", "..."]
        boxes = VGroup(*[memory_box(l) for l in labels])
        boxes.arrange(RIGHT, buff=0)
        boxes.next_to(title, DOWN, buff=0.8)

        self.play(Create(boxes))

        # -------------------------------------------------
        # Time labels
        # -------------------------------------------------
        time_labels = VGroup(
            MarkupText("t1", font_size=28).next_to(boxes[1], DOWN, buff=0.2),
            MarkupText("t2", font_size=28).next_to(boxes[2], DOWN, buff=0.2),
            MarkupText("t3", font_size=28).next_to(boxes[3], DOWN, buff=0.2),
            MarkupText("t4", font_size=28).next_to(boxes[4], DOWN, buff=0.2),
        )

        self.play(FadeIn(time_labels))

        # -------------------------------------------------
        # Screen
        # -------------------------------------------------
        screen = Rectangle(width=5.5, height=2.5, stroke_width=2)
        screen_label = MarkupText("Screen").next_to(screen, DOWN, buff=0.3)

        screen_group = VGroup(screen, screen_label)
        screen_group.to_edge(DOWN).shift(RIGHT * 2)

        self.play(Create(screen_group))

        # -------------------------------------------------
        # Initial object (t1)
        # -------------------------------------------------
        t1 = MarkupText("A").move_to(boxes[1].get_center())
        self.play(FadeIn(t1))

        # Projection line
        proj = DashedLine(
            boxes[1].get_bottom(),
            screen.get_corner(DR),
            dash_length=0.1
        )

        self.play(Create(proj))

        # Move t1 to screen
        self.play(t1.animate.move_to(screen.get_center()))

        self.wait(0.5)

        # -------------------------------------------------
        # Transform t1 → t2
        # -------------------------------------------------
        t2 = MarkupText("A").move_to(boxes[2].get_center())
        proj2 = DashedLine(boxes[2].get_bottom(), screen.get_corner(DR), dash_length=0.1)

        self.play(Create(proj2))
        self.play(Transform(t1, t2))
        self.wait(0.5)

        # -------------------------------------------------
        # Transform t1 → t3
        # -------------------------------------------------
        t3 = MarkupText("B").move_to(boxes[3].get_center())
        proj3 = DashedLine(boxes[3].get_bottom(), screen.get_corner(DR), dash_length=0.1)

        self.play(Create(proj3))
        self.play(Transform(t1, t3))
        self.wait(0.5)

        # -------------------------------------------------
        # Transform t1 → t4
        # -------------------------------------------------
        t4 = MarkupText("C").move_to(boxes[4].get_center())
        proj4 = DashedLine(boxes[4].get_bottom(), screen.get_corner(DR), dash_length=0.1)

        self.play(Create(proj4))
        self.play(Transform(t1, t4))
        self.wait(0.5)

        # -------------------------------------------------
        # Fade out t1 (identity)
        # -------------------------------------------------
        self.play(FadeOut(t1))
        self.wait()


from manim import *

class TransformMemoryStepByStep(Scene):
    def construct(self):
        self.camera.frame_width = 14
        self.camera.frame_height = 10
        self.camera.background_color = BLACK

        # -------------------------------------------------
        # Title
        # -------------------------------------------------
        title = MarkupText("Memory")
        title.to_edge(UP).shift(UP * 0.2)
        self.play(Create(title))

        # -------------------------------------------------
        # Code panel (left)
        # -------------------------------------------------
        code_lines = [
            "t1 = 'A'",              # 0
            "show(t1)",             # 1
            "t1 = 'A'",              # 2
            "t1 = 'B'",              # 3
            "t1 = 'C'",              # 4
            "delete(t1)"             # 5
        ]

        code_mobs = VGroup(*[
            MarkupText(line, font_size=28)
            for line in code_lines
        ])
        code_mobs.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        code_mobs.to_edge(LEFT).shift(UP * 1.2)
        self.play(FadeIn(code_mobs))

        highlight = SurroundingRectangle(code_mobs[0], color=YELLOW, buff=0.1)
        self.play(Create(highlight))

        # -------------------------------------------------
        # Memory boxes
        # -------------------------------------------------
        box_w, box_h = 1.6, 1.0

        def memory_box(label):
            r = Rectangle(width=box_w, height=box_h, stroke_width=2)
            t = MarkupText(label)
            return VGroup(r, t)

        labels = ["<i>...</i>", "A", "A", "B", "C", "<i>...</i>"]
        boxes = VGroup(*[memory_box(l) for l in labels])
        boxes.arrange(RIGHT, buff=0)
        boxes.next_to(title, DOWN, buff=0.8)
        self.play(Create(boxes))

        # -------------------------------------------------
        # Screen
        # -------------------------------------------------
        screen = Rectangle(width=5.5, height=2.5, stroke_width=2)
        screen_label = MarkupText("Screen").next_to(screen, DOWN, buff=0.3)
        screen_group = VGroup(screen, screen_label)
        screen_group.to_edge(DOWN).shift(RIGHT * 2)
        self.play(Create(screen_group))

        # -------------------------------------------------
        # Step 1: show t1
        # -------------------------------------------------
        t1 = MarkupText("A").move_to(boxes[1].get_center())
        self.play(FadeIn(t1))
        self.play(highlight.animate.move_to(code_mobs[1]))
        self.play(t1.animate.move_to(screen.get_center()))
        self.wait(0.4)

        # -------------------------------------------------
        # Step 2: t1 = 'A'
        # -------------------------------------------------
        self.play(highlight.animate.move_to(code_mobs[2]))
        self.play(Transform(t1, MarkupText("A")))
        self.wait(0.4)

        # -------------------------------------------------
        # Step 3: t1 = 'B'
        # -------------------------------------------------
        self.play(highlight.animate.move_to(code_mobs[3]))
        self.play(Transform(t1, MarkupText("B")))
        self.wait(0.4)

        # -------------------------------------------------
        # Step 4: t1 = 'C'
        # -------------------------------------------------
        self.play(highlight.animate.move_to(code_mobs[4]))
        self.play(Transform(t1, MarkupText("C")))
        self.wait(0.4)

        # -------------------------------------------------
        # Step 5: delete t1
        # -------------------------------------------------
        self.play(highlight.animate.move_to(code_mobs[5]))
        self.play(FadeOut(t1))
        self.wait()
from manim import *

class ShowScreenResolution(Scene):
    def construct(self):
        pixel_height = config["pixel_height"]  #  1080 is default
        pixel_width = config["pixel_width"]  # 1920 is default
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]
        self.add(Dot())
        d1 = Line(frame_width * LEFT / 2, frame_width * RIGHT / 2).to_edge(DOWN)
        self.add(d1)
        self.add(Text(str(pixel_width)).next_to(d1, UP))
        d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
        self.add(d2)
        self.add(Text(str(pixel_height)).next_to(d2, RIGHT))

from manim import *

class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.add(t)
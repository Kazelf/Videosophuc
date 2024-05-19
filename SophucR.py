from manim import *

config.tex_template.add_to_preamble("\\usepackage{pifont}")

class Video(Scene):
    def construct(self):
        import manimpango 
        defaultfont = "Times New Roman"
       #Debai
        text1 = Tex(
            r'Let $z\in\mathbb{C},z=x+yi,(x,y\in\mathbb{R}): 4(z-\overline{z})-15i=i(z+\overline{z}-1)^2$'
        ).scale(0.75).to_corner(UL)

        text2 = Tex(
            r'When $|z-\frac{1}{2}+3i|$ reach the minimum value, find S = 8(x+y):'
        ).scale(0.75).shift(2.8*UP, 1.5*LEFT)
        self.play(Write(text1), run_time = 2)
        self.play(Write(text2), run_time =2)
        self.wait(0.5)

        dapanA = Tex(r'A.8').scale(0.8).shift(2.3*UP,6*LEFT)
        self.play(Write(dapanA))
        dapanB = Tex(r'B.16').scale(0.8).shift(2.3*UP,2*LEFT )
        self.play(Write(dapanB))
        dapanC = Tex(r'C.14').scale(0.8).shift(2.3*UP,2*RIGHT)
        self.play(Write(dapanC))
        dapanD = Tex(r'D.19').scale(0.8).shift(2.3*UP,6*RIGHT)
        self.play(Write(dapanD))
        self.wait(10)

        loigiai = Text(
            "Solution: Vu Dinh Thai",
            font=defaultfont,
            color=YELLOW
        ).scale(0.6).shift(1.9*UP)
        self.play(Write(loigiai), run_time = 1)
        self.wait(3)

        #Batdau loigiai
        giai1 = Tex(
            r'$4(z-\overline{z})-15i=i(z+\overline{z}-1)^2 \Leftrightarrow 4(x+yi-x+yi)-15i=i(x+yi+x-yi-1)^2$'
        ).scale(0.75).to_corner(LEFT).shift(1.4*UP)
        self.play(Write(giai1),run_time = 3)
        self.wait(1)

        giai2 = MathTex(
            r'\Leftrightarrow 4.2yi-15i=i(2x-1)^2 \Leftrightarrow  8y-15=(2x-1)^2 '
        ).scale(0.75).to_corner(LEFT).shift(0.9*UP)
        self.play(Write(giai2), run_time = 2)
        self.wait(1)

        giai3 = MathTex(
            r'\Leftrightarrow y=\frac{(2x-1)^2+15}{8}'
        ).scale(0.75).to_corner(LEFT).shift(0.2*UP)
        giai3.set_color_by_tex("x", RED)
        self.play(Write(giai3), run_time = 1)
        self.wait(4)

        giai4 = Tex(
            r'Therefore: $z=x+\frac{(2x-1)^2+15}{8}i$'
        ).scale(0.75).to_corner(LEFT).shift(0.4*DOWN)
        self.play(Write(giai4), run_time = 1)
        self.wait(1)

        giai5 = Tex(
            r'Next: P = $|z-\frac{1}{2}+3i|=|(x-\frac{1}{2})+i[\frac{(2x-1)^2+15}{8}+3]|$'
        ).scale(0.75).to_corner(LEFT).shift(1*DOWN)
        self.play(Write(giai5), run_time = 3)
        self.wait(2)

        giai6 = MathTex(
            r'=\sqrt{(x-\frac{1}{2})^2+(\frac{(2x-1)^2+15}{8}+3)^2}'
        ).scale(0.75).to_corner(LEFT).shift(1.8*DOWN)
        self.play(Write(giai6), run_time = 2)
        self.wait(3)

        giai7 = Tex(
            r'min at $x=\frac{1}{2}$'
        ).scale(0.75).next_to(giai6)
        giai7.set_color_by_tex("x", BLUE)
        self.play(Write(giai7), run_time = 2)
        self.wait(2)

        giai8 = Tex(
            r'Thus: $y=\frac{(2.\frac{1}{2}-1)^2+15}{8}=\frac{15}{8}$'
        ).scale(0.75).to_corner(LEFT).shift(2.7*DOWN)
        self.play(Write(giai8), run_time = 2)
        self.wait(1)

        giai9 = MathTex(
            r'\Rightarrow S = 8(\frac{1}{2}+\frac{15}{8}) = 19'
        ).scale(0.75).next_to(giai8)
        self.play(Write(giai9), run_time = 1)
        
        rectangle = Rectangle(
            width=giai9.width-0.2,
            height=giai9.height+0.5,
            stroke_color = RED
        ).shift(2.7*DOWN,0.2*RIGHT)
        self.play(Create(rectangle))
        self.wait(5)


from manim import *

config.tex_template.add_to_preamble("\\usepackage{pifont}")

class Image(Scene):
    def construct(self):
        import manimpango 
        defaultfont = "Times New Roman"
       #Debai
        text1 = Tex(
            r'Let $z\in\mathbb{C},z=x+yi,(x,y\in\mathbb{R}): 4(z-\overline{z})-15i=i(z+\overline{z}-1)^2$'
        ).scale(0.75).to_corner(UL)
        self.add(text1)

        text2 = Tex(
            r'When $|z-\frac{1}{2}+3i|$ reach the minimum value, find S = 8(x+y):'
        ).scale(0.75).shift(2.8*UP, 1.5*LEFT)
        self.add(text2)

        dapanA = Tex(r'A.8').scale(0.8).shift(2.3*UP,6*LEFT)
        self.add(dapanA)
        dapanB = Tex(r'B.16').scale(0.8).shift(2.3*UP,2*LEFT )
        self.add(dapanB)
        dapanC = Tex(r'C.14').scale(0.8).shift(2.3*UP,2*RIGHT)
        self.add(dapanC)
        dapanD = Tex(r'D.19').scale(0.8).shift(2.3*UP,6*RIGHT)
        self.add(dapanD)

        loigiai = Text(
            "Solution: Vu Dinh Thai",
            font=defaultfont,
            color=YELLOW
        ).scale(0.6).shift(1.9*UP)
        self.add(loigiai)

        #Batdau loigiai
        giai1 = Tex(
            r'$4(z-\overline{z})-15i=i(z+\overline{z}-1)^2 \Leftrightarrow 4(x+yi-x+yi)-15i=i(x+yi+x-yi-1)^2$'
        ).scale(0.75).to_corner(LEFT).shift(1.4*UP)
        self.add(giai1)

        giai2 = MathTex(
            r'\Leftrightarrow 4.2yi-15i=i(2x-1)^2 \Leftrightarrow  8y-15=(2x-1)^2 '
        ).scale(0.75).to_corner(LEFT).shift(0.9*UP)
        self.add(giai2)

        giai3 = MathTex(
            r'\Leftrightarrow y=\frac{(2x-1)^2+15}{8}'
        ).scale(0.75).to_corner(LEFT).shift(0.2*UP)
        giai3.set_color_by_tex("x", RED)
        self.add(giai3)

        giai4 = Tex(
            r'Therefore: $z=x+\frac{(2x-1)^2+15}{8}i$'
        ).scale(0.75).to_corner(LEFT).shift(0.4*DOWN)
        self.add(giai4)

        giai5 = Tex(
            r'Next: P = $|z-\frac{1}{2}+3i|=|(x-\frac{1}{2})+i[\frac{(2x-1)^2+15}{8}+3]|$'
        ).scale(0.75).to_corner(LEFT).shift(1*DOWN)
        self.add(giai5)

        giai6 = MathTex(
            r'=\sqrt{(x-\frac{1}{2})^2+(\frac{(2x-1)^2+15}{8}+3)^2}'
        ).scale(0.75).to_corner(LEFT).shift(1.8*DOWN)
        self.add(giai6)

        giai7 = Tex(
            r'min at $x=\frac{1}{2}$'
        ).scale(0.75).next_to(giai6)
        giai7.set_color_by_tex("x", BLUE)
        self.add(giai7)

        giai8 = Tex(
            r'Thus: $y=\frac{(2.\frac{1}{2}-1)^2+15}{8}=\frac{15}{8}$'
        ).scale(0.75).to_corner(LEFT).shift(2.7*DOWN)
        self.add(giai8)

        giai9 = MathTex(
            r'\Rightarrow S = 8(\frac{1}{2}+\frac{15}{8}) = 19'
        ).scale(0.75).next_to(giai8)
        self.add(giai9)

        rectangle = Rectangle(
            width=giai9.width-0.2,
            height=giai9.height+0.5,
            stroke_color = RED
        ).shift(2.7*DOWN,0.2*RIGHT)
        self.add(rectangle)



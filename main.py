import random
from math import pi

import flet as ft
from flet import Container, ElevatedButton, Page, Stack, alignment, colors


def main(page: Page):

    size = 6
    gap = 2
    duration = 2000


    c1 = colors.PINK_500
    c2 = colors.AMBER_500
    c3 = colors.LIGHT_GREEN_500
    c4 = colors.DEEP_PURPLE_500
    c5 = colors.BLUE_500
    c6 = colors.RED_500
    c7 = colors.ORANGE_500
    c8 = colors.CYAN_500
    c9 = colors.INDIGO_500
    c10 = colors.TEAL_500
    c11 = colors.BROWN_500
    c12 = colors.LIME_500
    c13 = colors.YELLOW_500
    c14 = colors.GREEN_500
    c15 = colors.PURPLE_500
    c16 = colors.PINK_400
    c17 = colors.AMBER_400
    c18 = colors.LIGHT_GREEN_400
    c19 = colors.DEEP_PURPLE_400
    c20 = colors.BLUE_400
    c21 = colors.RED_400
    c22 = colors.ORANGE_400
    c23 = colors.CYAN_400

    all_colors = [
        colors.AMBER_400,
        colors.AMBER_ACCENT_400,
        colors.BLUE_400,
        colors.BROWN_400,
        colors.CYAN_700,
        colors.DEEP_ORANGE_500,
        colors.CYAN_500,
        colors.INDIGO_600,
        colors.ORANGE_ACCENT_100,
        colors.PINK,
        colors.RED_600,
        colors.GREEN_400,
        colors.GREEN_ACCENT_200,
        colors.TEAL_ACCENT_200,
        colors.LIGHT_BLUE_500,
    ]

    parts = [
        # H
        (0, 0, c1),
        (0, 1, c1),
        (0, 2, c1),
        (0, 3, c1),
        (0, 4, c1),
        (0, 5, c1),
        (0, 6, c1),
        (1, 3, c1),
        (2, 3, c1),
        (3, 3, c1),
        (0, 4, c1),
        (4, 0, c1),
        (4, 1, c1),
        (4, 2, c1),
        (4, 3, c1),
        (4, 4, c1),
        (4, 5, c1),
        (4, 6, c1),
        
        # A
        (6, 2, c2),
        (6, 3, c2),
        (6, 4, c2),
        (6, 5, c2),
        (6, 6, c2),
        (7, 1, c2),
        (7, 4, c2),
        (8, 0, c2),
        (8, 4, c2),
        (9, 1, c2),
        (9, 4, c2),
        (10, 2, c2),
        (10, 3, c2),
        (10, 4, c2),
        (10, 5, c2),
        (10, 6, c2),
        
        # P
        (12, 0, c3),
        (12, 1, c3),
        (12, 2, c3),
        (12, 3, c3),
        (12, 4, c3),
        (12, 5, c3),
        (12, 6, c3),
        (13, 0, c3),
        (13, 3, c3),
        (14, 0, c3),
        (14, 3, c3),
        (15, 0, c3),
        (15, 3, c3),
        (16, 1, c3),
        (16, 2, c3),
        
        # P
        (18, 0, c4),
        (18, 1, c4),
        (18, 2, c4),
        (18, 3, c4),
        (18, 4, c4),
        (18, 5, c4),
        (18, 6, c4),
        (19, 0, c4),
        (19, 3, c4),
        (20, 0, c4),
        (20, 3, c4),
        (21, 0, c4),
        (21, 3, c4),
        (22, 1, c4),
        (22, 2, c4),
        
        # Y
        (24, 0, c5),
        (24, 1, c5),
        (24, 2, c5),
        (25, 3, c5),
        (26, 4, c5),
        (26, 5, c5),
        (26, 6, c5),
        (27, 3, c5),
        (28, 0, c5),
        (28, 1, c5),
        (28, 2, c5),
        
        # B
        (0, 8, c6),
        (0, 9, c6),
        (0, 10, c6),
        (0, 11, c6),
        (0, 12, c6),
        (0, 13, c6),
        (0, 14, c6),
        (1, 8, c6),
        (1, 11, c6),
        (1, 14, c6),
        (2, 8, c6),
        (2, 11, c6),
        (2, 14, c6),
        (3, 8, c6),
        (3, 11, c6),
        (3, 14, c6),
        (4, 9, c6),
        (4, 10, c6),
        (4, 12, c6),
        (4, 13, c6),

        # I
        (7, 8, c7),
        (7, 14, c7),
        (8, 8, c7),
        (8, 9, c7),
        (8, 10, c7),
        (8, 11, c7),
        (8, 12, c7),
        (8, 13, c7),
        (8, 14, c7),
        (9, 8, c7),
        (9, 14, c7),

        # R
        (12, 8, c8),
        (12, 9, c8),
        (12, 10, c8),
        (12, 11, c8),
        (12, 12, c8),
        (12, 13, c8),
        (12, 14, c8),
        (13, 8, c8),
        (13, 11, c8),
        (14, 8, c8),
        (14, 11, c8),
        (14, 12, c8),
        (15, 8, c8),
        (15, 11, c8),
        (15, 13, c8),
        (16, 9, c8),
        (16, 10, c8),
        (16, 14, c8),
        
        # T
        (18, 8, c9),
        (19, 8, c9),
        (20, 8, c9),
        (20, 9, c9),
        (20, 10, c9),
        (20, 11, c9),
        (20, 12, c9),
        (20, 13, c9),
        (20, 14, c9),
        (21, 8, c9),
        (22, 8, c9),

        # H
        (24, 8, c10),
        (24, 9, c10),
        (24, 10, c10),
        (24, 11, c10),
        (24, 12, c10),
        (24, 13, c10),
        (24, 14, c10),
        (25, 11, c10),
        (26, 11, c10),
        (27, 11, c10),
        (28, 8, c10),
        (28, 9, c10),
        (28, 10, c10),
        (28, 11, c10),
        (28, 12, c10),
        (28, 13, c10),
        (28, 14, c10),
        
        # D
        (30, 8, c11),
        (30, 9, c11),
        (30, 10, c11),
        (30, 11, c11),
        (30, 12, c11),
        (30, 13, c11),
        (30, 14, c11),
        (31, 8, c11),
        (31, 14, c11),
        (32, 8, c11),
        (32, 14, c11),
        (33, 8, c11),
        (33, 14, c11),
        (34, 9, c11),
        (34, 10, c11),
        (34, 11, c11),
        (34, 12, c11),
        (34, 13, c11),
        
        # A
        (36, 10, c12),
        (36, 11, c12),
        (36, 12, c12),
        (36, 13, c12),
        (36, 14, c12),
        (37, 9, c12),
        (37, 12, c12),
        (38, 8, c12),
        (38, 12, c12),
        (39, 9, c12),
        (39, 12, c12),
        (40, 10, c12),
        (40, 11, c12),
        (40, 12, c12),
        (40, 13, c12),
        (40, 14, c12),
        
        # Y
        (42, 8, c13),
        (42, 9, c13),
        (42, 10, c13),
        (43, 11, c13),
        (44, 12, c13),
        (44, 13, c13),
        (44, 14, c13),
        (45, 11, c13),
        (46, 8, c13),
        (46, 9, c13),
        (46, 10, c13),
        
        # H
        (0, 16, c14),
        (0, 17, c14),
        (0, 18, c14),
        (0, 19, c14),
        (0, 20, c14),
        (0, 21, c14),
        (0, 22, c14),
        (1, 19, c14),
        (2, 19, c14),
        (3, 19, c14),
        (0, 20, c14),
        (4, 16, c14),
        (4, 17, c14),
        (4, 18, c14),
        (4, 19, c14),
        (4, 20, c14),
        (4, 21, c14),
        (4, 22, c14),
        
        # I
        (7, 16, c15),
        (7, 22, c15),
        (8, 16, c15),
        (8, 17, c15),
        (8, 18, c15),
        (8, 19, c15),
        (8, 20, c15),
        (8, 21, c15),
        (8, 22, c15),
        (9, 16, c15),
        (9, 22, c15),
        
        # R
        (12, 16, c16),
        (12, 17, c16),
        (12, 18, c16),
        (12, 19, c16),
        (12, 20, c16),
        (12, 21, c16),
        (12, 22, c16),
        (13, 16, c16),
        (13, 19, c16),
        (14, 16, c16),
        (14, 19, c16),
        (14, 20, c16),
        (15, 16, c16),
        (15, 19, c16),
        (15, 21, c16),
        (16, 17, c16),
        (16, 18, c16),
        (16, 22, c16),
        
        # O
        (18, 17, c17),
        (18, 18, c17),
        (18, 19, c17),
        (18, 20, c17),
        (18, 21, c17),
        (19, 16, c17),
        (19, 22, c17),
        (20, 16, c17),
        (20, 22, c17),
        (21, 16, c17),
        (21, 22, c17),
        (22, 17, c17),
        (22, 18, c17),
        (22, 19, c17),
        (22, 20, c17),
        (22, 21, c17),
        
        # K
        (24, 16, c18),
        (24, 17, c18),
        (24, 18, c18),
        (24, 19, c18),
        (24, 20, c18),
        (24, 21, c18),
        (24, 22, c18),
        (25, 19, c18),
        (26, 18, c18),
        (26, 20, c18),
        (27, 17, c18),
        (27, 21, c18),
        (28, 16, c18),
        (28, 22, c18),
        
        # O
        (30, 17, c19),
        (30, 18, c19),
        (30, 19, c19),
        (30, 20, c19),
        (30, 21, c19),
        (31, 16, c19),
        (31, 22, c19),
        (32, 16, c19),
        (32, 22, c19),
        (33, 16, c19),
        (33, 22, c19),
        (34, 17, c19),
        (34, 18, c19),
        (34, 19, c19),
        (34, 20, c19),
        (34, 21, c19),
        
        # 1
        (1, 25, c20),
        (2, 24, c20),
        (2, 25, c20),
        (2, 26, c20),
        (2, 27, c20),
        (2, 28, c20),
        (2, 29, c20),
        (2, 30, c20),
        
        # .
        (7, 30, c21),
        
        # 2
        (12, 25, c22),
        (12, 30, c22),
        (13, 24, c22),
        (13, 29, c22),
        (13, 30, c22),
        (14, 24, c22),
        (14, 28, c22),
        (14, 30, c22),
        (15, 24, c22),
        (15, 27, c22),
        (15, 30, c22),
        (16, 25, c22),
        (16, 26, c22),
        (16, 30, c22),
        
        # 4
        (18, 27, c23),
        (18, 28, c23),
        (19, 26, c23),
        (19, 28, c23),
        (20, 25, c23),
        (20, 28, c23),
        (21, 24, c23),
        (21, 25, c23),
        (21, 26, c23),
        (21, 27, c23),
        (21, 28, c23),
        (21, 29, c23),
        (21, 30, c23),
        (22, 28, c23),
        
    ]

    width = 50 * (size + gap)
    height = 40 * (size + gap)

    canvas = Stack(
        width=width,
        height=height,
        animate_scale=duration,
        animate_opacity=duration,
    )

    # spread parts randomly
    for i in range(len(parts)):
        canvas.controls.append(
            Container(
                animate=duration,
                animate_position=duration,
                animate_rotation=duration,
            )
        )

    def randomize(e):
        random.seed()
        for i in range(len(parts)):
            c = canvas.controls[i]
            part_size = random.randrange(int(size / 2), int(size * 3))
            c.left = random.randrange(0, width)
            c.top = random.randrange(0, height)
            c.bgcolor = all_colors[random.randrange(0, len(all_colors))]
            c.width = part_size
            c.height = part_size
            c.border_radius = random.randrange(0, int(size / 2))
            c.rotate = random.randrange(0, 90) * 2 * pi / 360
        canvas.scale = 5
        canvas.opacity = 0.3
        go_button.visible = True
        again_button.visible = False
        page.update()

    def assemble(e):
        i = 0
        for left, top, bgcolor in parts:
            c = canvas.controls[i]
            c.left = left * (size + gap)
            c.top = top * (size + gap)
            c.bgcolor = bgcolor
            c.width = size
            c.height = size
            c.border_radius = 5
            c.rotate = 0
            i += 1
        canvas.scale = 1
        canvas.opacity = 1
        go_button.visible = False
        again_button.visible = True
        page.update()

    go_button = ft.ElevatedButton("Go!", on_click=assemble)
    again_button = ft.ElevatedButton("Again!", on_click=randomize)

    # Add canvas and buttons to a Stack
    content = Stack(
        controls=[
            Container(
                content=canvas,
                alignment=alignment.center,  # Canvas を画面中央に配置
            ),
            Container(
                content=ft.Row(
                    controls=[go_button, again_button],
                    alignment="center",
                ),
                alignment=alignment.bottom_center,
                padding=10,
            ),
        ],
        expand=True,
    )   

    page.add(content)
    
    randomize(None)

ft.app(main)
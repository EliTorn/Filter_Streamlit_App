import streamlit as st
from PIL import Image
import random


class Filter:
    def __init__(self, image, width, height):
        self.image = image
        self.width = width
        self.height = height

    # Create a new blank image for modifications

    def filters(self, num):
        modified_image = Image.new("RGB", (self.width, self.height))
        for x in range(self.width):
            for y in range(self.height):
                red, green, blue = self.image.getpixel((x, y))
                color = [red, green, blue]
                if num == 1:
                    color = black_and_white(color)
                if num == 2:
                    color = color_shift_right(color)
                if num == 3:
                    color = color_shift_left(color)
                if num == 4:
                    color = lighter(color)
                if num == 5:
                    color = upside(color)
                if num == 6:
                    color = eliminate(color)
                modified_pixel = color[0], color[1], color[2]
                modified_image.putpixel((x, y), modified_pixel)
        return modified_image

    def buttons(self):
        button_clicked = []
        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)

        button_clicked.append(col1.button("Black and White"))
        button_clicked.append(col2.button('Shift Right'))
        button_clicked.append(col3.button('Shift Left'))
        button_clicked.append(col4.button('Lighter'))
        button_clicked.append(col5.button('Upside'))
        button_clicked.append(col6.button('Eliminate'))

        for i in range(6):
            if button_clicked[i]:
                f = Filter(self.image, self.width, self.height)
                return f.filters(i + 1)


def black_and_white(color):
    avg = int((color[0] + color[1] + color[2]) / 3)
    return [avg, avg, avg]


def color_shift_right(color):
    return [color[2], color[0], color[1]]


def color_shift_left(color):
    return [color[1], color[2], color[0]]


def lighter(color):
    for i in range(3):
        color[i] = intense_color(color[i], 1.2)
    return color


def intense_color(original, by):
    original *= by
    if original > 255:
        original = 255
    return int(original)


def eliminate(color):
    list_random = [0, 1, 2]
    random_part = random.choice(list_random)
    color[random_part] = 0
    return color


def upside(color):
    color[0] = int(255 - color[0])
    color[1] = int(255 - color[1])
    color[2] = int(255 - color[2])
    return color

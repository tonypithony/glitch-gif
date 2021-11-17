# from glitch_this import ImageGlitcher
# glitch_img = glitcher.glitch_image('python1.png', 2, color_offset=True, gif=True)

from PIL import Image
from glitch_this import ImageGlitcher

glitcher = ImageGlitcher()

img = Image.open('rock.png')
glitch_img = glitcher.glitch_image(img, 2, color_offset=True, gif=True)

DURATION = 200      # Set this to however many centiseconds each frame should be visible for
LOOP = 0            # Set this to how many times the gif should loop
                    # LOOP = 0 means infinite loop
glitch_img[0].save('glitched_rock.gif',
                   format='GIF',
                   append_images=glitch_img[1:],
                   save_all=True,
                   duration=DURATION,
                   loop=LOOP)
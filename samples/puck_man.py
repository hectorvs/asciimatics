import sys
from asciimatics.effects import Sprite
from asciimatics.exceptions import ResizeScreenError
from asciimatics.paths import Path
from asciimatics.renderers import StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen

puck_man = """
        ${3,2,3}##########
    ${3,2,3}##################
  ${3,2,3}############${7,2,7}    ${3,2,3}######
  ${3,2,3}############${4,2,4}  ${7,2,7}  ${3,2,3}######
${3,2,3}##########################
${3,2,3}##########################
${3,2,3}##########################
${3,2,3}##########################
${3,2,3}##########################
  ${3,2,3}######################
  ${3,2,3}######################
    ${3,2,3}##################
        ${3,2,3}##########
""", """
        ${3,2,3}##########
    ${3,2,3}##################
  ${3,2,3}############${7,2,7}    ${3,2,3}######
  ${3,2,3}############${4,2,4}  ${7,2,7}  ${3,2,3}######
${3,2,3}##########################
${3,2,3}##########################
              ${3,2,3}############
${3,2,3}##########################
${3,2,3}##########################
  ${3,2,3}######################
  ${3,2,3}######################
    ${3,2,3}##################
        ${3,2,3}##########
""", """
        ${3,2,3}##########
    ${3,2,3}##################
  ${3,2,3}############${7,2,7}    ${3,2,3}######
  ${3,2,3}############${4,2,4}  ${7,2,7}  ${3,2,3}######
${3,2,3}##########################
      ${3,2,3}####################
              ${3,2,3}############
      ${3,2,3}####################
${3,2,3}##########################
  ${3,2,3}######################
  ${3,2,3}######################
    ${3,2,3}##################
        ${3,2,3}##########
""", """
        ${3,2,3}##########
    ${3,2,3}##################
  ${3,2,3}############${7,2,7}    ${3,2,3}######
  ${3,2,3}############${4,2,4}  ${7,2,7}  ${3,2,3}######
      ${3,2,3}####################
          ${3,2,3}################
              ${3,2,3}############
          ${3,2,3}################
      ${3,2,3}####################
  ${3,2,3}######################
  ${3,2,3}######################
    ${3,2,3}##################
        ${3,2,3}##########
""", """
        ${3,2,3}##########
    ${3,2,3}##################
  ${3,2,3}############${7,2,7}    ${3,2,3}######
    ${3,2,3}##########${4,2,4}  ${7,2,7}  ${3,2,3}######
        ${3,2,3}##################
            ${3,2,3}##############
              ${3,2,3}############
            ${3,2,3}##############
        ${3,2,3}##################
    ${3,2,3}####################
  ${3,2,3}######################
    ${3,2,3}##################
        ${3,2,3}##########
"""

direction = 1
value = 0
def cycle():
    global value, direction
    value += direction
    if value <= 0 or value >= 4:
        direction = -direction
    return value

class BigMan(Sprite):
    def __init__(self, screen, path, start_frame=0, stop_frame=0):
        super(BigMan, self).__init__(
            screen,
            renderer_dict={
                "default": StaticRenderer(images=puck_man, animation=cycle),
                "left": StaticRenderer(images=puck_man, animation=cycle),
                "right": StaticRenderer(images=puck_man),
                "down": StaticRenderer(images=puck_man),
                "up": StaticRenderer(images=puck_man),
            },
            colour=Screen.COLOUR_YELLOW,
            path=path,
            start_frame=start_frame,
            stop_frame=stop_frame)

def demo(screen):
    scenes = []
    centre = (screen.width // 2, screen.height // 2)
    path = Path()
    path.jump_to(screen.width + 16, centre[1])
    path.move_straight_to(-16, centre[1], screen.width // 2)

    effects = [
        BigMan(screen, path),
    ]
    scenes.append(Scene(effects, 600))

    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass

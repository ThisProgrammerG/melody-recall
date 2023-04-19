import pygame

from assets import IMAGE_CURSOR
from assets import IMAGE_ICON
from assets import get_path

def set_cursor():
    cursor_image = pygame.image.load(get_path(images=IMAGE_CURSOR)).convert_alpha()
    cursor_hotspot = (0, 0)
    pygame.mouse.set_cursor(cursor_hotspot, cursor_image)

def main():
    pygame.init()

    import engine

    pygame.display.set_icon(pygame.image.load(get_path(images=IMAGE_ICON)))
    pygame.display.set_caption(engine.caption)
    pygame.display.set_mode(engine.window_rect.size)
    set_cursor()

    app = engine.Application()
    app.run()
    
if __name__ == '__main__':
    main()

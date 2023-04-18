import pygame

def main():
    pygame.init()

    import engine

    pygame.display.set_caption(engine.caption)
    pygame.display.set_mode(engine.window_rect.size)

    app = engine.Application()
    app.run()
    
if __name__ == '__main__':
    main()

import pygame

class Display(object):
    def __init__(self, resW, resH):
        self.width = resW
        self.height = resH
        self.size = self.width, self.height
        self.bg = 0, 0, 0
        self.scale = 1.0
        self.offset = [0, 0]
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
    
    def start(self):
        self.screen.fill(self.bg)
    
    def end(self):
        pygame.display.flip()

    def drawLine(self, line, color, width):
        # line(Surface, color, start_pos, end_pos, width=1) -> Rect
        pygame.draw.line(self.screen, color, [line[0][0] * self.scale, line[0][1] * self.scale], [line[1][0] * self.scale, line[1][1] * self.scale], width)

    def drawLines(self, lines, color, width, connect = False):
        pygame.draw.lines(self.screen, color, connect, lines, width)

    def drawPoint(self, pos, color, width):
        pygame.draw.circle(self.screen, color, [(int)(pos[0] * self.scale), (int)(pos[1] * self.scale)], width)
    
    def drawText(self, text, textpos):
        self.screen.blit(text, textpos)

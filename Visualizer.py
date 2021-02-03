import pygame

class Visualizer():

    def __init__(self, cells):
        # cells is list of columns of cells
        self.cells = cells
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.main_line_v = pygame.Rect(0, 0, 1, 800)
        self.main_line_h = pygame.Rect(0, 0, 800, 1)
        self.font = pygame.font.Font(None, 50)

    def draw(self):
        self.screen.fill((255, 255, 255))
        # drawing vertical lines, 8
        # every 3rd line is thicker
        for i in range(1, 9):
            new_rect = self.main_line_v.copy()
            new_rect.centerx = 89*i
            if(i%3 == 0):
                new_rect.width = 5
            pygame.draw.rect(self.screen, (0, 0, 0), new_rect)

        # drawing horizontal lines, 8
        # every 3rd line is thicker
        for i in range(1, 9):
            new_rect = self.main_line_h.copy()
            new_rect.centery = 89*i
            if(i%3 == 0):
                new_rect.height = 5
            pygame.draw.rect(self.screen, (0, 0, 0), new_rect)
        
        for row_i in range(len(self.cells)):
            for cel_i in range(len(self.cells[row_i])):
                cell = self.cells[row_i][cel_i]
                if cell.num != 0:
                    if cell.is_fixed:
                        numtxt = self.font.render(str(cell.num), True, (255, 0, 0))
                    else: 
                        numtxt = self.font.render(str(cell.num), True, (0, 0, 0))
                    self.screen.blit(numtxt, (44.5+cel_i*89, 44.5+row_i*89))




        pygame.display.flip()
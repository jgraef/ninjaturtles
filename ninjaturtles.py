import pygame
from threading import Thread
from math import sin, cos, radians
from time import asctime


EVENT_REDRAW = pygame.USEREVENT
#TURTLEICON = b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xa4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xa4\xa4\xa4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xa4\xa4\xa4\xa4\xa4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xffA)Iaaa@hU\xc4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4~,O\'\'\'\'\'\'O\xdb\x1d\xc4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4\xce$\'\'\'\'\'\'\'\'\'\':"\xc4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xffU\xad\'\'\'\'\'\'\'\'\'\'\'\'\x19\xdf\xc4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4;\'\'\'\'\'\'\'\'\'\'\'\'\'\'?A\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x15\xcc\xd0\xd9\x0fO\'\'\'\'\'\'\'\'\'\'\'\xc1\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4\xba\xfb\x1a\xa8!B\x1a\xd9\xe91\'1OO_3\xebF\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4\xf9\'O\x19+\x1f\xa9H!B\x1c\xd8H\xb4\xb4!\x12X\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4\x9a\'\'\'\'\'\'\x19+\xe0\xd8.t\x0eQ\xea[\xc1\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4h\'\'\'\'\'\'\'\'\'\x1f.\x13\'\'\'\'\\\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4~\xc6r\'\'\'\'\'\'\'\'^vH\x1aO\'\'s\xc6\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc46999^\'\'\'O\t\t9H\xe2\xa6Bs\'\'\xf9\xc4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc1_\'\'\'\'\'\'\x01===<l\xa7\x1f\xd7v\x01O:R\xc4\xff\xff\xff\xff\xff\xff\xff\xff\xffC\'\'\'\'\'\'\x19\x1b{*x\xe6\x12*\xa7.\x05\x05=\'\t\xb7\xc4\xff\xff\xff\xff\xff\xff\xff\xff,\'\'\'\'\'\'[=*\r\xbb\xc5\xd1\r\x05\x05ee\x05\x01\'O\xf5\xc4\xff\xff\xff\xff\xff\xff\xff\xc6\xdd_\'\'\'\'\x0c\x1b\r\x05{*x{\x05{\x1b{x=\'\'\t\\\xff\xff\xff\xff\xff\xff\xff\xff\xc4U";O\'j{\x1b(e{({*((\xcae=O\'O\xa2\xff\xff\xff\xff\xff\xff\xff\xff\xff\xffA\xf5O\'\x1b\x05\xbb\x1b(\x05\xca\xbb{\rxxxjOO\t\x15\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xeeO\'\'Dx{x\x1b\x05\x1b\xbb{{(\xcaej\x19\xb7\x1d\xc4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xd5\'\'\'&\x1b({{{]{*(xx\x1b?\'5U\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xd5\'\'\'\x01\x1b(\xbb{\x1b(]\x05\x1b\r*x\x01\'\'6\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc1\'\'\'_ex(\x05\r\r(\r\x1bx\x05\x1b\x01\'\'\xdd\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff~_\'\'\'j\xca\x05x(\x05*(x]\x1b\x05\'\'\'#\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4RO\'\'Oj\xca\r\r\r\xcae\xca\xca=\x19\'\'O"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf5\t\'\'\'\x01\x01\x0c==j&&\t?w\x8bh\xc4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4y\x0c\x01O\'\'\'\'\x01\'\'\'O`\xc4\xc4\xc4\xc4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff6OO\'\'\'\x01\x0c\x19\'\'\'\'T\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xd5_\'\'\'\'&\x01\'\'\'\'_"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc4\xefr/;\xe4I\xe3\x06##"\xc6\xc4\xff\xff\xff\xff\xff\xff\xff\xff\xff'


class NinjaTurtle:
    def __init__(self, resolution = (800, 600), title = "", fps = 25):
        self.reset()

        pygame.init()
        flags = pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode(resolution, flags)
        #self.turtle_icon = pygame.image.fromstring(TURTLEICON, (32, 32), "P")
        self.turtle_icon = pygame.image.load("turtle.gif")
        pygame.display.set_icon(self.turtle_icon)
        pygame.display.set_caption("Ninjaturtle - "+title)
        
        self.screenbuf = pygame.Surface(resolution)
        self.screenbuf.fill((255, 255, 255))
        self.thread = Thread(None, self.handle_events)
        self.thread.start()
        pygame.time.set_timer(EVENT_REDRAW, int(1000.0/fps))

    def __del__(self):
        pygame.quit()

    def reset(self):
        self.pos = (0.0, 0.0)
        self.angle = 0.0
        self.color = (0.0, 0.0, 0.0)
        self.visible = False
        self.on_paper = True
        self.width = 1
        self.zoom = 1.0

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def up(self):
        self.on_paper = False

    def down(self):
        self.on_paper = True

    def set_color(self, r, g, b):
        self.color = (r, g, b)

    def set_width(self, w):
        self.width = w

    def set_zoom(self, z):
        self.zoom = z

    def set_pos(self, p):
        self.pos = p

    def get_pos(self):
        return self.pos

    def left(self, angle):
        self.angle += angle

    def right(self, angle):
        self.angle -= angle

    def forward(self, x):
        phi = radians(self.angle)
        zp = (self.pos[0]-x*sin(phi),
              self.pos[1]-x*cos(phi))
        if (self.on_paper):
            width = int(self.width*self.zoom)
            if (width<1):
                width = 1
            pygame.draw.line(self.screenbuf, self.convert_color(self.color), self.convert_pos(self.pos), self.convert_pos(zp), width)
        self.pos = zp

    def backward(self, x):
        self.forward(-x)

    def dot(self):
        w, h = self.screenbuf.get_size()
        p = self.convert_pos(self.pos)
        if (self.on_paper and p[0]>=0 and p[0]<w and p[1]>=0 and p[1]<h):
            self.screenbuf.set_at(p, self.convert_color(self.color))

    def handle_events(self):
        while (True):
            e = pygame.event.wait()
            if (e.type==pygame.QUIT):
                break
            elif (e.type==pygame.VIDEOEXPOSE or e.type==EVENT_REDRAW):
                self.render()
            elif (e.type==pygame.KEYUP and e.key==pygame.K_F10):
                self.screenshot()

    def render(self):
        self.screen.blit(self.screenbuf, (0, 0))
        if (self.visible):
            self.screen.blit(self.turtle_icon, self.convert_pos(self.pos))
        pygame.display.flip()

    def screenshot(self):
        path = "screenshots/"+asctime()+".jpg"
        print("Screenshot saved to: "+path)
        pygame.image.save(self.screenbuf, path)

    def convert_color(self, c):
        return tuple(map(lambda ch: int(255*ch), c))
    
    def convert_pos(self, p):
        w, h = self.screenbuf.get_size()
        return (int(p[0]*self.zoom+w/2),
                int(p[1]*self.zoom+h/2))
        

__all__ = ["NinjaTurtle"]

if (__name__=="__main__"):
    nt = NinjaTurtle()
    nt.forward(50)
    while (True):
        pass

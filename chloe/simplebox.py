'''
todo:
    - how will i make the finger joints??
        - how to draw them w/ pycairo
            - look into using masks
    - after generating all the faces, 
      how do i draw them in the right places 
      on svg file so they dont overlap?
    - how do i make it so i know which edges should
      have male or female finger joints
    
plans:
    architecture:
        - box class
        has x,y,z,t (universal) params
        has an array of "parts"
            - face class
                - is passed dimensions from box 
                  when being constructed
                - has name param (bottom, top, left, right face)
                - has an array of edges
                    - edges class
                        - is passed dimensions from face
                        when being constructed
                        - has name param (bottom, top, left, right edge)
                        - has param male or female for finger joints
        - pyqt gui
            - collects args, initializes box(args) and runs
            box.render() which outputs the svg
            - after running box.render(),
            output msg of done
'''
import cairo
from IPython.display import Image, display
from math import pi
from io import BytesIO
import numpy as np

class box():
    def __init__(self, x,y,text):
        self.x = x
        self.y = y
        self.text = text.upper()
        self.width = 1000
        self.height = 1000

    def draw(self):
        with cairo.SVGSurface("gen.svg", self.width, self.height) as surface:
            cr = cairo.Context(surface)
            cr.scale(self.width, self.height)
            #paper
            cr.set_source_rgb(1,1,1)
            cr.rectangle(0,0,self.width,self.height)
            cr.fill()

            
            cr.set_font_size(self.y/(len(self.text)))
            cr.select_font_face("Arial", 
                                cairo.FONT_SLANT_NORMAL, 
                                cairo.FONT_WEIGHT_NORMAL)
            cr.move_to(0,0)
            cr.set_line_width(self.y/(len(self.text))/60)  
            cr.move_to(0,0)
            #cr.line_to(100,100)
            cr.set_source_rgb(0,0,1)
            cr.stroke()
            

            cr.set_source_rgb(0,0,0)
            cr.rectangle(.5-self.x/2, .5-self.y/2,self.x,self.y)
            cr.stroke()
            cr.set_source_rgb(1,0,0)
            (x,y,w,h,dx,dy) = cr.text_extents(self.text)
            cr.move_to(.5-w/2, .5+h/2)
            cr.text_path(self.text)
            cr.stroke()

def main():
    obj = box(.9,.9,"xd")
    obj.draw()

if __name__ == '__main__':
    main()


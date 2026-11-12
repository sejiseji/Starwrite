import pyxel
from js import window
class Probe:
 def __init__(self):
  self.presses=0
  pyxel.init(240,240,title='Starwrite touch input probe',fps=30)
  pyxel.run(self.update,self.draw)
 def update(self):
  if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): self.presses+=1
  window.starwriteProbeFrame=pyxel.frame_count
  window.starwriteProbePresses=self.presses
  window.starwriteProbeDown=pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)
 def draw(self):
  pyxel.cls(1)
  pyxel.text(10,10,'TOUCH INPUT PROBE',7)
  pyxel.text(10,20,'presses: '+str(self.presses),7)
  pyxel.circ(120,120,pyxel.frame_count%100,10)
Probe()

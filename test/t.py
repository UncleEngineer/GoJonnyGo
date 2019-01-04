from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject
from direct.actor.Actor import Actor
from panda3d.core import *

 
class MyApp(ShowBase):
 
  def __init__(self):
    ShowBase.__init__(self)
    
    # set light
    alight = AmbientLight('alight')
    alight.setColor(VBase4(0.8, 0.8, 0.8, 1))
    alnp = render.attachNewNode(alight)
    self.render.setLight(alnp)

    # Load the environment model.
    self.jonny = Actor("../models/jonny/jonny_tutorial_04.egg")
    
    
    # Reparent the model to render.
    self.jonny.reparentTo(self.render)
    # Apply scale and position transforms on the model.
    self.jonny.setScale(0.5, 0.5, 0.5)
    self.jonny.setPos(0, 5, -1)
    self.jonny.setShaderAuto()

 
class ReadKeys(DirectObject.DirectObject):
  def __init__(self, model):
    #self.accept('time-a-repeat', self.rotateTank)
    print("ReadKeys constructor")
    self.accept('a', self.headTurn)
    self.accept('b', self.jumpUp)
    self.accept('c', self.relex)
    self.model = model
    print("use \"a\" key to play turn head animation")
    print("use \"b\" key to play jump animation")
    print("use \"c\" key to set relexed pose")
 
  def headTurn(self):
    self.model.play('headTurn')
    
  def jumpUp(self):
    self.model.play('jumpUp')
    
  def relex(self):
    self.model.play('relex')


m = MyApp()
r = ReadKeys(m.jonny)
m.run()

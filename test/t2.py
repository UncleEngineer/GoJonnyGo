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

    # Load the model.
    self.jonny = Actor("../models/jonny/jonny_tutorial_portuguese_04.egg")
    
    
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
    self.accept('a', self.cabeca)
    self.accept('b', self.jumpUp)
    self.accept('c', self.relex)
    self.accept('d', self.braco)
    self.model = model
    print("use tecla \"a\" para animar cabeca.")
    print("use tecla \"b\" para animar saltar.")
    print("use tecla \"c\" para pose relaxada.")
    print("use tecla \"d\" para animar braco.")
    print("use Control-C para sair (ou feche a janela).")
 
  def cabeca(self):
    self.model.play('cabeca')
    
  def jumpUp(self):
    self.model.play('jump')
    
  def relex(self):
    self.model.play('relex')

  def braco(self):
    self.model.play('braco')

m = MyApp()
r = ReadKeys(m.jonny)
m.run()

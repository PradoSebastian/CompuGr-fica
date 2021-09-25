import math, re
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Mesh import *

class OpenGLObject:

  def __init__( self ):
    self.rotateInfo = [ 0, 0, 0, 1 ]
    self.traslateInfo = [ 0, 0, 0 ]
    self.traslateFlag = False
    self.scaleInfo = [ 1, 1, 1 ]
  # end def

  def rotate( self, eje, angulo ):
    if eje == 'x':
      self.rotateInfo = [ angulo, 1, 0, 0 ]
    elif eje == 'y':
      self.rotateInfo = [ angulo, 0, 1, 0 ]
    else:
      self.rotateInfo = [ angulo, 0, 0, 1 ]
    # end if
  # end def

  def traslate( self, x, y, z ):
    self.traslateInfo = [ x, y, z ]
    self.traslateFlag = True
  # end def

  def scale( self, x, y, z ):
    self.scaleInfo = [ x, y, z ]
  # end def

# end class

class Cube:

  def __init__( self ):
    self.length = 2
  # end def

  def Draw( self ):
    glBegin(GL_QUADS)

    glMaterialfv( GL_FRONT, GL_DIFFUSE, [ 1.0, 1.0, 1.0, 1.0 ] )
    glMaterialfv( GL_FRONT, GL_SPECULAR, [ 0.5019, 0.25, 0.0, 1.0 ] )
    glMaterialfv( GL_FRONT, GL_SHININESS, [ 0.5 ] )      

    # Top face    
    glVertex3f(self.length, self.length, -self.length)
    glVertex3f(-self.length, self.length, -self.length)
    glVertex3f(-self.length, self.length, self.length)
    glVertex3f(self.length, self.length, self.length)

    # Bottom face
    glVertex3f(self.length, -self.length, self.length)
    glVertex3f(-self.length, -self.length, self.length)
    glVertex3f(-self.length, -self.length, -self.length)
    glVertex3f(self.length, -self.length, -self.length)

    # Front face  
    glVertex3f(self.length, self.length, self.length)
    glVertex3f(-self.length, self.length, self.length)
    glVertex3f(-self.length, -self.length, self.length)
    glVertex3f(self.length, -self.length, self.length)

    # Back face
    glVertex3f(self.length, -self.length, -self.length)
    glVertex3f(-self.length, -self.length, -self.length)
    glVertex3f(-self.length, self.length, -self.length)
    glVertex3f(self.length, self.length, -self.length)

    # Left face
    glVertex3f(-self.length, self.length, self.length)
    glVertex3f(-self.length, self.length, -self.length)
    glVertex3f(-self.length, -self.length, -self.length)
    glVertex3f(-self.length, -self.length, self.length)

    # Right face
    glVertex3f(self.length, self.length, -self.length)
    glVertex3f(self.length, self.length, self.length)
    glVertex3f(self.length, -self.length, self.length)
    glVertex3f(self.length, -self.length, -self.length)

    glEnd()
  #end def

# end class

class Museum_Mesh( OpenGLObject ):

  def __init__( self, path ):
    OpenGLObject.__init__( self )
    self.mesh = Mesh( )
    self.mesh.read(path)
  # end def

  def Draw( self ):
    if self.traslateFlag:
        glTranslatef(self.traslateInfo[0], self.traslateInfo[1], self.traslateInfo[2])
    glRotatef(self.rotateInfo[0], self.rotateInfo[1], self.rotateInfo[2], self.rotateInfo[3])
    glScalef(self.scaleInfo[0], self.scaleInfo[0], self.scaleInfo[0])
    self.mesh.draw2()
  #end def

# end class

class Museum_item( OpenGLObject ):

  def __init__( self, m_mesh, center ):
    OpenGLObject.__init__( self )
    self.center = center
    self.shelf = Cube( )
    self.mesh = m_mesh
  # end def

  def Draw( self ):
    glPushMatrix( )
    
    glTranslatef(self.center[0], self.center[1], self.center[2])
    glRotatef(self.rotateInfo[0], self.rotateInfo[1], self.rotateInfo[2], self.rotateInfo[3])
    glScalef(self.scaleInfo[0], self.scaleInfo[0], self.scaleInfo[0])

    glPushMatrix( )
    self.shelf.Draw( )
    glPopMatrix( )

    glPushMatrix( )
    glTranslatef( 0, self.shelf.length, 0 )
    self.mesh.Draw( )
    glPopMatrix( )

    glPopMatrix( )
  # end def

# end class

class Museum:

  def __init__( self, radius , y): 
    self.radius = radius
    self.theta = 0
    self.position = [ 0 , y, self.radius ]
    pi = math.atan( 1.0 ) * 4.0    

    glShadeModel( GL_SMOOTH )
    #glLightfv( GL_LIGHT0, GL_POSITION, [ self.position[0], self.position[1], self.position[2], 1.0 ] )
    glLightfv( GL_LIGHT0, GL_POSITION, [ 0.0, 10.0, 0.0, 1.0 ] )
    # glLightfv( GL_LIGHT0, GL_AMBIENT, [ 0.0, 0.0, 0.0, 1.0 ] )
    glLightfv( GL_LIGHT0, GL_DIFFUSE, [ 0.0, 0.0, 0.0, 1.0 ] )

    glLightfv( GL_LIGHT1, GL_POSITION, [ self.radius, 10.0, self.radius, 1.0 ] )
    glLightfv( GL_LIGHT1, GL_DIFFUSE, [ 0.0, 0.0, 0.0, 1.0 ] )

    glLightfv( GL_LIGHT2, GL_POSITION, [ -self.radius, 10.0, self.radius, 1.0 ] )
    glLightfv( GL_LIGHT2, GL_DIFFUSE, [ 0.0, 0.0, 0.0, 1.0 ] )

    glLightfv( GL_LIGHT3, GL_POSITION, [ -self.radius, 10.0, -self.radius, 1.0 ] )
    glLightfv( GL_LIGHT3, GL_DIFFUSE, [ 0.0, 0.0, 0.0, 1.0 ] )

    glLightfv( GL_LIGHT4, GL_POSITION, [ self.radius, 10.0, -self.radius, 1.0 ] )
    glLightfv( GL_LIGHT4, GL_DIFFUSE, [ 0.0, 0.0, 0.0, 1.0 ] )

    glEnable( GL_LIGHTING )
    glEnable( GL_LIGHT0 )
    glEnable( GL_LIGHT1 )
    glEnable( GL_LIGHT2 )
    glEnable( GL_LIGHT3 )
    glEnable( GL_LIGHT4 )

    # Define Meshes

    self.meshes = {}    
    self.meshes["Skull"] = Museum_Mesh("Skull/12140_Skull_v3_L2.obj")
    self.meshes["Wolf"] = Museum_Mesh("Wolf/Wolf_One_obj.obj")
    self.meshes["Sofa"] = Museum_Mesh("Sofa/Koltuk.obj")
    self.meshes["IronMan"] = Museum_Mesh("ironMan/IronMan.obj")
    self.meshes["SpaceShip"] = Museum_Mesh("SpaceShip/Intergalactic_Spaceship-(Wavefront).obj")
    self.meshes["Carro"] = Museum_Mesh("Carro/Shelby.obj")

    # end Define Meshes
    
    # Transform Meshes

    # Skull
    self.meshes["Skull"].rotate('x', -90.0)
    self.meshes["Skull"].scale( 0.1, 0.1, 0.1 )

    # Wolf
    self.meshes["Wolf"].scale( 5, 5, 5 )

    # SpaceShip
    self.meshes["SpaceShip"].traslate( 0, 1, 0 )
    self.meshes["SpaceShip"].scale( 0.6, 0.6, 0.6 )

    # Sofa
    self.meshes["Sofa"].scale( 2, 2, 2 )

    # IronMan
    self.meshes["IronMan"].scale( 0.01, 0.01, 0.01 )

    # Carro
    self.meshes["Carro"].traslate( -0.5, 0, 0 )
    self.meshes["Carro"].scale( 0.5, 0.5, 0.5 )

    # end Transform Meshes

    # Calculate increase
    self.increase = 2 * pi / len(self.meshes)

    # Define Models

    self.models = {}
    self.models["Skull"] = Museum_item(self.meshes["Skull"], self.position.copy())
    self.models["Skull"].rotate('y', self.theta * 180 / pi)
    self.updatePosition()
    self.models["Wolf"] = Museum_item(self.meshes["Wolf"], self.position.copy())
    self.models["Wolf"].rotate('y', self.theta * 180 / pi)
    self.updatePosition()
    self.models["SpaceShip"] = Museum_item(self.meshes["SpaceShip"], self.position.copy())
    self.models["SpaceShip"].rotate('y', self.theta * 180 / pi)
    self.updatePosition()
    self.models["Sofa"] = Museum_item(self.meshes["Sofa"], self.position.copy())
    self.models["Sofa"].rotate('y', self.theta * 180 / pi)
    self.updatePosition()
    self.models["IronMan"] = Museum_item(self.meshes["IronMan"], self.position.copy())
    self.models["IronMan"].rotate('y', self.theta * 180 / pi)
    self.updatePosition()
    self.models["Carro"] = Museum_item(self.meshes["Carro"], self.position.copy())
    self.models["Carro"].rotate('y', self.theta * 180 / pi)
    

    # end Define Models

  # end def

  def Draw( self ):
    for model in self.models.values():
        model.Draw()
    # end for
  # end def

  def updatePosition( self ):    
    self.theta += self.increase    
    self.position[0] = math.sin(self.theta) * self.radius
    self.position[2] = math.cos(self.theta) * self.radius
  # end def

# end class
## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================
## Install OpenGL: pip3 install PyOpenGL PyOpenGL_accelerate
## =========================================================================

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math, sys

## -------------------------------------------------------------------------
## Some global variables: DON'T DO THIS IN REAL LIFE APPLICATIONS!!!!
## -------------------------------------------------------------------------

class Cabeza:
  def __init__( self, x, y, z, rgb = [1, 1, 1]):
    self.Center = [ x, y, z ]
    self.Color = rgb
    self.Rotacion = [ 0, 0, 0, 1 ]
  # end def

  def Draw( self ):
    glPushMatrix( )
    glRotate( self.Rotacion[ 0 ], self.Rotacion[ 1 ], self.Rotacion[ 2 ], self.Rotacion[ 3 ] )
    glColor3fv( self.Color )
    self.dibujarEsfera()
    glPopMatrix( )
  # end def

  def dibujarEsfera( self ):
    pi = math.atan( 1.0 ) * 4.0
    r = 3
    glBegin( GL_POINTS )
    for s_phi in range(0, 100):
      phi = (pi * ( s_phi / 100 )) - (pi * 0.5)
      for s_theta in range(0, 100):
        theta = (2 * pi * s_theta / 100) - pi
        glVertex3f(
        r * math.cos( phi ) * math.cos( theta ) + self.Center[0],
        r * math.cos( phi ) * math.sin( theta ) + self.Center[1],
        r * math.sin( phi ) + self.Center[2]
        )
      # end for
    # end for
    glEnd( )
  # end def

# end class

class Articulacion:
  def __init__( self, x, y, z, rgb = [ 1, 1, 1 ] ):
    self.EndPoint = [ x, y, z ]
    self.Color = rgb
    self.Hijos = []
    self.Rotacion = [ 0, 0, 0, 1 ]
  # end def

  def AdicionarHijo( self, h, endpoint = True ):
    self.Hijos.append( [ h, endpoint ] )
  # end def

  def Draw( self ):
    glPushMatrix( )
    glRotate( self.Rotacion[ 0 ], self.Rotacion[ 1 ], self.Rotacion[ 2 ], self.Rotacion[ 3 ] )
    glColor3fv( self.Color )
    glBegin( GL_LINES )
    glVertex3f( 0, 0, 0 )
    glVertex3fv( self.EndPoint )
    glEnd( )

    for h, endpoint in self.Hijos:
      glPushMatrix( )
      if endpoint:
        glTranslate( self.EndPoint[ 0 ], self.EndPoint[ 1 ], self.EndPoint[ 2 ] )
      # end if
      h.Draw( )
      glPopMatrix( )
    # end for

    glPopMatrix( )
  # end def

  def Rotate( self, eje, angulo ):
    if eje == 'x':
      self.Rotacion = [ angulo, 1, 0, 0 ]
    elif eje == 'y':
      self.Rotacion = [ angulo, 0, 1, 0 ]
    else:
      self.Rotacion = [ angulo, 0, 0, 1 ]
    # end if
  # end def

# end class

class StickMan:
  def __init__( self ):
    self.Models = {}
    self.Models[ "tronco" ] = Articulacion( 0, 7, 0 )
    self.Models[ "brazo_der" ] = Articulacion( 4, 0, 0, [ 1, 1, 0 ] )
    self.Models[ "antebrazo_der" ] = Articulacion( 3, 0, 0, [ 1, 0, 1 ] )
    self.Models[ "brazo_izq" ] = Articulacion( -4, 0, 0, [ 0, 1, 1 ] )
    self.Models[ "antebrazo_izq" ] = Articulacion( -3, 0, 0, [ 0, 1, 0 ] )
    self.Models[ "mano_der" ] = Articulacion(  2, 0, 0, [ 1, 0, 0 ] )
    self.Models[ "mano_izq" ] = Articulacion( -2, 0, 0, [ 0, 0, 1 ] )
    self.Models[ "falange_sup_der" ] = Articulacion( 0,  2, 0, [ 1, 1, 1 ] )
    self.Models[ "falange_inf_der" ] = Articulacion( 0, -2, 0, [ 1, 1, 1 ] )
    self.Models[ "falange_sup_izq" ] = Articulacion( 0,  2, 0, [ 1, 1, 1 ] )
    self.Models[ "falange_inf_izq" ] = Articulacion( 0, -2, 0, [ 1, 1, 1 ] )
    self.Models[ "cabeza" ] = Cabeza( 0, 3, 0, [ 1, 1, 1 ] )

    self.Models[ "dedo_sup_der" ] = Articulacion( 2,  0, 0, [ 1, 1, 1 ] )
    self.Models[ "dedo_inf_der" ] = Articulacion( 2,  0, 0, [ 1, 1, 1 ] )
    self.Models[ "dedo_sup_izq" ] = Articulacion( -2, 0, 0, [ 1, 1, 1 ] )
    self.Models[ "dedo_inf_izq" ] = Articulacion( -2, 0, 0, [ 1, 1, 1 ] )

    self.Models[ "cuello" ] = Articulacion( 0, 3, 0 )
    self.Models[ "cadera_der" ] = Articulacion( 3, 0, 0 )
    self.Models[ "cadera_izq" ] = Articulacion( -3, 0, 0 )
    self.Models[ "cadera_media_der" ] = Articulacion( -3, -(math.sqrt(18)), 0 )
    self.Models[ "cadera_media_izq" ] = Articulacion( 3, -(math.sqrt(18)), 0 )
    self.Models[ "femur_der" ] = Articulacion( 0, -4, 0 )
    self.Models[ "femur_izq" ] = Articulacion( 0, -4, 0 )
    self.Models[ "tibia_der" ] = Articulacion( 0, -3, 0 )
    self.Models[ "tibia_izq" ] = Articulacion( 0, -3, 0 )
    self.Models[ "pie_der" ] = Articulacion( 2, 0, 0 )
    self.Models[ "pie_izq" ] = Articulacion( -2, 0, 0 )

    self.Models[ "tronco" ].AdicionarHijo( self.Models[ "brazo_der" ], True )
    self.Models[ "tronco" ].AdicionarHijo( self.Models[ "brazo_izq" ], True )
    self.Models[ "tronco" ].AdicionarHijo( self.Models[ "cadera_der" ], False )
    self.Models[ "tronco" ].AdicionarHijo( self.Models[ "cadera_izq" ], False )
    self.Models[ "tronco" ].AdicionarHijo( self.Models[ "cuello" ], True )    
    self.Models[ "brazo_der" ].AdicionarHijo( self.Models[ "antebrazo_der" ], True )
    self.Models[ "brazo_izq" ].AdicionarHijo( self.Models[ "antebrazo_izq" ], True )
    self.Models[ "antebrazo_der" ].AdicionarHijo( self.Models[ "mano_der" ], True )
    self.Models[ "antebrazo_izq" ].AdicionarHijo( self.Models[ "mano_izq" ], True )
    self.Models[ "mano_der" ].AdicionarHijo( self.Models[ "falange_sup_der" ], True )
    self.Models[ "mano_der" ].AdicionarHijo( self.Models[ "falange_inf_der" ], True )
    self.Models[ "mano_izq" ].AdicionarHijo( self.Models[ "falange_sup_izq" ], True )
    self.Models[ "mano_izq" ].AdicionarHijo( self.Models[ "falange_inf_izq" ], True )

    self.Models[ "falange_sup_der" ].AdicionarHijo( self.Models[ "dedo_sup_der" ], True )
    self.Models[ "falange_inf_der" ].AdicionarHijo( self.Models[ "dedo_inf_der" ], True )
    self.Models[ "falange_sup_izq" ].AdicionarHijo( self.Models[ "dedo_sup_izq" ], True )
    self.Models[ "falange_inf_izq" ].AdicionarHijo( self.Models[ "dedo_inf_izq" ], True )

    self.Models[ "cuello" ].AdicionarHijo( self.Models[ "cabeza" ], True )
    self.Models[ "cadera_der" ].AdicionarHijo( self.Models[ "cadera_media_der" ], True )
    self.Models[ "cadera_izq" ].AdicionarHijo( self.Models[ "cadera_media_izq" ], True )
    self.Models[ "cadera_der" ].AdicionarHijo( self.Models[ "femur_der" ], True )
    self.Models[ "cadera_izq" ].AdicionarHijo( self.Models[ "femur_izq" ], True )
    self.Models[ "femur_der" ].AdicionarHijo( self.Models[ "tibia_der" ], True )
    self.Models[ "femur_izq" ].AdicionarHijo( self.Models[ "tibia_izq" ], True )
    self.Models[ "tibia_der" ].AdicionarHijo( self.Models[ "pie_der" ], True )
    self.Models[ "tibia_izq" ].AdicionarHijo( self.Models[ "pie_izq" ], True )

    self.Raiz = self.Models[ "tronco" ]

  # end def

  def Draw( self ):
    self.Raiz.Draw( )
  # end def

  def Rotate( self, articulacion, eje, angulo ):
    if articulacion in self.Models:
      self.Models[ articulacion ].Rotate( eje, angulo )
    # end if
  # end def

# end class

myModel = StickMan( )

## -------------------------------------------------------------------------
def init( ):
  glClearColor( 0.0, 0.0, 0.0, 0.0 )
  glEnable( GL_DEPTH_TEST )
# end def

## -------------------------------------------------------------------------
def drawOrthoBase( ):
  glPushMatrix( )

  cur_color = glGetFloatv( GL_CURRENT_COLOR )
  lw = glGetFloatv( GL_LINE_WIDTH )

  glLineWidth( 2 )
  glBegin( GL_LINES )

  glColor3f( 1, 0, 0 )
  glVertex3f( 0, 0, 0 )
  glVertex3f( 1, 0, 0 )

  glColor3f( 0, 1, 0 )
  glVertex3f( 0, 0, 0 )
  glVertex3f( 0, 1, 0 )

  glColor3f( 0, 0, 1 )
  glVertex3f( 0, 0, 0 )
  glVertex3f( 0, 0, 1 )

  glEnd( )

  glColor3f( cur_color[ 0 ], cur_color[ 1 ], cur_color[ 2 ] )
  glLineWidth( lw )

  glPopMatrix( )
# end def

## -------------------------------------------------------------------------
def draw( ):
  global myModel

  # -- Clear framebuffer
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

  # -- Draw stuff
  glMatrixMode( GL_MODELVIEW )
  glLoadIdentity( )

  # -- Camera
  gluLookAt( 20, 20, 20, 0, 0, 0, 0, 1, 0 )

  # -- Scene
  drawOrthoBase( )
  myModel.Draw( )

  # -- Prepare next frame
  glutSwapBuffers( )
# end def

## -------------------------------------------------------------------------
def reshape( width, height ):
  # Compute aspect ratio of the new window
  aspect = width
  if height != 0:
    aspect /= height
  # end if

  # Set the viewport to cover the new window
  glViewport( 0, 0, width, height )

  # Compute projection
  glMatrixMode( GL_PROJECTION )
  glLoadIdentity( )
  gluPerspective( 45, aspect, 1e-2, 3000 )
# end def

## -------------------------------------------------------------------------
def keyboard( key, x, y ):
  global camera_angle, camera_pos, camera_height
  if key == b'q' or key == b'Q':
    sys.exit( 0 )
  # end if
# end def

## -------------------------------------------------------------------------
## ---------------------------------- MAIN ---------------------------------
## -------------------------------------------------------------------------

# Prepare window
glutInit( )
glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH )
glutInitWindowSize( 700, 700 )
glutInitWindowPosition( 0, 0 )
wind = glutCreateWindow( "An OBJ viewer" )

# Prepare OpenGL
init( )

myModel.Rotate( "antebrazo_der", "z", -67 )
myModel.Rotate( "mano_der", "y", -235 )
myModel.Rotate( "brazo_izq", "y", 90 )

# Associate callbacks
glutDisplayFunc( draw )
glutReshapeFunc( reshape )
glutKeyboardFunc( keyboard )

# Main loop
glutMainLoop( )

## eof - ShowOBJ.py

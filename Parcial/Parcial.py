## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================
## Install OpenGL: pip3 install PyOpenGL PyOpenGL_accelerate
## =========================================================================

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math, sys, re, random, glm
#from PIL import Image

## -------------------------------------------------------------------------
## Some global iables: DON'T DO THIS IN REAL LIFE APPLICATIONS!!!!
## -------------------------------------------------------------------------

class RotationMatrix:

  def getRotationResult( self, angles, vector):

    pi = math.atan( 1.0 ) * 4.0
    convertion = pi/180
    result = vector.copy( )
    result = [0, 0, 0]
    cont = len(angles) - 1
    #cont = 0
    for angle in angles:        
      result[0] += angles.copy()[cont][0][0]
      result[1] += angles.copy()[cont][0][1]
      result[2] += angles.copy()[cont][0][2] 
      result = glm.rotateZ(result, angles[cont][1][2][0] * convertion)
      result = glm.rotateY(result, angles[cont][1][1][0] * convertion)
      result = glm.rotateX(result, angles[cont][1][0][0] * convertion)                           
      cont -= 1
    # end for
    result[1] += vector[1]
    return result
  #end def

# end class

class ReaderFile:

  def __init__( self, filename ):
    self.joints = []
    self.read( filename )
    self.image = None        
    #self.readHelpImage()
  # end def

  def read( self, filename ):
    file_stream = open( filename, "r" )
    lines = file_stream.readlines( )
    n = int(lines[0])

    if n <= 1 and n >= 10:
      print("The number of joints must be between 2 and 9")
      exit()
    # end if
    
    joints = list( filter( None, re.split( " ", lines[1] ) ) )

    if len(joints) != n:
      print("The number of joints must match with the lengths")
      exit()
    # end if

    self.joints = [int(joint) for joint in joints]
  # end def

  #def readHelpImage( self ):
  #  self.image = Image.open("Ayuda1.png")
  # end def

  #def printHelpImage( self ):
  #  img_data = self.image.convert("RGBA").tobytes()    
  #  glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.image.width, self.image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
  # end def

  def getValues( self ):
    return self.joints
  # end def

# end class

class OpenGLObject:

  def __init__( self ):
    self.rotateInfo = [
      [ 0, 1, 0, 0 ],
      [ 0, 0, 1, 0 ],
      [ 0, 0, 0, 1 ]
    ]
    self.traslateInfo = [ 0, 0, 0 ]
    self.traslateFlag = False
    self.scaleInfo = [ 1, 1, 1 ]
  # end def

  def rotate( self, eje, angulo ):
    if eje == 'x':
      self.rotateInfo[0] = [ self.rotateInfo[0][0] + angulo, 1, 0, 0 ]
    elif eje == 'y':
      self.rotateInfo[1] = [ self.rotateInfo[1][0] + angulo, 0, 1, 0 ]
    else:
      self.rotateInfo[2] = [ self.rotateInfo[2][0] + angulo, 0, 0, 1 ]
    # end if
  # end def

  def traslate( self, x, y, z ):
    self.traslateInfo = [ self.traslateInfo[0] + x, self.traslateInfo[1] + y, self.traslateInfo[2] + z ]
    self.traslateFlag = True
  # end def

  def scale( self, x, y, z ):
    self.scaleInfo = [ x, y, z ]
  # end def

# end class

class Floor:
  def __init__( self, length, y, rgb = [1, 1, 1] ):    
    self.length = length * 1.2
    self.position = y - self.length
    self.Color = rgb
  # end def

  def Draw( self ):
    glPushMatrix( )
    glBegin(GL_QUADS)
    glColor3fv(self.Color)
    glVertex3f( self.length, self.position,  self.length)    
    glVertex3f( self.length, self.position,  -self.length)
    glVertex3f( -self.length, self.position,  -self.length)
    glVertex3f( -self.length, self.position,  self.length)    
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f( self.length, self.position - 2,  self.length)    
    glVertex3f( self.length, self.position - 2,  -self.length)
    glVertex3f( -self.length, self.position - 2,  -self.length)
    glVertex3f( -self.length, self.position - 2,  self.length)
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f( self.length, self.position,  self.length) 
    glVertex3f( self.length, self.position - 2,  self.length)        
    glVertex3f( self.length, self.position - 2,  -self.length)
    glVertex3f( self.length, self.position,  -self.length)   
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f( -self.length, self.position,  -self.length) 
    glVertex3f( -self.length, self.position - 2,  -self.length)        
    glVertex3f( -self.length, self.position - 2,  self.length)
    glVertex3f( -self.length, self.position,  self.length)   
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f( -self.length, self.position,  -self.length) 
    glVertex3f( -self.length, self.position - 2,  -self.length)        
    glVertex3f( self.length, self.position - 2,  -self.length)
    glVertex3f( self.length, self.position,  -self.length)   
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f( self.length, self.position,  self.length) 
    glVertex3f( self.length, self.position - 2,  self.length)        
    glVertex3f( -self.length, self.position - 2,  self.length)
    glVertex3f( -self.length, self.position,  self.length)   
    glEnd()
    glPopMatrix( )
  # end def

# end class

class Sphere( OpenGLObject ):
  def __init__( self, length, rgb = [1, 1, 1] ):
    OpenGLObject.__init__( self )
    self.radius = length * 0.05
    randRadius = random.randint( int(length*0.3), length ) - (2 * self.radius)
    randPhi = random.randint( 0, 100 )    
    randTheta = random.randint( 0, 100 )          
    self.Center = [ 
      randRadius * math.cos( randPhi ) * math.cos( randTheta ), 
      randRadius * math.cos( randPhi ) * math.sin( randTheta ) + 10,
      randRadius * math.sin( randPhi )
    ]
    self.Color = rgb
    self.calculatePoints( self.Center )
    self.isFalling = False
    self.isGrabbed = False
  # end def

  def Draw( self ):
    glPushMatrix( )
    if self.traslateFlag:
      glTranslatef(self.traslateInfo[0], self.traslateInfo[1], self.traslateInfo[2])

    for rotate in self.rotateInfo:
      glRotate( rotate[ 0 ], rotate[ 1 ], rotate[ 2 ], rotate[ 3 ] )    
    # end for

    glRotate( rotate[ 0 ], rotate[ 1 ], rotate[ 2 ], rotate[ 3 ] )    
    glScalef(self.scaleInfo[0], self.scaleInfo[0], self.scaleInfo[0])
    glColor3fv( self.Color )
    self.drawSphere( )
    glPopMatrix( )
  # end def

  def calculatePoints( self, center ):
    self.points = []
    pi = math.atan( 1.0 ) * 4.0
    r = self.radius
    for s_phi in range(0, 100):
      phi = (pi * ( s_phi / 100 )) - (pi * 0.5)
      for s_theta in range(0, 100):
        theta = (2 * pi * s_theta / 100) - pi
        self.points.append([
          r * math.cos( phi ) * math.cos( theta ) + center[0],
          r * math.cos( phi ) * math.sin( theta ) + center[1],
          r * math.sin( phi ) + center[2]
        ])
      # end for
    # end for
  # end def

  def drawSphere( self ):
    
    glBegin( GL_POINTS )
    for point in self.points:
        glVertex3f( point[0], point[1], point[2] )
    # end for
    glEnd( )
  # end def

  def setCenter( self, center ):
    self.Center = center
    self.calculatePoints(center)
  # end def

  def grab( self, center ):
    self.Center = center
    self.calculatePoints([0,0,0])

  def isInContact( self, point ):
    distance = math.sqrt( math.pow(self.Center[0] - point[0], 2) 
    + math.pow(self.Center[1] - point[1], 2) 
    + math.pow(self.Center[2] - point[2], 2) )
    return distance < self.radius

  # end def

# end class

class Articulacion( OpenGLObject ):
  def __init__( self, x, y, z, rgb = [ 1, 1, 1 ]):
    OpenGLObject.__init__( self )
    self.EndPoint = [ x, y, z ]
    self.Color = rgb
    self.Hijos = []
  # end def

  def AdicionarHijo( self, h ):
    self.Hijos.append( h )
  # end def

  def RemoverHijo( self ):
    self.Hijos.clear()
  # end def

  def Draw( self ):
    glPushMatrix( )

    for rotate in self.rotateInfo:
      glRotate( rotate[ 0 ], rotate[ 1 ], rotate[ 2 ], rotate[ 3 ] )    
    # end for  

    glColor3fv( self.Color )
    glBegin( GL_LINES )
    glVertex3f( 0, 0, 0 )
    glVertex3fv( self.EndPoint )
    glEnd( )

    for h in self.Hijos:
      glPushMatrix( )
      glTranslate( self.EndPoint[ 0 ], self.EndPoint[ 1 ], self.EndPoint[ 2 ] )
      h.Draw( )
      glPopMatrix( )
    # end for

    glPopMatrix( )
  # end def

# end class

class Robot:
  def __init__( self, filename, y ):

    reader = ReaderFile( filename )

    self.rotationMatrix = RotationMatrix()

    self.totalLength = 0
    self.initialHeight = y    

    colors = [      
      [1, 1, 0],
      [1, 0, 1],
      [0, 1, 1],
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1],
      [0.2, 1, 0.94],
      [1, 0.63, 0.2],
      [1, 0.2, 0.41]
    ]

    self.Models = {}
    cont = 1    
    for joint in reader.getValues():
      self.Models[cont] = Articulacion( joint, 0, 0, colors[cont-1])    
      self.totalLength += joint
      if cont > 1:
        self.Models[cont-1].AdicionarHijo( self.Models[cont] )
      # end if
      cont += 1
    # end for

    self.Raiz = self.Models[ 1 ]
    
    self.initialPoint = [self.totalLength, y, 0]

  # end def

  def Draw( self ):   
    glPushMatrix()
    glTranslatef(0, self.initialHeight, 0) 
    self.Raiz.Draw( )
    glPopMatrix()
  # end def

  def Rotate( self, articulacion, eje, angulo ):
    if articulacion in self.Models:
      self.Models[ articulacion ].rotate( eje, angulo )
    else:
      print("There isn't a joint with number ", articulacion)
    # end if
  # end def

  def getFinalPosition( self ):
    angles = []
    for joint in range( 1, len(self.Models) + 1 ):
      if hasattr(self.Models[joint],'EndPoint'):
        point = self.Models[joint].EndPoint
      else:
        point = [0,0,0]
      angles.append([point, self.Models[joint].rotateInfo])
    # end for
    return self.rotationMatrix.getRotationResult(angles, self.initialPoint)
  # end def

  def grabSphere( self, sphere ):
    lastKey = list(self.Models)[-1]
    finalPoint = self.getFinalPosition()
    if sphere.isInContact( finalPoint ):
      self.Models[lastKey + 1] = sphere
      self.Models[lastKey].AdicionarHijo( sphere )
      sphere.grab( finalPoint )
      sphere.isGrabbed = True
    # end if
  # end def

  def dropSphere( self, sphere ):
    lastKey = list(self.Models)[-1]
    self.Models[lastKey - 1].RemoverHijo( )
    sphere.isGrabbed = False
    sphere.isFalling = True
    sphere.setCenter(self.getFinalPosition())
    self.Models.pop(lastKey)
    # end if
  # end def

# end class

if len(sys.argv) < 2:
  print("Please give the input file as a parameter")
  exit()
# end if

## -------------------------------------------------------------------------
def init( ):
  global camera_pos, camera_angle, camera_height, center
    
  glClearColor( 0.0, 0.0, 0.0, 0.0 )
  glEnable( GL_DEPTH_TEST )

  camera_angle = 0
  camera_height = 2
  camera_pos = 50.0
  center = [0, 10, 0]

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
  global myModel, camera_pos, camera_angle, camera_height, center, floor, sphere

  # -- Clear framebuffer
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

  # -- Draw stuff
  glMatrixMode( GL_MODELVIEW )
  glLoadIdentity( )

  # -- Camera
  camera_z = camera_pos * math.cos( camera_angle )
  camera_x = camera_pos * math.sin( camera_angle )
  gluLookAt( camera_x, camera_height, camera_z, center[0], center[1], center[2], 0, 1, 0 )

  # -- Scene
  drawOrthoBase( )

  # -- Floor
  floor.Draw()

  # -- Robot
  myModel.Draw( )

  # -- Sphere
  if not sphere.isGrabbed:
    sphere.Draw()

  #reader.printHelpImage()

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
  global camera_angle, camera_pos, camera_height, camera_style, rotationInfo, myModel, floor, sphere
  if key == b'q' or key == b'Q':
    sys.exit( 0 )
  elif key == b'a' or key == b'A':
    camera_angle -= 1e-1
    glutPostRedisplay( )
  elif key == b'd' or key == b'D':
    camera_angle += 1e-1
    glutPostRedisplay( )
  elif key == b'w' or key == b'W':
    camera_pos -= 2e-1
    glutPostRedisplay( )
  elif key == b's' or key == b'S':
    camera_pos += 2e-1
    glutPostRedisplay( )
  elif key == b'v' or key == b'V':
    camera_height -= 1
    glutPostRedisplay( )
  elif key == b'c' or key == b'C':
    camera_height += 1
    glutPostRedisplay( )
  elif key == b'1':    
    rotationInfo['jointToMove'] = 1
    rotationInfo['axisToMove'] = None
  elif key == b'2':    
    rotationInfo['jointToMove'] = 2
    rotationInfo['axisToMove'] = None
  elif key == b'3':    
    rotationInfo['jointToMove'] = 3
    rotationInfo['axisToMove'] = None
  elif key == b'4':    
    rotationInfo['jointToMove'] = 4
    rotationInfo['axisToMove'] = None
  elif key == b'5':    
    rotationInfo['jointToMove'] = 5
    rotationInfo['axisToMove'] = None
  elif key == b'6':    
    rotationInfo['jointToMove'] = 6
    rotationInfo['axisToMove'] = None
  elif key == b'7':    
    rotationInfo['jointToMove'] = 7
    rotationInfo['axisToMove'] = None
  elif key == b'8':    
    rotationInfo['jointToMove'] = 8
    rotationInfo['axisToMove'] = None
  elif key == b'9':    
    rotationInfo['jointToMove'] = 9
    rotationInfo['axisToMove'] = None
  elif key == b'x' or key == b'X':
    if rotationInfo['jointToMove'] != 0:
      rotationInfo['axisToMove'] = 'x'
  elif key == b'y' or key == b'Y':
    if rotationInfo['jointToMove'] != 0:
      rotationInfo['axisToMove'] = 'y'
  elif key == b'z' or key == b'Z':
    if rotationInfo['jointToMove'] != 0:
      rotationInfo['axisToMove'] = 'z'
  elif key == b'+':
    if rotationInfo['axisToMove'] is not None :
      myModel.Rotate(rotationInfo['jointToMove'], rotationInfo['axisToMove'], 5)
      glutPostRedisplay( )
  elif key == b'-':
    if rotationInfo['axisToMove'] is not None :
      myModel.Rotate(rotationInfo['jointToMove'], rotationInfo['axisToMove'], -5)
      glutPostRedisplay( )
  elif key == b'p' or key == b'P':
    if sphere.isGrabbed: 
      myModel.dropSphere( sphere )
      initFallingInfo()
    else:
      myModel.grabSphere( sphere )
    glutPostRedisplay( )
  elif key == b'r' or key == b'R':
    myModel = Robot( sys.argv[ 1 ], 10 )  
    glutPostRedisplay( )
  elif key == b'm' or key == b'M':
    if camera_style == 0:
      camera_height = floor.position + 1
      camera_pos = myModel.totalLength * 5
      camera_style = 1
    else:
      camera_height = 2
      camera_pos = 50.0
      camera_style = 0
    glutPostRedisplay( )
  elif key == b'b' or key == b'B':
    sphere = Sphere(myModel.totalLength, [ 1, 1, 0 ])
    glutPostRedisplay( )
# end def

## -------------------------------------------------------------------------
def mouse_click( button, state, x, y ):
  global center, draggingInfo, camera_angle
  if button == GLUT_LEFT_BUTTON:
    if state == GLUT_DOWN:
      draggingInfo['dragging'] = True
      draggingInfo['drag_x_origin'] = x
      draggingInfo['drag_y_origin'] = y
    else:
      draggingInfo['dragging'] = False
      center[0] = draggingInfo['movement_h'] * math.cos( camera_angle )
      center[1] = draggingInfo['movement_v']
      center[2] = draggingInfo['movement_h'] * math.sin( camera_angle )
  # end if
# end def

def mouse_move( x, y ):
  global draggingInfo
  if draggingInfo['dragging']:
      draggingInfo['movement_v'] += (y - draggingInfo['drag_y_origin']) *0.3
      draggingInfo['movement_h'] += (x - draggingInfo['drag_x_origin'])*0.3
      draggingInfo['drag_x_origin'] = x
      draggingInfo['drag_y_origin'] = y
  # end if
# end def

## -------------------------------------------------------------------------

def fall( value ):
  global floor, sphere, fallingInfo, myModel

  if sphere.isFalling:
    gravity = fallingInfo['gravity']
    time = fallingInfo['time']
    vi = fallingInfo['vi']
    vi += gravity
    sphere.traslate( 0, -vi, 0 )
    fallingInfo['distance'] -= vi
    fallingInfo['vi'] = vi
    fallingInfo['time'] -= 1
    if fallingInfo['distance'] <= 0:
      fallingInfo['isBouncing'] = True
      fallingInfo['vi'] *= 0.8
      fallingInfo['time'] = fallingInfo['vi'] / fallingInfo['gravity']
      bounce( 0 )
  # end if

  if fallingInfo['isBouncing'] != True:
    glutTimerFunc( int(1000/30), fall, 1 )
    glutPostRedisplay( )
# end def

## -------------------------------------------------------------------------

def bounce( value ):
  global floor, sphere, fallingInfo  
  if sphere.isFalling:
    vi = fallingInfo['vi']
    gravity = fallingInfo['gravity']
    vi -= gravity
    sphere.traslate( 0, vi, 0 )
    fallingInfo['distance'] += vi
    fallingInfo['vi'] = vi
    fallingInfo['time'] = vi / gravity
    if fallingInfo['vi'] <= 0:
      fallingInfo['isBouncing'] = False
      if fallingInfo['distance'] > 0:
        fallingInfo['time'] = math.sqrt( 2 * fallingInfo['distance'] / fallingInfo['gravity'] )         
        fall( 0 )
      else:
        initFallingInfo( )
        sphere.isFalling = False
        sphere.Center[1] = floor.position + sphere.radius
  # end if
  if fallingInfo['isBouncing']:
    glutTimerFunc( int(1000/30), bounce, 1 )
    glutPostRedisplay( )
# end def

## -------------------------------------------------------------------------

def initFallingInfo( ):
  global floor, sphere, fallingInfo
  fallingInfo['gravity'] = 0.05
  distance = sphere.Center[1] - (floor.position + sphere.radius)
  fallingInfo['distance'] = distance
  time = math.sqrt( 2 * distance / fallingInfo['gravity'] )
  fallingInfo['time'] = int(time)
  if sphere.isFalling:
    fall(1)
# end def

## -------------------------------------------------------------------------
## ---------------------------------- MAIN ---------------------------------
## -------------------------------------------------------------------------

# Prepare window
glutInit( )
glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH )
glutInitWindowSize( 700, 700 )
glutInitWindowPosition( 0, 0 )
wind = glutCreateWindow( "Parcial Brazo Robotico" )

myModel = Robot( sys.argv[ 1 ], 10 )

camera_angle  = 0
camera_pos    = 0
camera_height = 0
camera_style = 0

center = []

reader = ReaderFile('input.txt')

rotationInfo = {
  'jointToMove' : 0,
  'axisToMove' : None
}

fallingInfo = {
  'gravity' : 0.05,
  'distance' : 0,
  'time' : 0,
  'vi' : 0,
  'isBouncing': False
}

draggingInfo = {
  'movement_v': 0,
  'movement_h': 0,
  'drag_x_origin': 0,
  'drag_y_origin': 0,
  'dragging': False,
}

floor = Floor( myModel.totalLength, myModel.initialHeight )

sphere = Sphere( myModel.totalLength, [ 1, 1, 0 ] )

# Prepare OpenGL
init( )

# Associate callbacks
glutDisplayFunc( draw )
glutReshapeFunc( reshape )
glutKeyboardFunc( keyboard )
glutMouseFunc( mouse_click )
glutMotionFunc( mouse_move )

# Main loop
glutMainLoop( )

## eof - ShowOBJ.py

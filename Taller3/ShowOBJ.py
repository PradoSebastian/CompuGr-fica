## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================
## Install OpenGL: pip3 install PyOpenGL PyOpenGL_accelerate
## =========================================================================

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Museum import *
import math, sys
import numpy as np

## -------------------------------------------------------------------------
## Some global variables: DON'T DO THIS IN REAL LIFE APPLICATIONS!!!!
## -------------------------------------------------------------------------
camera_angle  = 0
camera_pos    = 0
camera_height = 0
museum = None

cube_geometry = np.array([
  [ -1, -1,  1 ], [  1, -1,  1 ], [  1, -1, -1 ], [ -1, -1, -1 ],
  [ -1,  1,  1 ], [  1,  1,  1 ], [  1,  1, -1 ], [ -1,  1, -1 ]
  ])
cube_topology = [
  [ 0, 1, 3 ], [ 1, 2, 3 ],
  [ 1, 5, 2 ], [ 5, 6, 2 ],
  [ 4, 7, 5 ], [ 7, 6, 5 ],
  [ 2, 6, 7 ], [ 7, 3, 2 ],
  [ 3, 7, 4 ], [ 0, 3, 4 ],
  [ 1, 0, 4 ], [ 1, 4, 5 ]
  ]

## -------------------------------------------------------------------------
def init( ):
  global camera_angle, camera_pos, camera_height

  camera_angle = 0
  camera_height = 0
  camera_pos = 30.0

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

def drawCube( size ):
  global cube_geometry, cube_topology

  auxGeo = cube_geometry * size

  glColor3f( 1, 1, 1 )
  for t in cube_topology:
    glBegin( GL_LINE_LOOP )
    glVertex3fv( auxGeo[ t[ 0 ] ])
    glVertex3fv( auxGeo[ t[ 1 ] ])
    glVertex3fv( auxGeo[ t[ 2 ] ])
    glEnd( )
  # end for
# end def

## -------------------------------------------------------------------------

def draw( ):
  global camera_angle, camera_pos, camera_height, museum

  # -- Clear framebuffer
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

  # -- Draw stuff
  glMatrixMode( GL_MODELVIEW )  
  glLoadIdentity( )

  # -- Camera
  camera_z = camera_pos * math.cos( camera_angle )
  camera_x = camera_pos * math.sin( camera_angle )
  gluLookAt( camera_x, camera_height, camera_z, 0, 0, 0, 0, 1, 0 )

  # -- Scene
  drawOrthoBase( )

  # -- Museum
  museum.Draw()

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
    exit( )
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
  elif key == b'z' or key == b'Z':
    camera_height -= 1
    glutPostRedisplay( )
  elif key == b'c' or key == b'C':
    camera_height += 1
    glutPostRedisplay( )
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

museum = Museum( 10, 0 )

# Prepare OpenGL
init( )

# Associate callbacks
glutDisplayFunc( draw )
glutReshapeFunc( reshape )
glutKeyboardFunc( keyboard )

# Main loop
glutMainLoop( )

## eof - ShowOBJ.py

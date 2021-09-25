/* -------------------------------------------------------------------------
 * @author Leonardo Fl�rez-Valencia (florez-l@javeriana.edu.co)
 * -------------------------------------------------------------------------
 */

#include <GL/glut.h>
#include <cmath>
#include <iostream>

#include "Camera.h"

// -------------------------------------------------------------------------
Camera myCamera;

// -------------------------------------------------------------------------
void initWorld( int argc, char* argv[] );

void drawBase( );

// -------------------------------------------------------------------------
void displayCbk( );
void resizeCbk( int w, int h );
void keyboardCbk( unsigned char key, int x, int y );
void mouseClickCbk( int button, int state, int x, int y );
void mouseMoveCbk( int x, int y );

// -------------------------------------------------------------------------
int main( int argc, char* argv[] )
{
  // Init OpenGL context
  glutInit( &argc, argv );
  glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB );
  glutInitWindowPosition( 50, 50 );
  glutInitWindowSize( 1024, 768 );
  glutCreateWindow( "Example!" );

  // Init world
  try
  {
    initWorld( argc, argv );

    glutDisplayFunc( displayCbk );
    glutReshapeFunc( resizeCbk );
    glutKeyboardFunc( keyboardCbk );
    glutMouseFunc( mouseClickCbk );
    glutMotionFunc( mouseMoveCbk );
    glutMainLoop( );

    return( 0 );
  }
  catch( std::exception& err )
  {
    std::cerr << err.what( ) << std::endl;
    return( 1 );
  } // end if
}

// -------------------------------------------------------------------------
void initWorld( int argc, char* argv[] )
{
  // Initialize camera
  myCamera.setFOV( 45 );
  myCamera.setPlanes( 1e-2, 100 );
  myCamera.move( Vector( 0, 0, 15 ) );
  myCamera.lookAt( Vector( 0, 0, 0 ) );

  // OpenGL initialization
  glClearColor( 0, 0, 0, 0 );
}

// -------------------------------------------------------------------------
void drawBase( )
{
  glBegin( GL_LINES );
  {
    glColor3f( 1, 0, 0 );
    glVertex3f(  0, 0, 0 );
    glVertex3f( 10, 0, 0 );

    glColor3f( 0, 1, 0 );
    glVertex3f( 0,  0, 0 );
    glVertex3f( 0, 10, 0 );

    glColor3f( 0, 0, 1 );
    glVertex3f( 0, 0,  0 );
    glVertex3f( 0, 0, 10 );
  }
  glEnd( );
}

// -------------------------------------------------------------------------

void displayCbk( )
{
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );
  glMatrixMode( GL_MODELVIEW );
  glLoadIdentity( );

  // Prepare model matrix
  myCamera.loadCameraMatrix( );

  // Show base
  drawBase( );

  // Show a sphere
  glColor3f( 1, 1, 1 );
  glutWireSphere( 1, 10, 10 );

  //glColor3f( 1, 1, 0 );

  //glutWireCube( 1 );
  // glutWireCone( 1, 1, 10, 10 );
  // glutWireTorus( 0.1, 1, 10, 10 );
  // glutWireTetrahedron( );
  // glutWireOctahedron( );
  // glutWireDodecahedron( );
  // glutWireIcosahedron( );
  // glutWireTeapot( 1 );

  // Finish
  glutSwapBuffers( );
}

// -------------------------------------------------------------------------
void resizeCbk( int w, int h )
{
  glMatrixMode( GL_PROJECTION );
  glLoadIdentity( );
  myCamera.setWindow( w, h );
  myCamera.loadProjectionMatrix( );
}

// -------------------------------------------------------------------------
void keyboardCbk( unsigned char key, int x, int y )
{
  switch( key ) 
  {
  case 'w': case 'W':
  {
    myCamera.forward( 1 ) ;
    glutPostRedisplay( );
  }
  break;
     case 's': case 'S':
     {
       myCamera.forward( -1 ) ;
       glutPostRedisplay( );
     }
     break;
  case 'a': case 'A':
  {
    myCamera.strafe( -1 ) ;
    glutPostRedisplay( );
  }
  break;
  case 'd': case 'D':
  {
    myCamera.strafe( 1 ) ;
    glutPostRedisplay( );
  }
  break;
  case 27: // ESC
    std::exit( 0 );
    break;
  default:
    break;
  } // end switch
}

// -------------------------------------------------------------------------
void mouseClickCbk( int button, int state, int x, int y )
{
  if( state == GLUT_DOWN )
    myCamera.setReference( x, y );
  else
    myCamera.setReference( 0, 0 );
}

// -------------------------------------------------------------------------
void mouseMoveCbk( int x, int y )
{
  int dx, dy;
  myCamera.getReference( dx, dy, x, y );
  myCamera.setReference( x, y );

  // Apply rotations
  if( dx > 0 )      myCamera.rotY( -0.5 );
  else if( dx < 0 ) myCamera.rotY( 0.5 );
  if( dy > 0 )      myCamera.rotX( 0.5 );
  else if( dy < 0 ) myCamera.rotX( -0.5 );

  // Redraw
  glutPostRedisplay( );
}

// eof - SolarSystem.cxx

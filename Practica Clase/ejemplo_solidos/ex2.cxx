/* -------------------------------------------------------------------------
 * @author Leonardo Flórez-Valencia (florez-l@javeriana.edu.co)
 * -------------------------------------------------------------------------
 */

#include <GL/glut.h>
#include <cmath>
#include <iostream>

#include "Camera.h"

// -------------------------------------------------------------------------
Camera myCamera;
GLUquadricObj* myObject = nullptr;

// -------------------------------------------------------------------------
void initWorld( int argc, char* argv[] );
void destroyWorld( );

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

    destroyWorld( );
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

  // Create quadric
  myObject = gluNewQuadric( );
  gluQuadricDrawStyle( myObject, GLU_LINE );
  // gluQuadricDrawStyle( myObject, GLU_FILL );
  // gluQuadricDrawStyle( myObject, GLU_SILHOUETTE );
  // gluQuadricDrawStyle( myObject, GLU_POINT );
}

// -------------------------------------------------------------------------
void destroyWorld( )
{
  if( myObject != nullptr )
    gluDeleteQuadric( myObject );
  myObject = nullptr;
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

  // Show a quadric
  glColor3f( 1, 1, 0 );
  gluSphere( myObject, 1, 10, 10 );
  // gluCylinder( myObject, 1, 1, 1, 10, 10 );
  // gluDisk( myObject, 0.5, 1, 10, 10 );

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
    myCamera.forward( 0.1 ) ;
    glutPostRedisplay( );
  }
  break;
     case 's': case 'S':
     {
       myCamera.forward( -0.1 ) ;
       glutPostRedisplay( );
     }
     break;
  case 'a': case 'A':
  {
    myCamera.strafe( -0.1 ) ;
    glutPostRedisplay( );
  }
  break;
  case 'd': case 'D':
  {
    myCamera.strafe( 0.1 ) ;
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
  if( dx > 0 )      myCamera.rotY( -0.1 );
  else if( dx < 0 ) myCamera.rotY( 0.1 );
  if( dy > 0 )      myCamera.rotX( 0.1 );
  else if( dy < 0 ) myCamera.rotX( -0.1 );

  // Redraw
  glutPostRedisplay( );
}

// eof - SolarSystem.cxx

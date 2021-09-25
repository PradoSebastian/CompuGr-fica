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

GLuint myDisplayLists = 0;
GLUquadricObj* myObject = nullptr;

// -------------------------------------------------------------------------
void initWorld( int argc, char* argv[] );
void destroyWorld( );

GLuint createStaticObjects( );
void drawBase( );

// -------------------------------------------------------------------------
void drawSphere( double r, unsigned int PHI_SAMPLES, unsigned int THETA_SAMPLES )
{
  glBegin( GL_POINTS );
  for( unsigned int s_phi = 0; s_phi <= PHI_SAMPLES; ++s_phi )
  {
    double phi = ( _PI * double( s_phi ) / double( PHI_SAMPLES ) ) - ( _PI * 0.5 );
    for( unsigned int s_theta = 0; s_theta <= THETA_SAMPLES; ++s_theta )
    {
      double theta = ( 2.0 * _PI * double( s_theta ) / double( THETA_SAMPLES ) ) - _PI;
      glVertex3f(
        r * std::cos( phi ) * std::cos( theta ),
        r * std::cos( phi ) * std::sin( theta ),
        r * std::sin( phi )
        );
    } // end for
  } // end for
  glEnd( );
}

// -------------------------------------------------------------------------
void drawEllipsoid( double rx, double ry, double rz, unsigned int PHI_SAMPLES, unsigned int THETA_SAMPLES )
{
  glBegin( GL_POINTS );
  for( unsigned int s_phi = 0; s_phi <= PHI_SAMPLES; ++s_phi )
  {
    double phi = ( _PI * double( s_phi ) / double( PHI_SAMPLES ) ) - ( _PI * 0.5 );
    for( unsigned int s_theta = 0; s_theta <= THETA_SAMPLES; ++s_theta )
    {
      double theta = ( 2.0 * _PI * double( s_theta ) / double( THETA_SAMPLES ) ) - _PI;
      glVertex3f(
        rx * std::cos( phi ) * std::cos( theta ),
        ry * std::cos( phi ) * std::sin( theta ),
        rz * std::sin( phi )
        );
    } // end for
  } // end for
  glEnd( );
}

// -------------------------------------------------------------------------
void drawTorus( double ra, double r, unsigned int PHI_SAMPLES, unsigned int THETA_SAMPLES )
{
  glBegin( GL_POINTS );
  for( unsigned int s_phi = 0; s_phi <= PHI_SAMPLES; ++s_phi )
  {
    double phi = ( 2.0 * _PI * double( s_phi ) / double( PHI_SAMPLES ) ) - _PI;
    for( unsigned int s_theta = 0; s_theta <= THETA_SAMPLES; ++s_theta )
    {
      double theta = ( 2.0 * _PI * double( s_theta ) / double( THETA_SAMPLES ) ) - _PI;
      glVertex3f(
        ( ra + r * std::cos( phi ) ) * std::cos( theta ),
        ( ra + r * std::cos( phi ) ) * std::sin( theta ),
        r * std::sin( phi )
        );
    } // end for
  } // end for
  glEnd( );
}

// -------------------------------------------------------------------------
void drawRose( double a, double m, double n, double k, unsigned int PHI_SAMPLES, unsigned int THETA_SAMPLES )
{
  glBegin( GL_POINTS );
  for( unsigned int s_phi = 0; s_phi <= PHI_SAMPLES; ++s_phi )
  {
    double phi = ( 2.0 * _PI * double( s_phi ) / double( PHI_SAMPLES ) ) - _PI;
    for( unsigned int s_theta = 0; s_theta <= THETA_SAMPLES; ++s_theta )
    {
      double theta = ( 2.0 * _PI * double( s_theta ) / double( THETA_SAMPLES ) ) - _PI;
      glVertex3f(
        a * std::cos( m * phi ) * std::pow( std::cos( n * theta ), k ) * std::cos( phi ) * std::cos( theta ),
        a * std::cos( m * phi ) * std::pow( std::cos( n * theta ), k ) * std::sin( phi ) * std::cos( theta ),
        a * std::cos( m * phi ) * std::pow( std::cos( n * theta ), k ) * std::sin( theta )
         );
    } // end for
  } // end for
  glEnd( );
}

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

  // Create display lists
  myDisplayLists = createStaticObjects( );
}

// -------------------------------------------------------------------------
void destroyWorld( )
{
  if( myObject != nullptr )
    gluDeleteQuadric( myObject );
  myObject = nullptr;
}

// -------------------------------------------------------------------------
GLuint createStaticObjects( )
{
  GLuint id = 0;
  id = glGenLists( 2 );

  // First list
  glNewList( id, GL_COMPILE );
  {
    drawBase( );
  }
  glEndList( );

  // Second list
  glNewList( id + 1, GL_COMPILE );
  {
    myObject = gluNewQuadric( );
    gluQuadricDrawStyle( myObject, GLU_LINE );
    glColor3f( 1, 1, 0 );
    gluSphere( myObject, 1, 10, 10 );
  }
  glEndList( );

  return( id );
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

  // Show static objects
  glCallList( myDisplayLists );
  glCallList( myDisplayLists + 1 );

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

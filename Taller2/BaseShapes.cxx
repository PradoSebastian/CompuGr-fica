// =========================================================================
// Taller 2 - Introd. Computación Gráfica
// @author Juan Sebastián Prado Valero
// =========================================================================

/* 
 * =========================================================================
 * Plantilla creada por:
 * =========================================================================
 * @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
 * =========================================================================
 * g++ -std=c++17 BaseShapes.cxx -lGL -lglut -o BaseShapes
 * =========================================================================
 */

#include <cmath>
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>

// -------------------------------------------------------------------------
void ortho_base( )
{
  float cur_color[ 4 ];
  float lw;

  glGetFloatv( GL_CURRENT_COLOR, cur_color );
  glGetFloatv( GL_LINE_WIDTH, &lw );

  glLineWidth( 2 );
  glBegin( GL_LINES );
  {
    glColor3f( 1, 0, 0 );
    glVertex2f( 0, 0 );
    glVertex2f( 5, 0 );

    glColor3f( 0, 1, 0 );
    glVertex2f( 0, 0 );
    glVertex2f( 0, 5 );
  }
  glEnd( );

  glColor3fv( cur_color );
  glLineWidth( lw );
}

// -------------------------------------------------------------------------
void circle( int mode = GL_LINE_LOOP, int samples = 100 )
{
  float pi2 = atan( 1.0 ) * 8.0;

  glBegin( mode );
  {
    for( int i = 0; i < samples; i++ )
    {
      float w = pi2 * ( float( i ) / float( samples ) );
      glVertex2f( std::cos( w ), std::sin( w ) );
    } // end for
  }
  glEnd( );
}

// -------------------------------------------------------------------------
void square( int mode = GL_LINE_LOOP )
{
  glBegin( mode );
  {
    glVertex2f( -1, -1 );
    glVertex2f(  1, -1 );
    glVertex2f(  1,  1 );
    glVertex2f( -1,  1 );
  }
  glEnd( );
}

// -------------------------------------------------------------------------
void triangle( int mode = GL_LINE_LOOP )
{
  float s3 = sqrt( 3.0 );
  glBegin( mode );
  {
    glVertex2f( -1, -s3 / 3.0 );
    glVertex2f(  1, -s3 / 3.0 );
    glVertex2f(  0,  s3 / 1.5 );
  }
  glEnd( );
}

// -------------------------------------------------------------------------
void reshape( int width, int height )
{
  // Viewport
  glViewport( 0, 0, width, height );

  // Prepare projection
  glMatrixMode( GL_PROJECTION );
  glLoadIdentity( );
  glOrtho( -10, 10, -10, 10, -1, 1 );
}

// -------------------------------------------------------------------------
void draw( )
{
  // Clear framebuffer
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );

  // Draw stuff
  glMatrixMode( GL_MODELVIEW );
  glLoadIdentity( );

  ortho_base( );

  // ------------------------------------------
  // Rectangulo parqueadero
  // ------------------------------------------
  glTranslatef(-5.6, -4.75, 1);
  glScalef(3.4, 0.25, 1);
  square( ); 
  glLoadIdentity( );

  // ------------------------------------------
  // Circulo Rueda 1
  // ------------------------------------------
  glTranslatef(-4.6, -4, 1);
  glScalef(0.5, 0.5, 1);
  circle( );
  glLoadIdentity( );

  // ------------------------------------------
  // Circulo Rueda 2
  // ------------------------------------------
  glTranslatef(-7.3, -4, 1);
  glScalef(0.5, 0.5, 1);
  circle( );
  glLoadIdentity( );

  // ------------------------------------------
  // Rectangulo Camión Carga
  // ------------------------------------------
  glTranslatef(-6, -2.3, 1);
  glScalef(2, 1.2, 1);
  square( ); 
  glLoadIdentity( );

  // ------------------------------------------
  // Rectangulo Camión Conductor
  // ------------------------------------------
  glTranslatef(-3.2, -3, 1);
  glScalef(0.8, 0.5, 1);
  square( ); 
  glLoadIdentity( );

  // ------------------------------------------
  // Rectangulo Casa
  // ------------------------------------------
  glTranslatef(1, -1.5, 1);
  glScalef(3, 3.5, 1);
  square( ); 
  glLoadIdentity( );

  // ------------------------------------------
  // Triangulo Techo Casa
  // ------------------------------------------
  glTranslatef(1, 2.7, 1);
  glScalef(5, 1.2, 1);
  triangle( ); 
  glLoadIdentity( );

  // ------------------------------------------
  // Rectangulo Tronco Arbol
  // ------------------------------------------
  glTranslatef(7.9, -3.5, 1);
  glScalef(0.85, 1.5, 1);
  square( ); 
  glLoadIdentity( );

  // ------------------------------------------
  // Triangulo Hojas arbol 1
  // ------------------------------------------
  glTranslatef(7.9, -1.3, 1);
  glScalef(1.8, 1.2, 1);
  triangle( ); 
  glLoadIdentity( );

  // ------------------------------------------
  // Triangulo Hojas arbol 2
  // ------------------------------------------
  glTranslatef(7.9, -0.5, 1);
  glScalef(1.8, 1.2, 1);
  triangle( ); 
  glLoadIdentity( );

  // ------------------------------------------
  // Triangulo Hojas arbol 3
  // ------------------------------------------
  glTranslatef(7.9, 0.2, 1);
  glScalef(1.8, 1.2, 1);
  triangle( ); 
  glLoadIdentity( );

  // Prepare next frame
  glutSwapBuffers( );
}

// -------------------------------------------------------------------------
int main( int argc, char** argv )
{
  glutInit( &argc, argv );
  glutInitDisplayMode( GLUT_RGBA );
  glutInitWindowSize( 700, 700 );
  glutInitWindowPosition( 0, 0 );

  glutCreateWindow( "Basic shapes in OpenGL" );

  glutDisplayFunc( draw );
  glutReshapeFunc( reshape );

  glutMainLoop( );

  return( 0 );
}

// eof - BaseShapes.cxx

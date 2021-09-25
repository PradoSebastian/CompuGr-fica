/* =========================================================================
 * Taller 1.5 - Introd. Computación Gráfica
 * @author Juan Sebastián Prado Valero
 ===========================================================================

 ===========================================================================
 * Plantilla creada por:
 -------------------------------------------------------------------------
 * @author Leonardo Fl�rez-Valencia (florez-l@javeriana.edu.co)
 * -------------------------------------------------------------------------
 * Compilation on linux:
 *
 * g++ -std=c++17 line_experiments.cxx -lGL -lGLU -lglut -o line_experiments
 *
 * -------------------------------------------------------------------------
 ===========================================================================
 */

#include <cstring>
#include <iostream>

#include <GL/glut.h>
#include <GL/glu.h>
#include <GL/gl.h>

// -------------------------------------------------------------------------
int Width, Height;
int ClickX0, ClickY0, ClickX1, ClickY1;
int NumberOfClicks;
unsigned char* Screen;

// -------------------------------------------------------------------------
float abs(float num) 
{
  if(num < 0) {
    num *= -1;
  }

  return num;
}

// -------------------------------------------------------------------------
void DDA( int x0, int y0, int x1, int y1 ) // Red
{
  // Screen[ x ][ y ] :: Screen[ ( y * Height ) + x ] += 1;
  // Screen[ ( y0 * Height ) + x0 ] += 1;
  // Screen[ ( y1 * Height ) + x1 ] += 1;

  float dx = x1 - x0;
  float dy = y1 - y0;
  int step = -1;

  if(abs(dy) < abs(dx)) {
    step = abs(dx);
  } else {
    step = abs(dy);
  }

  dx /= step;
  dy /= step;

  float x = x0;
  float y = y0;

  int pos = 0;

  for (int i = 1; i <= step; i++)
  {
    pos = ( (int)y * Height ) + (int)x;

    //Screen[ pos ] += 1;

    x += dx;
    y += dy;  

  }

}

// -------------------------------------------------------------------------
void Bresenham( int x0, int y0, int x1, int y1 )  // Green
{
  // Screen[ x ][ y ] :: Screen[ ( y * Height ) + x ] += 2;
  // Screen[ ( y0 * Height ) + x0 ] += 2;
  // Screen[ ( y1 * Height ) + x1 ] += 2;

  bool xDominante = true;

  int dx = x1 - x0;
  int dy = y1 - y0;

  float m = (float)dy/(float)dx;

  int incremento = 1;
  int D = -1;
  int aux = -1;

  int x = x0;
  int y = y0;

  if( abs(m) > 1) {
    xDominante = false;
  }

  if(dy < 0) {

    if(!xDominante) {
      aux = y1;
      y1 = y0;
      y0 = aux;

      y = y0;

      x = x1;
    }

    incremento *= -1;
    dy = -dy;
  }

  if(dx < 0) {
    
    if(xDominante) {
      aux = x1;
      x1 = x0;
      x0 = aux;

      x = x0;

      y = y1;
    }

    incremento *= -1;
    dx = -dx;
  }


  int ejeDom = -1;
  int ejeSec = -1;
  int ep0 = -1;
  int ep1 = -1;

  if (xDominante) {
    ep0 = x0;
    ep1 = x1;
    ejeSec = y;
  } else {
    ep0 = y0;
    ep1 = y1;
    ejeSec = x;
    aux = dx;
    dx = dy;
    dy = aux;
  }

  D = 2 * dy - dx;

  int pos = 0;

  for (ejeDom = ep0; ejeDom <= ep1; ejeDom++)
  {
    if (xDominante) {
      pos = ( ejeSec * Height ) + ejeDom;  
    } else {
      pos = ( ejeDom * Height ) + ejeSec;
    }
    
    //Screen[ pos ] += 2;

    if(D >= 0) {
      ejeSec += incremento;
      D -= 2 * dx;
    }

    D += 2 * dy;

  }

}

// -------------------------------------------------------------------------

int pow(int x, int y) {
  return x^y;
}

void Dibujar(int x0, int y0, int x, int y) {
  std::cout << "x0: " << x0 << std::endl;
  std::cout << "y0: " << y0 << std::endl;
  std::cout << "x1: " << x << std::endl;
  std::cout << "y1: " << y << std::endl << std::endl;
  Screen[((y0+y)* Height) + (x0+x)] += 2;
  Screen[((y0+y)* Height) + (x0-x)] += 2;
  Screen[((y0-y)* Height) + (x0+x)] += 2;
  Screen[((y0-y)* Height) + (x0-x)] += 2;
}

void BresenhamElipse( int x0, int y0, int x1, int y1 )
{

  int rx = abs(x1-x0);
  int ry = abs(y1-y0);
  int x = 0;
  int y = ry;

  int rxpow = rx^2;
  int rypow = ry^2;

  int P1k = rypow - (rxpow * ry) + ((1/4)*rxpow);

  while((rypow * x) <= (rxpow * y)) {
    x++;
    if(P1k < 0) {
      P1k = P1k + (2*rypow*x) + rypow;
    } else {
      y--;
      P1k = P1k + (2*rypow*x) - (2*rxpow*y) + rypow;
    }
    Dibujar(x0, y0, x, y);
  }

  int P2k = rypow * pow(x + (1/2), 2) + (rxpow * pow(y-1, 2)) - (rypow*rxpow);

  while(y > 0) {
    y--;
    if(P2k > 0) {
      P2k = P2k - (2*rxpow*y) + rxpow;
    } else {
      x++;
      P2k = P2k + (2*rypow*x) - (2*rxpow*y) + rxpow;
    }
    Dibujar(x0, y0, x, y);
  }
}

// -------------------------------------------------------------------------
void Init( )
{
  glClearColor( 0.2, 0.2, 0.2, 0.0 );
  gluOrtho2D( 0.0f, float( Width ), 0.0f, float( Height ) );
}

// -------------------------------------------------------------------------
void MouseCbk( int button, int state, int x, int y )
{
  if( button == GLUT_LEFT_BUTTON && state == GLUT_UP )
  {
    if( NumberOfClicks == 0 )
    {
      ClickX0 = x;
      ClickY0 = Height - y;
      NumberOfClicks++;
      std::memset( Screen, 0, Width * Height );
    }
    else
    {
      ClickX1 = x;
      ClickY1 = Height - y;

      DDA( ClickX0, ClickY0, ClickX1, ClickY1 );
      Bresenham( ClickX0, ClickY0, ClickX1, ClickY1 );
      BresenhamElipse( ClickX0, ClickY0, ClickX1, ClickY1 );

      NumberOfClicks = 0;
    } // end if
    glutPostRedisplay( );
  } // end if
}

// -------------------------------------------------------------------------
void DisplayCbk( )
{
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );

  glPointSize( 3 );
  glBegin( GL_POINTS );
  unsigned int k = 0;
  for( unsigned int j = 0; j < Height; ++j )
  {
    for( unsigned int i = 0; i < Width; ++i )
    {
      if( Screen[ k ] > 0 )
      {
        if     ( Screen[ k ] == 1 ) glColor3f( 1, 0, 0 );
        else if( Screen[ k ] == 2 ) glColor3f( 0, 1, 0 );
        else              glColor3f( 1, 1, 0 );
        glVertex2i( i, j );
      } // end if
      k++;
    } // end for
  } // end for
  glEnd( );

  glutSwapBuffers( );
}

// -------------------------------------------------------------------------
int main( int argc, char* argv[] )
{
  if( argc < 3 )
  {
    std::cerr << "Usage: " << argv[ 0 ] << " width height" << std::endl;
    return( 1 );
  } // end if

  Width = std::atoi( argv[ 1 ] );
  Height = std::atoi( argv[ 2 ] );
  NumberOfClicks = 0;
  Screen = new unsigned char[ Width * Height ];

  glutInit( &argc, argv );
  glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB );
  glutInitWindowPosition( 50, 50 );
  glutInitWindowSize( Width, Height );
  glutCreateWindow( "Line experiments" );

  glutDisplayFunc( DisplayCbk );
  glutMouseFunc( MouseCbk );

  Init( );
  glutMainLoop( );

  delete Screen;

  return( 0 );
}

// eof - line_experiments.cxx

#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <GL/glut.h>
#include <iostream>
#include <cstring>
#include <fstream>
#include <stdlib.h>
#include <Windows.h>
#include <mmsystem.h>

using namespace std;

#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

GLfloat xRotated, yRotated, zRotated;
GLdouble radius = 1;

int rotateSphere = 1;
int backgroundColor = 0;
// default 0.563, 0.763, 0.500, 0.500
double colorR = 0.563;
double colorG = 0.763;
double colorB = 0.500;
double colorA = 0.500;

double sphereColorR = 1.0;
double sphereColorG = 0.3;
double sphereColorB = 0.0;





fstream fArchive("Data.txt", ios::in | ios::out | ios::binary);
void menu() {
	
	printf("\n -> Press X to save position");
	printf("\n -> Press SQUARE to delete data");
	printf("\n -> Press CIRCLE to do the travel");
	printf("\n -> Press TRIANGLE to exit \n \n");

}

/*
	max x = -350        max y = 250                 min x =     350                     min y = -250
*/
int positionX = 0;
int positionY = 0;
int option = -1;

//struct used to be saved in the data file
struct data {
public:
	int savedPositionX;
	int savedPositionY;

	data() {
		savedPositionX = -1;
		savedPositionY = -1;
	}

}regData;


void createAFile() {
	fstream fArchive("Data.txt", ios::in | ios::out | ios::binary | ios::trunc );
}

//Function to save the position x and y in the data file, whith a struct format
void writeInFile() {
	regData.savedPositionX = positionX;
	regData.savedPositionY = positionY;
	fArchive.seekg(0, ios::end);
	fArchive.write(reinterpret_cast<char *> (&regData), sizeof(regData));
	printf("Position saved \n");
}

void changeColors() {
	if (backgroundColor == 0)
	{
		colorR = 0.563;
		colorG = 0.763;
		colorB = 0.500;
		colorA = 0.500;

		sphereColorR = 1.0;
		sphereColorG = 0.3;
		sphereColorB = 0.0;
		return;
	}
	if (backgroundColor % 2 != 0) {
		colorR = 0.0;
		colorG = 0.0;
		colorB = 0.0;
		colorA = 0.0;

		sphereColorR = 255;
		sphereColorG = 255;
		sphereColorB = 255;

	}
	else {
		colorR = 255;
		colorG = 255;
		colorB = 255;
		colorA = 255;

		sphereColorR = 0.0;
		sphereColorG = 0.0;
		sphereColorB = 0.0;
	}
}




void idleFunc();

//function that recives a position x and a position y to move the sphere
void autoMove(int x, int y) {

	do{

		if (x > positionX)
		{
			positionX++;
			option = 1;
		}
		if (x < positionX)
		{
			if (positionX ==0)
			{
				positionX = -1;
			}
			else
			{
				positionX--;
			}
			option = 0;
		}
		if (y > positionY)
		{
			positionY++;
			option = 2;
		}
		if (y < positionY)
		{
			if (positionY == 0)
			{
				positionY = -1;
			}
			else
			{
				positionY--;
			}
			option = 3;
		}
		
		idleFunc();


		if (positionX == x && positionY == y)
		{
			return;
		}
	} while (true);

}

//fucntion to read the data file and call the automove Function
void readInFile() {

	system("cls");
	menu();
	int index = 0;
	fArchive.seekg(0, ios::end);
	int indexStop = fArchive.tellg();
	fstream fArchiveTemp("Data.txt", ios::in | ios::out | ios::binary);
	fArchiveTemp.seekg(0);
	rotateSphere = 0;
	do {
		backgroundColor++;
		
		fArchiveTemp.read(reinterpret_cast<char *> (&regData), sizeof(regData));
		if (regData.savedPositionX == -1 && regData.savedPositionY == -1) {
			printf("Track not saved \n");
			return;
		}
		cout << "Position X,    Position Y    " << endl;
		cout <<regData.savedPositionX << endl;
		cout <<regData.savedPositionY << endl;
		index += sizeof(regData);
		
		autoMove(regData.savedPositionX, regData.savedPositionY);
		PlaySound(TEXT("glassSound.wav"), NULL, SND_ASYNC | SND_FILENAME | SND_LOOP);
		changeColors();
		glClearColor(colorR, colorG, colorB, colorA);


	} while (index < indexStop);
	rotateSphere = 1;
	backgroundColor = 0;
	changeColors();
	glClearColor(colorR, colorG, colorB, colorA);
	glColor3f(sphereColorR, sphereColorG, sphereColorB);
	PlaySound(TEXT("sound.wav"), NULL, SND_ASYNC | SND_FILENAME | SND_LOOP);
}

//Function to overwrite the data file 
void deleteDataInFile() {
	fstream fArchive("Data.txt", ios::in | ios::out | ios::binary | ios::trunc);
	regData.savedPositionX = -1;
	regData.savedPositionY = -1;
	system("cls");
	menu();
	printf("Data deleted \n");
}


//function to show the sphere in the projection matrix
void redisplayFunc(void)
{
	glMatrixMode(GL_MODELVIEW);
	glViewport(positionX,positionY,SCREEN_WIDTH,SCREEN_HEIGHT);
	// clear the drawing buffer.
	glClear(GL_COLOR_BUFFER_BIT);

	// clear the identity matrix.
	glLoadIdentity();

	// traslate the draw by z = -4.0
	// Note this when you decrease z like -8.0 the drawing will looks far , or smaller.
	glTranslatef(0.0, 0.0, -20.0);

	// Orange color used to draw.
	glColor3f(sphereColorR ,sphereColorG, sphereColorB);
	
	// changing in transformation matrix.
	// rotation about X axis
	glRotatef(xRotated, 1.0, 0.0, 0.0);
	// rotation about Y axis
	glRotatef(yRotated, 0.0, 1.0, 0.0);
	// rotation about Z axis
	glRotatef(zRotated, 0.0, 0.0, 1.0);

	// scaling transfomation 
	glScalef(1.0, 1.0, 1.0);

	// built-in (glut library) function , draw you a sphere.
	glutSolidSphere(radius, 20, 20);

	// Flush buffers to screen
	glFlush();
	// sawp buffers called because we are using double buffering 
	 glutSwapBuffers();
}

//function to create a projection matrix
void reshapeFunc(int x, int y)
{
	if (y == 0 || x == 0) return;  //Nothing is visible then, so return
								   //Set a new projection matrix
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	//Angle of view:40 degrees
	//Near clipping plane distance: 0.5
	//Far clipping plane distance: 20.0
	gluPerspective(40.0, (GLdouble)x / (GLdouble)y, 0.5, 20.0);
	glMatrixMode(GL_MODELVIEW);
	glViewport(positionX, positionY, x, y);  //Use the whole window for rendering
}

//Function tho change the sphere's rotation direction
void idleFunc(void)
{
	
	if (option == 0)
	{
		yRotated -= 0.1;
	}
	if (option == 1)
	{
		yRotated += 0.1;
	}
	if (option == 2)
	{
		xRotated -= 0.1;
	}
	if (option == 3)
	{
		xRotated += 0.1;
	}
	if (option == 4)
	{
		yRotated, xRotated = 270;
	}
	redisplayFunc();
}

void joystick(unsigned int buttonmask, int x, int y, int z)
{
	
	int buttonCount;
	const unsigned char *buttons = glfwGetJoystickButtons(GLFW_JOYSTICK_1, &buttonCount);

	
	if (GLFW_RELEASE == buttons[0] && rotateSphere == 1) {
		option = 4;
	}

	if (GLFW_PRESS == buttons[0]) {
		// button X
		writeInFile();
	}
	if (GLFW_PRESS == buttons[1]) {
		// button circle
		deleteDataInFile();
	}
	if (GLFW_PRESS == buttons[2]) {
		// button square
		readInFile();
	}
	if (GLFW_PRESS == buttons[3]) {
		// button tringle
		exit(0);
	}

	if (x < 0)
	{
		//move left
		xRotated = 270;
		option = 0;
		if (positionX - 5 >= -350) {
			positionX -= 5;
		}

	}
	if (x > 0)
	{
		//move right 
		xRotated = 270;
		option = 1;
		if (positionX + 5 <= 350)
		{
			positionX += 5;
		}
	}
	if (y < 0)
	{
		//move up
		yRotated = 270;
		option = 2;
		if (positionY + 5 <= 250)
		{
			positionY += 5;
		}

	}
	if (y > 0)
	{
		//move down		
		yRotated = 270;
		option = 3;
		if (positionY - 5 >= -250)
		{
			positionY -= 5;
		}

	}

}


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main( int argc, char **argv) {
	
	if (!fArchive)
	{
		createAFile();
	}

	//Initialize GLUT
	glutInit(&argc, argv);
	//double buffering used to avoid flickering problem in animation
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB); 
	// window size
	glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT);
	// create the window 
	glutCreateWindow("OpenGL and C++ Proyect");
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
	
	xRotated = yRotated = zRotated = 0;
	xRotated = 0;
	yRotated = 0;
	glClearColor(colorR,colorG,colorB,colorA);// 0.563, 0.763, 0.500, 0.500
	//Assign  the function used in events
	glutDisplayFunc(redisplayFunc);

	glutReshapeFunc(reshapeFunc);

	glutIdleFunc(idleFunc);


	glfwInit();
	
	//Function to catch the joystick's buttons 
	glutJoystickFunc(joystick,100);
	
	system("cls");
	menu();
	PlaySound(TEXT("sound.wav"), NULL, SND_ASYNC | SND_FILENAME | SND_LOOP);
	//Let start glut loop
	glutMainLoop(); 

}
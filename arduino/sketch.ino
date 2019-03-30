#include <Servo.h>

Servo string;        // create servo object to control the six servos

int pos_0 = 0 ;      // variable stores the left-most position the servo will send the pick
int pos_1 = 20 ;     // variable stores the righ- most position the servo will send the pick
int string_number;   // variable to identify each string/servo
int string_state[] = {0, 0, 0, 0, 0, 0};  // to keep track of the picks position : ie is to the left or right of the string
int manual_button;   // To dientify each of the 6 manual button on the breadboard above each string
int manual_button_state = 0;   // To track state of the button (pressed or NOT pressed)

void setup()  //Setup only gets run once when the Arduino is powered on
{
    pinMode(8, INPUT_PULLUP);  // Set the 6 manual buttons to be inputs
    pinMode(9, INPUT_PULLUP);
    pinMode(10, INPUT_PULLUP);
    pinMode(11, INPUT_PULLUP);
    pinMode(12, INPUT_PULLUP);
    pinMode(13, INPUT_PULLUP);

    Serial.begin(9600);  //Start the Serial interface, the interface to the Raspberry Pi
    for (string_number = 0; string_number < 6 ; string_number++)  {   // At boot time, initialize each servo to a starting pick position
      string.attach(string_number+2);  // Attach to the servo pin corresponding to the correct string number
      string.write(pos_0);   // Tell the servo to go to pos_0, get ready to rock.
      delay(100);  // Give plenty of time for each pick to get into starting position
    }
}

//////// As its name suggests, the ardunio "loops" through this function continually, as fast as it can
void loop()
{
////// MANUAL BUTTON CONTROL
    for (int manual_button = 0; manual_button < 6; manual_button++)  {
      manual_button_state = digitalRead(manual_button + 8);  // Read the status of the pin attached to the button
      string_number = manual_button;
      if (manual_button_state  == 0) {  // If the pin is set to INPUT_PULLUP, a state of zero means the button is pressed.
        pluck(string_number,string_state[string_number]);  // call pluck function, also pass the state of the string so we'll know which way to pluck it
        if ( string_state[string_number] == 0) {
          string_state[string_number] = 1;  //toggle the state of the servo to keep track of where the pick is for next time we want to pluck it
         }
        else  {
          string_state[string_number] = 0;  //toggle the state of the servo to keep track of where the pick is for next time we want to pluck it
        }

	while(manual_button_state == 0) {
	manual_button_state = digitalRead(manual_button + 8);
	}
	}
      }

////// SERIAL COMMUNICATIONS CONTROL (from the Pi)
   if (Serial.available())  {
     string_number = Serial.read() - '0';  //Read what value is being sent over Serial from the Pi
     Serial.println(string_number);
     pluck(string_number,string_state[string_number]);   // call pluck function, also pass the state of the string so we'll know which way to pluck it
     if ( string_state[string_number] == 0) {
        string_state[string_number] = 1; //toggle the state of the servo to keep track of where the pick is for next time we want to pluck it
      }
     else
     {
        string_state[string_number] = 0; //toggle the state of the servo to keep track of where the pick is for next time we want to pluck it
     }
   }
   delay(100);
}
//////// END OF MAIN LOOP

//////// Pluck function makes the servo move
void pluck(int string_number , int state){
    string.attach(string_number + 2);   //Attach to the servo sitting above string_number
    if (state == 0)                     //move the servo from left to right
    {
      string.write(pos_1);              //Tell servo to go to position in variable 'pos_1'
     }
    if (state == 1)                     //move the servo from right to left
    {
      string.write(pos_0);              //Tell servo to go to position in variable 'pos_2'
    }
}

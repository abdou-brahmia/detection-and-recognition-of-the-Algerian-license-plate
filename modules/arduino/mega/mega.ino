
#include <Servo.h>

Servo name_servo;

const int trigPin = 9;
const int echoPin = 10;
const int ledPin = 52; // pin the LED is attached to
const int ledPin2 = 53; // pin the LED is attached to
const int servoPin = 12; // pin the LED is attached to


int servo_position = 0;
int incomingByte;      // variable stores  serial data
bool state = false;      // variable stores  serial data
long duration;
int distance;
void setup() {
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
pinMode(ledPin, OUTPUT);
pinMode(ledPin2, OUTPUT);
name_servo.attach (servoPin);
name_servo.write(0);
digitalWrite(ledPin, LOW );
digitalWrite(ledPin2,HIGH);

Serial.begin(9600); // Starts the serial communication
}
void loop() {
// Clears the trigPin

if (Serial.available() > 0) {
    
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
      digitalWrite(ledPin2, LOW);
      name_servo.write(90);
    
      digitalWrite(trigPin, LOW);
      state=false;
      while (state==false){
        delayMicroseconds(2);
        // Sets the trigPin on HIGH state for 10 micro seconds
      
        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);
        // Reads the echoPin, returns the sound wave travel time in microseconds
        duration = pulseIn(echoPin, HIGH);
        // Calculating the distance
        distance= duration*0.034/2;
        // the distance on the Serial Monitor
        if (distance<=5){
          while (state==false){
            delayMicroseconds(2);
            digitalWrite(trigPin, HIGH);
            delayMicroseconds(10);
            digitalWrite(trigPin, LOW);
            // Reads the echoPin, returns the sound wave travel time in microseconds
            duration = pulseIn(echoPin, HIGH);
            // Calculating the distance
            distance= duration*0.034/2;
            // the distance on the Serial Monitor
            if (distance>=5){

              state=true;
              digitalWrite(ledPin, LOW);
              digitalWrite(ledPin2, HIGH);
              name_servo.write(0);
              Serial.println("1");

            }
          
          delay(1000);

          }
          
        
        }
      
      
      delay(1000);

      }
  }
  else{
    delay(500);
  
  }
  


}


}

#include <Servo.h>

// Arduino pin assignment

#define PIN_POTENTIOMETER 3 // Potentiometer at Pin A3
#define PIN_IR 0             // IR at Pin A0

#define PIN_SERVO 10
#define PIN_LED 9
#define _DUTY_MIN 553   // servo full clock-wise position (0 degree)
#define _DUTY_NEU 1476  // servo neutral position (90 degree)
#define _DUTY_MAX 2399  // servo full counter-clockwise position (180 degree)
#define _DIST_MIN 100.0
#define _DIST_MAX 250.0
#define alpha 0.5
#define LOOP_INTERVAL 40       // Loop Interval (unit: msec)

Servo myservo;
unsigned long last_loop_time;   // unit: msec

void setup()
{
  pinMode(PIN_LED, OUTPUT);
  myservo.attach(PIN_SERVO);
  myservo.writeMicroseconds(_DUTY_NEU);

  Serial.begin(1000000);
}

void loop()
{
  unsigned long time_curr = millis();
  int value, duty;
  double dist_;
  double ema = 0;

  // wait until next event time
  if (time_curr < (last_loop_time + LOOP_INTERVAL))
    return;
  last_loop_time += LOOP_INTERVAL;

  // Read IR Sensor value !!!
  value = analogRead(PIN_IR);

  // Convert IR sensor value into distance !!!
  dist_ = (6762.0 / (value - 9) - 4.0) * 10.0 - 60.0;

  // we need distance range filter here !!!


  if (dist_ < _DIST_MIN) {      // Set Lower Value
    digitalWrite(PIN_LED, 1);  // LED OFF
  }

  else if (dist_ > _DIST_MAX) {  // Set Higher Value
    digitalWrite(PIN_LED, 1);   // LED OFF
  }

  else {
    duty = ((dist_ - 100.0) / 150.0) * (3500 - _DUTY_MIN);
    digitalWrite(PIN_LED, 0);
  }

  // we need EMA filter here !!!
  ema = alpha * dist_ + (1 - alpha) * ema;

  // map distance into duty
  //duty = map(value, 0, 1023, _DUTY_MIN, _DUTY_MAX);
  //duty = (_DUTY_MAX - _DUTY_MIN) * 180
  myservo.writeMicroseconds(duty);

  // print IR sensor value, distnace, duty !!!
  Serial.print("MIN: "); Serial.print(_DIST_MIN);
  Serial.print(", IR: "); Serial.print(value);
  Serial.print(", dist_: "); Serial.print(dist_);
  Serial.print(", ema: "); Serial.print(ema);
  Serial.print(", servo: "); Serial.print(duty);
  //Serial.print(", low: "); Serial.print(LOW);
  // Serial.print(", high: "); Serial.print(HIGH);
  Serial.print(", MAX: "); Serial.print(_DIST_MAX);
  Serial.println("");

  
  // Serial.print(" = ");
  //  Serial.println((value / 1024.0) * 5.0);
  //  Serial.print("IR_SENSOR"); Serial.println(dist_);
  //  Serial.print(" Volt => Duty : ");
  //  Serial.print(duty);
  //  Serial.println("usec");
}

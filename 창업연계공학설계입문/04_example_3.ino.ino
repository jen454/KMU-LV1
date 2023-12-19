#define PIN_LED 13
unsigned int count, toggle;

void setup() {
  // put your setup code here, to run once:
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(115200); // Initialize serial port 
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }
  Serial.println("Hello world");
  int count = 0;
  int toggle = 0;
  digitalWrite(PIN_LED, toggle); // turn off LED.
}

void loop() {
  // put your main code here, to run repeatedly:
  int count = 0, toggle = 0;
  Serial.println(++count);
  toggle = toggle_state(toggle);
  digitalWrite(PIN_LED, toggle);
  delay(1000);
}

int toggle_state(int toggle){
  if (toggle == 0) return 1;
  else return 0;
}

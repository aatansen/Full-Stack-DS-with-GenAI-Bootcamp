// JARVIS Smart Home Controller
// Receives commands from Python via Serial

char command;

const int bedroomLight = 2;
const int table_lamp  = 3;
const int fan          = 4;
const int tv           = 5;

void setup() {
  Serial.begin(9600);

  pinMode(bedroomLight, OUTPUT);
  pinMode(table_lamp, OUTPUT);
  pinMode(fan, OUTPUT);
  pinMode(tv, OUTPUT);

  // Turn everything OFF at start
  digitalWrite(bedroomLight, LOW);
  digitalWrite(table_lamp, LOW);
  digitalWrite(fan, LOW);
  digitalWrite(tv, LOW);
}

void loop() {
  if (Serial.available()) {
    command = Serial.read();

    switch (command) {

      case '1':  // Bedroom light ON
        digitalWrite(bedroomLight, HIGH);
        break;

      case '2':  // Bedroom light OFF
        digitalWrite(bedroomLight, LOW);
        break;

      case '3':  // Dining light ON
        digitalWrite(table_lamp, HIGH);
        break;

      case '4':  // Dining light OFF
        digitalWrite(table_lamp, LOW);
        break;

      case '5':  // Fan ON
        digitalWrite(fan, HIGH);
        break;

      case '6':  // Fan OFF
        digitalWrite(fan, LOW);
        break;

      case '7':  // TV ON
        digitalWrite(tv, HIGH);
        break;

      case '8':  // TV OFF
        digitalWrite(tv, LOW);
        break;

      case '9':
        digitalWrite(bedroomLight, HIGH);
        digitalWrite(table_lamp, HIGH);
        digitalWrite(fan, HIGH);
        digitalWrite(tv, HIGH);
        break;

      case '0':
        digitalWrite(bedroomLight, LOW);
        digitalWrite(table_lamp, LOW);
        digitalWrite(fan, LOW);
        digitalWrite(tv, LOW);
        break;
    }
  }
}

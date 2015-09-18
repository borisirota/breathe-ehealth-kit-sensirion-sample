#include <PinChangeInt.h>
#include <eHealth.h>

// count for pulsioximeter
int cont = 0;

void setup() {
  Serial.begin(115200);  
  eHealth.initPulsioximeter();

  //Attach the inttruptions for using the pulsioximeter.   
  PCintPort::attachInterrupt(6, readPulsioximeter, RISING);
}

void loop() {
  // Create the data JSON
  String data = "";
  data += "\"{";
  data += "\\\"BPM\\\": ";
  data += eHealth.getBPM();
  data += ", \\\"oxygenSaturation\\\": ";
  data += eHealth.getOxygenSaturation();
  float temperature = eHealth.getTemperature();
  data += ", \\\"temperature\\\": ";
  data += temperature; //, 2);  
  data += ", \\\"airFlow\\\": "; 
  int air = eHealth.getAirFlow(); 
  data += air;  
  data += "}\"";

  // Calcualte checksum
  long chk = 0;
  for (int i = 0; i < data.length(); i++) {
    chk += ((int)data.charAt(i) * (i+1));
  }
 
  // Print the result to serial
  Serial.print (data + "|" + chk + "\n");
}


// Include always this code when using the pulsioximeter sensor
// =========================================================================
void readPulsioximeter(){  

  cont ++;

  if (cont == 50) { //Get only of one 50 measures to reduce the latency
    eHealth.readPulsioximeter();  
    cont = 0;
  }
}

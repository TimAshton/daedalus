#include <Arduino.h>
#include "DHT_Async.h"

#define DHT_SENSOR_TYPE DHT_TYPE_11

static const int DHT_SENSOR_PIN = 10;
DHT_Async dht_sensor(DHT_SENSOR_PIN, DHT_SENSOR_TYPE);

void setup() {
    Serial.begin(115200);
}

static bool measure_environment(float *temperature, float *humidity) {
    static unsigned long measurement_timestamp = millis();

    /* Measure once every 1 seconds. */
    if (millis() - measurement_timestamp > 1000ul) {
        if (dht_sensor.measure(temperature, humidity)) {
            measurement_timestamp = millis();
            return (true);
        }
    }

    return (false);
}

void loop() {
    float temperature;
    float humidity;

    if (measure_environment(&temperature, &humidity)) {
        Serial.print(millis());
        Serial.print(",");
        Serial.print(temperature, 1);
        Serial.print(",");
        Serial.println(humidity, 1);
    }
}

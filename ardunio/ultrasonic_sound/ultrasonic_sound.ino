/*
 *  Train‑crossing warning tone triggered by an ultrasonic sensor
 *  (Arduino UNO / Nano / Mega etc.)
 *
 *  Connect:
 *   • Ultrasonic sensor TRIG  → pin 6
 *   • Ultrasonic sensor ECHO  → pin 7
 *   • Piezo buzzer            → pin 3 (plus GND)
 *
 *  The sketch uses the standard tone() / noTone() functions.
 */

#include "pitches.h"          // contains NOTE_A4 and NOTE_E5 definitions

// -------------------- pins & thresholds --------------------
const int TRIG_PIN   = 6;   // Ultrasonic sensor TRIG
const int ECHO_PIN   = 7;   // Ultrasonic sensor ECHO
const int BUZZER_PIN = 3;   // Piezo buzzer
const int DISTANCE_THRESHOLD = 20;   // cm – trigger distance

// -------------------- train‑crossing tone data --------------------
const uint16_t crossingMelody[]     = { NOTE_A4, NOTE_E5 };   // ding – dong
const uint16_t crossingDurations[] = { 150,    150    };   // ms per beep

#define CROSSING_PAUSE_BETWEEN   200   // silence after the first beep
#define CROSSING_REPEAT_PAUSE    800   // silence after the second beep

// -----------------------------------------------------------------
void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

// -----------------------------------------------------------------
void loop() {
  // --- 1. Trigger the ultrasonic sensor ---
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // --- 2. Measure echo time and compute distance ---
  float duration_us = pulseIn(ECHO_PIN, HIGH);
  float distance_cm = 0.017 * duration_us;   // conversion factor

  // --- 3. If something is close enough, play the warning tone ---
  if (distance_cm < DISTANCE_THRESHOLD) {
    playTrainCrossing();
    delay(500);                 // brief pause before next measurement
  }
}

// -----------------------------------------------------------------
void playTrainCrossing() {
  const int notes = sizeof(crossingMelody) / sizeof(crossingMelody[0]);

  for (int i = 0; i < notes; ++i) {
    // Emit the beep
    tone(BUZZER_PIN, crossingMelody[i], crossingDurations[i]);
    delay(crossingDurations[i]);   // wait for the beep to finish

    // Add the appropriate pause
    if (i == 0) {
      delay(CROSSING_PAUSE_BETWEEN);   // after “ding”
    } else {
      delay(CROSSING_REPEAT_PAUSE);    // after “dong” before next pair
    }

    noTone(BUZZER_PIN);                // ensure the tone stops cleanly
  }
}
# Raspberry Pi GPIO and Flask experiments

Raspberry Pi breadboard experiments using LEDs, a push button, a PIR motion sensor, and a Flask web server.

## Structure

- `gpio-basics/` — push-button and LED control examples.
- `motion-sensor/` — PIR sensor testing and automatic LED control.
- `web-control/` — Flask endpoints for reading the button and controlling LEDs.

The original scripts were moved into topic folders without rewriting their behaviour. Hardware pin assignments and wiring should be checked against the actual breadboard before running them.

## Project notes

The original project description also mentions a possible camera/email extension. No camera implementation was present in the reviewed repository files.

#include <iostream>

class AirConditioner {
public:
    // Constructor to initialize the air conditioner
    AirConditioner(float initTemp, float targetTemp) 
        : currentTemperature(initTemp), targetTemperature(targetTemp), isOn(false) {}

    // Method to turn on the air conditioner
    void turnOn() {
        isOn = true;
        std::cout << "Air conditioner turned on.\n";
    }

    // Method to turn off the air conditioner
    void turnOff() {
        isOn = false;
        std::cout << "Air conditioner turned off.\n";
    }

    // Method to cool the room
    void coolRoom() {
        if (isOn && currentTemperature > targetTemperature) {
            currentTemperature -= 0.5; // Cooling rate
            std::cout << "Cooling... Current temperature: " << currentTemperature << "°C\n";
            if (currentTemperature <= targetTemperature) {
                turnOff();
            }
        }
    }

    // Method to check the temperature and control the air conditioner
    void checkTemperature() {
        if (currentTemperature > targetTemperature && !isOn) {
            turnOn();
        }
        else if (currentTemperature <= targetTemperature && isOn) {
            turnOff();
        }
    }

    // Method to simulate the room temperature rise over time (for testing)
    void increaseTemperature(float amount) {
        currentTemperature += amount;
        std::cout << "Room temperature increased to: " << currentTemperature << "°C\n";
        checkTemperature();
    }

private:
    float currentTemperature;
    float targetTemperature;
    bool isOn;
};

int main() {
    // Create an air conditioner with an initial temperature of 30°C and target temperature of 22°C
    AirConditioner ac(30.0f, 22.0f);

    // Simulate the air conditioning system
    for (int i = 0; i < 20; ++i) {
        ac.coolRoom();
        if (i % 5 == 0) { // Simulate temperature increase every 5 iterations
            ac.increaseTemperature(2.0f);
        }
    }

    return 0;
}

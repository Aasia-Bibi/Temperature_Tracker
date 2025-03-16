import requests
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TemperatureTracker:
    def __init__(self):
        self.temperatures = []
        self.days = []

    def add_temperature(self, day, temp):
        """Add a temperature record."""
        self.days.append(day)
        self.temperatures.append(temp)
        logging.info(f"Added temperature: {temp}°C for {day}")

    def calculate_average(self):
        """Calculate and return the average temperature."""
        return round(sum(self.temperatures) / len(self.temperatures), 2) if self.temperatures else None

    def get_max_temperature(self):
        """Get the maximum temperature."""
        return max(self.temperatures) if self.temperatures else None

    def get_min_temperature(self):
        """Get the minimum temperature."""
        return min(self.temperatures) if self.temperatures else None

    def visualize_data(self):
        """Plot temperature data using Matplotlib."""
        plt.plot(self.days, self.temperatures, marker='o', linestyle='-', color='b', label='Temperature')
        plt.xlabel('Days')
        plt.ylabel('Temperature (°C)')
        plt.title('Weekly Temperature Trends')
        plt.legend()
        plt.grid()
        plt.show()

    def display_summary(self):
        """Display temperature statistics."""
        print("\n--- Weekly Temperature Stats ---")
        print(f"Average Temperature: {self.calculate_average()}°C")
        print(f"Maximum Temperature: {self.get_max_temperature()}°C")
        print(f"Minimum Temperature: {self.get_min_temperature()}°C")

# Example Usage
temp_tracker = TemperatureTracker()
temp_tracker.add_temperature("Monday", 22)
temp_tracker.add_temperature("Tuesday", 25)
temp_tracker.add_temperature("Wednesday", 20)
temp_tracker.add_temperature("Thursday", 23)
temp_tracker.add_temperature("Friday", 26)
temp_tracker.add_temperature("Saturday", 21)
temp_tracker.add_temperature("Sunday", 24)

temp_tracker.display_summary()
temp_tracker.visualize_data()

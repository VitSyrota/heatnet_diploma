import numpy as np
from scipy.interpolate import interp1d

# Дані з таблиці
diameters = np.array([50, 50, 50, 65, 65, 65, 80, 80, 80, 100, 100, 100, 125, 125, 125, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 400, 400, 400, 500, 500, 500, 600, 600, 600])
flows = np.array([0.87, 1.74, 2.61, 1.53, 3.06, 4.59, 2.45, 4.90, 7.35, 3.76, 7.52, 11.28, 5.42, 10.84, 16.26, 7.43, 14.86, 22.29, 13.10, 26.20, 39.30, 19.74, 39.48, 59.22, 27.38, 54.76, 82.14, 43.02, 86.04, 129.06, 63.80, 127.60, 191.40, 88.72, 177.44, 266.16])
press_losses = np.array([100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300])
diameters_unique = np.unique(diameters)

# Створення функцій інтерполяції для кожного діаметра труби
interpolated_flows = {}
interpolated_press_losses = {}
for diameter in diameters_unique:
    mask = diameters == diameter
    flows_for_diameter = flows[mask]
    press_losses_for_diameter = press_losses[mask]
    flows_for_diameter_sorted = np.sort(flows_for_diameter)
    interpolated_flows[diameter] = interp1d(flows_for_diameter_sorted, flows_for_diameter_sorted, fill_value="extrapolate")
    interpolated_press_losses[diameter] = interp1d(flows_for_diameter_sorted, press_losses_for_diameter[np.argsort(flows_for_diameter)], fill_value="extrapolate")

# Генерація інтерпольованих значень для кожного діаметра труби з кроком 1 т/год
interpolated_values = {}
for diameter, interp_func in interpolated_flows.items():
    min_flow = np.min(flows[diameters == diameter])
    max_flow = np.max(flows[diameters == diameter])
    interpolated_values[diameter] = {
        "flow": interp_func(np.arange(min_flow, max_flow + 1)),
        "press_loss": interpolated_press_losses[diameter](np.arange(min_flow, max_flow + 1)),
        "velocity": np.arange(min_flow, max_flow + 1) / (np.pi * (diameter / 1000)**2 / 4)
    }

# Виведення інтерпольованих значень
print("Діаметр труби (мм) | Витрати (т/год) | Удельна потеря давления (Па/м) | Швидкість (м/с)")
for diameter, values in interpolated_values.items():
    for i in range(len(values["flow"])):
        print(f"{diameter:<19} | {values['flow'][i]:<15.2f} | {values['press_loss'][i]:<31.2f} | {values['velocity'][i]:<16.6f}")

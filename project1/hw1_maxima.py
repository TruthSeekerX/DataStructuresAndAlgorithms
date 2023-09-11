import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def SavitzkyGolayFilter(signal):  # five-point
    newSignal = []
    newSignal.append(signal[0])
    newSignal.append(signal[1])
    for i in range(2,len(signal)-2):
        y = 1//35 * (-3*signal[i-2] + 12*signal[i-1] + 17*signal[i] + 12*signal[i+1] -3*signal[i+2])
        newSignal.append(y)
    newSignal.append(signal[len(signal)-2])
    newSignal.append(signal[len(signal)-1])
    return newSignal

def LocalMaximaWithoutNoise(signal):
    localMaximaDict = {}
    for i in range(1, len(signal)-2):
        if (signal[i - 1] <= signal[i]) and (signal[i+1] < signal[i]):
            localMaximaDict[i] = signal[i]
    return localMaximaDict

def GetLineData(filePath):
    dataList = []
    try:
        with open(filePath, 'r') as file:
            for line in file:
                number = float(line.strip())
                dataList.append(number)
    except FileNotFoundError:
        print(f"File not found: {filePath}")
    except ValueError:
        print("Invalid number format in the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return dataList


filePath = './project1/hw1a.txt'
temperatureList = GetLineData(filePath)
maximaDictionary = LocalMaximaWithoutNoise(temperatureList)

windowLength = 5
polynomialOrder = 2
newTemperatureList = savgol_filter(temperatureList, windowLength, polynomialOrder)

x = range(0, len(temperatureList))
count = 1
plt.figure(figsize=(10, 6))
plt.plot(x, temperatureList, label='Temp')
plt.plot(x, newTemperatureList, label='Smooth Temp')
for key, value in maximaDictionary.items():
    plt.plot(x[key], value, 'ro', label=f'LM{count}:{value}')
    count += 1
plt.legend()
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature Signal with Local Maxima')
plt.show()
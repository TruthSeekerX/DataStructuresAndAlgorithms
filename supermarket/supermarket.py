import random
from queue import Queue
import matplotlib.pyplot as plt

class SuperMarketSimulation():
    def __init__(self, casherNumber, trafficRate, customerNumberRange, shoppingTimeSpan, patienceTimeSpan, checkoutTimeSpan, profitRate, salaryRate, lossRate) -> None:
        self._storeTrafficRate = trafficRate
        self._customers = list()
        self._customerId = 0
        self._casherNumber = casherNumber
        self._cashers = list()
        self._customerNumberRange = customerNumberRange
        self._shoppingTimeSpan = shoppingTimeSpan
        self._patienceTimeSpan = patienceTimeSpan
        self._checkoutTimeSpan = checkoutTimeSpan
        self._profit = 0.0
        self._profitHistory = list()
        self._profitRate = profitRate
        self._salaryRate = salaryRate
        self._lossRate = lossRate
        self._totalCustomer = 0
        self._totalLostCustomer = 0
        self.InitCashers(casherNumber)
        pass

    def __str__(self) -> str:
        return str.format(
            "Cashers: {0}\nStore traffic rate: {1}\nNew customer Range: {2}\n"\
            "Shopping time range:{3}\nPatience range:{4}\nCheckout time:{5}\n"\
            "Profit rate:{6}\nSalary rate:{7}\nLoss rate:{8}".format(
                self._casherNumber, self._storeTrafficRate, self._customerNumberRange,
                self._shoppingTimeSpan, self._patienceTimeSpan, self._checkoutTimeSpan,
                self._profitRate, self._salaryRate, self._lossRate))
        pass

    def InitCashers(self, casherNumber):
        for index in range(casherNumber):
            self._cashers.append(Casher(index, self._salaryRate))

    def RandomCustomerGenerator(self):
        number = random.uniform(0.0, 1.0)
        customerQueue = list()
        if number <= self._storeTrafficRate:
            queueSize = random.randint(self._customerNumberRange[0], self._customerNumberRange[1])
            self._totalCustomer += queueSize
            for i in range(queueSize):
                self._customerId += 1
                shoppingTime = random.randint(self._shoppingTimeSpan[0], self._shoppingTimeSpan[1])
                patienceTime = random.randint(self._patienceTimeSpan[0], self._patienceTimeSpan[1])
                checkoutTime = random.randint(self._checkoutTimeSpan[0], self._checkoutTimeSpan[1])
                profit = checkoutTime * self._profitRate
                customerQueue.append(Customer(self._customerId, shoppingTime, patienceTime, checkoutTime, profit))
        return customerQueue    

    def Run(self, duration):
        while duration >= 0:
            # TBD - business logic
            readyCustomerList = self.ShoppingCustomerUpdate()
            if len(readyCustomerList) != 0:
                self.CustomerGoCheckout(readyCustomerList)

            profit = self.CheckoutUpdate()
            self._profit += profit
            
            # hourly salary logic
            salary = len(self._cashers) * self._salaryRate
            self._profit -= salary

            if profit != 0:
                self._profitHistory.append(self._profit)
            newCustomerList = self.RandomCustomerGenerator()
            if newCustomerList is not None:
                self._customers += newCustomerList
            duration -= 1

        return self._profit

    def CustomerGoCheckout(self, customerList):
        for index in range(len(customerList)):
            customer = customerList.pop(0)
            casherIndex = random.randint(0, self._casherNumber - 1)
            self._cashers[casherIndex].TakeCustomer(customer)

    def ShoppingCustomerUpdate(self):
        readyCustomerList = list()
        for index in range(len(self._customers)):
            customer = self._customers[index]
            customer._shoppingTime -= 1
            if customer._shoppingTime == 0:
                readyCustomerList.append(self._customers[index])
        for customer in readyCustomerList:
            self._customers.remove(customer)
        return readyCustomerList
    
    def CheckoutUpdate(self):
        profit = 0
        for casher in self._cashers:
            profit += casher.CheckoutCustomer()
            lostCustomerNumber = casher.UpdateCustomerStatus()
            profit -= self._lossRate * lostCustomerNumber
            self._totalLostCustomer += lostCustomerNumber
        return profit
        pass

    def CurrentQueue(self):
        queueNumber = 0
        for casher in self._cashers:
            queueNumber += casher.CurrentQueue()
        return queueNumber

class Customer():
    def __init__(self, id, shoppingTime, patienceTime, checkoutTime, profit) -> None:
        self._id = id
        self._shoppingTime = shoppingTime
        self._patienceTime = patienceTime
        self._checkoutTime = checkoutTime
        self._profit = profit
        pass

class Casher():
    def __init__(self, id, salaryRate) -> None:
        self._id = id
        self._salaryRate = salaryRate
        self._customerQueue = list()
        self._currentCustomer = None
        self._currentCheckoutTime = 0
        self._totalCustomer = 0
        self._totalServedCustomer = 0
        self._totalLostCustomer = 0

    def TakeCustomer(self, customer):
        self._customerQueue.append(customer)
        self._totalCustomer += 1

    def CheckoutCustomer(self):
        profit = 0
        if len(self._customerQueue) == 0:
            return 0
        if self._currentCustomer is None:
            self._currentCustomer = self._customerQueue.pop(0)
            self._currentCheckoutTime = self._currentCustomer._checkoutTime
            if self._currentCustomer is None:
                return 0
            
        self._currentCustomer._checkoutTime -= 1
        if self._currentCustomer._checkoutTime == 0:
            profit += self._currentCustomer._profit
            # original logic for the salary comment out if using second salary
            # profit -= self._currentCheckoutTime * self._salaryRate
            self._totalServedCustomer += 1
            self._currentCustomer = None

        return profit
        
    # return number of loss customer
    def UpdateCustomerStatus(self):
        lossCustomerNumber = 0
        removeList = list()
        for i in range(len(self._customerQueue)):
            customer = self._customerQueue[i]
            customer._patienceTime -= 1
            if customer._patienceTime == 0:
                lossCustomerNumber += 1
                removeList.append(customer)
        for customer in removeList:
            self._customerQueue.remove(customer)
        self._totalLostCustomer += lossCustomerNumber
        return lossCustomerNumber
    
    def CurrentQueue(self):
        return len(self._customerQueue) + 1 # plus one current serving customer


import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('./supermarketSettings.xml')
root = tree.getroot()

# Iterate through the <setting> elements and retrieve their values
settings = {}
for setting in root.findall('setting'):
    name = setting.get('name')
    value_elem = setting.find('value')
    if value_elem is not None:
        # For settings with <value> elements, store them as arrays
        values = [int(value.text) if value.text.replace('.', '', 1).isdigit() else value.text for value in setting.findall('value')]
    else:
        # For settings without <value> elements, store the value as-is
        value = setting.get('value')
        values = float(value) if value.replace('.', '', 1).isdigit() else value
    settings[name] = values

statistics = list()
for i in range(int(settings['simulationRounds'])):
    print("*************************************************************************************************")
    print("Simulation Round {0}".format(i))
    print("Simulation time {0}".format(settings['simulationTime']))

    superMarketSimulation = SuperMarketSimulation(int(settings['casherNumber']) + i,
                                              settings['trafficRate'],
                                              settings['customerNumberRange'],
                                              settings['shoppingTimeSpan'],
                                              settings['patienceTimeSpan'],
                                              settings['checkoutTimeSpan'],
                                              settings['profitRate'],
                                              settings['salaryRate'],
                                              settings['lossRate']
                                              )

    superMarketSimulation.Run(settings['simulationTime'])
    print(superMarketSimulation)
    print("profit: {0}".format(superMarketSimulation._profit))
    print("total customers: {0}".format(superMarketSimulation._totalCustomer))
    print("total lost customers: {0}".format(superMarketSimulation._totalLostCustomer))
    print("current shopping customers: {0}".format(len(superMarketSimulation._customers)))
    print("current queue customers: {0}".format(superMarketSimulation.CurrentQueue()))
    for casher in superMarketSimulation._cashers:
        print("casher {0}: total customers = {1}, served customers = {2}, lost customers = {3}, current queue = {4}".format(casher._id, casher._totalCustomer, casher._totalServedCustomer, casher._totalLostCustomer, casher.CurrentQueue()))
    # print(superMarketSimulation._profitHistory)
    statistics.append([superMarketSimulation._casherNumber, superMarketSimulation._profit, superMarketSimulation._totalCustomer, superMarketSimulation._totalLostCustomer])
    print("*************************************************************************************************")


cashers = list()
profits = list()
totalCustomers = list()
lostCustomers = list()
for data in statistics:
    print("casher:{0}, profit:{1}, total customers:{2}, lost customers:{3}".format(data[0], f"{data[1]:.2f}", data[2], data[3]))
    profits.append(data[1])
    totalCustomers.append(data[2])
    lostCustomers.append(data[3])
x = range(0, int(settings['simulationRounds']))
count = 1
plt.figure(figsize=(10, 6))
plt.plot(x, profits, label='Profit')
plt.plot(x, totalCustomers, label='Total Customers')
plt.plot(x, lostCustomers, label='Lost Customers')
plt.legend()
plt.xlabel('Cashers')
plt.ylabel('Profit')
plt.title('Supermarket Simulation')
plt.show()
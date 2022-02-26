# Hash-Function-Analysis

## Introduction
With the growing popularity of the Internet of Things (IoT), more and more devices are being fitted with the ability to connect to the internet. Instead of a home network consisting primarily of PCs, cell phones, and televisions, we are now seeing a much larger variety of connected devices such as light bulbs, door locks, refrigerators, automobiles, thermostats, and even wearables like watches and glasses. However, with so many connected devices in our lives, security becomes a legitimate concern. What if an adversary was able to unlock the smart lock to your house or remotely control your smart car when you’re driving? While devices with faster processors and more RAM may be able to handle the same heavy security applications used on PCs, smart devices with very little resources like lightbulbs or thermostats may not even have a fraction of those resources to spare. How do you protect those devices with limited computing resources? Enter hash functions. A cryptographic hash function is a function which takes an input (or 'message') as some form of data and returns a fixed-size alphanumeric string called a “hash” or “digest.” Not only are hash functions relatively light on resource consumption, but they also cannot be broken and are quite sensitive to changes in data. By hashing a file stored on a connected device, we can continuously measure the integrity of that file by repeatedly hashing it at regular intervals, making sure that the resulting hash remains the same. The purpose of our experiment is to determine/measure the performance of various hash functions on modern architecture that is commonly used in IoT devices. By running many different libraries of hash functions with a fixed set of different-sized data inputs, we can determine which hash function is ideal for processor demand, usage of RAM, or energy consumption. We can also compare the generated hashes to gauge the level of security they offer, especially in regards to collision resistance and reversibility. Whether a smart device is limited by its battery capacity or by processing power, we will be able to deploy the appropriate hash function to meet that particular need. Our initial research suggests that the BLAKE hash family, which includes BLAKE2b and BLAKE2s has a particularly quick runtime when hashing input size under ten megabytes. However, more data collection is required in order to establish a clear ranking of the various hash functions within all three categories of performance.

## Python Libraries/Modules Used
- hashlib (main hash function library)
- time
- timeit
- random
- csv
- Matplotlib
- NumPy
- Pandas
- Seaborn

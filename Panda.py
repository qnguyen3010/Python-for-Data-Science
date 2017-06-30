import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)


# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# Fix import by including index_col
cars2 = pd.read_csv('cars.csv',index_col = 0)

# Print out cars
print(cars2)

# Print out country column as Pandas Series
print(cars2['country'])

# Print out country column as Pandas DataFrame
print(cars2[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars2[["country","drives_right"]])

print(cars2.loc[:,"drives_right"])
print(car2.loc[:,["drives_right"]])
print(car2.loc[:,["cars_per_cap","drives_right"]])

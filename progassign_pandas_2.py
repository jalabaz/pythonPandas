import pandas as pd
cars = pd.read_csv('cars.csv')
print(cars.iloc[0:5,1:10:2])
print('\n',cars[cars['Model'] == 'Mazda RX4'])
print('\n',cars['cyl'][cars['Model']== 'Camaro Z28'])
print('\n', cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']), ['gear','cyl']])
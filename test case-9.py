#53.Food Waste Monitoring System
prepared = int(input("Meals prepared: "))
served = int(input("Meals served: "))

waste = prepared - served
percentage = (waste / prepared) * 100

print("Waste Percentage:", percentage, "%")

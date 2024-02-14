def hotel_cost(num_nights):
  # You can adjust the nightly rate based on your preferences
  nightly_rate = 100
  return num_nights * nightly_rate

def plane_cost(city_flight):
  # Set prices based on destination city
  if city_flight == "New York":
      return 300
  elif city_flight == "Paris":
      return 500
  elif city_flight == "Tokyo":
      return 700
  else:
      # Default cost for other cities
      return 400

def car_rental(rental_days):
  # Set daily rental rate for the car
  daily_rate = 50
  return rental_days * daily_rate

def holiday_cost(hotel, plane, car):
  return hotel + plane + car

# Get user inputs
city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo, etc.): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car: "))

# Calculate costs using functions
hotel = hotel_cost(num_nights)
plane = plane_cost(city_flight)
car = car_rental(rental_days)
total_cost = holiday_cost(hotel, plane, car)

# Print details
print("\nHoliday Details:")
print(f"Destination: {city_flight}")
print(f"Hotel Cost: ${hotel}")
print(f"Flight Cost: ${plane}")
print(f"Car Rental Cost: ${car}")
print(f"Total Holiday Cost: ${total_cost}")

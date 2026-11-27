class InvalidSpeedError(Exception):
     pass
try:
        speed = int(input("Enter speed: "))
        if speed < 0 or speed > 120:
         raise InvalidSpeedError("Speed must be 0 to 120 km/h.")
        print("Valid speed:", speed)
except ValueError:
        print("Enter a whole number.")
except InvalidSpeedError as error:
      print(error)
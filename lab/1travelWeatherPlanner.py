# Build a Travel Weather Planner
# Objective: Fulfill the user stories below and get all the 
# tests to pass to complete the lab.

distance_mi = 0.0 # distance to travel in miles
is_raining = True # boolean representing rainy weather
has_bike = True # boolean if user has a bicycle
has_car = True # boolean if the user has a car
has_ride_share_app = True # boolean representing if user has share app

if not distance_mi:
    print("False")
elif distance_mi <= 1 and not is_raining:
    print("True")
elif distance_mi <= 1 and is_raining:
    print("False")
elif 1 < distance_mi <= 6 and (is_raining and not has_bike):
    print("False")
elif 1 < distance_mi <= 6 and (not is_raining and not has_bike):
    print("False")
elif 1 < distance_mi <= 6 and (has_bike and not is_raining):
    print("True")
elif 1 < distance_mi <= 6 and (has_bike and is_raining):
    print("False")
elif distance_mi > 6 and has_ride_share_app:
    print("True")
elif distance_mi > 6 and has_car:
    print("True")
elif distance_mi > 6 and (not has_car and not has_ride_share_app):
    print("False")
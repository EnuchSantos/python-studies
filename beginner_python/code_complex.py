"""
Muitos if (ruim)
    <- contagem de complexidade (ruim)
"""

speed = 41
car_location = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

car_speed_pass_radar = speed > RADAR_1
car_pass_radar = car_location >= (LOCAL_1 - RADAR_RANGE) and \
    car_location <= (LOCAL_1 + RADAR_RANGE)
multed_car = car_pass_radar and car_speed_pass_radar

if car_speed_pass_radar:
    print('Velocidade do carro passou do radar 1')

if car_pass_radar:
    print('Carro passou o radar 1')

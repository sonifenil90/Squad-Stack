import sys
from middleware import *

def run_input_queries(Parking_Lot, query):

    if query[0] == 'Create_parking_lot':
        Parking_Lot = design_lot_middleware(query[1])

    elif query[0] == 'Park':
        print(park_vehicle_middleware(Parking_Lot, query[1], query[3]))

    elif query[0] == 'Slot_numbers_for_driver_of_age':
        print(get_slot_nos_by_driver_age_middleware(Parking_Lot, query[1]))

    elif query[0] == 'Slot_number_for_car_with_number':
        print(get_slot_no_by_reg_no_middleware(Parking_Lot, query[1]))

    elif query[0] == 'Leave':
        print(depart_vehicle_middleware(Parking_Lot, query[1]))

    elif query[0] == 'Vehicle_registration_number_for_driver_of_age':
        print(get_reg_nos_by_driver_age_middleware(Parking_Lot, query[1]))

    else:
        print('Not a Valid Input. Check Again !!!')

    return Parking_Lot

def read_input_file(file):
    Parking_Lot = None
    with open(file) as file:
        inputs = file.readlines()
        for input in inputs:
            input = input.strip().split()
            Parking_Lot = run_input_queries(Parking_Lot, input)

if __name__ == '__main__':
    print(sys.argv[1])
    read_input_file(sys.argv[1])
    

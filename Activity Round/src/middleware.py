import parking_lot


''' Creates a parking lot of capacity = size '''

def design_lot_middleware(size):
	parking = parking_lot.Parking_Lot()
	parking.design_lot(int(size))
	print('Created parking of ' + size + ' slots')
	return parking


''' Parks the newly arrived vehicle '''

def park_vehicle_middleware(parking, vehicle_reg_no, driver_age):
	
	if parking is None:
		return 'No slots are available'

	available = parking.isAvailable()
	if not available:
		return 'Reached the capacity. No more slots left.'

	valid_slot = parking.park_vehicle(vehicle_reg_no, int(driver_age))

	if valid_slot:
		status = 'Car with vehicle registration number "{0}" '\
			'has been parked at slot number {1}'.format(vehicle_reg_no, valid_slot)
	else:
		status = 'Car could not be parked'

	return status


''' Departure of the vehicle from the parking lot '''

def depart_vehicle_middleware(parking, slot):
	
	if parking is None:
		return 'Parking lot has not been created yet!'
	slot = int(slot)
	capacity = parking.get_capacity()
	if slot < 1 or slot > capacity:
		return 'No such slot exists!'
	car_info = parking.depart_vehicle(slot)
	
	if not car_info:
		status = 'No car found this in this slot!'
	else:
		status = 'Slot number {2} vacated, the car with vehicle registration number "{0}" '\
			'left the space, the driver of the car '\
			'was of age {1}'.format(car_info.vehicle_reg_no, car_info.driver_age, slot)

	return status


''' Returns parking slots where the age of the driver is same the requested age '''

def get_slot_nos_by_driver_age_middleware(parking, driver_age):
	valid_slots = parking.get_slot_nos_by_driver_age(int(driver_age))
	if not valid_slots:
		return 'No car found with driver age - {0}'.format(driver_age)
	status = ', '.join(map(str, valid_slots))
	return status


''' Returns slot in parking lot where the specified car is parked '''

def get_slot_no_by_reg_no_middleware(parking, vehicle_reg_no):
	valid_slot = parking.get_slot_no_by_reg_no(vehicle_reg_no)
	if not valid_slot:
		return 'No such car found!'
	return valid_slot


''' Returns registration number of cars where the drivers of the car are of the specified age '''

def get_reg_nos_by_driver_age_middleware(parking, driver_age):
	valid_regnos = parking.get_reg_nos_by_driver_age(int(driver_age))
	if valid_regnos:
		status = ', '.join(map(str, valid_regnos))
	else:
		status = 'No such cars found!'
	return status

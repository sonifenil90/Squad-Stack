from vehicle import Vechicle_Info

class Parking_Lot:
    ''' Constructor to initialize the parking lot object with the info given in input '''
    def __init__(self):
        self.capacity = None
        self.slots = []
        self.vacant_slots = 0
    
    def design_lot(self, capacity):
        self.capacity = capacity
        self.slots = [None] * capacity
        self.vacant_slots = capacity
        return self.capacity

    def isAvailable(self):
        if self.vacant_slots == 0:
            return False
        else:
            return True

    def get_next_available_slot(self):
        for slot_no in range(self.capacity):
            if self.slots[slot_no] == None:
                return slot_no

    def park_vehicle(self, vehicle_reg_no, driver_age):
        if self.vacant_slots == 0:
            return False
        else:
            slot_no = self.get_next_available_slot()
            self.slots[slot_no] = Vechicle_Info(vehicle_reg_no, driver_age)
            self.vacant_slots -= 1
            slot_no += 1
            return slot_no
    
    def get_capacity(self):
        if self.capacity != None:
            return self.capacity
        else:
            return None

    def depart_vehicle(self, slot_no):
        if self.vacant_slots < self.capacity and self.slots[slot_no - 1] != None:
            vehicle_info = self.slots[slot_no - 1]
            self.slots[slot_no - 1] = None
            self.vacant_slots += 1
            return vehicle_info
        else:
            return False

    def get_reg_nos_by_driver_age(self, driver_age):
        vehicle_reg_nos = []
        for slot in self.slots:
            if slot and slot.driver_age == driver_age:
                vehicle_reg_nos.append(slot.vehicle_reg_no)
        return vehicle_reg_nos

    def get_slot_no_by_reg_no(self, vehicle_reg_no):
        for slot_no, slot in enumerate(self.slots):
            if slot and slot.vehicle_reg_no == vehicle_reg_no:
                return slot_no + 1
            else:
                continue
        return None 

    def get_slot_nos_by_driver_age(self, driver_age):
        slot_nos = []
        for slot_no, slot in enumerate(self.slots):
            if slot and slot.driver_age == driver_age:
                slot_nos.append(slot_no + 1)
        return slot_nos

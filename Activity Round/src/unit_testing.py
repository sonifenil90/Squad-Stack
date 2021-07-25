import unittest
from parking_lot import Parking_Lot

class TestParkingLot(unittest.TestCase):

    def test_design_lot(self):
        parkingLot = Parking_Lot()
        result = parkingLot.design_lot(4)
        self.assertEqual(4, result)

    def test_park_vehicle(self):
        parkingLot = Parking_Lot()
        result = parkingLot.design_lot(4)
        result = parkingLot.park_vehicle('KA-01-HH-1234', 21)
        self.assertNotEqual(-1, result)

    def test_depart_vehicle(self):
        parkingLot = Parking_Lot()
        result = parkingLot.design_lot(4)
        result = parkingLot.park_vehicle('KA-01-HH-1234', 21)
        result = parkingLot.depart_vehicle(2)
        self.assertEqual(False, result)

    def test_get_reg_nos_by_driver_age(self):
        parkingLot = Parking_Lot()
        result = parkingLot.design_lot(4)
        result = parkingLot.park_vehicle('KA-01-HH-1234', 21)
        result = parkingLot.park_vehicle('PB-01-HH-7894', 21)
        regnos = parkingLot.get_reg_nos_by_driver_age(21)
        self.assertIn("KA-01-HH-1234", regnos)
        self.assertIn("PB-01-HH-7894", regnos)

    def test_get_slot_no_by_reg_no(self):
        parkingLot = Parking_Lot()
        result = parkingLot.design_lot(4)
        result = parkingLot.park_vehicle('KA-01-HH-1234', 21)
        result = parkingLot.park_vehicle('PB-01-HH-7894', 21)
        slotNo = parkingLot.get_slot_no_by_reg_no('PB-01-HH-7894')
        self.assertEqual(2,slotNo)

    def test_get_slot_nos_by_driver_age(self):
        parkingLot = Parking_Lot()
        result = parkingLot.design_lot(4)
        result = parkingLot.park_vehicle('KA-01-HH-1234', 21)
        result = parkingLot.park_vehicle('PB-01-HH-7894', 21)
        slotNos = parkingLot.get_slot_nos_by_driver_age(21)
        self.assertIn(1, slotNos)
        self.assertIn(2, slotNos)

if __name__ == '__main__':
	unittest.main()

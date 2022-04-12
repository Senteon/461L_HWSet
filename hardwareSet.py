# Class representing a hardware set with fixed capacity
class HWSet():
    capacity = 0
    availability = 0
    num = 0

    # Initialize HWSet with specified quantity and set availability to same value
    def __init__(self, num, cap) -> None:
        # HWSet 1 or HWSet 2
        self.num = num
        self.capacity = cap
        self.availability = self.capacity

    # Return availability
    def get_availability(self) -> int:
        return self.availability

    # Return capacity
    def get_capacity(self) -> int:
        return self.capacity

    # Use simple math to determine checked out quantity
    def get_checkedout_qty(self) -> int:
        return self.capacity - self.availability
        
    # Check out a certain quantity
    def check_out(self, qty) -> None:
        # Case for user requesting more quantity than available
        if (qty > self.availability):
            # No remaining quantity
            if (self.availability == 0):
                return -1
            # Give user rest of available capacity
            else:
                ret = self.availability
                self.availability = 0
                return ret
        # Case for user requesting less quantity than available
        else:
            # Give user requested quantity
            self.availability -= qty
            return 0
    
    # Check in a certain quantity
    def check_in(self, qty) -> None:
        self.availability += qty

    
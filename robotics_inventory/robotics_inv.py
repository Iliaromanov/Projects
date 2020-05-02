
import datetime


class BaseRecord:
    def __init__(self, id: int):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.id = id


class Bin(BaseRecord):
    all_bins = []

    def __init__(self, location: str, part_id: str, qty_in_bin: int):
        id = len(Bin.all_bins)
        super().__init__(id)
        self.location = location
        self.part_id = part_id
        self._qty_in_bin = qty_in_bin
        Bin.all_bins.append(self)

    def get_qty_in_bin(self):
        return self._qty_in_bin

    def set_qty_in_bin(self, new_value):
        assert new_value is int
        assert new_value >= 0
        self._qty_in_bin = new_value
        self.updated_at = datetime.datetime.now()


class Part(BaseRecord):
    all_parts = []

    def __init__(self, name: str, quantity: int, bin_id: int):
        id = len(Part.all_parts)
        super().__init__(id)
        self.name = name
        self._quantity = quantity
        self.bin_id = bin_id
        Part.all_parts.append(self)

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, new_value):
        assert new_value is int
        assert new_value >= 0
        self._quantity = new_value
        self.updated_at = datetime.datetime.now()


class User:
    all_users = []

    def __init__(self, email: str, student_num: int):
        self.email = email
        self.student_num = student_num
        User.all_users.append(self)


class Log(BaseRecord):
    all_logs = []

    def __init__(self, user_id: int, part_id: int, quantity: int):
        self.user_id = user_id
        self.part_id = part_id
        self._quantity = quantity
        Log.all_logs.append(self)

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, new_value):
        assert new_value is int
        assert new_value >= 0
        self._quantity = new_value
        self.updated_at = datetime.datetime.now()


class InventoryManager:
    def __init__(self):
        self.parts = Part.all_parts
        self.bins = Bin.all_bins
        self.logs = Log.all_logs
        self.users = User.all_users

    def find_bin_by_location(self, location: str) -> Bin:
        for bin in self.bins:
            if bin.location == location:
                return bin

    def find_user_by_student_num(self, num: int) -> User:
        for user in self.users:
            if user.student_num == num:
                return user

    def add_part(self, name, quantity, bin_location) -> None:
        bin_id = self.find_bin_by_location(bin_location).id
        Part(name, quantity, bin_id)

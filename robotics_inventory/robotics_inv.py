import os
import datetime


class BaseRecord:
    def __init__(self, id: int):
        self.created_at = datetime.datetime.now
        self.updated_at = datetime.datetime.now()
        self.id = id


class User(BaseRecord):
    all_users = []

    def __init__(self, email: str, student_num: int):
        id = len(User.all_users)
        super().__init__(id)
        self.email = email
        self.student_num = student_num
        User.all_users.append(self)


class Part(BaseRecord):
    all_parts = []

    def __init__(self, name: str, quantity: int, barcode: str, bin_id: int):
        id = len(Part.all_parts)
        super().__init__(id)
        self.name = name
        self.quantity = quantity
        self._barcode = barcode
        self.bin_id = bin_id
        Part.all_parts.append(self)

        for bin in Bin.all_bins:
            if bin.id == bin_id:
                bin.qty_in_bin += quantity

    def get_barcode(self):
        return self._barcode

    def set_barcode(self, new_barcode: str):
        assert new_barcode is str
        self.barcode = new_barcode
        self.updated_at = datetime.datetime.now()


class Bin(BaseRecord):
    all_bins = []

    def __init__(self, location: str, part_id: int):
        id = len(Bin.all_bins)
        super().__init__(id)
        self._location = location
        self.part_id = part_id
        self.qty_in_bin = 0
        Bin.all_bins.append(self)

    def get_location(self):
        return self._location

    def set_location(self, new_location: str):
        assert new_location is str
        assert len(new_location) <= 2
        self._location = new_location
        self.updated_at == datetime.datetime.now()
        

class Log(BaseRecord):
    all_logs = []

    def __init__(self, user_id, part_id, quantity):
        id = len(Log.all_logs)
        super().__init__(id)
        self.user_id = user_id
        self.part_id = part_id
        self.quantity = quantity
        Log.all_logs.append(self)


class InventoryManager:
    def __init__(self):
        self.users = User.all_users
        self.parts = Part.all_parts
        self.bins = Bin.all_bins
        self.logs = Log.all_logs

    def create_user(self, email: str, student_num: int) -> None:
        User(email, student_num)

    def find_bin_by_location(self, location: str) -> Bin:
        for bin in self.bins:
            if bin._location == location:
                return bin

    def find_bin_by_id(self, bin_id: int) -> Bin:
        for bin in self.bins:
            if bin.id == bin_id:
                return bin

    def find_user_by_student_num(self, num: int) -> User:
        for user in self.users:
            if user.student_num == num:
                return user

    def find_part_by_barcode(self, barcode: str) -> Part:
        for part in self.parts:
            if part._barcode == barcode:
                return part

    def add_part(self, name, quantity, barcode, bin_location) -> None:
        bin = self.find_bin_by_location(bin_location)
        bin_id = bin.id
        Part(name, quantity, barcode, bin_id)
        bin.qty_in_bin += quantity

    def sign_out(self, part: Part, quantity: int, user: User) -> None:
        bin_id = part.bin_id
        associated_bin = self.find_bin_by_id(bin_id)

        if associated_bin.qty_in_bin >= quantity:
            associated_bin.qty_in_bin -= quantity

        user_id = user.student_num
        part_id = part.id

        Log(user_id, part_id, -1 * quantity)

    def return_part(self, part: Part, quantity: int, user: User) -> None:
        bin_id = part.bin_id
        associated_bin = self.find_bin_by_id(bin_id)

        if part.quantity >= quantity:
            associated_bin.qty_in_bin += quantity

        user_id = user.student_num
        part_id = part.id

        Log(user_id, part_id, quantity)


if __name__ == "__main__":
    os.system("pytest")
#    os.system("mypy main.py --disallow-untyped-defs")
    os.system("pycodestyle main.py --ignore=E501,W")

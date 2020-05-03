class RequestPoolEntity:
    def __init__(self, AddressSpace: str, Pool: str = None, SubPool: str = None, Options: dict = None, V6: bool = None):
        self.AddressSpace = AddressSpace
        self.Pool = Pool
        self.SubPool = SubPool
        self.Options = {} if Options is None else Options
        self.V6 = V6


class ReleasePoolEntity:
    def __init__(self, PoolID: str):
        self.PoolID = PoolID


class RequestAddressEntity:
    def __init__(self, PoolID: str, Address: str = None, Options: dict = None):
        self.PoolID = PoolID
        self.Address = Address
        self.Options = {} if Options is None else Options


class ReleaseAddressEntity:
    def __init__(self, PoolID: str, Address: str):
        self.PoolID = PoolID
        self.Address = Address

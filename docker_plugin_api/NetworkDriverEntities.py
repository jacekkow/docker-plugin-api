class NetworkIpDataEntity:
    def __init__(self, AddressSpace: str, Pool: str, Gateway: str, AuxAddresses: dict = None):
        if AuxAddresses is None:
            AuxAddresses = {}

        self.AddressSpace = AddressSpace
        self.Pool = Pool
        self.Gateway = Gateway
        self.AuxAddresses = AuxAddresses


class NetworkCreateEntity:
    def __init__(self, NetworkID: str, IPv4Data: list = None, IPv6Data: list = None, Options: dict = None):
        if IPv6Data is None:
            IPv6Data = []
        if IPv4Data is None:
            IPv4Data = []
        if Options is None:
            Options = {}

        self.NetworkID = NetworkID
        self.IPv4 = []
        for ipv4_data in IPv4Data:
            self.IPv4.append(NetworkIpDataEntity(**ipv4_data))
        self.IPv6 = []
        for ipv6_data in IPv6Data:
            self.IPv6.append(NetworkIpDataEntity(**ipv6_data))
        self.Options = Options


class NetworkDeleteEntity:
    def __init__(self, NetworkID: str):
        self.NetworkID = NetworkID


class InterfaceEntity:
    def __init__(self, Address: str, AddressIPv6: str, MacAddress: str):
        self.Address = Address
        self.AddressIPv6 = AddressIPv6
        self.MacAddress = MacAddress


class EndpointCreateEntity:
    def __init__(self, NetworkID: str, EndpointID: str, Interface: dict, Options: dict = None):
        if Options is None:
            Options = {}

        self.NetworkID = NetworkID
        self.EndpointID = EndpointID
        self.Interface = InterfaceEntity(**Interface)
        self.Options = Options


class EndpointOperInfoEntity:
    def __init__(self, NetworkID: str, EndpointID: str):
        self.NetworkID = NetworkID
        self.EndpointID = EndpointID


class EndpointDeleteEntity:
    def __init__(self, NetworkID: str, EndpointID: str):
        self.NetworkID = NetworkID
        self.EndpointID = EndpointID


class JoinEntity:
    def __init__(self, NetworkID: str, EndpointID: str, SandboxKey: str, Options: dict = None):
        if Options is None:
            Options = {}

        self.NetworkID = NetworkID
        self.EndpointID = EndpointID
        self.SandboxKey = SandboxKey
        self.Options = Options


class LeaveEntity:
    def __init__(self, NetworkID: str, EndpointID: str):
        self.NetworkID = NetworkID
        self.EndpointID = EndpointID


class DiscoverNewEntity:
    def __init__(self, DiscoveryType: int, DiscoveryData: dict = None):
        if DiscoveryData is None:
            DiscoveryData = {}

        self.DiscoveryType = DiscoveryType
        self.DiscoveryData = DiscoveryData


class DiscoverDeleteEntity:
    def __init__(self, DiscoveryType: int, DiscoveryData: dict = None):
        if DiscoveryData is None:
            DiscoveryData = {}

        self.DiscoveryType = DiscoveryType
        self.DiscoveryData = DiscoveryData


class ProgramExternalConnectivityEntity:
    def __init__(self, NetworkID: str, EndpointID: str, Options: dict = None):
        if Options is None:
            Options = {}

        self.NetworkID = NetworkID
        self.EndpointID = EndpointID
        self.Options = Options


class RevokeExternalConnectivityEntity:
    def __init__(self, NetworkID: str, EndpointID: str):
        self.NetworkID = NetworkID
        self.EndpointID = EndpointID

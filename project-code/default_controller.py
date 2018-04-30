import connexion
import six

from swagger_server.models.flavor import Flavor  # noqa: E501
from swagger_server.models.image import Image  # noqa: E501
from swagger_server.models.keypair import Keypair # noqa: E501
from swagger_server.models.network import Network  # noqa: E501
from swagger_server.models.server import Server  # noqa: E501
from swagger_server.models.subnet import Subnet  # noqa: E501
from swagger_server import util

import openstack
conn = openstack.connect(cloud="cham")
KEYFILE = "gen-keys"

def create_network(network=None):  # noqa: E501
    """create_network

    Create a new network with the sepcified parameters # noqa: E501

    :param network: object specifying network to be created
    :type network: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        network = Network.from_dict(connexion.request.get_json())  # noqa: E501

    new_network= conn.network.create_network(name = network.name)
                                         # subnets = network.subnets,
                                         # mtu = network.mtu,
                                         # is_router_external =
                                         # network.is_router_external)
    return new_network.to_dict()
    # except:
    #     return "an error occured, network could not be created"

def create_server(server=None):  # noqa: E501
    """create_server

    Create a server with the given parameters # noqa: E501

    :param server: object specifying server to be created
    :type server: dict | bytes

    :rtype: Server
    """
    if connexion.request.is_json:
         server = Server.from_dict(connexion.request.get_json())  # noqa: E501
    print(server)
    try:
        new_server = conn.compute.create_server(name = server.name,
                                                image_id=server.image_id,
                                                flavor_id = server.flavour_id,
                                                networks = [{"uuid":
                                                             server.network}],
                                                key_name = server.keypair)
    
        new_server = conn.compute.wait_for_server(new_server)
        return new_server.to_dict()
    except:
        return "An Error Occured, Can't create server"

def delete_network(network=None):  # noqa: E501
    """delete_network

    Delete a new network with the sepcified name # noqa: E501

    :param network: object specifying network to be deleted
    :type network: dict | bytes

    :rtype: Network
    """
    if connexion.request.is_json:
        network = Network.from_dict(connexion.request.get_json())  # noqa: E501

    del_net = conn.network.find_network(network.name)
    if not del_net:
        return "Cant find the specified network"
    for subnet in del_net.subnet_ids:
        conn.network.delete_subnet(subnet)
    conn.network.delete_network(del_net)
    return del_net.to_dict()


def get_flavors():  # noqa: E501
    """get_flavors

    Returns a list of all available Flavors # noqa: E501


    :rtype: List[Flavor]
    """
    flavor_list = []
    for flavor in conn.compute.flavors():
        flav_dict = flavor.to_dict()
        name = flav_dict["name"]
        id = flav_dict["id"]
        ram = flav_dict["ram"]
        disk = flav_dict["disk"]
        vcpus = flav_dict["vcpus"]
        flav_obj = Flavor(name=name,
                          id=id,
                          ram=ram,
                          disk=disk,
                          vcpus=vcpus)
        flavor_list.append(flav_obj)
    return flavor_list


def get_image_by_id(name):  # noqa: E501
    """get_image_by_id

    Returns details of the image with the given name # noqa: E501

    :param image_name: name of the image
    :type image_name: str

    :rtype: Image
    """
    images = get_images()
    for image in images:
        print(str(image.name))
        print(name)
        if str(image.name) == name:
            return image
        else:
            return 'Image Not Found'


def get_images():  # noqa: E501
    """get_images

    Returns a list of all available Images # noqa: E501


    :rtype: List[Image]
    """
    image_list = []
    for image in conn.compute.images():
        image_dict = image.to_dict()
        name = image_dict["name"]
        id = image_dict["id"]
        min_ram = image_dict["min_ram"]
        min_disk = image_dict["min_disk"]
        updated_at = image_dict["updated_at"]
        status = image_dict["status"]
        size = image_dict["size"]
        image_obj = Image(name = name,
                          id=id,
                          min_disk = min_disk,
                          min_ram = min_ram,
                          status = status,
                          updated_at = updated_at,
                          size = size)
        image_list.append(image_obj)
    return image_list


def get_keys():  # noqa: E501
    """get_keys:
    Returns a List of available keypairs # noqa: E501
    :rtype: List[Keypair]
    """
    keys_list = []
    for keys in conn.compute.keypairs():
        key_dict = keys.to_dict()
        key_obj = Keypair(name = key_dict["name"],
                          public_key = key_dict["public_key"])
        keys_list.append(key_obj)
    return keys_list



def get_networks():  # noqa: E501
    """get_networks

    Returns a List of all Networks # noqa: E501


    :rtype: List[Network]
    """
    network_list = []
    for network in conn.network.networks():
        net_dict = network.to_dict()
        name = net_dict["name"]
        id = net_dict["id"]
        status = net_dict["status"]
        mtu = net_dict["mtu"]
        is_router_external = net_dict["is_router_external"]
        subnets = net_dict["subnet_ids"]
        net_obj = Network(name = name,
                          id = id,
                          subnets = subnets,
                          status = status,
                          mtu = mtu,
                          is_router_external = is_router_external)
        network_list.append(net_obj)
    return network_list


def get_servers():  # noqa: E501
    """get_servers

    Returns a List of all VMs # noqa: E501


    :rtype: List[Server]
    """
    server_list = []
    for server in conn.compute.servers():
        server_dict = server.to_dict()
        server_name = server_dict["name"]
        print(server_name)
        image_id = server_dict["image_id"]
        flavor_id = server_dict["flavor"]['id']
        floating_ip = None
        found = False
        
        for name, net_list in server_dict["addresses"].items():
            for item in net_list:
                if item["OS-EXT-IPS:type"] == 'floating':
                    floating_ip = item["addr"]
                    found = True
                    break
            if found:
                break
            
        status = server_dict["status"]
        created_at = server_dict["created_at"]
        security_groups = server_dict["security_groups"]
        server_obj = Server(name = server_name,
                            image_id = image_id,
                            flavour_id = flavor_id,
                            floating_ip = floating_ip,
                            status = status,
                            created_at = created_at,
                            security_groups = security_groups)
                            
        server_list.append(server_obj)
    return server_list


def get_subnets():  # noqa: E501
    """get_subnets

    Returns a List of all Subnets # noqa: E501


    :rtype: List[Subnet]
    """
    subnet_list = []
    for subnet in conn.network.subnets():
        net_dict = subnet.to_dict()
        name = net_dict["name"]
        id = net_dict["id"]
        dns_nameservers = net_dict['dns_nameservers']
        project_id = net_dict["project_id"]
        is_dhcp_enabled = net_dict["is_dhcp_enabled"]
        net_obj = Subnet(name = name,
                         #id = id,
                         dns_nameservers = dns_nameservers,
                         project_id = project_id,
                         is_dhcp_enabled = is_dhcp_enabled)
        subnet_list.append(net_obj)
    return subnet_list
    


def start_server(server=None):  # noqa: E501
    """start_server

    start a server with the given parameters # noqa: E501

    :param server: object specifying server to be created
    :type server: dict | bytes

    :rtype: Server
    """
    if connexion.request.is_json:
        server = Server.from_dict(connexion.request.get_json())  # noqa: E501
    
    stack_server = conn.compute.find_server(server.name)
    if not stack_server:
        return 'Server Not Found'
    else:
        conn.compute.start_server(stack_server)
        return server

def stop_server(server=None):  # noqa: E501
    """stop_server

    stop a server with the given parameters # noqa: E501

    :param server: object specifying server to be created
    :type server: dict | bytes

    :rtype: Server
    """
    if connexion.request.is_json:
        server = Server.from_dict(connexion.request.get_json())  # noqa: E501

    stack_server = conn.compute.find_server(server.name)
    if not stack_server:
        return 'Server Not Found'
    else:
        conn.compute.stop_server(stack_server)
        return server

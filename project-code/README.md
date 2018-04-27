### Swagger service for openstack

* Use the Makefile to start the service
  This will install all requirements and fetch swagger-codegen
        make
	make run

* To clean the directory run 

     	make clean

* The APIs available are:
      GET: /cloudmesh/openstack/flavors: List all flavors
      GET: /cloudmesh/openstack/images: List all images
      GET: /cloudmesh/openstack/image/{name}: List image with the given name
      GET: /cloudmesh/openstack/networks: List all available networks
      GET: /cloudmesh/openstack/networks/subnets : List all available subnets
      GET: /cloudmesh/openstack/servers : lists all servers
      GET: /cloudmesh/openstack/keypairs : List of all available keypairs
      POST: /cloudmesh/openstack/server/create : create a server
      	    curl -H "Content-Type:application/json" -d '{"name": "test-vm-503",\
	    "flavour": "1", "image": "59876aa4-4d5e-4037-a7be-088998e53e6b",\
	    "keypair":<keyname>,\
	    "network":"dbf29083-ff90-406e-b69a-b1d93b8f0a2d"}' \
	     http://localhost:8080/cloudmesh/openstack/server/create

      POST: /cloudmesh/openstack/server/start : start the server with given name
      POST: /cloudmesh/openstack/server/stop : stop the server with given name
## Swagger service for openstack

### Starting the service with the help of docker

* To start the service using Docker first build the docker image
  and start the service:
  
  	make docker-build
		make docker-start

* To stop the servive run the command:

     	  make docker-stop

* To remove the containers created and clean the directory run

     	    make-clean

### Testing with the help of docker
The following commands should be used to test the various endpoints

* **make test-get-flavors**: get a list of all available flavors
* **make test-get-images**: get a list of all available images
* **make test-get-image-by-name**: get the image *CC-ubuntu16.04*
* **make test-get-keypairs**: get a list of all available keypairs
* **make test-get-networks**: get a list of all available networks
* **make test-get-subnets**: get a list of all available flavors
* **make test-get-servers**: get a list of all available servers

* **make test-create-keypair**: create a new keypair named *test-key*
* **make test-create-network**: create a new network named *test-net*

* **make test-delete-keypair**: delete the keypair named *test-key*
* **make test-delete-keypair**: create the network named *test-net*

To test server commands run
   export SERVER_NAME=<name_of_server>
   

* **make test-server-start**: start the server with name $(SERVER_NAME)
* **make test-server-stop**: stop the server with name $(SERVER_NAME)
* **make test-server-create**: create a new server with name $(SERVER_NAME)

* Use the Makefile to start the service without docker
  This will install all requirements and fetch swagger-codegen
  
        make
		make run

* To clean the directory run 

     	make clean

* The endpoints available are:

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
      POST: /cloudmesh/openstack/network/create : create a new network with
      	    specified name
      POST: /cloudmesh/openstack/keypair/create : create a new compute keypair
      	    with the given name
      DELETE: /cloudmesh/openstack/network/delete : delete a specified network
      DELETE: /cloudmesh/openstack/keypair/delete : delete a keypair with the
      	      given name

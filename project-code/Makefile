# assumes swager_codegen environment variable contains
# the path to swagger codegen jarfile


SPEC=devstack.yml
SERVICE_NAME=cloudmesh_openstack_service
swagger_codegen=java -jar swagger-codegen-cli.jar
#swagger_codegen=java -jar ~/swagger/swagger-codegen-cli-2.3.1.jar

all: fetch generate requirements
	@echo "DONE"

docker-build:
	@echo "BUILDING IMAGE"
	docker build . -t cloudmesh/openstack
	@echo "IMAGE BUILT SUCCESSFULLY"

docker-start:

	docker run --name  $(SERVICE_NAME) \
	-p 8080:8080 -d cloudmesh/openstack

	@echo "service running inside container 'service' \
	mapped to port 8080 of host"

docker-stop:
	docker stop $(SERVICE_NAME)
fetch:
	wget http://central.maven.org/maven2/io/swagger/\
	swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar \
	-O swagger-codegen-cli.jar

generate:
	$(swagger_codegen) generate \
		-i $(SPEC) \
		-l python-flask \
		-o server/devstack/flaskConnexion \
		-D supportPython2=true 
	@echo "generated code"
	cp *_controller.py server/devstack/flaskConnexion/swagger_server/controllers/
	cp clouds.yaml server/devstack/flaskConnexion/
	@echo "copied"
run:
	cd server/devstack/flaskConnexion &&\
	python -m swagger_server

requirements:
	pip install -r requirements.txt
	cd server/devstack/flaskConnexion; pip install -r requirements.txt

clean:
	rm -rf server/
	rm swagger-codegen-cli.jar
	docker rm $(SERVICE_NAME)

test-get-flavors:
	curl http://localhost:8080/cloudmesh/openstack/flavors
test-get-images:
	curl http://localhost:8080/cloudmesh/openstack/images
test-get-image-by-name:
	curl http://localhost:8080/cloudmesh/openstack/image/CC-Ubuntu16.04
test-get-servers:
	curl http://localhost:8080/cloudmesh/openstack/servers
test-server-start:
	curl -H "Content-Type:application/json" -d '{"name": "${SERVER_NAME}", "flavour": "1",	"image": "59876aa4-4d5e-4037-a7be-088998e53e6b", "keypair":"gen-keys",  "network":"dbf29083-ff90-406e-b69a-b1d93b8f0a2d"}' http://localhost:8080/cloudmesh/openstack/server/start

test-server-stop:

	curl -H "Content-Type:application/json"  -d '{"name": "${SERVER_NAME}", "flavour": "1", "image": "59876aa4-4d5e-4037-a7be-088998e53e6b","keypair":"gen-keys", "network":"dbf29083-ff90-406e-b69a-b1d93b8f0a2d"}' http://localhost:8080/cloudmesh/openstack/server/stop

test-server-create:
	curl -H "Content-Type:application/json"  -d '{"name": "test-vm-503", "flavour": "1", "image": "59876aa4-4d5e-4037-a7be-088998e53e6b","keypair":"gen-keys", "network":"dbf29083-ff90-406e-b69a-b1d93b8f0a2d"}' http://localhost:8080/cloudmesh/openstack/server/create

test-get-networks:
	curl http://localhost:8080/cloudmesh/openstack/networks
test-create-network:
	curl -H "Content-Type:application/json"  \
	-d '{"name": "test-net"}' \
	http://localhost:8080/cloudmesh/openstack/network/create
test-delete-network:
	curl -H "Content-Type:application/json"  \
	-d '{"name": "test-net"}' \
	http://localhost:8080/cloudmesh/openstack/network/delete \
	-X DELETE

test-get-subnets:
	curl http://localhost:8080/cloudmesh/openstack/networks/subnets
test-get-keypairs:
	curl http://localhost:8080/cloudmesh/openstack/keypairs
test-create-keypair:
	 curl -H "Content-Type:application/json"  \
	-d '{"name": "test-key"}' \
	http://localhost:8080/cloudmesh/openstack/keypair/create
test-delete-keypair:
	 curl -H "Content-Type:application/json"  \
	-d '{"name": "test-key"}' \
	http://localhost:8080/cloudmesh/openstack/keypair/delete \
	-X DELETE

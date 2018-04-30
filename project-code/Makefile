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

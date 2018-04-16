# assumes swager_codegen environment variable contains
# the path to swagger codegen jarfile


SPEC=virtual_dir_v0_0_3.yml
DB=${mongo_path}
DB_NAME=cloudmesh_vdir_db
SERVICE_NAME=cloudmesh_vdir_service
swagger_codegen="java -jar swagger-codegen-cli.jar"

all: fetch generate requirements
	@echo "DONE"

docker-build:
	@echo "BUILDING IMAGE"
	docker build . -t cloudmesh/virtualdirectory
	@echo "IMAGE BUILT SUCCESSFULLY"

docker-start:
	docker pull mongo
	docker run --name  $(DB_NAME) \
	--volume $(DB):/data/db -p 27017:27017 -d mongo

	@echo "mongodb running inside container 'db' mapped \
	to port 27017"

	docker run --name  $(SERVICE_NAME) \
	-p 8080:8080 -d cloudmesh/virtualdirectory

	@echo "service running inside container 'service' \
	mapped to port 8080 of host"

docker-stop:
	docker stop $(DB_NAME)
	docker stop $(SERVICE_NAME)
fetch:
	wget http://central.maven.org/maven2/io/swagger/\
	swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar \
	-O swagger-codegen-cli.jar && \

generate:
	$(swagger_codegen) generate \
		-i $(SPEC) \
		-l python-flask \
		-o server/virtual_directory/flaskConnexion \
		-D supportPython2=true 
	@echo "generated code"
	cp *_controller.py server/virtual_directory/flaskConnexion/swagger_server/controllers/  
	@echo "copied"
run:
	cd server/virtual_directory/flaskConnexion/ &&\
	python -m swagger_server

requirements:
	pip install -r requirements.txt
	cd server/virtual_directory/flaskConnexion; pip install -r requirements.txt

clean:
	rm swagger-codegen-cli.jar
	rm -rf server/
	docker rm $(DB_NAME)
	docker rm $(SERVICE_NAME)

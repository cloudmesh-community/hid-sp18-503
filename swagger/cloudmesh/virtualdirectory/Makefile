# assumes swager_codegen environment variable contains
# the path to swagger codegen jarfile

SWAGGER=${swagger_codegen}
SPEC=virtual_dir_v3.yml

all: generate requirements run
	@echo "DONE"

generate:
	$(SWAGGER) generate \
		-i $(SPEC) \
		-l python-flask \
		-o server/virtual_directory/flaskConnexion \
		-D supportPython2=true
	cp *_controller.py server/virtual_directory/flaskConnexion/swagger_server/controllers/  

run:
	cd server/virtual_directory/flaskConnexion/ &&\
	python -m swagger_server

requirements:
	pip install -r requirements.txt
	cd server/virtual_directory/flaskConnexion; pip install -r requirements.txt

clean:
	rm -rf server/

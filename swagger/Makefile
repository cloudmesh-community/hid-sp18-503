# assumes swager_codegen environment variable contains
# the path to swagger codegen jarfile
all:

	${swagger_codegen} generate \
		-i virtual_dir_v3.yml \
		-l python-flask \
		-o server/virtual_directory/flaskConnexion \
		-D supportPython2=true

	cp default_controller.py server/virtual_directory/flaskConnexion/swagger_server/controllers/default_controller.py  
	#cp *_controller.py server/virtual_directory/flaskConnexion/swagger_server/controllers/  

run:
	cd server/virtual_directory/flaskConnexion/ &&\
	python -m swagger_server

clean:

	rm -rf server/

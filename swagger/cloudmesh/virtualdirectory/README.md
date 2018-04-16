### Swagger service for virtual directory

* Prerequisite: docker should be installed
  Also note that the Makefile requires the environment variable
  *mongo_path* that contains the path to the mongo db directory
  for example ~/cloudmesh/data/db
  The program assumes that data resides in a database named "rest_db"
  inside a collection named "dirs"

  	  export mongo_path = /path to mongo db directory/       

  This path is used as the volume for the mongodb container, whose image
  will be pulled form docker hub
  
* Use the Makefile to build docker image for the service using

      make docker-build

* Use the Makefile to start the service,
  
	make docker-start
	
  This will start 2 containers, one with the mongodb database,
  (mapped to host port 27017) and the other with run the swagger
  service (mapped to host port 8080)

  The endpoints available are:

      /cloudmesh/virtualdirectory/dirs : lists all directories
      /cloudmesh/virtualdirectory/dir/{dirName}: get data for {dirName}


* To stop the service and clean the directory run

     make clean
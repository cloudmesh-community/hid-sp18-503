### Swagger service for virtual directory

* prerequisite: store the path to swagger codegen jarfile in an
  environment variable named swagger_codegen
  
      export swagger_codegen="path to swagger codegen jarfile"

* To generate swagger code run the command

      make

* to run the code, execute the following

      make run

* To remove swagger codegen files run the command, and clean the
  directory

       make clean

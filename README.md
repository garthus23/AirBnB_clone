# AirBnB_clone

it will be the clone of the AirBnB Website !

## *** The Console ***

 -  Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances.
 -  Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
 -  Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
 -  Create the first abstracted storage engine of the project: File storage.
 -  Create all unittests to validate all our classes and storage engine.

 How to launch it :
 
     ./console.py
  
 How to use it :
 
  - (hbnb) create BaseModel : Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
  - (hbnb) show BaseModel 1234-1234-1234 : Prints the string representation of an instance based on the class name and id.
  - (hbnb) destroy BaseModel 1234-1234-1234 : Deletes an instance based on the class name and id (in progress).
  - (hbnb) all : Prints all string representation of all instances based or not on the class name.
  - (hbnb) update \<class name' 'id' 'attribute name' 'attribute value' : Updates an instance based on the class name and id (in progress)
 

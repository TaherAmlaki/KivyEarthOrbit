# Earth Orbit Game 
## With Python and Kivy

This is a simple game I created using Python for entities and game logic, and Kivy for GUI.
As the player you control movements of the Sun and simultaneously Earth is orbiting around sun. Earth is 
under sun's gravity. You can adjust Earth's speed but gravity is always there. The goal is to keep 
the earth in the screen as long as possible. If Earth gets too close to sun, gravity will win and Earth picks up 
speed and will go out of the screen.

Design

* EarthOrbitApp
    * A Kivy App instance which will initialize the app and screens.

* Entity: 
    * Each entity class inherits from base entity class which has (x,y) coordinates, velocities
    and line points which is a list of points that the entity passes through and is updated at each frame.
    * Base entity has move method which is an abstract method and should be implemented by entities.

* IntroductionScreen:
    * Label widget to have explanation of the game for user
    * _on_start_clicked() method to tell Kivy to go to the next page
    
* GameScreen:
    * Earth entity
    * Sun entity
    * _move() method which will execute move for all entities
    * Keyboard registration methods to register, validate, and execute user's keyboard actions
    * Pause/Continue click registration 
    
* Background:
    * A Kivy widget to display a background image which is present in all the screens.
     
    
      


'''Draw a class inheritance diagram for the following set of classes:
    • Class Goat extends object and adds an instance variable tail and methods milk( ) and jump( ).
    • Class Pig extends object and adds an instance variable nose and methods eat(food) and wallow( ).
    • Class Horse extends object and adds instance variables height and color, and methods run( ) and jump( ).
    • Class Racer extends Horse and adds a method race( ).
    • Class Equestrian extends Horse, adding an instance variable weight and methods trot( ) and is trained( ).
'''

'''
                        Object
                       /   |   \
                    Horse  Pig  Goat
                   /    \
                Racer  Equestrian
    
    class diagram
    |----------------------------------------|-------------------|-------------------|
    |Class: Horse                            |Class: pig         |Class: Goat        |
    |----------------------------------------|-------------------|-------------------|
    |Instance Variables                      |Instance Variables |Instance Variables |
    | _height                                | _nose             | _tail             |
    | _color                                 |                   |                   |
    |----------------------------------------|-------------------|-------------------|
    |Methods                                 |Methods            |Methods            |
    | run()                                  | eat(food)         | milk()            |
    | jump()                                 | wallow()          | jump()            |
    |----------------------------------------|-------------------|-------------------|
    |Class: Racer        |Class: Equestrian  |
    |--------------------|-------------------|
    |Instance Variables  |Instance Variables |
    |                    | _weight           |
    |--------------------|-------------------|
    |Methods             |Methods            |
    | race()             | trot()            |
    |                    | is trained()      |
    |--------------------|-------------------|
'''
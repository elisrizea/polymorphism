
# **Python class polymorphism explication with example**
    This is a very simple example of Python polymorphism with the purpose 
    to shade some light in how this is working.

# **Description:**
    I defined 2 parent classes ParentA, ParentB each having defined a method
    named method_xx. The class ParentA have an additional method named method_a
    I defined a class named Child(ParentA, ParentB) which inherit ParentA, ParentB 
    with a method named method_a which overwrite the ParentA method_a
    I made an instance of Child(ParentA, ParentB) named my_child_class_instance
    Using my_child_class_instance I will acces:
            -   method_a from class Child
            -   method_a from class ParentA
            -   method_xx from class ParentA
            -   method_xx from class ParentB
            
 
# **Running:**
    class_polymorphism.py

# **Credits:**
    Alin Rizea
    https://www.linkedin.com/in/alin-rizea-b10368104/

       

# Save colors in constants to decorate the console output
BLUE = '\033[94m'
GREEN = '\033[92m'
ORANGE = '\033[33m'
RED = '\033[91m'
END = '\033[0m'


# **********************************************
# Define first parent class ParentA color=BLUE
class ParentA:
    def method_a(self):
        print(f"{BLUE}I am method_a from ParentA\n{END}")

    def method_xx(self):
        print(f"{BLUE}I am method_xx from ParentA\n{END}")


# **********************************************
# Define second parent class ParentB  color=GREEN
class ParentB:
    def method_xx(self):
        print(f"{GREEN}I am method_xx from ParentB\n{END}")


# **********************************************
# Define the child with 2 parents class Child(ParentA, ParentB)
class Child(ParentA, ParentB):
    def method_a(self):
        print(f"{ORANGE}my_child_class_instance{END}")
        print(f"{ORANGE}I am method_a from child class. I overwrite the parent class\n{END}")

    # Use the method_a from class ParentA
    def method_from_parent_a(self):
        print(f"{ORANGE}my_child_class_instance{END}")
        super(Child, self).method_a()

    # Use the method_xx from class ParentB
    def choose_parent_b(self):
        print(f"{ORANGE}my_child_class_instance{END}")
        ParentB.method_xx(self)


# Create an instance of Child
my_child_class_instance = Child()

print('\n***  Use Child class method_a ***')
# Use child method_a
my_child_class_instance.method_a()

print('\n***  Use ParentA class method_a ***')
# Use Parent_a class method_a
my_child_class_instance.method_from_parent_a()

print('\n***  Child class utilise ParentA class method_xx direct inheritance ***')
# Use Child ParentA method_xx because child has no method_xx, it is inherited directly
# from ParentA (ParentA is on the left when we declare Child class) class Child(ParentA, ParentB):
my_child_class_instance.method_xx()

print('\n***  Use ParentA class method_a ***')
# Use Parent_a class method_xx
my_b_class_instance.choose_parent_b()

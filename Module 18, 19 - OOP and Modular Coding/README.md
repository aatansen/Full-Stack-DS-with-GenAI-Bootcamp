# **Context**

- [**Context**](#context)
- [**Day 15 - Introduction to OOP**](#day-15---introduction-to-oop)
  - [**The Robot Problem**](#the-robot-problem)
    - [Class \& Object](#class--object)
    - [Constructor (`__init__`)](#constructor-__init__)
    - [`self` Keyword](#self-keyword)
    - [Instance Variables](#instance-variables)
    - [Class Variables](#class-variables)
    - [Instance Methods](#instance-methods)
  - [**Class vs Object**](#class-vs-object)
    - [Class](#class)
    - [Object](#object)
    - [Key Differences in Class and Object](#key-differences-in-class-and-object)
    - [Multiple Objects from One Class](#multiple-objects-from-one-class)
- [**Day 16 - Writing our first Class in OOP**](#day-16---writing-our-first-class-in-oop)
  - [**ATM Machine Using OOP**](#atm-machine-using-oop)
- [**Day 17 - Self \& Encapsulation in OOP**](#day-17---self--encapsulation-in-oop)
  - [**Magic Method/Dunder Method**](#magic-methoddunder-method)
  - [**Concept of **self** keyword in OOP**](#concept-of-self-keyword-in-oop)
  - [**How objects access attributes in OOP**](#how-objects-access-attributes-in-oop)
  - [**Reference Variable in OOP**](#reference-variable-in-oop)
  - [**Pass by reference**](#pass-by-reference)
  - [**Mutability of object in OOP**](#mutability-of-object-in-oop)
  - [**What is instance variable**](#what-is-instance-variable)
  - [**Encapsulation in OOP**](#encapsulation-in-oop)
    - [Types of Access Control](#types-of-access-control)
    - [Getter \& Setter (Encapsulation Tool)](#getter--setter-encapsulation-tool)
    - [Name Mangling (Private Variable Internals)](#name-mangling-private-variable-internals)
- [**Day 18 - Inheritance in OOP**](#day-18---inheritance-in-oop)
  - [**Collection Of Class Objects**](#collection-of-class-objects)
  - [**Static Variable in OOP**](#static-variable-in-oop)
  - [**Instance vs Static Variable in OOP**](#instance-vs-static-variable-in-oop)
  - [**Aggregation**](#aggregation)
  - [**DRY Principle**](#dry-principle)
  - [**Inheritance**](#inheritance)
- [**Day 19 - Polymorphism, Abstraction \& Modular Coding**](#day-19---polymorphism-abstraction--modular-coding)
  - [**Types of Inheritance**](#types-of-inheritance)
    - [Single Inheritance](#single-inheritance)
    - [Multilevel Inheritance](#multilevel-inheritance)
    - [Multiple Inheritance](#multiple-inheritance)
    - [Hierarchical Inheritance](#hierarchical-inheritance)
    - [Hybrid Inheritance](#hybrid-inheritance)
    - [Diamond Problem (Special Case)](#diamond-problem-special-case)
  - [**Method Overriding**](#method-overriding)
  - [**Super Keyword in OOP**](#super-keyword-in-oop)
  - [**Multilevel Inheritance**](#multilevel-inheritance-1)
  - [**Polymorphism**](#polymorphism)
  - [**Abstraction**](#abstraction)
  - [**Modular Coding**](#modular-coding)

# [**Day 15 - Introduction to OOP**](./Day%2015%20-%20Introduction%20to%20OOP/)

## **The Robot Problem**

- Using function

  ```py
  # Robot 1
  def movement_1():
    print("Its Robot 1")
  def fire_detection_1():
    print("Its Robot 1")
  def wheel_control_1():
    print("Its Robot 1")

  ## Robot 2
  def movement_2():
    print("Its Robot 2")
  def fire_detection_2():
    print("Its Robot 2")
  def wheel_control_2():
    print("Its Robot 2")

  movement_1()
  movement_2()
  ```

- Solution using OOP

  ```py
  # using OOP

  class Robot:

    def __init__(self, robot_number):
      self.robot_number = robot_number

    def movement(self):
      print(f"Its Robot {self.robot_number}")


    def fire_detection(self):
      print(f"Its Robot {self.robot_number}")

    def wheel_controll(self):
      print(f"Its Robot {self.robot_number}")


    def ai_intelligence(self):
      print(f"Its Robot {self.robot_number}")

  # Robot 1
  robot1 = Robot(robot_number = 1)
  robot1.movement()

  # Robot 2
  robot2 = Robot(robot_number = 2)
  robot2.movement()
  ```

- In OOP `__init__` function is contructor. In construction data properties are defined
- And methods are called functional properties

[⬆️ Go to Context](#context)

### Class & Object

- **Class** - Blueprint for creating objects

  ```py
  class Person:
      pass
  ```

- **Object** - Instance of a class

  ```py
  p = Person()
  ```

[⬆️ Go to Context](#context)

### Constructor (`__init__`)

- **Basic Constructor**

  ```py
  class Person:
      def __init__(self):
          print("Object created")

  p = Person()
  ```

- **Constructor with Parameters**

  ```py
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

  p = Person("Rahim", 20)
  ```

[⬆️ Go to Context](#context)

### `self` Keyword

- Refers to the **current object**

  ```py
  class Student:
      def __init__(self, name):
          self.name = name

  s = Student("Ayesha")
  print(s.name)
  ```

[⬆️ Go to Context](#context)

### Instance Variables

- Variables unique to each object

  ```py
  class User:
      def __init__(self, username):
          self.username = username

  u1 = User("admin")
  u2 = User("guest")
  ```

[⬆️ Go to Context](#context)

### Class Variables

- Shared among all objects

  ```py
  class Company:
      name = "Google"

  c1 = Company()
  c2 = Company()
  print(c1.name)
  ```

[⬆️ Go to Context](#context)

### Instance Methods

- Methods that work with object data

  ```py
  class Car:
      def start(self):
          print("Car started")

  c = Car()
  c.start()
  ```

[⬆️ Go to Context](#context)

## **Class vs Object**

[⬆️ Go to Context](#context)

### Class

- A class is a **blueprint / template**
- It defines **properties (variables)** - and **behaviors (methods)**

- **Purpose**
  - Used to create multiple objects
  - Does not occupy memory until object is created

- **Example**

  ```py
  class Car:
      def start(self):
          print("Car started")
  ```

[⬆️ Go to Context](#context)

### Object

- An object is a **real instance*- of a class
- Created from a class

- **Purpose**
  - Used to access class variables and methods
  - Occupies memory

- **Example**

  ```py
  c1 = Car()
  c1.start()
  ```

[⬆️ Go to Context](#context)

### Key Differences in Class and Object

- **Blueprint vs Real Thing**

  - Class → Design of a house
  - Object → Actual house built from the design

- **Memory**

  - Class → No memory allocation
  - Object → Memory allocated

- **Creation**

  - Class → Created using `class` keyword
  - Object → Created using `ClassName()`

- **Quantity**

  - Class → One
  - Object → Can be many

[⬆️ Go to Context](#context)

### Multiple Objects from One Class

- **Same class, different objects**

  ```py
  class Student:
      def __init__(self, name):
          self.name = name

  s1 = Student("Rahim")
  s2 = Student("Karim")
  ```

- Class → Logical entity
- Object → Physical entity
- Class → Defines methods
- Object → Uses methods
- Class creates objects
- Objects use class features

[⬆️ Go to Context](#context)

# [**Day 16 - Writing our first Class in OOP**](./Day%2016%20-%20Writing%20our%20first%20Class%20in%20OOP/)

## **ATM Machine Using OOP**

  ```py
  class AtmMachine:
    # constructor (special function) --> super power
    def __init__(self):
      self.pin = ""
      self.balance = 0
      self.menu()

    def menu(self):
      user_input = input(
              """
              Hi how can i help you?

              1. Press 1 to create pin
              2. Press 2 to change pin
              3. Press 3 to check balence
              4. Press 4 to withdraw
              5. Anything to exit
              """
          )

      if user_input == "1":
        # create a pin
        self.create_pin()
      elif user_input == "2":
        # change pin
        self.change_pin()
      elif user_input == "3":
        # check balence
        self.check_balance()
      elif user_input == "4":
        # withdraw
        self.withraw_balance()
      else:
        exit()

    def create_pin(self):
      user_pin = input("Enter your pin: ")
      self.pin = user_pin

      user_balance = float(input("Enter your balance: "))
      self.balance = user_balance

      print("Pin Created Successfully!")

      self.menu()

    def change_pin(self):
      old_pin = input("Enter your old pin: ")
      if old_pin == self.pin:
        new_pin = input("Enter your new pin: ")
        self.pin = new_pin
        print("Pin changed successfully!")
        self.menu()
      else:
        print("Incorrect pin!")
        self.menu()

    def check_balance(self):
      user_pin = input("Enter your pin: ")
      if user_pin == self.pin:
        print("Your balance is: ", self.balance)

      else:
        print("Your pin is incorrect, please try again!")

      self.menu()

    def withraw_balance(self):
      user_pin = input("Enter your pin: ")
      if user_pin == self.pin:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= self.balance:
          self.balance -= amount
          print(f"You have withdrawn {amount}. Your new balance is {self.balance}")
        else:
          print("Insufficient balance!")
      else:
        print("Your pin is incorrect, please try again!")

      self.menu()

  atm = AtmMachine()

  # Similarly more object can be created
  islamibank = AtmMachine()
  primebank = AtmMachine()
  citybank = AtmMachine()
  ```

[⬆️ Go to Context](#context)

# [**Day 17 - Self & Encapsulation in OOP**](./Day%2017%20-%20Self%20&%20Encapsulation%20in%20OOP/)

## **Magic Method/Dunder Method**

- Special methods with double underscore: `__method__`
- Automatically called by Python
- Used to control class behavior
- **Common Magic Methods**

  ```py
  class Test:
      def __init__(self):
          print("Object created")

      def __str__(self):
          return "Test Object"

  t = Test()
  print(t)
  ```

- **Usecase**

  - Object creation → `__init__`
  - Object printing → `__str__`
  - Object deletion → `__del__`

[⬆️ Go to Context](#context)

## **Concept of **self** keyword in OOP**

- `self` refers to the **current object**
- Used to access object variables and methods
- **Why `self` is needed**
  - To differentiate object data from local variables

  ```py
  class Person:
      def set_name(self, name):
          self.name = name

  p = Person()
  p.set_name("Rahim")
  ```

[⬆️ Go to Context](#context)

## **How objects access attributes in OOP**

- **Using dot (`.`) operator**

  ```py
  class Student:
      def __init__(self):
          self.name = "Ayesha"

  s = Student()
  print(s.name)
  ```

- **Access order**
  - Object → Instance variables
  - Class → Class variables

[⬆️ Go to Context](#context)

## **Reference Variable in OOP**

- Variable that points to an object in memory
- Object can have multiple reference variables

  ```py
  class Demo:
      pass

  a = Demo()
  b = a   # both refer to same object
  ```

- **Key point**

  - Object is not copied
  - Only reference is shared

[⬆️ Go to Context](#context)

## **Pass by reference**

- Python passes **object references**
- Changes inside function affect original object (if mutable)

  ```py
  def update(lst):
      lst.append(4)

  nums = [1, 2, 3]
  update(nums)
  print(nums)
  ```

[⬆️ Go to Context](#context)

## **Mutability of object in OOP**

- Can be changed after creation
- List, Dictionary, Set, Class Objects

  ```py
  lst = [1, 2]
  lst.append(3)
  ```

- **Immutable Objects**
  - Cannot be changed
  - int, float, string, tuple

  ```py
  x = 10
  x = 20
  ```

[⬆️ Go to Context](#context)

## **What is instance variable**

- Variable that belongs to an **object**
- Different for each object
- **Created inside constructor**

  ```py
  class User:
      def __init__(self, name):
          self.name = name

  u1 = User("Admin")
  u2 = User("Guest")
  ```

[⬆️ Go to Context](#context)

## **Encapsulation in OOP**

- Wrapping data and methods together
- Protecting data from direct access

[⬆️ Go to Context](#context)

### Types of Access Control

- **Public Variable**

  ```py
  self.name = "Rahim"
  ```

- **Protected Variable**- (`_var`)
  - Should not be accessed directly (by convention)

  ```py
  self._email = "test@mail.com"
  ```

- **Private Variable**- (`__var`)
  - Cannot be accessed directly outside class

  ```py
  self.__password = "1234"
  ```

[⬆️ Go to Context](#context)

### Getter & Setter (Encapsulation Tool)

- **Safe access to private data**

  ```py
  class Account:
      def __init__(self):
          self.__balance = 0

      def get_balance(self):
          return self.__balance

      def set_balance(self, amount):
          self.__balance = amount
  ```

[⬆️ Go to Context](#context)

### Name Mangling (Private Variable Internals)

- **How Python stores private variables**

  ```py
  print(account._Account__balance)
  ```

- **Why**
  - Prevent accidental access
  - Not true security, but protection
- **Encapsulation Benefits**
  - Data protection
  - Controlled access
  - Easier maintenance
  - Better code structure
- **Summary**
  - `self` → current object
  - Dunder methods → automatic behavior
  - Reference variable → points to object
  - Mutable → changeable
  - Instance variable → object-specific
  - Encapsulation → data protection

[⬆️ Go to Context](#context)

# [**Day 18 - Inheritance in OOP**](./Day%2018%20-%20Inheritance%20in%20OOP/)

## **Collection Of Class Objects**

A collection of class objects allows you to manage multiple instances of the same class (or related classes) as a single unit. This is fundamental for modeling groups of real-world entities.

- **Homogeneous Collection:** Typically, the collection holds objects of the same class type (e.g., a list of `Employee` objects).
- **Iteration:** You can easily loop through the collection to access and process the data/methods of each individual object.
- **Encapsulation:** While the collection manages the group, each object maintains its own unique state (attributes).

**Python Example (Using a List):**

  ```py
  class Person:

    def __init__(self, name, country):
      self.name = name
      self.country = country

  p1 = Person("Bappy", "UK")
  p2 = Person("Alex", "USA")
  p3 = Person("Ahmed", "india")

  L = [p1, p2, p3]
  print(L)

  for i in L:
    print(i.name, i.country)
  ```

[⬆️ Go to Context](#context)

## **Static Variable in OOP**

A static variable (also commonly called a **class variable** in languages like Python) is a variable that is shared across all instances (objects) of a class. Unlike instance variables, which are unique to each object, the static variable maintains a single, persistent copy in memory for the entire class.

- **Single Copy:** Only one memory location is allocated for the static variable, no matter how many objects you create.
- **Shared State:** Any object can access and modify this single value. A change made by one object is immediately visible to all other objects.
- **Access Method:** It is typically accessed and modified using the **Class Name** directly, rather than through an object instance.
- **Common Use Case:** Counting the total number of objects created, storing a global constant specific to the class (e.g., maximum size), or logging class-wide activity.

  ```py
  class Atm:

    #static variable
    __customer_id = 0

    #constructor(special function) - superpower
    def __init__(self):
      self.pin = ""
      self.balance = 0
      Atm.__customer_id += 1
      print(Atm.__customer_id)
    ...

  obj1 = Atm() # 1
  obj2 = Atm() # 2
  ```

- For safety we define the static as private variable `__customer_id`
- To get value of static we use static method decorator

  ```py
  @staticmethod
  def get_customer_id():
    print(Atm.__customer_id)
  ```

[⬆️ Go to Context](#context)

## **Instance vs Static Variable in OOP**

The key difference between an Instance Variable and a Static (or Class) Variable lies in **ownership, memory allocation, and sharing** among the objects of a class.

- **Ownership:** Belongs to the **object** (instance) of the class.
- **Definition:** Declared inside the class, typically within the constructor (`__init__` in Python) and associated with the `self` or `this` keyword.
- **Memory:** A **separate copy** of the variable is created in **Heap Memory** for **every object** created from the class.
- **Sharing:** They are **not shared**. Changes made to an instance variable in one object do not affect the value in any other object.
- **Purpose:** To store data that is unique and specific to each instance (e.g., an employee's name, a car's color).
- **Access:** Accessed using the object reference (e.g., `object_name.instance_var`).

| Feature         | Instance Variable                                            | Static Variable (Class Variable)                                |
| :-------------- | :----------------------------------------------------------- | :-------------------------------------------------------------- |
| **Ownership**   | Belongs to the **object (instance)**.                        | Belongs to the **class**.                                       |
| **Memory**      | A **separate copy** for every object (in Heap Memory).       | **One single copy** shared by all objects (at the class level). |
| **Declaration** | Inside the class, typically in the constructor (`__init__`). | Inside the class, but outside all methods.                      |
| **Access**      | Requires an object reference (`obj.instance_var`).           | Accessed via the class name (`Class.static_var`).               |
| **Uniqueness**  | **Unique** value for each object.                            | **Same** shared value for all objects.                          |
| **Lifetime**    | Exists as long as the object exists.                         | Exists as long as the class is loaded (program lifetime).       |

[⬆️ Go to Context](#context)

## **Aggregation**

- Non-private attribute
- Non-private methods
- Aggregation method is deprecated currently used `Inheritance`

  ```py
  class Customer:
      def __init__(self,name,gender,address):
          self.name = name
          self.gender = gender
          self.address = address

      def print_info(self):
          print(f"Name: {self.name}, Gender: {self.gender}, Address: {self.address.city}, {self.address.pin}, {self.address.state}")



  class Address:
      def __init__(self, city, pin, state):
          self.city = city
          self.pin = pin
          self.state = state

  adds = Address("Dhaka", 1230, "Bangladesh")
  cus = Customer("Bappy", "Male",adds)
  cus.print_info()
  ```

- Aggregation Diagram

  ![aggregation diagram](https://i.imgur.com/Pz1o1SY.png)

[⬆️ Go to Context](#context)

## **DRY Principle**

DRY stands for **"Don't Repeat Yourself."** It is a fundamental software development principle that aims to reduce redundancy and repetition of information, logic, or knowledge within a system.

Every piece of knowledge must have a **single, unambiguous, authoritative representation** within the system.

| Benefit             | Description                                                                                                                                                            |
| :------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Maintainability** | When a piece of logic needs updating, you only change it in **one central place**, reducing effort and time.                                                           |
| **Fewer Bugs**      | By centralizing logic, you eliminate the risk of introducing inconsistencies or bugs that occur when a fix is applied in one duplicated location but missed in others. |
| **Readability**     | Less repetitive code is shorter, more organized, and easier for other developers (and your future self) to read and understand.                                        |
| **Consistency**     | Ensures that a specific functionality or calculation behaves exactly the same way every time it is used.                                                               |

[⬆️ Go to Context](#context)

## **Inheritance**

Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

- Non-private attribute
- Non-private methods

  ```py
  class User: #parent class
    def __init__(self):
      self.name = "Bappy"
      self.gender = "Male"
    def login(self):
      print("Login Done!")
    def register(self):
      print("register Done!")

  class Student(User): #child class
    def __init__(self):
      self.rollno = 12
    def enroll(self):
      print("Enrolled the course!")
    def review(self):
      print("Reviewing the course!")

  class Instructor(User): #child class
    def __init__(self):
      self.idno = 120
    def create(self):
      print("created the course!")
    def reply(self):
      print("Reply to student!")

  s = Student()
  s.enroll()
  s.register()
  s.login()

  I = Instructor()
  I.create()
  I.login()
  I.register()
  ```

- When a child class is instantiated and does not define its own `__init__`, Python automatically and implicitly calls the Parent class's `__init__`.
- When the child class defines its own `__init__`, it **overrides** the parent's `__init__`.
- The `super()` function allows you to explicitly call methods from the parent class, primarily the parent's constructor.

  ```py
  class User: #parent class
    def __init__(self):
      self.name = "Bappy"
      self.gender = "Male"
    def login(self):
      print("Login Done!")
    def register(self):
      print("register Done!")

  class Student(User): #child class
    def __init__(self):
      self.rollno = 12
    def enroll(self):
      print("Enrolled the course!")

  s = Student()
  s.name # error as child has constructor `self.rollno = 12`
  ```

[⬆️ Go to Context](#context)

# [**Day 19 - Polymorphism, Abstraction & Modular Coding**](./Day%2019%20-%20Polymorphism,%20Abstraction%20&%20Modular%20Coding/)

## **Types of Inheritance**

### Single Inheritance

- One child inherits from **one parent**.

  ```py
  class Parent:
      def show(self):
          print("Parent class")

  class Child(Parent):
      pass

  obj = Child()
  obj.show()
  ```

[⬆️ Go to Context](#context)

### Multilevel Inheritance

- A class inherits from a class that already inherits from another class.

  ```py
  class A:
      def a(self):
          print("A")

  class B(A):
      def b(self):
          print("B")

  class C(B):
      def c(self):
          print("C")

  obj = C()
  obj.a()
  obj.b()
  obj.c()
  ```

[⬆️ Go to Context](#context)

### Multiple Inheritance

- A class inherits from **more than one parent class**.

  ```py
  class Father:
      def skill(self):
          print("Driving")

  class Mother:
      def talent(self):
          print("Cooking")

  class Child(Father, Mother):
      pass

  obj = Child()
  obj.skill()
  obj.talent()
  ```

[⬆️ Go to Context](#context)

### Hierarchical Inheritance

- Multiple child classes inherit from **one parent**.

  ```py
  class Animal:
      def sound(self):
          print("Animal sound")

  class Dog(Animal):
      pass

  class Cat(Animal):
      pass

  Dog().sound()
  Cat().sound()
  ```

[⬆️ Go to Context](#context)

### Hybrid Inheritance

- Combination of **two or more** inheritance types.

  ```py
  class A:
      def a(self):
          print("A")

  class B(A):
      def b(self):
          print("B")

  class C(A):
      def c(self):
          print("C")

  class D(B, C):
      def d(self):
          print("D")

  obj = D()
  obj.a()
  obj.b()
  obj.c()
  obj.d()
  ```

[⬆️ Go to Context](#context)

### Diamond Problem (Special Case)

- Occurs in multiple inheritance when a class inherits from two classes that share a common parent.

  ```py
  class A:
      def show(self):
          print("A")

  class B(A):
      def show(self):
          print("B")

  class C(A):
      def show(self):
          print("C")

  class D(B, C):
      pass

  obj = D()
  obj.show()
  print(D.mro())
  ```

> [!NOTE]
>
> - Single        → One parent, one child
> - Multilevel    → Parent → Child → Grandchild
> - Multiple      → Multiple parents, one child
> - Hierarchical  → One parent, multiple children
> - Hybrid        → Combination of inheritance types

[⬆️ Go to Context](#context)

## **Method Overriding**

- Method overriding happens when a child class provides its own implementation of a method that already exists in the parent class
  - It allows a child class to change or extend the behavior of a parent class method while keeping the same method name.
  - A feature of inheritance
  - Same method name
  - Same parameters
  - Defined in parent and child class
  - Child method replaces parent method behavior
- When we inherite the parant class the child class also need those argument when child class object is created

  ```py
  class Phone:
    def __init__(self, price, brand, camera):
      print("Inside Phone constructor")
      self.__price = price
      self.brand = brand
      self.camera = camera

    def get_price(self):
      return self.__price

    def buy(self):
      print("Buying a Phone inside Phone constructor")

  class SmartPhone(Phone):
    def buy(self):
      print("Buying a Phone inside SmartPhone constructor")

  S  = SmartPhone(200000, "apple", 3) # output: Inside Phone constructor
  S.buy() # overriding parent buy() output: Buying a Phone inside SmartPhone constructor
  ```

[⬆️ Go to Context](#context)

## **Super Keyword in OOP**

- `super()` allows a child class to safely access parent class methods and constructors, especially powerful in multiple inheritance.
  - Built-in function in Python
  - Refers to the parent (super) class
  - Used inside child class
  - Commonly used in method overriding

  ```py
  class Parent:
      def show(self):
          print("This is Parent class")

  class Child(Parent):
      def show(self):
          super().show()   # call parent method
          print("This is Child class")

  obj = Child()
  obj.show()
  ```

- Accessing parent constructor properties

  ```py
  class Person:
      def __init__(self, name):
          self.name = name

  class Student(Person):
      def __init__(self, name, roll):
          super().__init__(name)   # call parent constructor
          self.roll = roll

  s = Student("Rahim", 101)
  print(s.name, s.roll)
  ```

[⬆️ Go to Context](#context)

## **Multilevel Inheritance**

- Inheritance allows one class to acquire properties and methods from another class. In multilevel inheritance, a class is derived from a class that is already derived from another class.
  - Involves more than two classes
  - Each class inherits from the previous class
  - Forms a hierarchy
  - Common in real-world modeling

  ```py
  class GrandParent:
      def house(self):
          print("Owns a house")

  class Parent(GrandParent):
      def car(self):
          print("Owns a car")

  class Child(Parent):
      def bike(self):
          print("Owns a bike")

  c = Child()
  c.house()
  c.car()
  c.bike()
  ```

  ```py
  class Device:
      def power_on(self):
          print("Device powered on")

  class Mobile(Device):
      def call(self):
          print("Calling...")

  class SmartPhone(Mobile):
      def internet(self):
          print("Browsing internet")

  phone = SmartPhone()
  phone.power_on()
  phone.call()
  phone.internet()
  ```

[⬆️ Go to Context](#context)

## **Polymorphism**

- In Object-Oriented Programming, different objects may need to respond to the same method name in different ways.
  - One interface, many forms
  - Same method name, different behavior
  - Achieved at runtime in Python
  - Strongly linked with inheritance

  ```py
  class Animal:
      def speak(self):
          print("Animal makes a sound")

  class Dog(Animal):
      def speak(self):
          print("Dog barks")

  class Cat(Animal):
      def speak(self):
          print("Cat meows")

  animals = [Dog(), Cat()]

  for a in animals:
      a.speak()
  ```

[⬆️ Go to Context](#context)

## **Abstraction**

- In large systems, exposing all internal details makes code complex and hard to maintain.
  - Hides internal implementation
  - Shows essential features only
  - Focuses on what an object does, not how
  - Achieved using abstract classes & interfaces (conceptually)

  ```py
  from abc import ABC, abstractmethod

  class Payment(ABC):
      @abstractmethod
      def pay(self):
          pass

  class Bkash(Payment):
      def pay(self):
          print("Payment using bKash")

  class Card(Payment):
      def pay(self):
          print("Payment using Card")
  ```

[⬆️ Go to Context](#context)

## **Modular Coding**

- Breaking a large program into smaller modules
- Each module is a separate file
- Modules can contain functions, classes, or variables
- Modules are imported where needed
- Improves readability
- Easier maintenance
- Encourages reuse
- Simplifies testing
- Supports team collaboration
- Example
  - `calculator.py` file content

    ```py
    # calculator.py
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b
    ```

  - Using `calculator.py` function in `main.py`

    ```py
    # main.py
    import calculator

    print(calculator.add(10, 5))
    print(calculator.sub(10, 5))
    ```

- Project structure of [ATM Machine](./Day%2019%20-%20Polymorphism,%20Abstraction%20&%20Modular%20Coding/atm_project/)

  ```txt
  atm_project
  ├── 📁 core
  │   ├── 🐍 __init__.py
  │   ├── 🐍 auth.py
  │   ├── 🐍 database.py
  │   └── 🐍 transactions.py
  ├── 📝 README.md
  └── 🐍 main.py
  ```

[⬆️ Go to Context](#context)

# Concept Deep-Dive: Python Syntax & Object-Oriented Programming (OOP)

This notebook-style guide covers everything from Python variables to advanced Object-Oriented Programming (OOP) patterns. It is designed to bridge the gap for JavaScript/TypeScript developers transitioning into AI Engineering.

---

## 1. Syntax, Data Types, and Type Systems

Python is a **dynamically and strongly typed** language. This means you do not declare variable types explicitly (unlike TypeScript), but the language will not implicitly coerce types (unlike JavaScript).

```python
# JavaScript: "5" + 5 results in "55"
# Python: "5" + 5 throws a TypeError!
```

### Basic Data Types
```python
x = 10         # Integer (int)
y = 3.14       # Floating-point number (float)
name = "AI"    # String (str) - single or double quotes are identical
is_valid = True # Boolean (bool) - Must be capitalized (True/False)
empty = None   # NoneType (None) - Equivalent to null/undefined in JS
```

### Data Structures (Collections)

#### A. Lists (Like JS Arrays)
Lists are ordered, mutable collections of items.
```python
fruits = ["apple", "banana", "cherry"]

# Indexing & Slicing (Crucial for Data Wrangling)
print(fruits[0])      # "apple"
print(fruits[-1])     # "cherry" (last item)
print(fruits[0:2])    # ["apple", "banana"] (slice from index 0 to 2, exclusive)

# Common Methods
fruits.append("date") # Adds to end
fruits.pop()          # Removes and returns last item
fruits.insert(1, "blueberry") # Insert at specific index
```

#### B. Dictionaries (Like JS Objects/Maps)
Dictionaries are unordered, mutable collections of key-value pairs.
```python
developer = {
    "name": "Aman",
    "role": "AI Engineer",
    "experience_years": 5
}

# Accessing values
print(developer["name"])             # "Aman"
# print(developer["skills"])         # Throws KeyError if not found!
print(developer.get("skills", []))    # Safe access with default value

# Mutating & Adding
developer["skills"] = ["Python", "PyTorch"]
developer["experience_years"] = 6
```

#### C. Tuples (Immutable Lists)
Tuples are ordered, immutable sequences. They are often used for fixed records or to return multiple values from a function.
```python
point = (10, 20)
# point[0] = 15  # Throws TypeError! Tuples cannot be mutated.
```

#### D. Sets (Unique Collections)
Sets are unordered collections of unique elements. Useful for deduplication and membership tests.
```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # Output: {1, 2, 3} (duplicates removed automatically)
print(2 in numbers) # Output: True (constant-time O(1) membership check)
```

---

## 2. Control Flow & Loops

Python relies on **indentation** to define scope. Avoid tabs; use 4 spaces.

### Conditionals
```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: F")
```

### Logical & Membership Operators
Instead of `&&`, `||`, and `!`, Python uses readable English words: `and`, `or`, and `not`.
```python
has_experience = True
knows_pytorch = False

if has_experience and not knows_pytorch:
    print("Candidate needs PyTorch training.")
```
We also have `in` and `not in` for checking containment:
```python
skills = ["Python", "FastAPI"]
if "PyTorch" not in skills:
    print("Warning: PyTorch is missing!")
```

### Loops
```python
# For loop over a collection
for skill in ["Python", "FastAPI", "Docker"]:
    print(f"Skill: {skill}")

# Loop with index using enumerate()
for index, val in enumerate(["a", "b", "c"]):
    print(f"Index {index}: Value {val}")

# While loop
count = 0
while count < 3:
    print(count)
    count += 1
```

---

## 3. Functions & Argument Scope

Functions in Python are defined using the `def` keyword.

```python
# Function with default argument
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Aman"))                # "Hello, Aman!"
print(greet("Aman", greeting="Hi"))  # "Hi, Aman!" (Keyword argument)
```

### Argument Types: Positional vs Keyword
- **Positional Arguments:** Matched by position.
- **Keyword Arguments:** Explicitly passed as `key=value`. They allow arguments to be in any order.

```python
def describe_model(architecture, parameters, framework="PyTorch"):
    return f"Model: {architecture} ({parameters} params) built in {framework}."

# Mixing positional and keyword arguments
print(describe_model("ResNet50", "25M", framework="TensorFlow"))
```

### Lambda Functions (Like JS Arrow Functions)
Lambda functions are small, anonymous, single-expression functions:
```python
# JS: (x, y) => x + y
add = lambda x, y: x + y
print(add(5, 3))  # 8
```

---

## 4. Object-Oriented Programming (OOP)

All deep learning and AI APIs (like PyTorch models, LangChain chains, and FastAPI endpoints) heavily employ OOP. Understanding Python classes is critical.

### Defining a Class
```python
class NeuralNetwork:
    # Class Attribute (shared by all instances)
    framework = "PyTorch"

    # Constructor method - initializes instance properties
    def __init__(self, layer_sizes, activation="ReLU"):
        self.layers = layer_sizes        # Instance Attribute
        self.activation = activation    # Instance Attribute
        
    # Instance Method
    def describe(self):
        return f"Architecture: {self.layers} layers with {self.activation} activation using {self.framework}."
```
*   **`self` parameter:** In Python, you must explicitly declare `self` as the first argument in all instance methods. When you call the method as `net.describe()`, Python automatically passes the instance `net` as the first parameter.
*   **Instantiation:** Do **not** use the `new` keyword:
    ```python
    my_net = NeuralNetwork([10, 5, 2])
    print(my_net.describe())
    ```

### Inheritance & Super Class
Inheritance allows one class to inherit the attributes and methods of another. This is how you define models in PyTorch.

```python
class BaseClassifier:
    def __init__(self, num_classes):
        self.num_classes = num_classes
        
    def predict(self, data):
        raise NotImplementedError("Subclasses must implement the predict method.")

# Inheriting from BaseClassifier
class ImageClassifier(BaseClassifier):
    def __init__(self, num_classes, image_size):
        # Call the parent class constructor
        super().__init__(num_classes)
        self.image_size = image_size
        
    # Overriding parent method
    def predict(self, data):
        return f"Predicting image class of size {self.image_size} across {self.num_classes} categories."
```

### Class Methods vs Static Methods
- **Instance Methods:** Access the instance via `self`.
- **Class Methods:** Decorated with `@classmethod`, access the class itself via `cls` (useful for factory methods).
- **Static Methods:** Decorated with `@staticmethod`, behave like standard functions namespace-grouped under a class. They do not access `self` or `cls`.

```python
class ConfigManager:
    default_format = "JSON"
    
    @classmethod
    def from_yaml(cls, yaml_string):
        print(f"Parsing YAML using {cls.default_format} default configs.")
        return cls()
        
    @staticmethod
    def validate_path(path):
        return os.path.exists(path)
```

---

## 🧠 Why OOP is Crucial for AI (PyTorch Example)

When you start learning PyTorch (Week 11), your models will always be defined as Python classes inheriting from PyTorch's base model class `nn.Module`.

```python
# A preview of how you will write neural network code:
import torch.nn as nn

class LinearModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearModel, self).__init__() # Initialize PyTorch module
        self.linear_layer = nn.Linear(input_dim, output_dim) # Define layer
        
    def forward(self, x):
        # Define forward pass sequence
        return self.linear_layer(x)
```
Without a firm grasp of classes, constructors, methods, and inheritance, PyTorch code will look like magic. OOP is the foundation.

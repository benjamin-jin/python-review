# Class

## Methods
```
class MyClass:
  @staticmethod
  def static_method(x):
    pass
  @classmthod
  def class_method(cls, x):
    pass
  def instance_method(self, x):
    pass
```

### Types
- static method
  - `@staticmethod` is required
  - Can call from class itself (i.e : `MyClass.static_method(1)`)
  - Cannot get class attributes
  - Cannot set class attributes
  - Cannot call class attributes
- class method
  - `@classmethod` is required
  - Can call from itself, just as static method
  - Can get class attributes
  - Can set class attributes. This effects all instances including not-yet instanced instances.
    - But, once this attribute is set by instance, class attribute is ignored.
  - Can call class attributes
    - When calling instance methods, `cls` keyword is required in the position of `self`. This indicates, calling instance method as class method (Check `Class5` in `method_types.py`)
- instance method
  - No keyword is required
  - Cannot call from itself. Should be called from instances only.
  - Can get class / isntance attributes
  - Can set instance attributes. Instance attributes override Class attributes (Check `Class2` in `method_types.py`)
  - Can call all types of methods

### Tips
- `cls` represents class itself. `self` represents instance. Check `Class6`
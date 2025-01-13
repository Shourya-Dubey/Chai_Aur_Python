# Tuple

>>> tea_types = ("Black", "Green", "Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types[1:]
('Green', 'Oolong')
>>> tea_types[0] = "Lemon"
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    tea_types[0] = "Lemon"
    ~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> len(tea_types)
3
>>> more_types = ("Herbal", "Earl Grey")
>>> all_tea = more_types + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>> if "Green" in all_tea:
...     print("I have Green tea")
...     
I have Green tea
>>> more_types = ("Herbal", "Earl", "Herbal")
>>> more_types
('Herbal', 'Earl', 'Herbal')
>>> more_types.count("Herbal")
2
>>> tea_types
('Black', 'Green', 'Oolong')
>>> 
>>> (black, green, oolong) = tea_types
>>> black
'Black'
>>> green
'Green'
>>> oolong
'Oolong'
>>> type(tea_types)
<class 'tuple'>
>>> 
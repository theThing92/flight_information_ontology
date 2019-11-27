# Simple Flight Information Ontology
Simple flight information ontology implemented in Python 3 with the Owlready2 framework.

# Dependencies
- [Owlready2 (v0.21)](https://pypi.org/project/Owlready2/)
  - [Dokumentation](https://owlready2.readthedocs.io/en/latest/)

Note: You need Python 3.x to run Owlready2, Python 2 **is not** supported.

# Installation
In the project root directory invoke
```
pip install -r requirements.txt 
```
It is recommended to use a virtual environment for installing the package. See [here](https://docs.python.org/3/tutorial/venv.html) for details.

# Usage
The source code for generating the given ontology can be found in **flight_information_ontology.py**

The ontology can be directly loaded within python by calling

```python
from owlready2 import *
onto = get_ontology("./flight_information_ontology.owl").load()
```

# Visualization
In order to visualize the content of the ontology, you can upload the **flight_information_ontology.owl** file [here](http://www.visualdataweb.de/webvowl/).


# Citations
>[Lamy JB. Owlready: Ontology-oriented programming in Python with automatic classification and high level constructs for biomedical ontologies. Artificial Intelligence In Medicine 2017;80:11-28](http://www.lesfleursdunormal.fr/_downloads/article_owlready_aim_2017.pdf)

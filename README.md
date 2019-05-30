# trackman-challenge

## Problem description 
Read JSON configuration files which describe SQL queries and extract implicit table dependencies by parsing the FROM part of the queries.

## Solution
### Implemented
- Read all configuration files in the `tables` folder 
- Used a third party library `sqlparse` to parse the FROM parts of the queries in all the configuration files and extracted the tables used by them
- print the FROM string and all the (schema, table) pairs present in them
- Defined a node class which will hold the schema and table names to build a dependency graph

### TODO
- Build the dependency graph
- Display the graph using DFS

### Execution
```
> pip install -r requirements.txt
> python main.py
```

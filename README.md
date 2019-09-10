# kthfsdv   

## Exercise 1   

### Requirements   

### Usage  (Ubuntu)
`cd exercise1`  
`catkin init`  
`catkin build` 
`source ./devel/setup.bash`   

`roscore` starts the roscore core service  
`rosrun package1 talker.py` runs the publisher  
`rosrun package2 listener.py` runs the subscriber  

## Exercise 2

### Requirements

> python3, python3 venv   

### Usage (Ubuntu)

`cd exercise2`  
`python3 -m venv kthfsdv`  
`source ./kthfsdv/bin/activate`  
`pip install -r requirements.txt`  
`./app.py`  
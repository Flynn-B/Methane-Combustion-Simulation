# Methane-Combustion-Simulation
Processing Model coded in Python by Flynn Basehart.

Model simulates the molecular combustion of methane when combined with oxygen resulting in CO<sub>2</sub> and water. 
Chemical Equation for methane combustion is CH<sub>4</sub> + 2O<sub>2</sub>2 -> CO<sub>2</sub> +2H<sub>2</sub>O

## How to Run
- Download [Processing](https://processing.org).
- Download and use 'Python Mode' from within Processing. More information of Processing.py [here](https://py.processing.org).
- Download and open file in Processing

## Code Explanation
The model creates 4 different molecules, CH<sub>4</sub>, 2O<sub>2</sub> (each modeled as one ellipse one for simplicity reasons), CO<sub>2</sub>, and 2H<sub>2</sub>O (each modeled as one ellipse for simplicity reasons).
The model bases the ellipses used to simulate the molecules on real world data including mass, density, and volume.
As expected in the equation, when CH4 and 2O2 collide it results in the production of CO2 and H2O.
However when any other molecules collide, they do not react and collide according the collision engine which takes into consideration the mass and size of an molecule.

## Results
Team won the 2021 New Mexico Governor's Stem Challange, sponsered by Los Alamos National Lab.

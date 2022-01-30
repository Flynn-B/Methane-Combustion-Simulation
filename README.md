# Methane-Combustion-Simulation
Processing Model coded in Python by Flynn Basehart.

Model simulates the molecular combustion of methane when combined with oxygen resulting in CO2 and water. 
Chemical Equation for methane combustion is CH4 + 2O2 -> CO2 + 2H20

## Code Explanation
The model creates 4 different molecules, CH4, 2O2 (merged into one for simplicity reasons), CO2, and 2H20 (merged into one for simplicity reasons).
The model bases the ellipses used to simulate the molecules on real world data including mass, density, and volume. 
As expected in the equation, when CH4 and 2O2 collide it results in the production of CO2 and H2O
However when any other molecules collide, they do not react and collide according the collision engine which takes into consideration the mass and size of an molecule

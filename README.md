# Projectile-Trajectory-Pro
HDA for SideFx Houdini that create a custom trajectory path. 

How to install and create: 

1- Put the HDA on the otls file in the current version of Houdini, in windows the path is something like "C:\Users\User\Documents\houdinixx.x\otls", if don't have any otls file create yourself.

2- The HDA works in a sop context, create a geometry node and inside create the HDA.

How to use:

- The HDA contains two inputs, one asks a projectile (a sphere is enough) for start working, the other asks a obstacles for collide with the trajectory path.
- HDA Parameters:

    -  Points Position: Allows control de initial position and the final 
    position of the trajectory, control the speed at which the projectile 
    will travel the trajectory and the curve points for control his 
    resolution.

    - Cruve Editor: Allows control the height and the bend of the curve 
    and have more control with ramps.

    - Show Trajectory: Show the trajectory path and the diferents impacts 
    of the obstacles.

    - Simulation: If this toggle is active, show a how the projectile destroy 
    the obstacles in the scene.

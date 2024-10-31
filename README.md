Pipeline:
1. Goal: select the points that will become the corners of the polygon.
input: processed mask, depth map.
Output: points selected as corners of the polygon.

2. Goal: to find out the coordinates of the polygon.
Input: user geolocation, angles of rotation of the phone camera in space, corners of the polygon as image points + depth at these points.
Output: polygon as a set of coordinates of corners.

3. Goal: to build directions for polygons (in fact graph construction).
Input: polygons as sets of coordinates.
Output: Directions for polygons.

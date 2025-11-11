## 2009 Polygon Simplifier

This algorithm detects and simplifies a polygon based on perpendicular distance between line segments of the polygon (built using two adjacent vertices) and the adjacent vertex. I originally came up with the algorithm to help detect (and eventually simplify) polygons with parts/sections with zero (or very small) area.  These types of polygons are also referred to as "degenerate" polygons.

Sometime later I discovered this algorithm is very similar to Ramer-Douglas-Peucker algorithm [Reference](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm) for line segment simplification.

Pseudocode Code:
```
in_polygon
# Add the first line segment of the polygon 
out_polygon=[in_polygon[0], in_polygon[1]]
i = 2

# Iterate overall all vertices after the first line segment 
while i < size(in_polygon):
  # Build a line (infinite in both directions)
  line = build_line(out_polygon[-2], in_polygon[-1])
  
  # Get next vertice (after the line)
  next_point = in_polygon[i]
  
  # Check perpendicular distance between line and point
  d = perpendicular_dist(line, point)
  
  # If distance is greater than threshold then keep the point
  if d >= threshold:
    out_polygon.append(next_point)
  else:  # Replace the current line segment's end vertex with the next point
    out_polygon[-1] = next_point

  # Go to next point
  i+=1
```

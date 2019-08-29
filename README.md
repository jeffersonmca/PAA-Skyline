# Skyline Problem

Given n rectangular buildings in a 2-dimensional city, computes the skyline of these buildings, eliminating hidden lines.
The main task is to view buildings from a side and remove all sections that are not visible.

All buildings share common bottom and every building is represented by triplet (left, ht, right)

- ‘left’: is x coordinated of left side (or wall).
- ‘right’: is x coordinate of right side
- ‘ht’: is height of building.

A skyline is a collection of rectangular strips.
A rectangular strip is represented as a pair (left, ht) where left is x coordinate of left side of strip and ht is height of strip.

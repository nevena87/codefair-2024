def count_water_cells(grid):
    rows = len(grid) 
    cols = len(grid[0]) 
    water_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                water_count += 1

    return water_count

puddle_grid_a = [
    [-1, 0, 0, 0, 0, 0, 0, 0],
    [-1, 1, 1, -1, 1, 1, 1, -1],
    [-1, 1, 1, -1, -1, 1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1]
]

water_volume_a = count_water_cells(puddle_grid_a)
print(f"Water Volume: {water_volume_a} units.")

puddle_grid_b = [
    [-1, 1, 1, 1, 1, 1, 1, -1],
    [-1, 1, 1, -1, 1, 1, 1, -1],
    [-1, 1, -1, -1, 1, 1, -1, -1],
    [-1, -1, -1, -1, 1, 1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1]
]

water_volume_b = count_water_cells(puddle_grid_b)
print(f"Water Volume: {water_volume_b} units.")

# 1 - water
# 0 - empty space
# -1 - road
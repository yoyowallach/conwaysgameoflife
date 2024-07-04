def displayboard(grid):
  for element in grid:
    for x in element:
      print(x, end="")
    print("")
  print()

def change(x, y, grid, symbol):
  grid[x][y] = symbol
  return grid

def count_alive_neighbors(x, y, grid):
  directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  alive_neighbors = 0
  for dx, dy in directions:
    nx, ny = x + dx, y + dy
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
      if grid[nx][ny] == "0":
        alive_neighbors += 1
  return alive_neighbors

def check_rules(x, y, gridscan, gridchange):
  alive_neighbors = count_alive_neighbors(x, y, gridscan)
  if gridscan[x][y] == "0":
    if alive_neighbors < 2 or alive_neighbors > 3:
      gridchange[x][y] = "-"
  else:
    if alive_neighbors == 3:
      gridchange[x][y] = "0"
  return gridchange

# Grid is 20 by 54
grid1 = [["-" for _ in range(54)] for _ in range(20)]

with open("design.in", "r") as f:
  lines = f.readlines()
  for line in lines:
    x, y = map(int, line.strip().split())
    grid1 = change(x - 1, y - 1, grid1, "0")

displayboard(grid1)

def gen(grid):
  newgrid = [row[:] for row in grid]
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      newgrid = check_rules(i, j, grid, newgrid)
  return newgrid

while True:
  grid1 = gen(grid1)
  displayboard(grid1)

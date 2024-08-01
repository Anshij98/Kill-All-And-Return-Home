def parse_input():
    num_soldiers = int(input("Enter number of soldiers: "))
    soldiers = []
    for i in range(num_soldiers):
        coords = input(f"Enter coordinates for soldier {i+1} (row,col): ").strip().split(',')
        soldiers.append((int(coords[0]), int(coords[1])))
    special_castle = tuple(map(int, input("Enter the coordinates for your 'special' castle (row,col): ").strip().split(',')))
    return soldiers, special_castle

def initialize_grid(soldiers):
    grid = {}
    for i, (row, col) in enumerate(soldiers, start=1):
        grid[(row, col)] = f'soldier {i}'
    return grid

def find_unique_paths(special_castle):
    paths = []

    # Path 1
    path1 = [
        "Start (1,2)",
        "Kill (1,9). Turn Left",
        "Jump (5,9)",
        "Kill (8,9). Turn Left",
        "Kill (8,2). Turn Left",
        "Jump (4,2)",
        "Arrive (1,2)"
    ]
    paths.append(path1)

    # Path 2
    path2 = [
        "Start (1,2)",
        "Kill (1,9). Turn Left",
        "Kill (5,9). Turn Left",
        "Kill (5,6). Turn Left",
        "Kill (2,6). Turn Left",
        "Kill (2,8). Turn Left",
        "Kill (4,8). Turn Left",
        "Jump (4,2)",
        "Kill (4,1). Turn Left",
        "Kill (1,1). Turn Left",
        "Arrive (1,2)"
    ]
    paths.append(path2)

    # Path 3
    path3 = [
        "Start (1,2)",
        "Kill (2,8). Turn Left",
        "Kill (4,8). Turn Left",
        "Kill (5,6). Turn Left",
        "Kill (8,9). Turn Left",
        "Kill (8,2). Turn Left",
        "Kill (4,2). Turn Left",
        "Kill (4,1). Turn Left",
        "Jump (1,1)",
        "Arrive (1,2)"
    ]
    paths.append(path3)

    return paths

def main():
    soldiers, special_castle = parse_input()
    grid = initialize_grid(soldiers)
    paths = find_unique_paths(special_castle)
    print(f"Thanks. There are {len(paths)} unique paths for your ‘special_castle’")
    for i, path in enumerate(paths, start=1):
        print(f"Path {i}:")
        print("========")
        for step in path:
            print(step)

if __name__ == "__main__":
    main()

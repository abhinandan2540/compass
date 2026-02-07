
# importing modules
from Module import navigation_weighted_graph, graph, dijkstra, generate_directions


# starting banner
def show_banner():
    banner = r"""

         ██████╗  ██████╗ ███╗   ███╗ ██████╗  █████╗ ███████╗ ███████╗
        ██╔════╝ ██╔═══██╗████╗ ████║ ██╔══██╗██╔══██╗██╔════╝ ██╔════╝
        ██║      ██║   ██║██╔████╔██║ ██████╔╝███████║███████╗ ███████╗
        ██║      ██║   ██║██║╚██╔╝██║ ██╔═══╝ ██╔══██║╚════██║ ╚════██║
        ╚██████╗ ╚██████╔╝██║ ╚═╝ ██║ ██║     ██║  ██║███████║ ███████║
        ╚═════╝  ╚═════╝ ╚═╝     ╚═╝ ╚═╝     ╚═╝  ╚═╝╚══════╝ ╚══════╝


              ----------------------------------------------------
                Welcome to IIITM Smart Campus Navigation System
              -----------------------------------------------------

    """
    print(banner)


# show locations
def show_locations(graph):
    print("\n============== Available Locations: ==================\n")
    for loc in sorted(graph.keys()):
        print(f" | {loc}", end=" ")



# input mode
def interactive_input(graph):
    while True:
        start = input("\nEnter START location: ").strip()
        if start not in graph:
            print(" =============== Invalid start location. Please try again.================== \n")
            continue
        break

    while True:
        goal = input("\nEnter DESTINATION location: ").strip()
        if goal not in graph:
            print(" =============== Invalid destination. Please try again.==================\n")
            continue
        break

    return start, goal


def main():
    show_banner()
    show_locations(navigation_weighted_graph)

    start, goal = interactive_input(navigation_weighted_graph)

    print("\nCalculating best route...............\n")

    distance, path = dijkstra(
        navigation_weighted_graph,
        start,
        goal
    )

    if not path:
        print(" ================== No path found. ====================")
        return

    print(" ====================== SHORTEST PATH =======================")
    print(" → ".join(path))
    print(f"\n # Total Distance: {distance} meters\n")

    print("================ TURN-BY-TURN NAVIGATION ==================\n")

    steps = generate_directions(navigation_weighted_graph, path)

    for i, step in enumerate(steps, 1):
        print(f"Step {i}:\n{step}\n")

    print("===================== You have arrived at your destination. Enjoy your visit! ======================")


if __name__ == "__main__":
    main()


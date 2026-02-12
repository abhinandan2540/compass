
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
              |  Welcome to IIITM Smart Campus Navigation System |
              ----------------------------------------------------

    """
    print(banner)


# show locations
def show_locations(graph):
    print("""
--------------------------------------------------------------
|                  Available Locations                       |
--------------------------------------------------------------
        """)

    for loc in sorted(graph.keys()):
        print(f" | {loc}", end=" ")


# input mode
def interactive_input(graph):
    while True:
        start=input("""\n
------------------------
| Enter START Location |
------------------------ 
""").strip()
        
        if start not in graph:
            print("""
-----------------------------------------------------------------
|            Invalid START location. Please try again           |       
-----------------------------------------------------------------
""")
            continue
        break

    while True:
        goal=input("""\n
------------------------------
| Enter DESTINATION Location |
------------------------------
""").strip()
        
        if goal not in graph:
            print("""
-----------------------------------------------------------------
|            Invalid DESTINATION location. Please try again      |
-----------------------------------------------------------------
""")
            
            continue
        break

    return start, goal


def main():
    show_banner()
    show_locations(navigation_weighted_graph)

    start, goal = interactive_input(navigation_weighted_graph)

    print("""
--------------------------------------------------------------
|                 Calculating best route                     |
--------------------------------------------------------------                                            
""")

    distance, path = dijkstra(
        navigation_weighted_graph,
        start,
        goal
    )

    if not path:
        print("""
--------------------------------------------------
|                No Path Found :(                |
--------------------------------------------------                             
""")
        return


    print("""
-------------------------------------------------------
|                 SHORTEST PATH                       |
-------------------------------------------------------                      
""")
    
    print(" → ".join(path))
    print(f"\nTOTAL DISTANCE: {distance} meters\n")
    print("""
---------------------------------------------------------
|                TURN-BY-TURN NAVIGATION                |
---------------------------------------------------------          
""")

    steps = generate_directions(navigation_weighted_graph, path)

    for i, step in enumerate(steps, 1):
        print(f"Step {i}:\n{step}\n")

    print("""
-------------------------------------------------------------------------------------------------
|                  You have arrived at your destination. Enjoy your visit!                      |
-------------------------------------------------------------------------------------------------          
""")


if __name__ == "__main__":
    main()

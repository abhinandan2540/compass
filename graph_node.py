
# node information
Node = list(set(("IIITM Gate", "Nescafe Cafeteria", "LT2", "LT1", "Admin Block", "LT1 Cafeteria", "Learning Resource Center", "Convention Center", "MDP",
            "Gangotri Hostel", "Health Center", "IVH", "OAT Cafeteria", "Open Air Theater", "Sports Complex", "Shivalik Hostel", "Aravalli", "Nilgiri", "Butterfly Garden")))


# graph information
graph = {
    "IIITM Gate": ["Admin Block", "MDP", "Nescafe"],
    "Admin Block": ["LT1", "Convention Center", "LRC", "IIITM Gate"],
    "MDP": ["IIITM Gate", "Gangotri Hostel"],
    "Nescafe": ["IIITM Gate", "LT2", "Nilgiri", "Butterfly Garden"],
    "LT1": ["LT2", "Admin Block", "LT1 Cafeteria"],
    "Convention Center": ["LRC", "Admin Block"],
    "LRC": ["Convention Center", "Admin Block", "LT1 Cafeteria"],
    "Gangotri Hostel": ["MDP", "Health Center"],
    "LT2": ["LT1", "Nescafe"],
    "Nilgiri": ["Aravalli", "Butterfly Garden", "Nescafe", "LT1 Cafeteria"],
    "Butterfly Garden": ["Nilgiri", "Nescafe"],
    "LT1 Cafeteria": ["LT1", "LRC", "Shivalik", "Nilgiri", "Aravalli"],
    "Health Center": ["IVH", "OAT", "Gangotri Hostel"],
    "Shivalik": ["Aravalli", "OAT", "LT1 Cafeteria"],
    "Aravalli": ["Nilgiri", "Shivalik", "LT1 Cafeteria"],
    "OAT": ["OAT Cafeteria", "Sports Complex", "Health Center", "Shivalik"],
    "OAT Cafeteria": ["OAT"],
    "Sports Complex": ["OAT"],
    "IVH": ["Health Center"],
}

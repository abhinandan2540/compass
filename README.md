# COMPASS

**Smart Campus Navigation System for IIITM Gwalior**

COMPASS is an intelligent, CLI-based campus navigation system designed for [**IIITM Gwalior**](https://www.iiitm.ac.in/index.php/en/).
It focuses on **efficient routing, human-friendly directions, and contextual campus awareness**, making navigation intuitive for **new visitors, students, and staff**.

Unlike generic shortest-path demos, COMPASS blends **graph algorithms with real-world landmarks and attractions**, creating a navigation experience that feels *natural*, *informative*, and *purpose-driven*.

---

## COMPASS CLI
<img width="1292" height="807" alt="Screenshot 2026-02-12 154821" src="https://github.com/user-attachments/assets/e198d729-5177-440b-a90f-bef315c6567a" />



## Key Highlights

* **Shortest-path routing** optimized for campus-scale navigation
* **Turn-by-turn directions** with human-readable instructions
* **Landmarks & attractions** embedded into navigation flow
* **Classic CLI UI/UX** with compass-style terminal interface
* Designed as a **real-world graph systems project**, not a toy example

---

## System Architecture

COMPASS models the IIITM campus as a **navigation-aware weighted graph**:

* **Nodes** → Campus locations (Gate, Academic Blocks, Hostels, Cafeterias, Gardens etc.)
* **Edges** → Walkable paths with real distance metrics
* **Edge Metadata** →
  * Distance
  * Navigation instructions (left / right / straight)
  * Landmarks
  * Environmental attractions

This architecture allows COMPASS to generate **context-aware navigation**, not just raw paths.

---

## Project Phases

### Phase 1 — Static Intelligent Navigation *(Implemented)*

A deterministic campus navigation system that:

* Computes the **shortest path** between a start and destination
* Generates **step-by-step navigation instructions**
* Enriches directions with **landmarks and attractions** from the campus environment

> Ideal for *first-time visitors and orientation purposes*.

---

### Phase 2 — Dynamic Preference-Based Navigation *(Planned)*

An advanced routing engine that will:

* Support **user preferences** (scenic paths, shaded routes, minimal crowd zones)
* Dynamically **re-rank routes** based on experience distribution
* Enable **adaptive navigation strategies** for different user profiles

> Targeted towards research-grade routing and intelligent mobility systems.

---

## CLI Experience

COMPASS is designed to be run directly from the terminal. Dwonload latest version of COMPASS from release section and run

```bash
compassv(version_specifics).exe
```

Users are greeted with a **classic compass-style CLI interface**, guided through:

1. Selecting a start location
2. Selecting a destination
3. Receiving optimized routes with descriptive navigation output

No flags. No complexity. Just intuitive navigation.

---

## Use Cases

* New students exploring the campus
* Visitors attending events or conferences
* Academic demonstrations of **graph algorithms in real-world systems**
* Research prototypes for **intelligent navigation & routing**

---

## Vision

> COMPASS aims to bridge the gap between **theoretical graph algorithms** and **human-centric navigation systems**, laying the foundation for scalable, intelligent routing solutions in controlled environments like campuses, institutions, and smart cities.

---

## Source Code Availability

The core navigation engine of COMPASS is currently maintained as a
**private research prototype**.

To encourage experimentation and feedback, users can:
- Test COMPASS via a **precompiled CLI binary**
- Interact with the navigation system without access to internal logic

This approach ensures:
- Controlled evaluation
- Protection of ongoing research work
- Stable user-facing experience

Source code will be released in future phases.


Thank you,

Abhinandan

[LinkedIn](https://www.linkedin.com/in/abhinandanmandal/)

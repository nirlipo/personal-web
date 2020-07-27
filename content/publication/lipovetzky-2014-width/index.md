---
title: "Width and inference based planners: Siw, bfs (f), and probe"
date: 2014-01-01
publishDate: 2020-07-26T09:42:49.091178Z
authors: ["Nir Lipovetzky", "Miquel Ramirez", "Christian Muise", "Hector Geffner"]
publication_types: ["2"]
abstract: "We entered the planners SIW, BFS (f), and PROBE to the agile-track of the 2014 International Planning Competition, and an anytime planner for the satisficing track that runs both SIW and BFS (f). SIW and BFS (f) are classical planners that make use of the notion of width (Lipovetzky and Geffner 2012), while PROBE is a standard bestfirst search planner that augments the expansion of a node by throwing an “intelligent” probe which either reaches the goal or terminates quickly in low polynomial time (Lipovetzky and Geffner 2011). The basic building block of SIW is the Iterative Width Procedure (IW) for achieving one atomic goal at a time. IW runs in time exponential in the problem width by performing a sequence of pruned breadth first searches. The planner BFS (f) integrates a novelty measure from IW with helpful-actions, landmarks and deleterelaxation heuristics in a Greedy Best-Fist search. In the following sections we introduce the basic notions of the algorithms and the implementation."
featured: false
publication: "*Proceedings of the 8th International Planning Competition (IPC-2014)*"
url_pdf: "http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.727.4904&rep=rep1&type=pdf"
---


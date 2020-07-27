---
title: "Traps, invariants, and dead-ends"
date: 2016-01-01
publishDate: 2020-07-26T09:42:49.105763Z
authors: ["Nir Lipovetzky", "Christian Muise", "Hector Geffner"]
publication_types: ["1"]
abstract: "We consider the problem of deriving formulas that capture traps, invariants, and dead-ends in classical planning through polynomial forms of preprocessing. An invariant is a formula that is true in the initial state and in all reachable states. A trap is a conditional invariant: once a state is reached that makes the trap true, all the states that are reachable from it will sat-isfy the trap formula as well. Finally, dead-ends are formulas that are satisfied in states that make the goal unreachable. We introduce a preprocessing algorithm that computes traps in k-DNF form that is exponential in the k parameter, and show how the algorithm can be used to precompute invariants and dead-ends. We report also preliminary tests that illustrate the effectiveness of the preprocessing algorithm for identifying dead-end states, and compare it with the identification that follows from the use of the h1 and h2 heuristics that cannot be preprocessed, and must be computed at run time."
featured: false
publication: "*Twenty-Sixth International Conference on Automated Planning and Scheduling*"
url_pdf: "https://www.aaai.org/ocs/index.php/ICAPS/ICAPS16/paper/download/13190/12679"
---


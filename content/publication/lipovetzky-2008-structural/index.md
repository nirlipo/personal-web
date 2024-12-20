---
title: "Structural Inference in Planning: Scaling up without Heuristic Estimators"
date: 2008-01-01
publishDate: 2020-07-26T09:42:49.077921Z
authors: ["Nir Lipovetzky", "Miquel Ramırez", "Hector Geffner"]
publication_types: ["0"]
abstract: "The aim of this paper is to introduce a different approach to the problem of inference in planning that is not based on either the extraction and use of heuristic functions or reductions into SAT or CSPs. The proposed approach is based on the new notion of consistent causal chains: sequences of causal links ai, pi+ 1, ai+ 1 starting with an action a0 applicable in the current state s and finishing in the goal, where pi+ 1 is an effect of action ai and a precondition of action ai+ 1. We show that by enforcing the semantics of causal links, it is possible to propagate side effects along such chains and detect that some of these chains cannot be part of any plan. Actions a0 that cannot start any consistent causal chain can then be pruned. We show that while simple, this pruning rule is quite powerful: a plain backtracking forward-state search planner with a version of this pruning rule solves as many benchmark problems as the effective Enforced Hill Climbing search of FF, many of them backtrack-free. We then consider extensions of this basic idea and discuss some of its implications."
featured: false
publication: "*Submitted*"
url_pdf: "https://www.researchgate.net/profile/Nir_Lipovetzky/publication/228950574_Structural_Inference_in_Planning_Scaling_up_without_Heuristic_Estimators/links/0912f506d9222da5e7000000.pdf"
---


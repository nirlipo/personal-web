---
title: Trapper 
summary: Invariants, Traps, Un-reachability Certificates, and Dead-end Detection
tags:
- AI Planning
- Verification
date: "02 Jun 2018"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Trapper
  focal_point: Smart
  preview_only: true

links:
url_code: "https://github.com/nirlipo/trapper-lapkt"
url_pdf: "http://people.eng.unimelb.edu.au/nlipovetzky/papers/icaps16_trapper.pdf"
url_video: "https://www.youtube.com/watch?v=dn46rqa6fnc&feature=emb_title"

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

{{< youtube dn46rqa6fnc >}}

We consider the problem of deriving formulas that capture traps, invariants, and dead-ends in classical planning through polynomial forms of preprocessing. An invariant is a formula that is true in the initial state and in all reachable states. A trap is a conditional invariant: once a state is reached that makes the trap true, all the states that are reachable from it will satisfy the trap formula as well. Finally, dead-ends are formulas that are satisfied in states that make the goal unreachable. We introduce a preprocessing algorithm that computes traps in k-DNF form that is exponential in the k parameter, and show how the algorithm can be used to precompute invariants and dead-ends. We report also preliminary tests that illustrate the effectiveness of the preprocessing algorithm for identifying dead-end states, and compare it with the identification that follows from the use of the h^1 and h^2 heuristics that cannot be preprocessed, and must be computed at run time.

---
title: Arcade Learning Environment
summary: Classical Planners playing Atari 2600 games as well as Deep Reinforcement Learning
tags:
- AI Planning
- ALE
- Deep Reinforcement Learning (RL)
date: "02 Jun 2015"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Atari
  focal_point: Smart
  preview_only: true  

# links:
# url_code: "https://github.com/planimation/"
# url_pdf: "https://icaps19.icaps-conference.org/files/pdfs/planimation_icaps19_sysdemo.pdf"
# url_video: "https://www.youtube.com/watch?v=Cj2rWdt1YQU&feature=youtu.be"

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

{{< youtube P-603qPMkSg >}}

The Atari 2600 games supported in the Arcade Learning Environment [(ALE)](http://www.arcadelearningenvironment.org/) all feature a known initial (RAM) state and actions that have deterministic effects. Classical planners, however, cannot be used off-the-shelf as there is no compact PDDL-model of the games, and action effects and goals are not known a priori. Indeed, there are no explicit goals, and the planner must select actions on-line while interacting with a simulator that returns successor states and rewards. None of this precludes the use of blind lookahead algorithms for action selection like breadth-first search or Dijkstra’s yet such methods are not effective over large state spaces. We thus turn to a different class of planning methods introduced recently that have been shown to be effective for solving large planning problems but which do not require prior knowledge of state transitions, costs (rewards) or goals. The empirical results over 54 Atari games show that the simplest such algorithm performs at the level of UCT, the state-of-the-art planning method in this domain, and suggest the potential of width-based methods for planning with simulators when factored, compact action models are not available.

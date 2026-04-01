---
title: "Inference and Decomposition in Planning Using Causal Consistent Chains"
event: ICAPS 2009
event_url: https://aaai.org/papers/00217-13376-inference-and-decomposition-in-planning-using-causal-consistent-chains/

location: ""

summary: ICAPS 2009 talk on path-based inference and decomposition for classical planning.
abstract: >-
  Current state-of-the-art planners solve problems, easy and hard alike, by
  search, expanding hundreds or thousands of nodes. Yet, given the ability of
  people to solve easy problems and to explain their solutions, it seems that an
  essential inferential component may be missing. The reasons expressed by people
  for selecting actions appear to be related to causal chains: sequences of
  causal links $a_i \rightarrow p_{i+1}$, $i = 0, \ldots, n-1$, such that $a_0$
  is applicable in the current state, $p_i$ is a precondition of action $a_i$,
  and $p_n$ is a goal. Some of these causal chains or paths appear to be good,
  some bad, others appear to be impossible. In this work, we focus on such paths
  and develop three techniques for performing inference over them from which a
  path-based planner is obtained. We define the conditions under which a path is
  consistent, provide a heuristic estimate of the cost of achieving the goal
  along a consistent path, and introduce a planning algorithm that uses paths as
  decomposition backbones. The resulting planner, called C3, is not complete and
  does not perform as well as recent planners that carry extensive but extremely
  efficient searches such as LAMA, but is competitive with FF and in particular
  with FF running in EHC mode, which yields very focused but incomplete
  searches. Moreover, many domains are solved backtrack-free, with no search at
  all, suggesting that planning with paths may be a meaningful idea both
  cognitively and computationally.

date: "2009-01-01"

publishDate: "2026-04-01T00:00:00Z"

authors: []
tags:
- planning
- inference
- decomposition
- icaps

featured: false

image:
  caption: ''
  focal_point: Center

links:
- icon: youtube
  icon_pack: fab
  name: Video
  url: https://www.youtube.com/watch?v=S3CcIez2Dbw
url_code: ""
url_pdf: "https://aaai.org/papers/00217-13376-inference-and-decomposition-in-planning-using-causal-consistent-chains/"
url_slides: ""

slides: ""
projects: []

math: true
---

Video available via the link above.
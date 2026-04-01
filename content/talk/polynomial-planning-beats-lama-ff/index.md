---
title: "A Polynomial Planning Algorithm That Beats LAMA and FF"
event: ICAPS 2017
event_url: https://ojs.aaai.org/index.php/ICAPS/article/view/13822

location: ""

summary: ICAPS 2017 talk on polynomial variants of best-first width search that outperform LAMA and FF empirically.
abstract: "It has been shown recently that heuristic and width-based search can be combined to produce planning algorithms with a performance that goes beyond the state-of-the-art. Such algorithms are based on best-first width search (BFWS), a plain best-first search set with evaluation functions combined lexicographically to break ties, some of which express novelty based preferences. In BFWS(f5), for example, the evaluation function f5 weights nodes by a novelty measure, breaking ties by the number of non-achieved goals. BFWS(f5) is a best-first algorithm, and hence, it is complete but not polynomial, and its performance doesn’t match the state of the art. In this work we show, however, that incomplete versions of BFWS(f5) where nodes with novelty greater than k are pruned, are not only polynomial but have an empirical performance that is better than both BFWS(f5) and state-of-the-art planners. This is shown by considering all the international planning competition instances. This is the first time where polynomial algorithms with meaningful bounds are shown to achieve state-of-the-art performance in planning. Practical and theoretical implications of this empirical finding are briefly sketched."

date: "2017-06-05"

publishDate: "2026-04-01T00:00:00Z"

authors: []
tags:
- planning
- width-based-planning
- bfws
- icaps

featured: false

image:
  caption: ''
  focal_point: Center

links:
- icon: youtube
  icon_pack: fab
  name: Video
  url: https://www.youtube.com/watch?v=pJGaVLwZYGM
url_code: ""
url_pdf: "https://ojs.aaai.org/index.php/ICAPS/article/view/13822"
url_slides: ""

slides: ""
projects: []

math: false
---

Video available via the link above.

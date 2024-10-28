---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Count-Based Novelty Exploration in Classical Planning - Master Thesis
subtitle: ''
summary: ''
authors:
- Giacomo Rosa
tags: []
categories: []
date: '2024-08-01'
lastmod: 2024-08-28T14:26:58+11:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-08-01'
publication_types:
- '7'
abstract: 'Count-based exploration methods are widely employed to improve the exploratory behavior of learning agents over sequential decision problems. Meanwhile, Novelty search
has achieved success in Classical Planning through recording of the first, but not successive, occurrences of tuples. In order to structure the exploration, however, the number
of tuples considered needs to grow exponentially as the search progresses. We propose
a new novelty technique, classical count-based novelty, which aims to explore the state
space with a constant number of tuples, by leveraging the frequency of each tuple’s appearance in a search tree. We then justify the mechanisms through which lower tuple
counts lead the search towards novel tuples. We also introduce algorithmic contributions
in the form of a trimmed open list that maintains a constant size by pruning nodes with
bad novelty values. These techniques are shown to complement existing novelty heuristics when integrated in a classical solver, achieving competitive results in challenging
benchmarks from recent International Planning Competitions. Moreover, adapting our
solver as the frontend planner in dual configurations that utilize both memory and time
thresholds demonstrates a significant increase in instance coverage, surpassing current
state-of-the-art solvers, while also maintaining competitive planning time performance.
Finally, we introduce two solvers implementing alternative count-based heuristics and
provide promising results for future developments of the ideas presented in this study'
publication: 'The Univesity of Melbourne'
url_pdf: 'publication/giacomo-master/giacomo_master_thesis.pdf'
---

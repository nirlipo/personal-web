---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Diverse, Top-k, and Top-Quality Planning Over Simulators
subtitle: ''
summary: ''
authors:
- Lyndon Benke
- Tim Miller
- Michael Papasimeon
- Nir Lipovetzky
tags: []
categories: []
date: '2023-09-01'
lastmod: 2023-09-02T23:09:21+11:00
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
publishDate: '2023-09-02T12:09:20.969593Z'
publication_types:
- '1'
abstract: Diverse, top-k, and top-quality planning are concerned with the generation
  of sets of solutions to sequential decision problems. Previously this area has been
  the domain of classical planners that require a symbolic model of the problem instance.
  This paper proposes a novel alternative approach that uses Monte Carlo Tree Search
  (MCTS), enabling application to problems for which only a black-box simulation model
  is available. We present a procedure for extracting bounded sets of plans from pre-generated
  search trees in best-first order, and a metric for evaluating the relative quality
  of paths through a search tree. We demonstrate this approach on a path-planning
  problem with hidden information, and suggest adaptations to the MCTS algorithm to
  increase the diversity of generated plans. Our results show that our method can
  generate diverse and high-quality plan sets in domains where classical planners
  are not applicable.
publication: '*Proceedings of the 26th European Conference on Artificial Intelligence
  (ECAI)*'
url_pdf: 'publication/benke-2023-diverse/FAIA-372-FAIA230275.pdf'
---

---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Width-Based Backward Search
subtitle: ''
summary: ''
authors:
- Chao Lei
- Nir Lipovetzky
tags: []
categories: []
date: '2021-08-01'
lastmod: 2021-09-22T16:18:21+10:00
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
publishDate: '2021-08-22T06:18:21.294712Z'
publication_types:
- '1'
abstract: It has been shown recently that duality mapping is a viable strategy to
  turn progression (forward search) into regression (backward search), but the experimental
  results suggest that the dual versions of standard IPCs benchmarks are quite difficult
  to solve for heuristic search planners. We aim to study the performance of width
  based planners over regression. Our experiments show that width-based search can
  solve dual problems efficiently when the goal state is restricted to single fluent,
  but it becomes challenging when the goal state contains conjunctive fluents. We
  then show that the backward versions of best-first width search with the evaluation
  function f5, BFWS(f5), and its polynomial variant, k-BFWS, are not competitive with
  their forward versions, but can be orthogonal over the IPC benchmarks. Hence, we
  propose a front-to-end bidirectional search k-BDWS and its front-to-front variant
  by integrating forward and backward k-BFWS with the additional intersection check
  between expanded states whose novelty is 1 in the opposite close list. Practical
  findings on the challenges of regression in classical planning are briefly discussed.
publication: '*Proceedings of the International Conference on Automated Planning and
  Scheduling*'
url_pdf: https://ojs.aaai.org/index.php/ICAPS/article/view/15965/15776
url_code: 'https://github.com/you68681/Width-based_backward_search'
url_poster: 'https://icaps21.icaps-conference.org/link/posters/index.html?id=123'
url_video: 'https://icaps21.icaps-conference.org/exhibition/index.html?channel=123'
---

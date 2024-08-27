---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Sampling from Pre-Images to Learn Heuristic Functions for Classical Planning
subtitle: ''
summary: ''
authors:
- Stefan O'Toole
- Miquel Ramirez
- Nir Lipovetzky
- Adrian R Pearce
tags: []
categories: []
date: '2022-01-01'
lastmod: 2023-03-15T17:53:21+11:00
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
publishDate: '2023-03-15T06:53:21.790657Z'
publication_types:
- '1'
abstract: We introduce a new algorithm, Regression based Supervised Learning (RSL),
  for learning per instance Neural Network (NN) defined heuristic functions for classical
  planning problems. RSL uses regression to select relevant sets of states at a range
  of different distances from the goal. RSL then formulates a Supervised Learning
  problem to obtain the parameters that define the NN heuristic, using the selected
  states labeled with exact or estimated distances to goal states. Our experimental
  study shows that RSL outperforms, in terms of coverage, previous classical planning
  NN heuristics functions while requiring a fraction of the training time.
publication: '*Proceedings of the International Symposium on Combinatorial Search*'
url_pdf: https://arxiv.org/pdf/2207.03336.pdf
---

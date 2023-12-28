---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Approximate Novelty Search - IPC-10
subtitle: ''
summary: ''
authors:
- Anubhav Singh
- Nir Lipovetzky
- Miquel Ramirez
- Javier Segovia-Aguas
tags: []
categories: []
date: '2023-06-01'
lastmod: 2023-12-28T14:26:58+11:00
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
publishDate: '2023-12-28T03:26:58.333716Z'
publication_types:
- '4'
abstract: Width-based search is an effective approach to classical planning which
  has produced many successful algorithms over the years. A key feature which distinguishes
  width-based search from classic heuristic search algorithms is the use of specific
  structural properties of the explored state space to guide the exploration and goal-directed
  heuristic measures for exploitation. The structural properties are captured as an
  n-ary relation over the fluents which is processed to compute the state novelty.
  The size of the relation and the time complexity of computing novelty measure is
  exponential on the arity n. Approximate novelty search introduces novel polynomial
  approximations of state novelty and width-based search. It uses Bloom filter to
  efficiently represent the interpretation of the relational predicate and random
  sampling in the computation of state novelty. It also uses an adaptive policy which
  decides to delay the generation of successor states. In this paper, we explain the
  integration of these two techniques into the polynomial-time variant of Best-First
  Width Search (BFWS), one of the most successful width-based algorithm in satisficing
  planning.
publication: '*Proceedings International Planning Competition (IPC-10)*'
url_pdf: 'publication/guang-master/ipc2023_apx_novelty_search.pdf'
---

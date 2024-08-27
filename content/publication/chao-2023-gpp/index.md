---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Novelty and Lifted Helpful Actions in Generalized Planning
subtitle: ''
summary: ''
authors:
- Chao Lei
- Nir Lipovetzky
- Ehinger Krista
tags: []
categories: []
date: '2023-07-15'
lastmod: 2023-05-31T21:45:32+10:00
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
publishDate: '2023-05-31T11:45:32.146933Z'
publication_types:
- '1'
abstract: It has been shown recently that successful techniques in classical planning,
  such as goal-oriented heuristics and landmarks, can improve the ability to compute
  planning programs for generalized planning (GP) problems. In this work, we introduce
  the notion of action novelty rank, which computes novelty with respect to a planning
  program, and propose novelty-based generalized planning solvers, which prune a newly
  generated planning program if its most frequent action repetition is greater than
  a given bound $v$, implemented by novelty-based best-first search BFS(v) and its
  progressive variant PGP(v). Besides, we introduce lifted helpful actions in GP derived
  from action schemes, and propose new evaluation functions and structural program
  restrictions to scale up the search. Our experiments show that the new algorithms
  BFS(v) and PGP(v) outperform the state-of-the-art in GP over the standard generalized
  planning benchmarks.  Practical findings on the above-mentioned methods in generalized
  planning are briefly discussed.
publication: '*Proceedings of the International Symposium on Combinatorial Search,
  SoCS*'
url_pdf: "publication/chao-2023-gpp/SoCS.pdf"
---

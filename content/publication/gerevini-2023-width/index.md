---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Width-Based Search for Multi Agent Privacy-Preserving Planning
subtitle: ''
summary: ''
authors:
- Alfonso E Gerevini
- Nir Lipovetzky
- Francesco Percassi
- Alessandro Saetti
- Ivan Serina
tags: []
categories: []
date: '2023-01-01'
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
publishDate: '2023-03-15T06:53:21.363518Z'
publication_types:
- '2'
abstract: In multi-agent planning, preserving the agents' privacy has become an increasingly
  popular research topic. For preserving the agents' privacy, agents jointly compute
  a plan that achieves mutual goals by keeping certain information private to the
  individual agents. Unfortunately, this can severely restrict the accuracy of the
  heuristic functions used while searching for solutions. It has been recently shown
  that, for centralized planning, blind search algorithms such as width-based search
  can solve instances of many existing domains in low polynomial time when they feature
  atomic goals. Moreover, the performance of goal-oriented search can be improved
  by combining it with width-based search. In this paper, we investigate the usage
  of width-based search in the context of (decentralised) collaborative multi-agent
  privacy-preserving planning, addressing the challenges related to the agents' privacy
  and performance. In particular, we show that width-based search is a very effective
  approach over several benchmark domains, even when the search is driven by heuristics
  that roughly estimate the distance from goal states, computed without using the
  private information of other involved agents. Moreover, we show that the use of
  width-based techniques can significantly reduce the number of messages transmitted
  among the agents, better preserving their privacy and improving their performance.
  An experimental study presented in the paper analyses the effectiveness of our techniques,
  and compares them with the state-of-the-art of collaborative multi-agent planning.
publication: '*Artificial Intelligence*'
url_pdf: https://www.sciencedirect.com/science/article/pii/S0004370223000292?dgcid=coauthor
---

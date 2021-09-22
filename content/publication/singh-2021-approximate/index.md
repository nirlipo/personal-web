---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Approximate Novelty Search
subtitle: ''
summary: ''
authors:
- Anubhav Singh
- Nir Lipovetzky
- Miquel Ramirez
- Javier Segovia-Aguas
tags: []
categories: []
date: '2021-08-01'
lastmod: 2021-09-22T16:27:16+10:00
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
publishDate: '2021-08-22T06:27:16.677366Z'
publication_types:
- '1'
abstract: Width-based search algorithms seek plans by prioritizing states according
  to a suitably defined measure of novelty, that maps states into a set of novelty
  categories. Space and time complexity to evaluate state novelty is known to be exponential
  on the cardinality of the set. We present novel methods to obtain polynomial approximations
  of novelty and width-based search. First, we approximate novelty computation via
  random sampling and Bloom filters, reducing the runtime and memory footprint. Second,
  we approximate the best-first search using an adaptive policy that decides whether
  to forgo the expansion of nodes in the open list. These two techniques are integrated
  into existing width-based algorithms, resulting in new planners that perform significantly
  better than other state-of-the-art planners over benchmarks from the International
  Planning Competitions.
publication: '*Proceedings of the International Conference on Automated Planning and
  Scheduling*'
url_pdf: https://ojs.aaai.org/index.php/ICAPS/article/view/15980/15791
url_code: '#'
url_poster: 'http://icaps21.icaps-conference.org/link/posters/index.html?id=187'
url_video: 'https://icaps21.icaps-conference.org/exhibition/index.html?channel=187'
---

---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Forward Backward Novelty Search
subtitle: ''
summary: ''
authors:
- Anubhav Singh
- Chao Lei
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
publishDate: '2023-12-28T03:26:58.418727Z'
publication_types:
- '4'
abstract: It has been shown recently that width-based search algorithms can be employed
  to search over the regression space (backward search). While many benchmarks are
  challenging for the width-based backward search, it performs significantly better
  than the forward counterparts in certain domains. This orthogonal behavior of forward
  and backward width-based search is quite suitable for an integrated approach. Indeed,
  it has been shown that a simple forward-backward integration that runs forward best-first
  width search (BFWS) with novelty pruning followed by the backward counterpart results
  in better coverage than both. Similarly, pairing forward-backward pruned BFWS algorithm
  with the state-of-the-art Dual-BFWS improves the overall coverage over the IPC satisficing
  benchmark. In this paper, we present an integration of approximate novelty search
  with the forward-backward BFWS.
publication: '*Proceedings International Planning Competition (IPC-10)*'
url_pdf: 'publication/anu-ipc-10-fb/ipc2023_bidirectional_novelty.pdf'
---

---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Width-Based Backward Search - Master Thesis
subtitle: ''
summary: ''
authors:
- Chao Lei
tags: []
categories: []
date: '2020-10-01'
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
publishDate: '2020-10-01'
publication_types:
- '7'
abstract: 'The current study on duality mapping proposed by Suda (2013) is a viable
  strategy to turn progression (forward search) into regression (backward search),
  and the experiment results suggest that the dual versions of standard IPCs benchmark
  domains are quite difficult to solve for heuristic-based search. We adopt width-based
  search (IW and SIW) in this thesis to test the performance on dual problems. The
  experiment results show that dual problems can be solved efficiently when the goal
  state is restricted to single fluent, but it becomes challenging when the goal state
  contains conjunctive fluents. 
  
  Then, we turn serialized iterated width, SIW, best-first
  width search with the evaluation function f 5, BFWS(f5), and the polynomial variants
  of BFWS(f5), k-BFWS(f5) from progression into regression by modifying the state
  space. Results show that the backward versions are uncompetitive with the forward
  versions but still outperform in some IPCs benchmark domains in all SIW, BFWS(f5)
  and k-BFWS(f5). 
  
  Furthermore, we build a bidirectional search, k-BFWBS by integrating
  forward and backward k-BFWS(f5) with six different combinations. Although these
  six combinations cannot solve more problems than only adopting forward k -BFWS(f
  5) among tested IPCs benchmark domains, they are distinctive. However, if we run
  forward k -BFWS(f5) first and then run backward k-BFWS(f5), it outperforms only
  running forward k-BFWS(f5), which proves that backward search is useful. 
  
  All results
  in this thesis indicate that although backward search is uncompetitive and multiple
  issues still exist, it is still worthy of having a deep exploration of backward
  search since it not only finds more plans in some domains but also proposes a different
  perspective to analyse classical planning tasks. Meanwhile, we point out the weaknesses
  of backward search and give relevant solutions, and a new method complete domain
  is presented to perfect backward search.'
publication: 'The Univesity of Melbourne'
url_pdf: 'publication/chao-master/Chao_University_of_Melbourne_Master_Thesis.pdf'
---

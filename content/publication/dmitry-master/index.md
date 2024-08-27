---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: 'Learning to Generalise through Features - Masters Thesis'
subtitle: ''
summary: ''
authors:
- Dmitry Grebenyuk
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
abstract: 'A Markov decision process (MDP) cannot be used for learning end-to-end control policies
in Reinforcement Learning when the dimension of the feature vectors changes from one
trial to the next. For example, this difference is present in an environment where the
number of blocks to manipulate can vary. Because we cannot learn a different policy
for each number of blocks, we suggest framing the problem as a POMDP instead of the
MDP. It allows us to construct a constant observation space for a dynamic state space.
There are two ways we can achieve such construction.
First, we can design a hand-crafted set of observations for a particular problem. However,
that set cannot be readily transferred to another problem, and it often requires domaindependent
knowledge.
On the other hand, a set of observations can be deduced from visual observations. This
approach is universal, and it allows us to easily incorporate the geometry of the problem
into the observations, which can be challenging to hard-code in the former method.
In this Thesis, we examine both of these methods. Our goal is to learn policies that
can be generalised to new tasks. First, we show that a more general observation space
can improve the performance of policies tested in untrained tasks. Second, we show
that meaningful feature vectors can be obtained from visual observations. If properly
regularised, these vectors can re
ect the spacial structure of the state space and used
for planning. Using these vectors, we construct an auto-generated reward function, able
to learn working policies.'
publication: 'The Univesity of Melbourne'
url_pdf: 'publication/dmitry-master/Dmitry_MPhil_thesis.pdf'
---

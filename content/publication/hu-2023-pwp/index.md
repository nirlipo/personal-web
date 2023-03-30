---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Planning with Multi-agent Belief Using Justified Perspectives
subtitle: ''
summary: ''
authors:
- Guang Hu
- Tim Miller
- Nir Lipovetzky
tags: []
categories: []
date: '2023-07-01'
lastmod: 2023-03-27T09:17:16+11:00
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
publishDate: '2023-03-26T22:17:16.775208Z'
publication_types:
- '1'
abstract: Epistemic planning plays an important role in multi-agent and human-agent
  interaction domains.  Most existing works solve multi-agent epistemic planning problems
  by either pre-compiling them into classical planning problems; or, using explicit
  actions and their effects to encode Kripke-based semantics.  A recent approach called
  Planning with Perspectives (PWP) delegates epistemic reasoning in planning to external
  functions using F-STRIPS, keeping the search within the planning algorithm and lazily
  evaluating epistemic formulae. Although PWP is expressive and efficient, it models
  S5 epistemic logic and does not support belief, including false belief.  In this
  paper, we extend the PWP model to handle multi-agent belief by following the intuition
  that agents believe something they have seen until they see otherwise. We call this
  justified perspectives. We formalise this notion of multi-agent belief based on
  the definition of knowledge in PWP. Using experiments on existing epistemic and
  doxastic planning benchmarks, we show that our belief planner can solve benchmarks
  more efficiently than the state-of-the-art baseline, and can model some problems
  that are infeasible to model using propositional-based approaches.
publication: '*Proceedings of the International Conference on Automated Planning and
  Scheduling*'
url_pdf: 'publication/hu-2023-pwp/Belief_with_PWP.pdf'
---

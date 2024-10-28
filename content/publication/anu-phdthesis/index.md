---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: 'Lazy Constraint Generation and Tractable
Approximations for Large-scale Planning
Problems'
subtitle: ''
summary: ''
authors:
- Anubhav Singh
tags: []
categories: []
date: '2024-4-01'
lastmod: 2024-04-01
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
publishDate: '2024-04-01'
publication_types:
- '7'
abstract: 'In our research, we explore two orthogonal but related methodologies of solving planning
instances: planning algorithms based on direct but lazy, incremental heuristic search over
transition systems and planning as satisfiability. We address numerous challenges associated with solving large planning instances within practical time and memory constraints.
This is particularly relevant when solving real-world problems, which often have numeric
domains and resources and, therefore, have a large ground representation of the planning
instance. Our first contribution is an approximate novelty search, which introduces two
novel methods. The first approximates novelty via sampling and Bloom filters, and the
other approximates the best-first search using an adaptive policy that decides whether
to forgo the expansion of nodes in the open list. For our second work, we present an
encoding of the partial order causal link (POCL) formulation of the temporal planning
problems into a CP model that handles the instances with required concurrency, which
cannot be solved using sequential planners. Our third significant contribution is on lifted
sequential planning with lazy constraint generation, which scales very well on large instances with numeric domains and resources. Lastly, we propose a novel way of using
novelty approximation as a polynomial reachability propagator, which we use to train
the activity heuristics used by the CP solvers.
'
publication: 'The Univesity of Melbourne'
url_pdf: 'publication/anu-phdthesis/anu_phd_thesis.pdf'
---

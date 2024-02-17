---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Generalized Planning for the Abstraction and Reasoning Corpus
subtitle: ''
summary: ''
authors:
- Chao Lei
- Nir Lipovetzky
- Krista A Ehinger
tags: []
categories: []
date: '2024-02-20'
lastmod: 2024-02-17T17:41:06+11:00
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
publishDate: '2024-02-17T06:41:05.905710Z'
publication_types:
- '1'
abstract: The Abstraction and Reasoning Corpus (ARC) is a general artificial intelligence
  benchmark that poses difficulties for pure machine learning methods due to its requirement
  for fluid intelligence with a focus on reasoning and abstraction. In this work,
  we introduce an ARC solver, Generalized Planning for Abstract Reasoning (GPAR).
  It casts an ARC problem as a generalized planning (GP) problem, where a solution
  is formalized as a planning program with pointers. We express each ARC problem using
  the standard Planning Domain Definition Language (PDDL) coupled with external functions
  representing object-centric abstractions. We show how to scale up GP solvers via
  domain knowledge specific to ARC in the form of restrictions over the actions model,
  predicates, arguments and valid structure of planning programs. Our experiments
  demonstrate that GPAR outperforms the state-of-the-art solvers on the object-centric
  tasks of the ARC, showing the effectiveness of GP and the expressiveness of PDDL
  to model ARC problems. The challenges provided by the ARC benchmark motivate research
  to advance existing GP solvers and understand new relations with other planning
  computational models.
publication: '*Thirty-Eighth AAAI Conference on Artificial Intelligence*'
url_pdf: https://arxiv.org/pdf/2401.07426.pdf
links:
  - name: HTML-paper
    url: https://arxiv.org/html/2401.07426v1
url_code: github.com/you68681/GPAR

---

---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: 'What you get is what you see: Decomposing Epistemic Planning using Functional
  STRIPS - Masters Thesis'
subtitle: ''
summary: ''
authors:
- Guang Hu
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
abstract: 'Epistemic planning -- planning with knowledge and belief -- is essentialin many multi-agent and human-agent interaction domains. Most state-of-the-art epistemic planners solve this problem by compiling to propositional
classical planning, for example, generating all possible knowledge
atoms, or compiling epistemic formula to normal forms. It is noted that the
compilations are typically exponentially larger than the original problem.
However, these methods become computationally infeasible as problems
grow. In addition, those methods only works on propositional variables in
discrete domains.

In this thesis, we decompose epistemic planning by delegating epistemic
logic reasoning to an external solver. We do this by modelling the
problem using functional STRIPS, which is more expressive than standard
STRIPS and supports the use of external, black-box functions within action
models. Exploiting recent work that demonstrates the relationship between
what an agent ‘sees’ and what it knows, we allow modellers to provide
new implementations of externals functions. These define what agents see
in their environment, allowing new epistemic logics to be defined without
changing the planner. As a result, the capability and flexibility of the
epistemic model itself are increased, as our model is able to avoid exponential
pre-compilation steps and handle logics from continuous domains.
We ran evaluations on well-known epistemic planning benchmarks to compare
with an existing state-of-the-art planner, and on new scenarios based
on different external functions. The results show that our planner scales
significantly better than the state-of-the-art planner which we compared
against, and can express problems more succinctly.'
publication: 'The Univesity of Melbourne'
url_pdf: 'publication/guang-master/Guang_University_of_Melbourne_Master_Thesis.pdf'
---

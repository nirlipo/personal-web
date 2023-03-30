---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Planning with Perspectives--Decomposing Epistemic Planning using Functional
  STRIPS
subtitle: ''
summary: ''
authors:
- Guang Hu
- Tim Miller
- Nir Lipovetzky
tags: []
categories: []
date: '2022-01-01'
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
publishDate: '2023-03-15T06:53:21.725203Z'
publication_types:
- '2'
abstract: In this paper, we present a novel approach to epistemic planning called
  planning with perspectives (PWP) that is both more expressive and computationally
  more efficient than existing state-of-the-art epistemic planning tools. Epistemic
  planning — planning with knowledge and belief — is essential in many multi-agent
  and human-agent interaction domains. Most state-of-the-art epistemic planners solve
  epistemic planning problems by either compiling to propositional classical planning
  (for example, generating all possible knowledge atoms or compiling epistemic formulae
  to normal forms); or explicitly encoding Kripke-based semantics. However, these
  methods become computationally infeasible as problem sizes grow. In this paper,
  we decompose epistemic planning by delegating reasoning about epistemic formulae
  to an external solver. We do this by modelling the problem using Functional STRIPS,
  which is more expressive than standard STRIPS and supports the use of external,
  black-box functions within action models. Building on recent work that demonstrates
  the relationship between what an agent ‘sees’ and what it knows, we define the perspective
  of each agent using an external function, and build a solver for epistemic logic
  around this. Modellers can customise the perspective function of agents, allowing
  new epistemic logics to be defined without changing the planner. We ran evaluations
  on well-known epistemic planning benchmarks to compare an existing state-of-the-art
  planner, and on new scenarios that demonstrate the expressiveness of the PWP approach.
  The results show that our PWP planner scales significantly better than the state-of-the-art
  planner that we compared against, and can express problems more succinctly.
publication: '*Journal of Artificial Intelligence Research*'
url_pdf: https://www.jair.org/index.php/jair/article/download/13446/26853/32149
---

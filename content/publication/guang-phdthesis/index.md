---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: '"Seen Is Believing": Modeling and Solving Epistemic Planning Problems using Justified Perspectives'
subtitle: ''
summary: ''
authors:
- Guang Hu
tags: []
categories: []
date: '2025-07-01'
lastmod: 2026-01-27T00:00:00+00:00
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
publishDate: '2025-07-01'
publication_types:
- '7'
abstract: 'Epistemic planning —– planning that incorporates knowledge and belief (knowledge that could be false) — is crucial in many multi-agent and human-agent interaction settings. However, existing approaches often struggle with scalability, particularly as the number of agents or the depth of nested epistemic relations grows. A notable exception is the state-based methods that use agent’s perspective model, which focuses reasoning only on the visible part of states for agents. By delegating epistemic reasoning to an external function, this method enhances expressiveness and efficiency in solving complex epistemic planning tasks. Despite these advantages, the PWP approach has limitations, including an imprecise trade-off between efficiency and completeness and a lack of systematic modeling for beliefs, especially false beliefs.

In this thesis, we extend agent’s perspective model to develop a more efficient and effective model for epistemic planning. First, we introduce multiple semantic formats with agent‘’s perspective model to clarify the balance between efficiency and completeness. Then, with the intuition that people reason unseen by retrieving their memory, we extend the original model to handle justified beliefs, resulting in the Justified Perspective (JP) model. Furthermore, we formalize the encoding, design a planner with various search algorithms, and conduct comprehensive experiments demonstrating that our approach is both more efficient and expressive than the current state-of-the-art in epistemic planning. Finally, the JP model is expanded to represent group beliefs (the final missing puzzle of the epistemic logic), including distributed beliefs and common beliefs.

Overall, in this thesis, we provide an efficient and expressive planning framework, including an (action) model-free epistemic logic reasoning model, establishing the framework’s potential for broader applications.'
publication: 'The University of Melbourne'
url_pdf: publication/guang-phdthesis/guang_phd_thesis.pdf
---

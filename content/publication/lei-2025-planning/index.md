---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: 'Planning-Driven Programming: A Large Language Model Programming Workflow'
subtitle: ''
summary: ''
authors:
- Chao Lei
- Yanchuan Chang
- Nir Lipovetzky
- Krista A Ehinger
tags: []
categories: []
date: '2025-07-21'
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
publishDate: '2025-07-21T00:00:00Z'
publication_types:
- '1'
abstract: 'The strong performance of large language models (LLMs) raises extensive discussion on their application to code generation. Recent research suggests continuous program refinements through visible tests to improve code generation accuracy in LLMs. However, these methods suffer from LLMs'' inefficiency and limited reasoning capacity. In this work, we propose an LLM programming workflow (LPW) designed to improve both initial code generation and subsequent refinements within a structured two-phase workflow. Specifically, the solution generation phase formulates a solution plan, which is then verified through visible tests to specify the intended natural language solution. Subsequently, the code implementation phase drafts an initial code according to the solution plan and its verification. If the generated code fails the visible tests, the plan verification serves as the intended solution to consistently inform the refinement process for correcting bugs. Compared to state-of-the-art methods across various existing LLMs, LPW significantly improves the Pass@1 accuracy by up to 16.4% on well-established text-to-code generation benchmarks.'
publication: '*Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)*'
url_pdf: https://aclanthology.org/2025.acl-long.621.pdf
url_doi: https://aclanthology.org/2025.acl-long.621/
---

---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: 'Planning in the Dark: LLM-Symbolic Planning Pipeline without Experts'
subtitle: ''
summary: ''
authors:
- Sukai Huang
- Nir Lipovetzky
- Trevor Cohn
tags: []
categories: []
date: '2025-04-11'
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
publishDate: '2025-04-11T00:00:00Z'
publication_types:
- '1'
abstract: 'Large Language Models (LLMs) have shown promise in solving natural language-described planning tasks, but their direct use often leads to inconsistent reasoning and hallucination. While hybrid LLM-symbolic planning pipelines have emerged as a more robust alternative, they typically require extensive expert intervention to refine and validate generated action schemas. It not only limits scalability but also introduces a potential for biased interpretation, as a single expert''s interpretation of ambiguous natural language descriptions might not align with the user''s actual intent. To address this, we propose a novel approach that constructs an action schema library to generate multiple candidates, accounting for the diverse possible interpretations of natural language descriptions. We further introduce a semantic validation and ranking module that automatically filters and ranks these candidates without expert-in-the-loop. The experiments show our pipeline maintains superiority in planning over the direct LLM planning approach. These findings demonstrate the feasibility of a fully automated end-to-end LLM-symbolic planner that requires no expert intervention, opening up the possibility for a broader audience to engage with AI planning with less prerequisite of domain expertise.'
publication: '*Proceedings of the AAAI Conference on Artificial Intelligence*'
url_pdf: https://ojs.aaai.org/index.php/AAAI/article/download/34855/37010
url_doi: https://ojs.aaai.org/index.php/AAAI/article/view/34855
---

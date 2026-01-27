---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: 'Chasing Progress, Not Perfection: Revisiting Strategies for End-to-End LLM Plan Generation'
subtitle: ''
summary: ''
authors:
- Sukai Huang
- Trevor Cohn
- Nir Lipovetzky
tags: []
categories: []
date: '2025-11-01'
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
publishDate: '2025-11-01T00:00:00Z'
publication_types:
- '1'
abstract: 'The capability of Large Language Models (LLMs) to plan remains a topic of debate. Some critics argue that strategies to boost LLMs'' reasoning skills are ineffective in planning tasks, while others report strong outcomes merely from training models on a planning corpus. This paper revisits these claims by developing an end-to-end LLM-based planner and evaluating a range of reasoning-enhancement strategies---including fine-tuning, Chain-of-Thought (CoT) prompting, and reinforcement learning (RL)---across multiple dimensions of plan quality: validity, executability, goal satisfiability, and more. Our findings reveal fine-tuning alone is insufficient, especially on out-of-distribution tasks. Strategies like CoT prompting primarily enhance local coherence, yielding higher executability rates---a necessary prerequisite for validity---but provide only incremental gains and struggle to ensure global plan validity. Notably, RL guided by a novel Longest Contiguous Common Subsequence reward significantly enhances both executability and validity, particularly on longer-horizon problems.'
publication: '*Proceedings of the International Conference on Automated Planning and Scheduling (ICAPS)*'
url_pdf: https://ojs.aaai.org/index.php/ICAPS/article/download/36119/38273
url_doi: https://ojs.aaai.org/index.php/ICAPS/article/view/36119
---

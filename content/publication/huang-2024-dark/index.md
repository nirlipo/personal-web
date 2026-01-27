---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: 'The Dark Side of Rich Rewards: Understanding and Mitigating Noise in VLM Rewards'
subtitle: ''
summary: ''
authors:
- Sukai Huang
- Shu-Wei Liu
- Nir Lipovetzky
- Trevor Cohn
tags: []
categories: []
date: '2025-09-15'
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
publishDate: '2025-11-15T00:00:00Z'
publication_types:
- '1'
abstract: 'While Vision-Language Models (VLMs) are increasingly used to generate reward signals for training embodied agents to follow instructions, our research reveals that agents guided by VLM rewards often underperform compared to those employing only intrinsic (exploration-driven) rewards, contradicting expectations set by recent work. We hypothesize that false positive rewards -- instances where unintended trajectories are incorrectly rewarded -- are more detrimental than false negatives. Our analysis confirms this hypothesis, revealing that the widely used cosine similarity metric is prone to false positive reward estimates. To address this, we introduce BiMI (Binary Mutual Information), a novel reward function designed to mitigate noise. BiMI significantly enhances learning efficiency across diverse and challenging embodied navigation environments. Our findings offer a nuanced understanding of how different types of reward noise impact agent learning and highlight the importance of addressing multimodal reward signal noise when training embodied agents.'
publication: '*ICAPS 2025 Workshop on Planning and Reinforcement Learning (PRL)*'
url_pdf: https://arxiv.org/pdf/2409.15922
url_arxiv: https://arxiv.org/abs/2409.15922
---

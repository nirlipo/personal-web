---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: 'State-Based Disassembly Planning'
subtitle: ''
summary: ''
authors:
- Chao Lei
- Nir Lipovetzky
- Krista A Ehinger
tags: []
categories: []
date: '2025-01-09'
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
publishDate: '2025-01-09T00:00:00Z'
publication_types:
- '1'
abstract: 'It has been shown recently that physics-based simulation significantly enhances the disassembly capabilities of real-world assemblies with diverse 3D shapes and stringent motion constraints. However, the efficiency suffers when tackling intricate disassembly tasks that require numerous simulations and increased simulation time. In this work, we propose a State-Based Disassembly Planning (SBDP) approach, prioritizing physics-based simulation with translational motion over rotational motion to facilitate autonomy, reducing dependency on human input, while storing intermediate motion states to improve search scalability. We introduce two novel evaluation functions derived from new Directional Blocking Graphs (DBGs) enriched with state information to scale up the search. Our experiments show that SBDP with new evaluation functions and DBGs constraints outperforms the state-of-the-art in disassembly planning in terms of success rate and computational efficiency over benchmark datasets consisting of thousands of physically valid industrial assemblies.'
publication: '*Proceedings of the AAAI Conference on Artificial Intelligence*'
url_pdf: https://ojs.aaai.org/index.php/AAAI/article/view/33600/35755
url_doi: https://ojs.aaai.org/index.php/AAAI/article/view/33600
---

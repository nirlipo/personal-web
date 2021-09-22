---
title: "Inference and decomposition in planning using causal consistent chains"
date: 2009-01-01
publishDate: 2020-07-26T09:42:49.072443Z
authors: ["Nir Lipovetzky", "Héctor Geffner"]
publication_types: ["1"]
abstract: "Current state-of-the-art planners solve problems, easy and hard alike, by search, expanding hundreds or thousands of nodes. Yet, given the ability of people to solve easy problems and to explain their solutions, it seems that an essential inferential component may be missing. The reasons expressed by people for selecting actions appear to be related to causal chains: sequences of causal links a i→ p i+ 1, i= 0,..., n–1, such that a 0 is applicable in the current state, p i is a precondition of action a i, and p n is a goal. Some of these causal chains or paths appear to be good, some bad, others appear to be impossible. In this work, we focus on such paths and develop three techniques for performing inference over them from which a path-based planner is obtained. We define the conditions under which a path is consistent, provide an heuristic estimate of the cost of achieving the goal along a consistent path, and introduce a planning algorithm that uses paths as decomposition backbones. The resulting planner, called C3, is not complete and does not perform as well as recent planners that carry extensive but extremely efficient searches such as LAMA, but is competitive with FF and in particular, with FF running in EHC mode which yields very focused but incomplete searches, and thus provides, a more apt comparison. Moreover, many domains are solved backtrack-free, with no search at all, suggesting that planning with paths may be a meaningful idea both cognitively and computationally."
featured: false
publication: "*Nineteenth International Conference on Automated Planning and Scheduling*"
url_pdf: "https://www.aaai.org/ocs/index.php/ICAPS/ICAPS09/paper/download/745/1115"
---


---
title: "A Polynomial Planning Algorithm that Beats LAMA and FF"
date: 2017-01-01
publishDate: 2020-07-26T09:42:49.109169Z
authors: ["Nir Lipovetzky", "Hector Geffner"]
publication_types: ["1"]
abstract: "It has been shown recently that heuristic and width-based search can be combined to produce planning algorithms with a performance that goes beyond the state-of-the-art. Such algorithms are based on best-first width search (BFWS), a plain best-first search set with evaluations functions combined lexicographically to break ties, some of which express novelty based preferences. In BFWS (f5), for example, the evaluation function f5 weights nodes by a novelty measure, breaking ties by the number of non-achieved goals. BFWS (f5) is a best-first algorithm, and hence, it is complete but not polynomial, and its performance doesn’t match the state of the art. In this work we show, however, that incomplete versions of BFWS (f5) where nodes with novelty greater than k are pruned, are not only polynomial but have an empirical performance that is better than both BFWS (f5) and state-of-the-art planners. This is shown by considering all the international planning competition instances. This is the first time where polynomial algorithms with meaningful bounds are shown to achieve state-of-the-art performance in planning. Practical and theoretical implications of this empirical finding are briefly sketched."
featured: false
publication: "*International Conference on Automated Planning and Scheduling (ICAPS)*"
url_pdf: "https://www.aaai.org/ocs/index.php/ICAPS/ICAPS17/paper/viewPDFInterstitial/15740/15105"
---


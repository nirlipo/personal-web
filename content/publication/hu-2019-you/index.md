---
title: "What you get is what you see: Decomposing Epistemic Planning using Functional STRIPS"
date: 2019-01-01
publishDate: 2020-07-26T09:42:49.124320Z
authors: ["Guang Hu", "Tim Miller", "Nir Lipovetzky"]
publication_types: ["2"]
abstract: "Epistemic planning---planning with knowledge and belief---is essential in many multi-agent and human-agent interaction domains. Most state-of-the-art epistemic planners solve this problem by compiling to propositional classical planning, for example, generating all possible knowledge atoms, or compiling epistemic formula to normal forms. However, these methods become computationally infeasible as problems grow. In this paper, we decompose epistemic planning by delegating reasoning about epistemic formula to an external solver. We do this by modelling the problem usingemph functional STRIPS, which is more expressive than standard STRIPS and supports the use of external, black-box functions within action models. Exploiting recent work that demonstrates the relationship between what an agentsees' and what it knows, we allow modellers to provide new implementations of externals functions. These define what agents see in their environment, allowing new epistemic logics to be defined without changing the planner. As a result, it increases the capability and flexibility of the epistemic model itself, and avoids the exponential pre-compilation step. We ran evaluations on well-known epistemic planning benchmarks to compare with an existing state-of-the-art planner, and on new scenarios based on different external functions. The results show that our planner scales significantly better than the state-of-the-art planner against which we compared, and can express problems more succinctly."
featured: false
publication: "*arXiv preprint arXiv:1903.11777*"
url_pdf: "https://arxiv.org/pdf/1903.11777"
---


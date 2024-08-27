---
title: "MAP-LAPKT: Omnipotent Multi-Agent Planning via Compilation to Classical Planning"
date: 2015-01-01
publishDate: 2020-07-26T09:42:49.101292Z
authors: ["Christian Muise", "Nir Lipovetzky", "Miquel Ramirez"]
publication_types: ["2"]
abstract: "In this paper we describe three related entries submitted to the CoDMAP planning contest (Stolba, Komenda, and Kovacs 2015). All three entries are configurations of the classical planning framework LAPKT (Ramirez, Lipovetzky, and Muise 2015), and all three use the same pre-compiled input. Our approach is based on the following insight: nn The task of planning for multiple agents with heterogeneous access to fluent observability can be solved by classical planners using the appropriate encoding. nn  The general approach is quite simple: we convert the unfactored domain and problem file into a classical planning problem such that the privacy of fluents and objects are respected. The translation is both sound and complete, and we solve the encoded problem using a centralized classical planner. None of the factorization is passed to the classical planner, because the encoded problem contains all the necessary information as part of the problem itself. In the remainder of the document, we outline (1) the simple encoding that we use to create a classical planning problem, (2) the planning framework that we use to solve the encoded problems, and (3) the configurations that we submitted to the CoDMAP contest."
featured: false
publication: "*Proceedings of the Competition of Distributed and Multiagent Planners (CoDMAP)*"
url_pdf: "https://people.eng.unimelb.edu.au/nlipovetzky/papers/CoDMAP15_LAPKT.pdf"
---


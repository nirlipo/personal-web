---
title: Linear Temporal Logic, Planning and Synthesis
summary: classical planners computing infinite loopy plans, and FOND planners synthesizing controllers expressed as policies.
tags:
- AI Planning,
- Linear Temporal Logic (LTL)
- Synthesis
- Verification
date: "02 Jun 2013"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Classical Planners
  focal_point: Smart

links:
- name: code IJCAI-11
  url: https://people.eng.unimelb.edu.au/nlipovetzky/software/LTL_ijcai2011.tar.bz2  
- name: code IJCAI-13  
  url: "https://github.com/nirlipo/ltl2pddl"
- name: PDF IJCAI-11
  url: "https://www.aaai.org/ocs/index.php/IJCAI/IJCAI11/paper/viewPDFInterstitial/3217/3798"
- name: PDF IJCAI-13
  url: "https://www.aaai.org/ocs/index.php/IJCAI/IJCAI13/paper/viewPDFInterstitial/6653/7045"
# url_video: "https://www.youtube.com/watch?v=Cj2rWdt1YQU&feature=youtu.be"

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

In this project we showed how to compute infinte plans for LTL goals. Infinite plans are akin to the problem of control synteshis. Given an LTL formula, the tools developed encodes the LTL goal formula as Deterministic Buchi Automata states. The Automata is encoded along with the allowed transitions of the agent in the Planning Domain Description Language (PDDL). The problem becomes a fully observable non-deterministic planning problem (FOND) or a classical problem, depending on whether the environment can act non-deterministically.


  
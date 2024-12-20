---
title: Width Based Planning
summary: Width Based Planning searches for solutions through a general measure of state novelty. Performs well over black-box simulators and PDDL problems.
tags:
- AI Planning
- Width Based Planning
date: "2020-04-27T00:00:00Z"

# links:
# - name: Documentation
#   url: https://planimation.github.io/documentation/
#   # icon_pack: fas
#   # icon: books
# url_code: "https://github.com/planimation/"
# url_pdf: "https://icaps19.icaps-conference.org/files/pdfs/planimation_icaps19_sysdemo.pdf"
# url_video: "https://www.youtube.com/watch?v=Cj2rWdt1YQU&feature=youtu.be"


# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Width
  focal_point: Smart
  preview_only: false

---


Width Based Planning searches for solutions through a general measure of state novelty. When the dynamics of the problem are given through simulator engines such as the Atari games (ALE), GVGAI, or complex robotic and UaV flight simulators, novelty exploration yields state-of-the-art performance compared to known alternatives such as MCTS. Novelty exploration can be combined as well with the exploitation of goal-based heuristics within a general Best First Width Search. BFWS can solve efficiently classical planning problems even when the action model is hidden, opening exciting opportunities to model beyond declarative action representations.

# Talks: 

- **Tractable novelty exploration over Continuous and Discrete Sequential Decision Problems**, _School of Computing and information Systems Seminar, The University of Melbourne, September 2021_
   {{< youtube -qQ4yPSt16U >}}

- [Width-Based Algorithms for Common Problems in Control, Planning and Reinforcement Learning](https://recorder-v3.slideslive.com/#/share?share=46565&s=8b78bd0a-2b0c-480b-aae2-ee2700d6fc05), [Early Career Spotlight](https://ijcai-21.org/early-career-spotlight-invited-talk/) at IJCAI 2021.

# Papers:

(Disclaimer: this is not a comprehensive list, please get in touch to add relevant work that has been missed)

A position paper `[Width-Based Algorithms for Common Problems in Control, Planning and Reinforcement Learning](https://www.ijcai.org/proceedings/2021/0702.pdf)' was presented as part of the [Early Career Spotlight](https://ijcai-21.org/early-career-spotlight-invited-talk/) at IJCAI 2021.

# Table of Contents
1. [Classical Planning over STRIPS/PDDL](#classical-planning-over-pddl)
2. [Classical Planning over Simulators](#classical-planning-over-simulators)
3. [Continous State Simulators](#continous-state-simulators)
4. [Planning and Learning](#planning-and-learning)
5. [Planning over Factored Simulators in Functional STRIPS](#planning-over-factored-simulators-in-functional-strips)
6. [MDP over Simulators](#mdp-over-simulators)
7. [Multi Agent (Descentralisd & Privacy Preserving) Planning](#multi-agent-descentralisd-and-privacy-preserving-planning)

## Classical Planning over PDDL
- Classical **Width Definition**, Iterative Width (**IW**), Serialized IW (**SIW**), **SIW+**, and **DFS+** algorithms 
   - [N. Lipovetzky and H. Geffner, ECAI12](https://nirlipo.github.io/publication/lipovetzky-2012-width/width-ecai-12.pdf)
   - [PhD. Thesis, Nir Lipovetzky, 2012](https://nirlipo.github.io/publication/lipovetzky-2014-structure/aiaccess_nirlipo.pdf), [ICAPS Best dissertation Award 2013](http://www.icaps-conference.org/index.php/Main/Awards)  
   - [N. Lipovetzky and H. Geffner, ECAI14](https://nirlipo.github.io/publication/lipovetzky-2014-width/width-ecai-14.pdf)

- Best First Width Search (**BFWS**) 
   - [N. Lipovetzky and H. Geffner, AAAI17](https://nirlipo.github.io/publication/lipovetzky-2017-best/bfws-aaai-17.pdf) 
   - Polynomial BFWS planner  [N. Lipovetzky and H. Geffner, ICAPS17](https://nirlipo.github.io/publication/lipovetzky-2017-polynomial/poly-bfws-icaps-17.pdf)
   - BFWS and quantified heuristic novelty measures [M. Katz, N. Lipovetzky, D. Moshkovich, A. Tuisov, ICAPS17](https://nirlipo.github.io/publication/katz-2017-adapting/icaps17-quantified-novelty.pdf)

- Approximate Novelty computation
   - [A. Singh, J. Segovia, M. Ramirez, N. Lipovetzky ICAPS21](https://ojs.aaai.org/index.php/ICAPS/article/view/15980/15791)

- Action Novelty 
   - [A. Tuisov, M. Katz, IJCAI21](https://www.ijcai.org/proceedings/2021/0576.pdf)

- Novelty Decompositions
   - [B Bonet, H Geffner, AAAI21](https://bonetblai.github.io/reports/AAAI21-width.pdf)
   - [D Drexler, J Seipp, H Geffner, KR21](https://www.diva-portal.org/smash/record.jsf?pid=diva2:1578987)
   - [M Junyent, A Jonsson, V Gómez, ICAPS21](https://ojs.aaai.org/index.php/ICAPS/article/download/15999/15810)

## Classical Planning over Simulators
- IW over **Atari** Simulator (ALE) 
   - [N. Lipovetzky, M. Ramirez, and H. Geffner, IJCAI15](https://nirlipo.github.io/publication/lipovetzky-2105-classical/iw-atari-ijcai-2015.pdf)
   - [A. Shleyfman, A. Tuisov, and C. Domshlak, IJCAI16](http://www.ijcai.org/Proceedings/16/Papers/460.pdf) 
   - [Y. Jinnai and A. Fukunaga, AAAI17](https://jinnaiyuu.github.io/pdf/papers/AAAI-17%20Jinnai-Fukunaga.pdf)  
   - [W. Bandres, B. Bonet, H. Geffner, AAAI18](https://arxiv.org/pdf/1801.03354) 
   
## Continous State Simulators
 - Features for Continuous-State Domains. Competitive with DRL and LQR on [control problems](https://gym.openai.com/envs/#control) over gym.openai simulator
   - [Florent Teichteil-Königsbuch, Miquel Ramirez, Nir Lipovetzky, IJCAI20](https://www.ijcai.org/Proceedings/2020/0578.pdf)
## Pleanning and Learning
 - IW and Learnt Policies [M Junyent, A Jonsson, V Gómez, ICAPS19](https://ojs.aaai.org/index.php/ICAPS/article/download/3554/3432/)
 - Hierarchical Learning [M Junyent, A Jonsson, V Gómez, ICAPS21](https://ojs.aaai.org/index.php/ICAPS/article/download/15999/15810)
 - Learning symbolic representation with VAE [A Dittadi, FK Drachmann, T Bolander](https://ojs.aaai.org/index.php/AAAI/article/view/16627)

## Planning over Factored Simulators in Functional STRIPS
Factored simulators accept finite domain variables, and mixed Declarative and Programatic (simulated) dynamics

- BFWS with **simulators** and **Functional STRIPS** (FSTRIPS) - [G. Francès, M. Ramirez, N. Lipovetzky, and H. Geffner, IJCAI17](https://nirlipo.github.io/publication/frances-2017-purely/ijcai17-planning-with-simulators.pdf)
- **Task and Motion** Planning - [J. Ferrer-Mestres, G. Francès, and H. Geffner, ARXIV17](https://arxiv.org/pdf/1706.06927.pdf) 
- UaV **Hybrid Control** - [M. Ramirez, M. Papasimeon, N. Lipovetzky, L. Benke, T. Miller, A. Pearce, E. Scala, M. Zamani, AAMAS18](https://nirlipo.github.io/publication/ramirez-2018-integrated/aamas18-uav.pdf)
- BFWS online POMDP for **Transparent Planning** - [A. MacNally, N. Lipovetzky, M. Ramirez, A. Pearce, AAMAS18](https://nirlipo.github.io/publication/macnally-2018-action/aamas18-transparent-planning.pdf)

## MDP over Simulators
- IW over **General Videogame** Competition (GVGAI) - [T. Geffner and H. Geffner, AAIDE15](https://ojs.aaai.org/index.php/AIIDE/article/download/12786/12634)

## Multi Agent Descentralised and Privacy Preserving Planning
 - Descentralised Best First Width Search (**MA-BFWS**) [AE Gerevini, N Lipovetzky, F Percassi, A Saetti, I Serina, ICAPS2019](https://ojs.aaai.org/index.php/ICAPS/article/view/3472)
 - **Novelty Communication filtering** for Strong Privacy Preserving Planning [AE Gerevini, N Lipovetzky, N Peli, F Percassi, A Saetti, I Serina, SoCS2019](https://ojs.aaai.org/index.php/SOCS/article/download/18505/18296)
 - **Width-based search for multi agent privacy-preserving planning** [AE Gerevini, N Lipovetzky, F Percassi, A Saetti, I Serina, AIJ 2023](https://www.sciencedirect.com/science/article/pii/S0004370223000292?dgcid=coauthor)

# Width Based Algorithms in Action
## Arcade Learning Environment
{{< youtube P-603qPMkSg >}}

## [More Youtube Atari videos](https://www.youtube.com/playlist?list=PLXpQcXUQ_CwenUazUivhXyYvjuS6KQOI0)


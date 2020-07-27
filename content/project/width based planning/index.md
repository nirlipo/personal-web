---
title: Width Based Planning
summary: Width Based Planning searches for solutions through a general measure of state novelty. Performs well over black-box simulators and PDDL problems.
tags:
- AI Planning
- Width Based Planning
date: "2018-04-27T00:00:00Z"

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

# Papers:

(Disclaimer: this is not a comprehensive list, please get in touch to add relevant work that has been missed)

# Table of Contents
1. [Classical Planning over STRIPS/PDDL](#classical-planning-over-pddl)
2. [Classical Planning over Simulators](#classical-planning-over-simulators)
3. [Continous State Simulators](#continous-state-simulators)
3. [Planning over Factored Simulators in Functional STRIPS](#planning-over-factored-simulators-in-functional-strips)
4. [MDP over Simulators](#mdp-over-simulators)
5. [Multi Agent (Descentralisd & Privacy Preserving) Planning](#multi-agent-descentralisd-and-privacy-preserving-planning)

## Classical Planning over PDDL
- Classical **Width Definition**, Iterative Width (**IW**), Serialized IW (**SIW**), **SIW+**, and **DFS+** algorithms 
   - [N. Lipovetzky and H. Geffner, ECAI12](http://people.eng.unimelb.edu.au/nlipovetzky/papers/classical-width-ecai12.pdf)
   - [PhD. Thesis, Nir Lipovetzky, 2012](https://people.eng.unimelb.edu.au/nlipovetzky/papers/aiaccess_nirlipo.pdf), [ICAPS Best dissertation Award 2013](http://www.icaps-conference.org/index.php/Main/Awards)  
   - [N. Lipovetzky and H. Geffner, ECAI14](https://people.eng.unimelb.edu.au/nlipovetzky/papers/width_ecai14.pdf)

- Best First Width Search (**BFWS**) - [N. Lipovetzky and H. Geffner, AAAI17](http://www.aaai.org/ocs/index.php/AAAI/AAAI17/paper/download/14862/14161) 
   - Polynomial BFWS planner  [N. Lipovetzky and H. Geffner, ICAPS17](http://people.eng.unimelb.edu.au/nlipovetzky/papers/icaps17-polytime-BFWS.pdf)
   - BFWS and quantified heuristic novelty measures [M. Katz, N. Lipovetzky, D. Moshkovich, A. Tuisov, ICAPS17](http://people.eng.unimelb.edu.au/nlipovetzky/papers/icaps17-quantified-novelty.pdf)

## Classical Planning over Simulators
- IW over **Atari** Simulator (ALE) 
   -  [N. Lipovetzky, M. Ramirez, and H. Geffner, IJCAI15](http://people.eng.unimelb.edu.au/nlipovetzky/papers/iw-atari-ijcai-2015.pdf)
   - [A. Shleyfman, A. Tuisov, and C. Domshlak, IJCAI16](http://www.ijcai.org/Proceedings/16/Papers/460.pdf) 
   - [Y. Jinnai and A. Fukunaga, AAAI17](http://www.aaai.org/ocs/index.php/AAAI/AAAI17/paper/download/14920/14194)  
   - [W. Bandres, B. Bonet, H. Geffner, AAAI18](https://arxiv.org/pdf/1801.03354) 
   
## Continous State Simulators
 - Features for Continuous-State Domains. Competitive with DRL and LQR on [control problems](https://gym.openai.com/envs/#control) over gym.openai simulator
   - [Florent Teichteil-Königsbuch, Miquel Ramirez, Nir Lipovetzky, IJCAI20](https://www.ijcai.org/Proceedings/2020/0578.pdf)
## Planning over Factored Simulators in Functional STRIPS
Factored simulators accept finite domain variables, and mixed Declarative and Programatic (simulated) dynamics

- BFWS with **simulators** and **Functional STRIPS** (FSTRIPS) - [G. Francès, M. Ramirez, N. Lipovetzky, and H. Geffner, IJCAI17](http://people.eng.unimelb.edu.au/nlipovetzky/papers/ijcai17-planning-with-simulators.pdf)
- **Task and Motion** Planning - [J. Ferrer-Mestres, G. Francès, and H. Geffner, ARXIV17](https://arxiv.org/pdf/1706.06927.pdf) 
- UaV **Hybrid Control** - [M. Ramirez, M. Papasimeon, N. Lipovetzky, L. Benke, T. Miller, A. Pearce, E. Scala, M. Zamani, AAMAS18](https://people.eng.unimelb.edu.au/nlipovetzky/papers/aamas18-uav.pdf)
- BFWS online POMDP for **Transparent Planning** - [A. MacNally, N. Lipovetzky, M. Ramirez, A. Pearce, AAMAS18](https://people.eng.unimelb.edu.au/nlipovetzky/papers/aamas18-transparent-planning.pdf)

## MDP over Simulators
- IW over **General Videogame** Competition (GVGAI) - [T. Geffner and H. Geffner, AAIDE15](http://www.aaai.org/ocs/index.php/AIIDE/AIIDE15/paper/download/11540/11350)

## Multi Agent Descentralised and Privacy Preserving Planning
 - Descentralised Best First Width Search (**MA-BFWS**) [AE Gerevini, N Lipovetzky, F Percassi, A Saetti, I Serina, ICAPS2019](https://aaai.org/ojs/index.php/ICAPS/article/view/3472/3340)
 - **Novelty Communication filtering** for Strong Privacy Preserving Planning [AE Gerevini, N Lipovetzky, N Peli, F Percassi, A Saetti, I Serina, SoCS2019](https://aaai.org/ocs/index.php/SOCS/SOCS19/paper/view/18331)

# Width Based Algorithms in Action
## Arcade Learning Environment
{{< youtube P-603qPMkSg >}}

## [More Youtube Atari videos](https://www.youtube.com/playlist?list=PLXpQcXUQ_CwenUazUivhXyYvjuS6KQOI0)


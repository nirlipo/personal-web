---
title: AI Planning Solvers Online
summary: Planning as a Service (PaaS) is an extendable API to deploy planners online in local or cloud servers
tags:
- AI Planning
- Teaching
date: "2023-04-12T00:00:00Z"

links:
#- name: Inter University Competition
#  url: https://sites.google.com/view/pacman-capture-hall-fame
  # icon_pack: fas
  # icon: books
url_code: "https://github.com/AI-Planning/planning-as-a-service"
url_pdf: "project/paas/ICAPS_23_Demo.pdf"
url_poster: "project/paas/poster.png"
url_video: "https://www.loom.com/share/7d72759cd71c47db9032970fddcb3e71"


# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Planning as a Service
  focal_point: Smart
  preview_only: true

text-align: center;
---

![image](/project/paas/poster.png)

Planning as a service (PaaS) provides an extendable API to deploy planners online in local or cloud servers. 

The service provides a queue manager to control a set of workers, which can easily be extended with one of several planners available in [PLANUTILS](https://github.com/AI-Planning/planutils). 

PaaS is designed to overcome the limitations of the Legacy online [solver.planning.domains](solver.planning.domains/legacy) interface and widen the adoption of planning. The current API is has been exposed through [http://paas-uom.org:5001/](http://paas-uom.org:5001/) and currently deployed packages are listed here: [https://paas-uom.org:5001/package](https://paas-uom.org:5001/package). The solvers can be used through the [https://editor.planning.domains/](https://editor.planning.domains/). 

## Demo Video 
<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/7d72759cd71c47db9032970fddcb3e71" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Acknowledgments
This project has been a collaboration between Queen's University, Canada and The University of Melbourne, Australia. A submission has been made to [ICAPS 2023 System Demonstations](https://icaps23.icaps-conference.org/) track by Yi Ding, Cam Cunningham, Christian Muise, and Nir Lipovetzky. 

This work has been partially funded by AIJ to promote AI Research - ”Enabling Education of AI Planning”

![image](/project/paas/AIJ_Cover.jpg)
---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: 'Job Scheduling in High Performance Computing Clusters with Deep Reinforcement Learning'
subtitle: ''
summary: ''
authors:
- Lingfei Wang
tags: []
categories: []
date: '2025-12-01'
lastmod: 2026-01-28T00:00:00+00:00
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
publishDate: '2025-12-01'
publication_types:
- '7'
abstract: 'High Performance Computing (HPC) systems are designed to execute large-scale computational workloads by leveraging parallel processing across multiple compute nodes. These systems support a wide range of applications, including scientific simulations, engineering design, and artificial intelligence, where tasks usually require substantial computational power and execution time. Efficient job scheduling in HPC environments is essential to ensure timely job completion and effective resource utilization. In HPC scheduling, two important components are the job queue and the computing cluster. The job queue holds jobs submitted by users, each describing the resources it needs — such as CPU cores, GPUs, memory, and expected runtime — before it can run. The computing cluster is the pool of available hardware resources that can be assigned to these jobs. Since resources are limited and jobs arrive over time with varying demands, the scheduler must continuously decide which jobs to run and how to allocate resources to them. This process, known as job scheduling, involves both selecting jobs from the queue and assigning suitable resources across the cluster. These decisions must respect system constraints, such as resource availability and job placement requirements, and aim to utilize resources well while maintaining job waiting time as low as possible.


Traditional HPC schedulers often rely on simple heuristics like First-Come-First-Served (FCFS) or Shortest Job First (SJF), which are easy to implement but can lead to poor resource utilization and job starvation under dynamic workloads. Meta-heuristic algorithms have been used to improve decision quality by exploring a broader solution space, but they are computationally costly and require careful tuning. Supervised machine learning methods have also been applied to predict job priorities, offering better scheduling decisions than fixed heuristics. However, they depend on labeled datasets and struggle to adapt to real-time system changes. In contrast, Deep Reinforcement Learning (DRL) enables a scheduler to learn scheduling policies through interaction with the system, using performance feedback to improve decisions over time. It does not rely on labeled data or predefined heuristics, and instead learns to optimize long-term scheduling outcomes by exploring and evaluating different actions in varied system states. This makes DRL well-suited for handling dynamic workloads, complex resource constraints, and changing system conditions in HPC environments. However, applying DRL to HPC scheduling introduces several key challenges. First, designing an effective job selector is difficult due to the unbounded and dynamic nature of the job queue. As jobs continuously arrive and depart, the number of scheduling actions and the information required to represent each job can vary significantly over time. This makes it challenging to define a consistent and scalable state representation and to construct a manageable action space for the agent. Second, job selection and resource allocation are often handled separately, which can result in poor coordination and inefficient scheduling. Addressing this requires a unified DRL framework that jointly considers both decisions. Third, scheduling objectives — such as minimizing job waiting time and maximizing resource utilization — can conflict and shift depending on workload intensity and system state, requiring the scheduler to dynamically adjust its priorities. Fourth, as HPC systems are upgraded, modified, or newly developed, changes in hardware architecture can alter the structure and semantics of the system state used by DRL-based schedulers. These changes affect how job and resource features are represented and interpreted, making it difficult to directly reuse DRL models trained in previous environments without adaptation.


In particular, this thesis makes the following contributions to DRL-based HPC scheduling. Develops a DRL-based job selector designed to handle unbounded job queues and support efficient backfilling. Presents a hierarchical DRL scheduler that jointly manages job selection and resource allocation in HPC environments. Introduces a dynamic controller that adjusts scheduling objectives based on real-time system conditions. Proposes a transfer learning framework that enables DRL schedulers to adapt efficiently to evolving HPC architectures.'
publication: 'The University of Melbourne'
url_pdf: 'publication/lingfei-phdthesis/lingfei_phd_thesis.pdf'
---

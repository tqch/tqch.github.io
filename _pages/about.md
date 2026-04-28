---
permalink: /
title: "Tianqi Chen — Diffusion models, generative AI"
excerpt: "Statistics PhD candidate at UT Austin working on diffusion models, generative AI, and trustworthy ML."
author_profile: false
layout: default
redirect_from:
  - /about/
  - /about.html
---

<section class="hero">
  <div class="container">
    <div class="hero__inner">
      <div class="hero__text">
        <span class="hero__eyebrow"><span class="dot"></span> PhD candidate · graduating May 2026</span>

        <div class="hero__name">
          <span class="name">Tianqi Chen</span>
          <span class="han">陈天麒</span>
        </div>

        <h1 class="hero__title">
          teaches machines to <span class="name-it">denoise</span> reality.
        </h1>

        <p class="hero__lede">
          Final-year Statistics PhD at <em>UT Austin</em>, advised by
          <a href="https://mingyuanzhou.github.io/" target="_blank" rel="noopener">Prof. Mingyuan Zhou</a>.
          I build <em>diffusion models</em> and <em>multimodal generative systems</em> — and the
          algorithms that keep them fast, safe, and trustworthy.
        </p>

        <div class="hero__meta">
          <span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            Austin, TX
          </span>
          <span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>
            tqch [at] utexas [dot] edu
          </span>
        </div>

        <div class="hero__cta">
          <a class="btn btn--primary" href="{{ base_path }}/cv/">
            View CV
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
          </a>
          <a class="btn" href="{{ base_path }}/publications/">Publications</a>
          <a class="btn" href="https://scholar.google.com/citations?user=jucvWbcAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
        </div>
      </div>

      <div class="diff-frame">
        <div class="diff-card"
             data-diffusion
             data-src="{{ base_path }}/images/portrait.png"
             data-src-clean="{{ base_path }}/images/portrait-clean.png"
             role="img"
             aria-label="Halftone portrait of Tianqi Chen; hover to denoise it into a clean photograph.">
          <canvas></canvas>
          <span class="diff-card__hint">hover · denoise</span>
          <span class="diff-card__caption"><span class="step" data-step>t = 1000</span></span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section reveal">
  <div class="container container--narrow">
    <div class="section-label">News</div>
    <h2 class="section-title">Recent updates</h2>

    <div class="news">
      <div class="news__item">
        <div class="news__date">May 2025</div>
        <div class="news__body">
          <span class="tag tag--sky">Internship</span>
          Joined Google as a Software Engineer Intern in Mountain View, building diffusion-based <em>video super-resolution</em> on top of CogVideoX 1.5.
        </div>
      </div>
      <div class="news__item">
        <div class="news__date">Jan 2025</div>
        <div class="news__body">
          <span class="tag tag--accent">ICLR 2025</span>
          <strong>Score Forgetting Distillation</strong> — a swift, data-free method for machine unlearning in diffusion models — accepted at ICLR 2025.
        </div>
      </div>
      <div class="news__item">
        <div class="news__date">Sep 2024</div>
        <div class="news__body">
          <span class="tag tag--warm">Award</span>
          Received the University Graduate Continuing Fellowship from UT Austin.
        </div>
      </div>
      <div class="news__item">
        <div class="news__date">Jun 2024</div>
        <div class="news__body">
          <span class="tag tag--sky">Internship</span>
          Applied Scientist Intern at Amazon, Seattle — short-form video localization and landscape-to-portrait conversion pipelines.
        </div>
      </div>
      <div class="news__item">
        <div class="news__date">May 2024</div>
        <div class="news__body">
          <span class="tag tag--accent">ICML 2024</span>
          <strong>A Dense Reward View on Aligning Text-to-Image Diffusion with Preference</strong> accepted at ICML 2024.
        </div>
      </div>
      <div class="news__item">
        <div class="news__date">Sep 2023</div>
        <div class="news__body">
          <span class="tag tag--accent">NeurIPS 2023</span>
          <strong>Beta Diffusion</strong> accepted at NeurIPS 2023.
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section reveal">
  <div class="container">
    <div class="section-label">Research</div>
    <h2 class="section-title">What I work on</h2>

    <p class="container--narrow" style="max-width: 760px; margin: 0 0 2.4rem; font-size: 1.05rem;">
      I'm interested in the <em>theory and practice of generative modeling</em> — particularly how
      iterative denoising processes can be generalized beyond the Gaussian playbook and pushed toward
      faster, safer, and more controllable systems. My recent work spans four threads:
    </p>

    <div class="pubs">
      <div class="pub">
        <div>
          <div class="pub__venue">Generalized diffusion</div>
          <span class="pub__year">2023 — present</span>
        </div>
        <div>
          <div class="pub__title">Beyond Gaussian noise</div>
          <p class="pub__abs">A unified, Bregman-divergence view of iterative corruption / recovery — leading to non-Gaussian variants like <strong>Beta Diffusion</strong> (NeurIPS '23) and <strong>Learning to Jump</strong> (ICML '23) for sparse, non-negative, heavy-tailed data.</p>
        </div>
        <div></div>
      </div>

      <div class="pub">
        <div>
          <div class="pub__venue">Trustworthy AI</div>
          <span class="pub__year">2024</span>
        </div>
        <div>
          <div class="pub__title">Machine unlearning for diffusion</div>
          <p class="pub__abs"><strong>Score Forgetting Distillation</strong> (ICLR '25): a swift, data-free way to forget unsafe classes or concepts (incl. specific celebrities and NSFW content) while preserving generation quality — and getting up to <strong>1000× sampling speedup</strong> for free.</p>
        </div>
        <div></div>
      </div>

      <div class="pub">
        <div>
          <div class="pub__venue">Alignment</div>
          <span class="pub__year">2024</span>
        </div>
        <div>
          <div class="pub__title">Dense reward for T2I diffusion</div>
          <p class="pub__abs">A dense-reward perspective on aligning text-to-image diffusion with human preference — turning the trajectory itself into the optimization signal (ICML '24).</p>
        </div>
        <div></div>
      </div>

      <div class="pub">
        <div>
          <div class="pub__venue">Multimodal</div>
          <span class="pub__year">2023</span>
        </div>
        <div>
          <div class="pub__title">Visual in-context learning</div>
          <p class="pub__abs"><strong>iPromptDiff</strong>: an SD-based architecture that decouples content from task and routes visual perception through text embeddings — strong in-domain and OOD performance even when text prompts are missing.</p>
        </div>
        <div></div>
      </div>
    </div>
  </div>
</section>

<section class="section reveal">
  <div class="container">
    <div class="section-label">Selected publications</div>
    <h2 class="section-title">Papers</h2>

    <div class="pubs">

      <div class="pub">
        <div>
          <div class="pub__venue">ICLR 2025</div>
          <span class="pub__year">2025</span>
        </div>
        <div>
          <div class="pub__title">Score Forgetting Distillation: A Swift, Data-Free Method for Machine Unlearning in Diffusion Models</div>
          <p class="pub__authors"><span class="me">T. Chen</span>, S. Zhang, M. Zhou</p>
          <p class="pub__abs">A teacher–student distillation that rapidly removes target classes or concepts from diffusion models without accessing real data, while preserving overall generative quality.</p>
        </div>
        <div class="pub__links">
          <a href="https://arxiv.org/abs/2409.11219" target="_blank" rel="noopener">Paper</a>
          <a href="https://github.com/tqch/score-forgetting-distillation" target="_blank" rel="noopener">Code</a>
        </div>
      </div>

      <div class="pub">
        <div>
          <div class="pub__venue">ICML 2024</div>
          <span class="pub__year">2024</span>
        </div>
        <div>
          <div class="pub__title">A Dense Reward View on Aligning Text-to-Image Diffusion with Preference</div>
          <p class="pub__authors">S. Yang*, <span class="me">T. Chen</span>*, M. Zhou <span class="muted">(*equal contribution)</span></p>
          <p class="pub__abs">Trajectory-level dense reward signals for aligning text-to-image diffusion to human preference, outperforming sparse-reward baselines.</p>
        </div>
        <div class="pub__links">
          <a href="https://arxiv.org/abs/2402.08265" target="_blank" rel="noopener">Paper</a>
          <a href="https://github.com/Shentao-YANG/Dense_Reward_T2I" target="_blank" rel="noopener">Code</a>
        </div>
      </div>

      <div class="pub">
        <div>
          <div class="pub__venue">NeurIPS 2023</div>
          <span class="pub__year">2023</span>
        </div>
        <div>
          <div class="pub__title">Beta Diffusion</div>
          <p class="pub__authors">M. Zhou, <span class="me">T. Chen</span>, H. Zheng, Z. Wang</p>
          <p class="pub__abs">A diffusion model defined on the simplex via Beta distributions — well-suited for bounded data such as images and probability vectors.</p>
        </div>
        <div class="pub__links">
          <a href="https://arxiv.org/abs/2309.07867" target="_blank" rel="noopener">Paper</a>
          <a href="https://github.com/tqch/beta-diffusion" target="_blank" rel="noopener">Code</a>
        </div>
      </div>

      <div class="pub">
        <div>
          <div class="pub__venue">ICML 2023</div>
          <span class="pub__year">2023</span>
        </div>
        <div>
          <div class="pub__title">Learning to Jump: Thinning and Thickening Latent Counts for Generative Modeling</div>
          <p class="pub__authors"><span class="me">T. Chen</span>, M. Zhou</p>
          <p class="pub__abs">A binomial / Poisson hierarchical VAE that handles sparsity, skewness, heavy tails, and heterogeneity — natural for count-like and non-negative data.</p>
        </div>
        <div class="pub__links">
          <a href="https://proceedings.mlr.press/v202/chen23ap.html" target="_blank" rel="noopener">Paper</a>
          <a href="https://github.com/tqch/Learning-to-Jump" target="_blank" rel="noopener">Code</a>
        </div>
      </div>

      <div class="pub">
        <div>
          <div class="pub__venue">IEEE Access</div>
          <span class="pub__year">2022</span>
        </div>
        <div>
          <div class="pub__title">ASK: Adversarial Soft k-Nearest Neighbor Attack and Defense</div>
          <p class="pub__authors">R. Wang, <span class="me">T. Chen</span>, P. Yao, S. Liu, I. Rajapakse, A. Hero</p>
          <p class="pub__abs">An information-theoretic surrogate for DkNN classification, plus matching attack and defense algorithms with state-of-the-art adversarial robustness.</p>
        </div>
        <div class="pub__links">
          <a href="https://ieeexplore.ieee.org/document/9902964" target="_blank" rel="noopener">Paper</a>
        </div>
      </div>

      <div class="pub">
        <div>
          <div class="pub__venue">IEEE Access</div>
          <span class="pub__year">2022</span>
        </div>
        <div>
          <div class="pub__title">RAILS: A Robust Adversarial Immune-Inspired Learning System</div>
          <p class="pub__authors">R. Wang, <span class="me">T. Chen</span>, …, I. Rajapakse, A. Hero</p>
          <p class="pub__abs">An immune-system-inspired adversarial framework that defends against unseen attacks by mimicking B-cell affinity maturation.</p>
        </div>
        <div class="pub__links">
          <a href="https://ieeexplore.ieee.org/document/9718107" target="_blank" rel="noopener">Paper</a>
        </div>
      </div>

    </div>

    <p style="margin-top: 28px; font-family: var(--font-mono); font-size: 0.85rem; color: var(--fg-muted);">
      → <a href="https://scholar.google.com/citations?user=jucvWbcAAAAJ&hl=en" target="_blank" rel="noopener">Full list on Google Scholar</a>
    </p>
  </div>
</section>

<section class="section reveal">
  <div class="container">
    <div class="section-label">Experience</div>
    <h2 class="section-title">Where I've worked</h2>

    <div class="timeline">
      <div class="t-item">
        <div class="t-meta">
          <span class="t-role">Software Engineer Intern</span>
          <span class="t-org">· Google</span>
          <span class="t-date">May 2025 – Aug 2025 · Mountain View, CA</span>
        </div>
        <p class="t-desc">Built a full data-curation and training pipeline for diffusion-based video super-resolution; designed temporally-consistent simulators of real-world video degradation; developed a VSR diffusion model on CogVideoX 1.5.</p>
      </div>

      <div class="t-item">
        <div class="t-meta">
          <span class="t-role">Applied Scientist Intern</span>
          <span class="t-org">· Amazon</span>
          <span class="t-date">Jun 2024 – Oct 2024 · Seattle, WA</span>
        </div>
        <p class="t-desc">Designed an automatic short-form video localization pipeline (object detection, OCR, inpainting, segmentation), and a landscape-to-portrait conversion workflow with KMeans + Gaussian-process smoothing for stable subject tracking.</p>
      </div>

      <div class="t-item">
        <div class="t-meta">
          <span class="t-role">Research Scientist Intern</span>
          <span class="t-org">· ByteDance</span>
          <span class="t-date">May 2023 – Nov 2023 · Bellevue, WA</span>
        </div>
        <p class="t-desc">Studied visual in-context learning for diffusion models; proposed iPromptDiff, an SD-based architecture that decouples content from task and pushes visual perception into text embeddings — beating baselines in-domain and OOD.</p>
      </div>

      <div class="t-item">
        <div class="t-meta">
          <span class="t-role">Graduate Research / Teaching Assistant</span>
          <span class="t-org">· UT Austin</span>
          <span class="t-date">Jun 2022 – Jun 2024</span>
        </div>
        <p class="t-desc">Built and open-sourced a PyTorch codebase for DDPM, DDIM, and classifier-free guidance (230★+ on GitHub), reproducing published diffusion results and exploring non-Gaussian generalizations.</p>
      </div>

      <div class="t-item">
        <div class="t-meta">
          <span class="t-role">Research Affiliate · GARD</span>
          <span class="t-org">· University of Michigan</span>
          <span class="t-date">Jul 2020 – May 2022</span>
        </div>
        <p class="t-desc">Co-developed adversarial soft k-NN (ASK) and the immune-inspired RAILS framework for adversarial robustness on deep classifiers.</p>
      </div>
    </div>
  </div>
</section>

<section class="section reveal">
  <div class="container">
    <div class="section-label">Education</div>
    <h2 class="section-title">Education</h2>

    <div class="timeline">
      <div class="t-item">
        <div class="t-meta">
          <span class="t-role">PhD, Statistics</span>
          <span class="t-org">· The University of Texas at Austin</span>
          <span class="t-date">Sep 2021 – May 2026</span>
        </div>
        <p class="t-desc">Advised by Prof. Mingyuan Zhou, IROM, McCombs School of Business.</p>
      </div>
      <div class="t-item">
        <div class="t-meta">
          <span class="t-role">MS, Applied Statistics</span>
          <span class="t-org">· University of Michigan, Ann Arbor</span>
          <span class="t-date">Sep 2019 – Apr 2021</span>
        </div>
      </div>
      <div class="t-item">
        <div class="t-meta">
          <span class="t-role">BS, Applied Mathematics</span>
          <span class="t-org">· Fudan University</span>
          <span class="t-date">Sep 2015 – Jun 2019</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section reveal">
  <div class="container">
    <div class="section-label">Recognition</div>
    <h2 class="section-title">Awards & service</h2>

    <div class="split-2">
      <div>
        <h3 class="col-label">Fellowships &amp; awards</h3>
        <ul class="kv-list">
          <li>University Graduate Continuing Fellowship <span class="v">2025</span></li>
          <li>McCombs Dean's Fellowship <span class="v">2022 – 2024</span></li>
          <li>NeurIPS Scholar Award <span class="v">2023</span></li>
          <li>UT Professional Development Award <span class="v">2023</span></li>
          <li>Fudan Excellent Freshman Scholarship — Top 1% <span class="v">2015</span></li>
        </ul>
      </div>
      <div>
        <h3 class="col-label">Service</h3>
        <ul class="kv-list">
          <li>Reviewer · ICLR <span class="v">'24 – '26</span></li>
          <li>Reviewer · NeurIPS <span class="v">'23 – '25</span></li>
          <li>Reviewer · ICML <span class="v">'23 – '25</span></li>
          <li>Reviewer · AISTATS <span class="v">'21, '26</span></li>
          <li>Teaching Assistant · UT Austin <span class="v">'21 – '22, '24</span></li>
        </ul>
      </div>
    </div>

    <div style="margin-top: 60px;">
      <h3 class="col-label">Toolbox</h3>
      <ul class="chips">
        <li>Python</li>
        <li>PyTorch</li>
        <li>JAX</li>
        <li>TensorFlow</li>
        <li>NumPy / SciPy</li>
        <li>scikit-learn</li>
        <li>R</li>
        <li>CUDA</li>
        <li>Diffusion models</li>
        <li>VAEs</li>
        <li>RLHF / DPO</li>
        <li>CogVideoX · SD · Flow Matching</li>
      </ul>
    </div>
  </div>
</section>

<section class="section reveal" style="padding-bottom: 120px;">
  <div class="container container--narrow" style="text-align: center;">
    <h2 class="section-title" style="text-align: center;">Let's talk.</h2>
    <p style="font-size: 1.1rem; max-width: 540px; margin: 0 auto 28px;">
      I'll be on the <strong>2026 academic and industry job market</strong>. If you're hiring, collaborating, or just want to argue about score-based vs. flow-based generative models — say hi.
    </p>
    <div class="hero__cta" style="justify-content: center;">
      <a class="btn btn--primary" href="mailto:tqch@utexas.edu">tqch@utexas.edu</a>
      <a class="btn" href="https://www.linkedin.com/in/tianqi-chen-4875671a3/" target="_blank" rel="noopener">LinkedIn</a>
      <a class="btn" href="https://github.com/tqch" target="_blank" rel="noopener">GitHub</a>
    </div>
  </div>
</section>

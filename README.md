<div align="center">


# The official seed skill library for [EurekaClaw](https://github.com/EurekaClaw/EurekaClaw) 

</div>

## 🌱 What are seed skills?

**Seed skills** is a curated collection of foundational skills for the [EurekaClaw](https://github.com/EurekaClaw/EurekaClaw) AI agent ecosystem. Each skill is a self-contained directory with a `SKILL.md` file that teaches the agent a new capability — from rigorous mathematical proof techniques to structured literature decomposition.

---

## 📦 Skill Catalog

| Skill | Description |
|---|---|
| [`compactness_argument`](./seedskills/compactness_argument/) | Techniques for constructing compactness-based proofs |
| [`complexity_template`](./seedskills/complexity_template/) | Structured templates for complexity analysis |
| [`concentration_inequalities`](./seedskills/concentration_inequalities/) | Applying Hoeffding, Bernstein, and related bounds |
| [`contradiction_proof`](./seedskills/contradiction_proof/) | Proof by contradiction strategies and patterns |
| [`eluder_dimension`](./seedskills/eluder_dimension/) | Eluder dimension reasoning for function classes |
| [`empirical_validation`](./seedskills/empirical_validation/) | Empirical testing and experimental validation workflows |
| [`fundamental_inequalities`](./seedskills/fundamental_inequalities/) | Core inequalities: Cauchy-Schwarz, Jensen, AM-GM, etc. |
| [`hypothesis_gen`](./seedskills/hypothesis_gen/) | Systematic hypothesis generation for research |
| [`induction_strategy`](./seedskills/induction_strategy/) | Mathematical induction — base cases, inductive steps, strong induction |
| [`latex_algorithm_and_syntax`](./seedskills/latex_algorithm_and_syntax/) | Writing algorithms and proofs in clean LaTeX |
| [`literature_decomp`](./seedskills/literature_decomp/) | Decomposing and synthesizing research papers |
| [`nonlinear_dueling_bandits_general_function_approximation`](./seedskills/nonlinear_dueling_bandits_general_function_approximation/) | Dueling bandits with general nonlinear function classes |
| [`overdamped_langevin_convergence`](./seedskills/overdamped_langevin_convergence/) | Convergence analysis for overdamped Langevin dynamics |
| [`paper_structure`](./seedskills/paper_structure/) | Academic paper structure and writing discipline |
| [`regularized_bandit_fast_rates`](./seedskills/regularized_bandit_fast_rates/) | Fast convergence rates in regularized bandit settings |
| [`rigorous_proof_citation_discipline`](./seedskills/rigorous_proof_citation_discipline/) | Citation standards and proof rigor in academic writing |
| [`underdamped_langevin_convergence`](./seedskills/underdamped_langevin_convergence/) | Convergence analysis for underdamped (kinetic) Langevin |

---

## 🚀 Quick Start

### Install the skills to your EurekaClaw

The seed skills will be automatically install at EurekaClaw onboarding. To update the seed skills, run

```bash
eurekaclaw install-skills --force
```

## 🏗️ Skill Structure

Every skill follows the OpenClaw-compatible format:

```
my_skill/
└── SKILL.md        # Required: Instructions, tools, and workflow for the agent
```

`SKILL.md` contains YAML frontmatter (name, description, requirements) followed by markdown instructions that the agent reads at runtime.

---

## 🤝 Contributing

We welcome new skills! Two ways to contribute:

**Option 1 — Pull Request (this repo)**

```bash
# 1. Fork and clone
git clone https://github.com/EurekaClaw/seed_skills.git

# 2. Create your skill directory
mkdir seedskills/my_new_skill
touch seedskills/my_new_skill/SKILL.md   # Write your skill here

# 3. Submit a PR
git checkout -b add-my-new-skill
git add seedskills/my_new_skill/
git commit -m "feat: add my_new_skill"
git push origin add-my-new-skill
```

**Option 2 — Publish directly to [ClawHub](https://clawhub.ai)**

Upload your skill to the public registry and share it with the entire OpenClaw community.

### Skill quality bar

A good seed skill should:
- ✅ Have a clear, single responsibility
- ✅ Include concrete examples or worked demonstrations in `SKILL.md`
- ✅ Be general enough to be reusable across research contexts
- ✅ Cite sources or foundational references where relevant

---

## 🧪 Testing

This repo enforces that every skill directory contains a valid `SKILL.md` via automated CI:

```bash
# Run locally
pip install pytest
pytest tests/ -v
```

CI runs on every push and pull request via GitHub Actions. A PR that adds a skill folder without a `SKILL.md` will fail automatically.

---

## 📚 Learn More

| Resource | Link |
|---|---|
| EurekaClaw main repo | [github.com/EurekaClaw](https://github.com/EurekaClaw/EurekaClaw_dev_zero) |

---

## ⚖️ License

Apache 2.0 — see [LICENSE](./LICENSE) for details.

---

<div align="center">
  <sub>Built with 🦞 by <a href="https://github.com/EurekaClaw">EurekaClaw</a></sub>
</div>
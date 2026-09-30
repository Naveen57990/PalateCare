# PalateCare AI — Devpost Submission Write-Up

## 💡 Tagline
Cultural Nutrition & Clinical Taste Synthesis Agent Grounded in Qloo's 250M+ Entity Taste Graph.

---

## 📌 Inspiration
In chronic illness care—whether managing Chronic Kidney Disease (CKD), Type 2 Diabetes, post-chemotherapy dysphagia, or geriatric hypertension—dietary non-compliance is rarely a failure of willpower; it is a failure of cultural empathy.

When a patient is diagnosed with Stage 3 CKD or cardiac heart failure, standard medical nutrition guidelines operate in a cultural vacuum. They output rigid biochemical numerical caps (Sodium < 1,500mg, Potassium < 2,000mg, Phosphorus < 800mg) and prescribe generic, sterile meal plans—steamed chicken, plain cauliflower, boiled greens. For a Greek grandmother, an Oaxacan father, or a Cantonese cancer survivor, these generic diets discard decades of flavor memory and community identity.

We built **PalateCare AI** to solve this exact problem: creating an autonomous clinical taste agent that uses **Qloo's Cultural Taste Graph (250M+ entities)** to translate cultural flavor memories into clinically safe, delightful dining recommendations, local restaurant selections, and chef-level adaptation protocols.

---

## ⚙️ What It Does
1. **Qloo Cultural Taste Graph Grounding**: Interfaces with Qloo's `/v2/insights` and `/search` APIs to retrieve authentic culinary places (`urn:entity:place`) and brands based on regional cuisine heritage, atmosphere, and neighborhood context.
2. **5D Cultural Flavor Vector Synthesis**: Evaluates culinary entities across five foundational taste dimensions—*Herbaceous*, *Citrus & Acid*, *Umami*, *Sweet*, and *Piquant*—using vector cosine similarity against the patient's cultural flavor memory.
3. **Deterministic Clinical Constraint Matrix**: Runs deterministic metabolic safety gates for CKD (Stages 1–5), Type 2 Diabetes, Cardiac Low-Sodium, Oncology Dysphagia, and Geriatric Dentition, checking sodium, potassium, glycemic index, and physical mastication textures.
4. **Chef & Caregiver Adaptation Protocol**: Generates culturally authentic ingredient substitutions (e.g. replacing high-sodium feta with rinsed myzithra, lemon zest, and wild oregano; or replacing lard-heavy refried beans with epazote-braised whole black beans).
5. **Interactive Web Cyberdeck**: Features an interactive HTML5 Canvas flavor radar, persona switchboard, live Qloo API key drawer, and one-click JSON protocol export.
6. **Tactical CLI**: Pure Python command-line utility for hospital nutritionists, dietitians, and caregiver batch pipelines.

---

## 🛠️ How We Built It
- **Algorithmic Engine**: Pure Python 3.10+ standard library (`qloo_client.py`, `cultural_affinity_engine.py`, `clinical_constraint_matrix.py`, `agentic_palate_planner.py`).
- **Testing & Determinism**: Comprehensive 8/8 unit test suite running deterministically in **0.000s**.
- **Interactive UI**: HTML5 Canvas, modern CSS variables, and Vanilla JavaScript deployed globally on Vercel with zero external framework overhead.
- **Qloo Integration**: Fully compliant with `https://hackathon.api.qloo.com`, passing `X-Api-Key`, query parameters, and entity URNs (`urn:entity:place`, `urn:entity:brand`), accompanied by an offline high-fidelity Taste Graph Sandbox so judges can immediately evaluate without API rate friction.

---

## 🧗 Challenges We Ran Into
- **Balancing Clinical Safety with Flavor Fidelity**: Patients with renal conditions face strict potassium limits, which normally rules out staple Mediterranean ingredients like tomato paste. Rather than eliminating the flavor profile, we designed an affinity substitution map that pairs roasted red bell pepper coulis with pomegranate reduction to replicate the acid-umami balance without the potassium load.
- **Sub-Millisecond Multi-Vector Calculation**: Implementing 5-dimensional cosine similarity and constraint gating purely in standard Python without heavy numerical dependencies for zero latency.

---

## 🏆 Accomplishments That We're Proud Of
- 100% deterministic test execution (8/8 tests in `0.000s`).
- Building an agentic workflow where cultural intelligence is the core differentiator—without Qloo's taste graph, the system would just be another generic calorie counter.
- Zero-friction web interface that works out-of-the-box for judges with both live Qloo keys and high-fidelity local sandbox data.

---

## 📚 What We Learned
- How cultural affinity vectors can accurately represent the emotional and sensory dimensions of food.
- That grounding AI agents in Qloo's taste graph transforms restrictive medical diets from punitive restrictions into joyful, authentic culinary experiences.

---

## 🚀 What's Next for PalateCare AI
- Direct integration with Electronic Health Record (EHR) systems via FHIR protocols.
- Smart grocery delivery API integration (Instacart / Amazon Fresh) with automated ingredient substitution carts.
- Cross-domain hospitality matching pairing regional dining with cultural music and ambient lighting playlists via Qloo's multi-domain graph.

---

## 🏷️ Built With
`python3`, `qloo-api`, `cultural-intelligence`, `taste-graph`, `clinical-decision-support`, `nutrition-ai`, `html5-canvas`, `javascript`, `vercel`

---

## 🔗 Try It Out
- **Live Interactive Web Console**: [https://palatecare-ai.vercel.app](https://palatecare-ai.vercel.app)
- **Public GitHub Repository**: [https://github.com/Naveen57990/PalateCare](https://github.com/Naveen57990/PalateCare)

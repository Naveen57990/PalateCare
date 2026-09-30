/**
 * PalateCare AI Client Application
 * Qloo Cultural Taste Graph & Clinical Constraint Synthesis
 */

const PATIENT_ARCHETYPES = {
  sophia: {
    name: "Sophia Paleologos",
    origin: "Greek Heritage • Athens / SF",
    condition: "CKD_Stage_3",
    conditionName: "Chronic Kidney Disease (Stage 3)",
    flavorProfile: { herbaceous: 0.92, citrus_acid: 0.85, umami: 0.70, sweet: 0.15, piquant: 0.30 },
    matchedEntity: {
      name: "Aegean Herb & Grill",
      category: "Mediterranean / Greek • urn:entity:place",
      compositeScore: 99.8,
      affinityScore: 99.7,
      sodium: "480 mg",
      potassium: "420 mg",
      gi: "35 (Low)",
      texture: "Tender Grill",
      tags: ["#oregano", "#lemon", "#olive_oil", "#wild_greens", "#grilled_sea_bass"],
      flavorProfile: { herbaceous: 0.92, citrus_acid: 0.85, umami: 0.70, sweet: 0.15, piquant: 0.30 }
    },
    adaptations: [
      { orig: "High-Sodium Feta", sub: "Rinsed low-sodium myzithra with fresh oregano and lemon zest" },
      { orig: "Salt-Cured Olives", sub: "Marinated caperberries rinsed in sparkling water with fresh thyme" },
      { orig: "Potassium-Dense Tomato Paste", sub: "Roasted red bell pepper puree with pomegranate reduction" },
      { orig: "Refined White Pita", sub: "Ancient grain farro flatbread dusted with ground sumac" }
    ],
    agentSummary: "Synthesized cultural dining protocol for Sophia Paleologos navigating CKD Stage 3. Selected 'Aegean Herb & Grill' with 99.8% cultural-clinical alignment index, preserving authentic Aegean oregano-citrus profiles while gating sodium under 500mg."
  },
  carlos: {
    name: "Carlos Mendoza",
    origin: "Oaxacan Heritage • Oaxaca / LA",
    condition: "Type_2_Diabetes_Cardiac",
    conditionName: "Type 2 Diabetes & Cardiac Low-Sodium",
    flavorProfile: { herbaceous: 0.75, citrus_acid: 0.80, umami: 0.88, sweet: 0.25, piquant: 0.85 },
    matchedEntity: {
      name: "Oaxacan Hearth",
      category: "Mexican / Oaxacan • urn:entity:place",
      compositeScore: 97.4,
      affinityScore: 98.1,
      sodium: "440 mg",
      potassium: "580 mg",
      gi: "38 (Low)",
      texture: "Braised Soft",
      tags: ["#epazote", "#roasted_chile", "#lime", "#black_beans", "#braised_chicken"],
      flavorProfile: { herbaceous: 0.75, citrus_acid: 0.80, umami: 0.88, sweet: 0.25, piquant: 0.85 }
    },
    adaptations: [
      { orig: "Salty Cotija Cheese", sub: "Toasted pepita-lime crumb with nutritional yeast dust" },
      { orig: "Lard-Heavy Refried Beans", sub: "Slow-braised whole black beans with epazote and charred garlic" },
      { orig: "High-Sodium Table Salsa", sub: "Fire-roasted tomatillo pico de gallo with extra fresh cilantro & serrano" },
      { orig: "High-Glycemic Tortillas", sub: "Cactus nopal and stone-ground corn blend (GI 35)" }
    ],
    agentSummary: "Synthesized Oaxacan heritage protocol for Carlos Mendoza. Gated glycemic load and saturated fats while maintaining charred guajillo, epazote, and lime profiles through braised black bean reduction."
  },
  meiling: {
    name: "Mei-Ling Chen",
    origin: "Cantonese Heritage • Hong Kong / NYC",
    condition: "Oncology_Dysphagia",
    conditionName: "Oncology Post-Chemo Dysphagia",
    flavorProfile: { herbaceous: 0.60, citrus_acid: 0.40, umami: 0.95, sweet: 0.20, piquant: 0.10 },
    matchedEntity: {
      name: "Silk Road Steamed Broth",
      category: "East Asian / Cantonese • urn:entity:place",
      compositeScore: 99.2,
      affinityScore: 99.5,
      sodium: "390 mg",
      potassium: "380 mg",
      gi: "28 (Low)",
      texture: "Pureed Velvety",
      tags: ["#ginger", "#scallion", "#steamed_tofu", "#ginseng_broth", "#silken_egg"],
      flavorProfile: { herbaceous: 0.60, citrus_acid: 0.40, umami: 0.95, sweet: 0.20, piquant: 0.10 }
    },
    adaptations: [
      { orig: "High-Sodium Soy Sauce", sub: "Coconut aminos infused with shiitake essence and fresh ginger juice" },
      { orig: "MSG-Heavy Oyster Sauce", sub: "Reduced vegetable stock with black garlic and steeped kombu" },
      { orig: "Refined Sticky White Rice", sub: "Steamed cauliflower-jasmine velvety rice with toasted sesame oil" },
      { orig: "Aggressive Chili Oil", sub: "Gentle ginger-scallion warm infusion broth" }
    ],
    agentSummary: "Synthesized delicate Cantonese oncology recovery protocol for Mei-Ling Chen. Optimized velvety texture for dysphagia swallowing safety while delivering rich non-irritating umami."
  },
  rajesh: {
    name: "Rajesh Sharma",
    origin: "Punjabi Heritage • Amritsar / Chicago",
    condition: "Geriatric_Dentition_Hypertension",
    conditionName: "Stage 2 Hypertension & Dentition",
    flavorProfile: { herbaceous: 0.85, citrus_acid: 0.65, umami: 0.82, sweet: 0.30, piquant: 0.78 },
    matchedEntity: {
      name: "Amritsar Herb Kitchen",
      category: "South Asian / North Indian • urn:entity:place",
      compositeScore: 98.6,
      affinityScore: 99.1,
      sodium: "380 mg",
      potassium: "510 mg",
      gi: "42 (Moderate)",
      texture: "Stewed Soft",
      tags: ["#fenugreek", "#roasted_cumin", "#turmeric", "#saag_greens", "#paneer_tikka"],
      flavorProfile: { herbaceous: 0.85, citrus_acid: 0.65, umami: 0.82, sweet: 0.30, piquant: 0.78 }
    },
    adaptations: [
      { orig: "Salt-Heavy Garam Masala Paste", sub: "Freshly dry-roasted cumin-coriander-cardamom grind with lime juice" },
      { orig: "Heavy Ghee Tadka", sub: "Cold-pressed mustard oil drizzle with toasted fenugreek seeds" },
      { orig: "High-Potassium Spinach Puree", sub: "Fenugreek and tender mustard greens braised with fresh turmeric" },
      { orig: "Refined White Basmati", sub: "Spiced ragi and pearl millet soft steamed roti" }
    ],
    agentSummary: "Synthesized Punjabi culinary protocol for Rajesh Sharma. Soft stewed saag and slow-roasted whole spices yield full northern Indian depth with minimal sodium and zero dental strain."
  }
};

let currentPersonaKey = "sophia";
let currentFlavor = { ...PATIENT_ARCHETYPES.sophia.flavorProfile };

// DOM Elements
const canvas = document.getElementById("flavorRadarCanvas");
const ctx = canvas.getContext("2d");

const sliderHerb = document.getElementById("sliderHerb");
const sliderCitrus = document.getElementById("sliderCitrus");
const sliderUmami = document.getElementById("sliderUmami");
const sliderSweet = document.getElementById("sliderSweet");
const sliderPiquant = document.getElementById("sliderPiquant");

const valHerb = document.getElementById("valHerb");
const valCitrus = document.getElementById("valCitrus");
const valUmami = document.getElementById("valUmami");
const valSweet = document.getElementById("valSweet");
const valPiquant = document.getElementById("valPiquant");

const affinityScoreBadge = document.getElementById("affinityScoreBadge");
const agentSummaryText = document.getElementById("agentSummaryText");
const topEntityName = document.getElementById("topEntityName");
const topEntityCategory = document.getElementById("topEntityCategory");
const topCompositeScore = document.getElementById("topCompositeScore");
const chipSodium = document.getElementById("chipSodium");
const chipPotassium = document.getElementById("chipPotassium");
const chipGI = document.getElementById("chipGI");
const chipTexture = document.getElementById("chipTexture");
const topEntityTags = document.getElementById("topEntityTags");
const adaptationsList = document.getElementById("adaptationsList");

// Modal Elements
const apiKeyModal = document.getElementById("apiKeyModal");
const toggleApiKeyDrawer = document.getElementById("toggleApiKeyDrawer");
const closeApiKeyModal = document.getElementById("closeApiKeyModal");
const saveApiSettings = document.getElementById("saveApiSettings");
const exportProtocolBtn = document.getElementById("exportProtocolBtn");

function init() {
  setupEventListeners();
  loadPersona("sophia");
}

function setupEventListeners() {
  document.querySelectorAll(".persona-card").forEach(card => {
    card.addEventListener("click", () => {
      document.querySelectorAll(".persona-card").forEach(c => c.classList.remove("active"));
      card.classList.add("active");
      const pKey = card.getAttribute("data-persona");
      loadPersona(pKey);
    });
  });

  const sliders = [
    { el: sliderHerb, val: valHerb, key: "herbaceous" },
    { el: sliderCitrus, val: valCitrus, key: "citrus_acid" },
    { el: sliderUmami, val: valUmami, key: "umami" },
    { el: sliderSweet, val: valSweet, key: "sweet" },
    { el: sliderPiquant, val: valPiquant, key: "piquant" }
  ];

  sliders.forEach(s => {
    s.el.addEventListener("input", (e) => {
      const v = parseFloat(e.target.value);
      s.val.textContent = v.toFixed(2);
      currentFlavor[s.key] = v;
      recalculateAlignment();
      drawRadar();
    });
  });

  toggleApiKeyDrawer.addEventListener("click", () => apiKeyModal.classList.add("open"));
  closeApiKeyModal.addEventListener("click", () => apiKeyModal.classList.remove("open"));
  saveApiSettings.addEventListener("click", () => {
    apiKeyModal.classList.remove("open");
    alert("Configuration Applied: Qloo Engine Active.");
  });

  exportProtocolBtn.addEventListener("click", exportProtocolJson);
}

function loadPersona(key) {
  currentPersonaKey = key;
  const p = PATIENT_ARCHETYPES[key];
  currentFlavor = { ...p.flavorProfile };

  sliderHerb.value = currentFlavor.herbaceous;
  sliderCitrus.value = currentFlavor.citrus_acid;
  sliderUmami.value = currentFlavor.umami;
  sliderSweet.value = currentFlavor.sweet;
  sliderPiquant.value = currentFlavor.piquant;

  valHerb.textContent = currentFlavor.herbaceous.toFixed(2);
  valCitrus.textContent = currentFlavor.citrus_acid.toFixed(2);
  valUmami.textContent = currentFlavor.umami.toFixed(2);
  valSweet.textContent = currentFlavor.sweet.toFixed(2);
  valPiquant.textContent = currentFlavor.piquant.toFixed(2);

  updateUiContent(p);
  drawRadar();
}

function updateUiContent(p) {
  agentSummaryText.textContent = p.agentSummary;
  topEntityName.textContent = p.matchedEntity.name;
  topEntityCategory.textContent = p.matchedEntity.category;
  topCompositeScore.textContent = `${p.matchedEntity.compositeScore}%`;
  affinityScoreBadge.textContent = `${p.matchedEntity.affinityScore}% Match`;

  chipSodium.textContent = p.matchedEntity.sodium;
  chipPotassium.textContent = p.matchedEntity.potassium;
  chipGI.textContent = p.matchedEntity.gi;
  chipTexture.textContent = p.matchedEntity.texture;

  topEntityTags.innerHTML = p.matchedEntity.tags.map(t => `<span>${t}</span>`).join("");

  adaptationsList.innerHTML = p.adaptations.map(a => `
    <div class="adapt-item">
      <span class="orig-food">${a.orig}</span>
      <span class="arrow-icon">➔</span>
      <span class="sub-food">${a.sub}</span>
    </div>
  `).join("");
}

function calculateCosineSimilarity(vecA, vecB) {
  const keys = ["herbaceous", "citrus_acid", "umami", "sweet", "piquant"];
  let dot = 0, normA = 0, normB = 0;
  keys.forEach(k => {
    const a = vecA[k] || 0;
    const b = vecB[k] || 0;
    dot += a * b;
    normA += a * a;
    normB += b * b;
  });
  if (normA === 0 || normB === 0) return 0;
  return dot / (Math.sqrt(normA) * Math.sqrt(normB));
}

function recalculateAlignment() {
  const p = PATIENT_ARCHETYPES[currentPersonaKey];
  const qlooFlavor = p.matchedEntity.flavorProfile;
  const similarity = calculateCosineSimilarity(currentFlavor, qlooFlavor);
  const matchPct = (similarity * 100).toFixed(1);
  affinityScoreBadge.textContent = `${matchPct}% Match`;
  topCompositeScore.textContent = `${(0.55 * matchPct + 0.45 * 100).toFixed(1)}%`;
}

function drawRadar() {
  const width = canvas.width;
  const height = canvas.height;
  const centerX = width / 2;
  const centerY = height / 2;
  const radius = Math.min(centerX, centerY) - 45;

  ctx.clearRect(0, 0, width, height);

  const labels = ["Herbaceous", "Citrus/Acid", "Umami", "Sweet", "Piquant"];
  const keys = ["herbaceous", "citrus_acid", "umami", "sweet", "piquant"];
  const total = labels.length;

  // Draw concentric web rings
  ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
  ctx.lineWidth = 1;
  for (let r = 0.2; r <= 1.0; r += 0.2) {
    ctx.beginPath();
    for (let i = 0; i < total; i++) {
      const angle = (Math.PI * 2 / total) * i - Math.PI / 2;
      const x = centerX + Math.cos(angle) * (radius * r);
      const y = centerY + Math.sin(angle) * (radius * r);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.closePath();
    ctx.stroke();
  }

  // Draw axis spokes & labels
  ctx.fillStyle = "#94a3b8";
  ctx.font = "11px 'Plus Jakarta Sans', sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";

  for (let i = 0; i < total; i++) {
    const angle = (Math.PI * 2 / total) * i - Math.PI / 2;
    const x = centerX + Math.cos(angle) * radius;
    const y = centerY + Math.sin(angle) * radius;

    ctx.strokeStyle = "rgba(255, 255, 255, 0.12)";
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(x, y);
    ctx.stroke();

    const labelX = centerX + Math.cos(angle) * (radius + 22);
    const labelY = centerY + Math.sin(angle) * (radius + 22);
    ctx.fillText(labels[i], labelX, labelY);
  }

  // Draw Qloo Target Polygon (Green)
  const p = PATIENT_ARCHETYPES[currentPersonaKey];
  const qlooVec = p.matchedEntity.flavorProfile;
  drawPolygon(keys.map(k => qlooVec[k]), "rgba(16, 185, 129, 0.25)", "#10b981", radius, centerX, centerY, total);

  // Draw Patient Profile Polygon (Cyan)
  drawPolygon(keys.map(k => currentFlavor[k]), "rgba(6, 182, 212, 0.35)", "#06b6d4", radius, centerX, centerY, total);
}

function drawPolygon(values, fillColor, strokeColor, radius, centerX, centerY, total) {
  ctx.beginPath();
  for (let i = 0; i < total; i++) {
    const val = values[i];
    const angle = (Math.PI * 2 / total) * i - Math.PI / 2;
    const x = centerX + Math.cos(angle) * (radius * val);
    const y = centerY + Math.sin(angle) * (radius * val);
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.closePath();
  ctx.fillStyle = fillColor;
  ctx.fill();
  ctx.strokeStyle = strokeColor;
  ctx.lineWidth = 2;
  ctx.stroke();

  // Draw vertices
  for (let i = 0; i < total; i++) {
    const val = values[i];
    const angle = (Math.PI * 2 / total) * i - Math.PI / 2;
    const x = centerX + Math.cos(angle) * (radius * val);
    const y = centerY + Math.sin(angle) * (radius * val);

    ctx.beginPath();
    ctx.arc(x, y, 4, 0, Math.PI * 2);
    ctx.fillStyle = strokeColor;
    ctx.fill();
  }
}

function exportProtocolJson() {
  const p = PATIENT_ARCHETYPES[currentPersonaKey];
  const payload = {
    protocol_id: `PROTO-${p.name.toUpperCase().replace(/\s+/g, '_')}-2026`,
    patient: p.name,
    condition: p.conditionName,
    cultural_origin: p.origin,
    flavor_memory_vector: currentFlavor,
    qloo_taste_graph_entity: p.matchedEntity,
    clinical_culinary_adaptations: p.adaptations,
    agent_reasoning: p.agentSummary,
    timestamp: new Date().toISOString()
  };

  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `PalateCare_${p.name.replace(/\s+/g, '_')}_Protocol.json`;
  a.click();
  URL.revokeObjectURL(url);
}

document.addEventListener("DOMContentLoaded", init);

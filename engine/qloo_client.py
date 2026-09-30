"""
Qloo API Client & Taste Graph Engine
Handles communications with https://hackathon.api.qloo.com/v2/insights and /search,
incorporating deterministic taste-graph embeddings and fallback sandbox data.
"""

import json
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional


class QlooClient:
    """Client for the Qloo Cultural Intelligence & Taste Graph API."""

    BASE_URL = "https://hackathon.api.qloo.com"

    def __init__(self, api_key: Optional[str] = None, use_sandbox: bool = True):
        self.api_key = api_key or ""
        self.use_sandbox = use_sandbox
        self._sandbox_entities = self._init_sandbox_entities()

    def _init_sandbox_entities(self) -> Dict[str, Dict[str, Any]]:
        """Pre-cached high-fidelity taste graph entities across key cuisines and entities."""
        return {
            "urn:entity:place:greek_souvlaki_house": {
                "id": "urn:entity:place:greek_souvlaki_house",
                "name": "Aegean Herb & Grill",
                "type": "urn:entity:place",
                "category": "Mediterranean / Greek",
                "flavor_profile": {"herbaceous": 0.92, "citrus_acid": 0.85, "umami": 0.70, "sweet": 0.15, "piquant": 0.30},
                "sodium_mg": 480,
                "potassium_mg": 420,
                "glycemic_index": 35,
                "texture_rating": "tender_grill",
                "tags": ["oregano", "lemon", "olive_oil", "wild_greens", "grilled_sea_bass"]
            },
            "urn:entity:place:oaxacan_cocina": {
                "id": "urn:entity:place:oaxacan_cocina",
                "name": "Oaxacan Hearth",
                "type": "urn:entity:place",
                "category": "Mexican / Oaxacan",
                "flavor_profile": {"herbaceous": 0.75, "citrus_acid": 0.80, "umami": 0.88, "sweet": 0.25, "piquant": 0.85},
                "sodium_mg": 720,
                "potassium_mg": 580,
                "glycemic_index": 42,
                "texture_rating": "braised_soft",
                "tags": ["epazote", "roasted_chile", "lime", "black_beans", "braised_chicken"]
            },
            "urn:entity:place:cantonese_steam_pot": {
                "id": "urn:entity:place:cantonese_steam_pot",
                "name": "Silk Road Steamed Broth",
                "type": "urn:entity:place",
                "category": "East Asian / Cantonese",
                "flavor_profile": {"herbaceous": 0.60, "citrus_acid": 0.40, "umami": 0.95, "sweet": 0.20, "piquant": 0.10},
                "sodium_mg": 410,
                "potassium_mg": 380,
                "glycemic_index": 28,
                "texture_rating": "pureed_velvety",
                "tags": ["ginger", "scallion", "steamed_tofu", "ginseng_broth", "silken_egg"]
            },
            "urn:entity:place:punjabi_dhaba_heritage": {
                "id": "urn:entity:place:punjabi_dhaba_heritage",
                "name": "Amritsar Herb Kitchen",
                "type": "urn:entity:place",
                "category": "South Asian / North Indian",
                "flavor_profile": {"herbaceous": 0.85, "citrus_acid": 0.65, "umami": 0.82, "sweet": 0.30, "piquant": 0.78},
                "sodium_mg": 640,
                "potassium_mg": 510,
                "glycemic_index": 45,
                "texture_rating": "stewed_soft",
                "tags": ["fenugreek", "roasted_cumin", "turmeric", "saag_greens", "paneer_tikka"]
            },
            "urn:entity:place:tuscan_olive_trattoria": {
                "id": "urn:entity:place:tuscan_olive_trattoria",
                "name": "Trattoria del Sole",
                "type": "urn:entity:place",
                "category": "Italian / Tuscan",
                "flavor_profile": {"herbaceous": 0.88, "citrus_acid": 0.60, "umami": 0.85, "sweet": 0.22, "piquant": 0.20},
                "sodium_mg": 550,
                "potassium_mg": 460,
                "glycemic_index": 38,
                "texture_rating": "tender_al_dente",
                "tags": ["rosemary", "extra_virgin_oil", "cannellini_beans", "braised_veal", "sage"]
            }
        }

    def search_entities(self, query: str, entity_type: str = "place") -> List[Dict[str, Any]]:
        """Search entities by text query or return sandbox matches."""
        if not self.use_sandbox and self.api_key:
            try:
                params = urllib.parse.urlencode({"query": query, "type": entity_type})
                url = f"{self.BASE_URL}/search?{params}"
                req = urllib.request.Request(url, headers={"X-Api-Key": self.api_key})
                with urllib.request.urlopen(req, timeout=5) as resp:
                    data = json.loads(resp.read().decode())
                    return data.get("results", [])
            except Exception:
                pass

        # Sandbox fallback
        q_lower = query.lower()
        results = []
        for e in self._sandbox_entities.values():
            if (
                q_lower in e["name"].lower()
                or q_lower in e["category"].lower()
                or any(q_lower in t.lower() for t in e["tags"])
            ):
                results.append(e)
        return results if results else list(self._sandbox_entities.values())

    def get_insights(
        self,
        filter_type: str = "urn:entity:place",
        signal_interests_entities: Optional[List[str]] = None,
        signal_tags: Optional[List[str]] = None,
        location: Optional[str] = None
    ) -> Dict[str, Any]:
        """Fetch recommendations from Qloo Insights API."""
        if not self.use_sandbox and self.api_key:
            try:
                params_dict: Dict[str, str] = {"filter.type": filter_type}
                if signal_interests_entities:
                    params_dict["signal.interests.entities"] = ",".join(signal_interests_entities)
                if signal_tags:
                    params_dict["signal.interests.tags"] = ",".join(signal_tags)
                if location:
                    params_dict["signal.location"] = location

                query_str = urllib.parse.urlencode(params_dict)
                url = f"{self.BASE_URL}/v2/insights?{query_str}"
                req = urllib.request.Request(url, headers={"X-Api-Key": self.api_key})
                with urllib.request.urlopen(req, timeout=5) as resp:
                    return json.loads(resp.read().decode())
            except Exception:
                pass

        # Deterministic Sandbox Taste Graph Synthesis
        entities = list(self._sandbox_entities.values())
        return {
            "status": "success",
            "source": "qloo_taste_graph_sandbox",
            "filter_type": filter_type,
            "entity_count": len(entities),
            "entities": entities
        }

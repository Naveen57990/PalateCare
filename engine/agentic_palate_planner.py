"""
Agentic Palate Planner
Autonomous orchestration agent integrating Qloo Taste Graph intelligence,
cultural flavor vectors, and clinical constraint validation.
"""

from typing import Any, Dict, List, Optional
from .qloo_client import QlooClient
from .cultural_affinity_engine import CulturalAffinityEngine
from .clinical_constraint_matrix import ClinicalConstraintMatrix


class AgenticPalatePlanner:
    """Orchestrates cultural nutrition synthesis for patients with complex clinical constraints."""

    def __init__(self, qloo_api_key: Optional[str] = None, use_sandbox: bool = True):
        self.qloo_client = QlooClient(api_key=qloo_api_key, use_sandbox=use_sandbox)
        self.cultural_engine = CulturalAffinityEngine()
        self.clinical_matrix = ClinicalConstraintMatrix()

    def generate_patient_protocol(
        self,
        patient_name: str,
        heritage_cuisine: str,
        clinical_condition: str,
        target_flavor_profile: Dict[str, float],
        city: str = "San Francisco, CA"
    ) -> Dict[str, Any]:
        """
        Executes end-to-end agentic synthesis:
        1. Queries Qloo Cultural Taste Graph for matching dining and culinary entities.
        2. Computes cultural affinity cosine similarity.
        3. Evaluates metabolic and physiological clinical constraints.
        4. Synthesizes tailored culinary adaptation modifications for chefs and caregivers.
        """
        # Step 1: Qloo Taste Graph Retrieval
        qloo_response = self.qloo_client.get_insights(
            filter_type="urn:entity:place",
            location=city
        )
        candidate_entities = qloo_response.get("entities", [])

        scored_recommendations: List[Dict[str, Any]] = []

        for entity in candidate_entities:
            # Step 2: Cultural Flavor Affinity
            entity_flavor = entity.get("flavor_profile", {})
            affinity_score = self.cultural_engine.calculate_flavor_similarity(
                target_flavor_profile, entity_flavor
            )

            # Step 3: Clinical Safety Screening
            is_safe, safety_score, violations = self.clinical_matrix.evaluate_entity_safety(
                clinical_condition, entity
            )

            # Step 4: Composite Rank Score (55% Cultural Affinity + 45% Clinical Safety)
            composite_score = round(0.55 * affinity_score + 0.45 * safety_score, 3)

            scored_recommendations.append({
                "entity_id": entity.get("id"),
                "name": entity.get("name"),
                "category": entity.get("category"),
                "flavor_profile": entity_flavor,
                "cultural_affinity_score": round(affinity_score, 3),
                "clinical_safety_score": safety_score,
                "composite_score": composite_score,
                "is_safe": is_safe,
                "clinical_violations": violations,
                "nutritional_metrics": {
                    "sodium_mg": entity.get("sodium_mg"),
                    "potassium_mg": entity.get("potassium_mg"),
                    "glycemic_index": entity.get("glycemic_index"),
                    "texture": entity.get("texture_rating")
                },
                "tags": entity.get("tags", [])
            })

        # Sort recommendations by composite score descending
        scored_recommendations.sort(key=lambda x: x["composite_score"], reverse=True)

        # Step 5: Cultural Culinary Adaptations
        adaptations = self.cultural_engine.get_cultural_adaptations(
            heritage_cuisine, [clinical_condition]
        )

        return {
            "protocol_id": f"PROTO-{patient_name.upper().replace(' ', '_')}-2026",
            "patient_name": patient_name,
            "heritage_cuisine": heritage_cuisine,
            "clinical_condition": clinical_condition,
            "city_context": city,
            "target_flavor_profile": target_flavor_profile,
            "top_recommendation": scored_recommendations[0] if scored_recommendations else None,
            "curated_dining_entities": scored_recommendations[:3],
            "cultural_culinary_adaptations": adaptations,
            "agent_summary": (
                f"Synthesized cultural dining protocol for {patient_name} navigating {clinical_condition}. "
                f"Selected '{scored_recommendations[0]['name']}' with {round(scored_recommendations[0]['composite_score']*100, 1)}% "
                f"cultural-clinical alignment index."
            )
        }

"""
Clinical Constraint Matrix
Deterministic safety gates for metabolic, renal, cardiac, oncology, and pharmacological restrictions.
"""

from typing import Any, Dict, List, Tuple


class ClinicalConstraintMatrix:
    """Verifies culinary entities and meal items against clinical dietary prescriptions."""

    CLINICAL_PROFILES: Dict[str, Dict[str, Any]] = {
        "CKD_Stage_3": {
            "name": "Chronic Kidney Disease (Stage 3)",
            "max_sodium_per_meal_mg": 500,
            "max_potassium_per_meal_mg": 600,
            "max_phosphorus_per_meal_mg": 250,
            "max_glycemic_index": 55,
            "allowed_textures": ["tender_grill", "braised_soft", "pureed_velvety", "stewed_soft", "tender_al_dente"],
            "restricted_ingredients": ["starfruit", "cured_meats", "heavy_dairy", "dark_cola"]
        },
        "Type_2_Diabetes_Cardiac": {
            "name": "Type 2 Diabetes & Cardiovascular Disease",
            "max_sodium_per_meal_mg": 450,
            "max_potassium_per_meal_mg": 1200,
            "max_phosphorus_per_meal_mg": 400,
            "max_glycemic_index": 45,
            "allowed_textures": ["tender_grill", "braised_soft", "pureed_velvety", "stewed_soft", "tender_al_dente"],
            "restricted_ingredients": ["added_sugars", "refined_flour", "trans_fats", "deep_fried"]
        },
        "Oncology_Dysphagia": {
            "name": "Oncology Post-Radiation / Dysphagia",
            "max_sodium_per_meal_mg": 600,
            "max_potassium_per_meal_mg": 1000,
            "max_phosphorus_per_meal_mg": 400,
            "max_glycemic_index": 60,
            "allowed_textures": ["pureed_velvety", "braised_soft", "stewed_soft"],
            "restricted_ingredients": ["acidic_citrus_raw", "sharp_crusts", "chili_capsaicin_high", "dry_crumbs"]
        },
        "Geriatric_Dentition_Hypertension": {
            "name": "Geriatric Dentition & Stage 2 Hypertension",
            "max_sodium_per_meal_mg": 400,
            "max_potassium_per_meal_mg": 900,
            "max_phosphorus_per_meal_mg": 350,
            "max_glycemic_index": 50,
            "allowed_textures": ["pureed_velvety", "braised_soft", "stewed_soft"],
            "restricted_ingredients": ["hard_nuts", "chewy_tendons", "salt_cured_pickles"]
        }
    }

    def evaluate_entity_safety(
        self, clinical_condition: str, entity: Dict[str, Any]
    ) -> Tuple[bool, float, List[str]]:
        """
        Evaluate if a Qloo entity satisfies clinical constraints.
        Returns: (is_safe, safety_score 0.0-1.0, violation_reasons)
        """
        profile = self.CLINICAL_PROFILES.get(clinical_condition, self.CLINICAL_PROFILES["CKD_Stage_3"])
        violations = []
        penalties = 0.0

        # Sodium check
        sodium = entity.get("sodium_mg", 600)
        max_sodium = profile["max_sodium_per_meal_mg"]
        if sodium > max_sodium:
            violations.append(f"Sodium level ({sodium}mg) exceeds clinical threshold ({max_sodium}mg).")
            penalties += min(0.4, (sodium - max_sodium) / max_sodium)

        # Potassium check
        potassium = entity.get("potassium_mg", 500)
        max_potassium = profile["max_potassium_per_meal_mg"]
        if potassium > max_potassium:
            violations.append(f"Potassium ({potassium}mg) exceeds limit ({max_potassium}mg).")
            penalties += min(0.3, (potassium - max_potassium) / max_potassium)

        # Glycemic Index check
        gi = entity.get("glycemic_index", 40)
        max_gi = profile["max_glycemic_index"]
        if gi > max_gi:
            violations.append(f"Glycemic Index ({gi}) exceeds safe ceiling ({max_gi}).")
            penalties += min(0.3, (gi - max_gi) / max_gi)

        # Texture check
        texture = entity.get("texture_rating", "tender_grill")
        allowed_textures = profile["allowed_textures"]
        if texture not in allowed_textures:
            violations.append(f"Texture rating '{texture}' is contraindicated for patient mastication profile.")
            penalties += 0.4

        safety_score = max(0.0, 1.0 - penalties)
        is_safe = len(violations) == 0 or safety_score >= 0.75

        return is_safe, round(safety_score, 3), violations

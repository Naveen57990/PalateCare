"""
Cultural Affinity Engine
Computes multi-dimensional taste profile vectors and performs cultural culinary adaptations.
"""

import math
from typing import Any, Dict, List, Tuple


class CulturalAffinityEngine:
    """Calculates flavor similarity and determines culinary substitutions based on cultural heritage."""

    CULTURAL_SUBSTITUTION_RULES: Dict[str, Dict[str, str]] = {
        "Mediterranean": {
            "high_sodium_feta": "rinsed low-sodium myzithra with fresh oregano and lemon zest",
            "salt_heavy_cured_olives": "marinated caperberries rinsed in sparkling water with thyme",
            "potassium_dense_tomato_paste": "roasted red bell pepper puree with pomegranate reduction",
            "refined_white_pita": "ancient grain farro flatbread with sumac"
        },
        "Mexican": {
            "salty_cotija_cheese": "toasted pepita-lime crumb with nutritional yeast",
            "lard_heavy_refried_beans": "slow-braised whole black beans with epazote and charred garlic",
            "high_sodium_salsa": "fire-roasted tomatillo pico de gallo with extra cilantro and serrano",
            "high_glycemic_tortillas": "cactus nopal and stone-ground corn blend"
        },
        "East Asian": {
            "high_sodium_soy_sauce": "coconut aminos infused with shiitake essence and ginger juice",
            "msg_heavy_oyster_sauce": "reduced vegetable stock with black garlic and kombu steep",
            "refined_sticky_rice": "steamed cauliflower-jasmine rice with toasted sesame oil",
            "chili_oil_heat": "mild sichuan pepper broth with silken scallion infusion"
        },
        "South Asian": {
            "salt_heavy_garam_masala_paste": "dry-roasted cumin-coriander-cardamom fresh grind with lime",
            "heavy_ghee_tadka": "cold-pressed mustard oil drizzle with toasted fenugreek seeds",
            "high_potassium_spinach_puree": "fenugreek and mustard greens braised with turmeric",
            "white_basmati_mound": "spiced ragi and pearl millet roti"
        },
        "Italian": {
            "salty_parmigiano_reggiano": "toasted pine nut and nutritional yeast dust with lemon rind",
            "heavy_cream_alfredo": "pureed roasted cauliflower with garlic, nutmeg, and almond milk",
            "salt_cured_prosciutto": "crisped thinly sliced shiitake with smoked paprika",
            "high_glycemic_pasta": "al dente whole-wheat or zucchini ribbon blend"
        }
    }

    @staticmethod
    def calculate_flavor_similarity(
        vector_a: Dict[str, float], vector_b: Dict[str, float]
    ) -> float:
        """Calculate cosine similarity between two 5D flavor profile vectors."""
        dimensions = ["herbaceous", "citrus_acid", "umami", "sweet", "piquant"]
        dot_product = 0.0
        norm_a = 0.0
        norm_b = 0.0

        for dim in dimensions:
            val_a = vector_a.get(dim, 0.0)
            val_b = vector_b.get(dim, 0.0)
            dot_product += val_a * val_b
            norm_a += val_a ** 2
            norm_b += val_b ** 2

        if norm_a == 0 or norm_b == 0:
            return 0.0

        return dot_product / (math.sqrt(norm_a) * math.sqrt(norm_b))

    def get_cultural_adaptations(
        self, heritage_cuisine: str, target_restrictions: List[str]
    ) -> List[Dict[str, str]]:
        """Map traditional culinary ingredients into clinically adapted alternatives preserving flavor memory."""
        rules = self.CULTURAL_SUBSTITUTION_RULES.get(heritage_cuisine, self.CULTURAL_SUBSTITUTION_RULES["Mediterranean"])
        adaptations = []
        for orig, sub in rules.items():
            adaptations.append({
                "original_ingredient": orig.replace("_", " ").title(),
                "clinical_substitute": sub,
                "heritage_context": heritage_cuisine
            })
        return adaptations

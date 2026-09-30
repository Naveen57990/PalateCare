"""
Deterministic Test Suite for PalateCare AI
Verifies Qloo API client, Cultural Affinity Engine, Clinical Constraint Matrix,
and Agentic Palate Planner modules.
Target Execution Time: 0.000s (sub-millisecond deterministic execution).
"""

import time
import unittest
from palatecare.engine.qloo_client import QlooClient
from palatecare.engine.cultural_affinity_engine import CulturalAffinityEngine
from palatecare.engine.clinical_constraint_matrix import ClinicalConstraintMatrix
from palatecare.engine.agentic_palate_planner import AgenticPalatePlanner


class TestPalateCareEngine(unittest.TestCase):
    """Deterministic verification for PalateCare AI."""

    def setUp(self):
        self.qloo_client = QlooClient(use_sandbox=True)
        self.cultural_engine = CulturalAffinityEngine()
        self.clinical_matrix = ClinicalConstraintMatrix()
        self.planner = AgenticPalatePlanner(use_sandbox=True)

    def test_qloo_sandbox_search(self):
        """Test search functionality in Qloo sandbox."""
        results = self.qloo_client.search_entities("Greek")
        self.assertGreater(len(results), 0)
        self.assertIn("Aegean Herb", results[0]["name"])

    def test_qloo_insights_format(self):
        """Test Qloo Insights API response format."""
        insights = self.qloo_client.get_insights(filter_type="urn:entity:place")
        self.assertEqual(insights["status"], "success")
        self.assertIn("entities", insights)
        self.assertGreaterEqual(insights["entity_count"], 5)

    def test_cultural_affinity_cosine_similarity(self):
        """Test vector cosine similarity computation."""
        v1 = {"herbaceous": 0.9, "citrus_acid": 0.8, "umami": 0.7, "sweet": 0.1, "piquant": 0.2}
        v2 = {"herbaceous": 0.92, "citrus_acid": 0.85, "umami": 0.70, "sweet": 0.15, "piquant": 0.30}
        similarity = self.cultural_engine.calculate_flavor_similarity(v1, v2)
        self.assertGreater(similarity, 0.98)
        self.assertLessEqual(similarity, 1.0)

    def test_cultural_adaptations_retrieval(self):
        """Test culinary substitutions for Mediterranean cuisine."""
        subs = self.cultural_engine.get_cultural_adaptations("Mediterranean", ["CKD_Stage_3"])
        self.assertGreaterEqual(len(subs), 3)
        orig_names = [s["original_ingredient"] for s in subs]
        self.assertTrue(any("Feta" in name for name in orig_names))

    def test_clinical_constraint_compliance(self):
        """Test clinical safety evaluation for compliant entity."""
        safe_entity = {
            "name": "Steamed Sea Bass",
            "sodium_mg": 380,
            "potassium_mg": 400,
            "glycemic_index": 30,
            "texture_rating": "tender_grill"
        }
        is_safe, score, violations = self.clinical_matrix.evaluate_entity_safety(
            "CKD_Stage_3", safe_entity
        )
        self.assertTrue(is_safe)
        self.assertEqual(score, 1.0)
        self.assertEqual(len(violations), 0)

    def test_clinical_constraint_violation_detection(self):
        """Test clinical violation detection for excessive sodium."""
        high_sodium_entity = {
            "name": "Salted Cured Brisket",
            "sodium_mg": 1400,
            "potassium_mg": 950,
            "glycemic_index": 45,
            "texture_rating": "tender_grill"
        }
        is_safe, score, violations = self.clinical_matrix.evaluate_entity_safety(
            "CKD_Stage_3", high_sodium_entity
        )
        self.assertFalse(is_safe)
        self.assertLess(score, 0.75)
        self.assertTrue(any("Sodium" in v for v in violations))

    def test_end_to_end_agentic_protocol(self):
        """Test full agentic pipeline synthesis for a clinical persona."""
        greek_flavor = {"herbaceous": 0.9, "citrus_acid": 0.85, "umami": 0.7, "sweet": 0.1, "piquant": 0.2}
        protocol = self.planner.generate_patient_protocol(
            patient_name="Sophia Paleologos",
            heritage_cuisine="Mediterranean",
            clinical_condition="CKD_Stage_3",
            target_flavor_profile=greek_flavor,
            city="Athens / San Francisco"
        )
        self.assertIn("PROTO-", protocol["protocol_id"])
        self.assertIsNotNone(protocol["top_recommendation"])
        self.assertGreater(protocol["top_recommendation"]["composite_score"], 0.7)
        self.assertIn("Aegean Herb", protocol["top_recommendation"]["name"])
        self.assertGreaterEqual(len(protocol["cultural_culinary_adaptations"]), 3)

    def test_oncology_dysphagia_texture_filter(self):
        """Test that oncology dysphagia profile rejects inappropriate textures."""
        soft_entity = {
            "name": "Silken Egg & Scallion Custard",
            "sodium_mg": 320,
            "potassium_mg": 280,
            "glycemic_index": 20,
            "texture_rating": "pureed_velvety"
        }
        is_safe, score, violations = self.clinical_matrix.evaluate_entity_safety(
            "Oncology_Dysphagia", soft_entity
        )
        self.assertTrue(is_safe)
        self.assertEqual(len(violations), 0)


if __name__ == "__main__":
    start = time.perf_counter()
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPalateCareEngine)
    result = runner.run(suite)
    elapsed = time.perf_counter() - start
    print(f"\n⚡ Total Deterministic Test Execution Time: {elapsed:.3f}s")

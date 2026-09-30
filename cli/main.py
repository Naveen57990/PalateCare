#!/usr/bin/env python3
"""
PalateCare Tactical CLI
Command-line interface for clinicians, caregivers, and hackathon judges to evaluate
cultural taste graph entities and synthesize clinical dining protocols.
"""

import argparse
import json
import os
import sys

# Bootstrap repository root into sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from palatecare.engine.agentic_palate_planner import AgenticPalatePlanner
from palatecare.engine.qloo_client import QlooClient
from palatecare.engine.clinical_constraint_matrix import ClinicalConstraintMatrix


def main():
    parser = argparse.ArgumentParser(
        description="PalateCare AI: Cultural Nutrition & Clinical Taste Synthesis CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Command: plan
    plan_parser = subparsers.add_parser("plan", help="Synthesize patient cultural dining protocol")
    plan_parser.add_argument("--name", type=str, default="Sophia Paleologos", help="Patient name")
    plan_parser.add_argument("--cuisine", type=str, default="Mediterranean", help="Heritage cuisine")
    plan_parser.add_argument(
        "--condition",
        type=str,
        default="CKD_Stage_3",
        choices=["CKD_Stage_3", "Type_2_Diabetes_Cardiac", "Oncology_Dysphagia", "Geriatric_Dentition_Hypertension"],
        help="Clinical condition"
    )
    plan_parser.add_argument("--city", type=str, default="San Francisco, CA", help="Target city / location")
    plan_parser.add_argument("--qloo-key", type=str, default="", help="Optional Qloo API Key")
    plan_parser.add_argument("--export", type=str, default="", help="Path to export JSON output")

    # Command: search
    search_parser = subparsers.add_parser("search", help="Search Qloo cultural taste graph entities")
    search_parser.add_argument("--query", type=str, required=True, help="Search query")
    search_parser.add_argument("--qloo-key", type=str, default="", help="Optional Qloo API Key")

    # Command: evaluate
    eval_parser = subparsers.add_parser("evaluate", help="Evaluate single entity against clinical constraints")
    eval_parser.add_argument("--condition", type=str, required=True, help="Clinical condition profile")
    eval_parser.add_argument("--sodium", type=int, default=500, help="Sodium in mg")
    eval_parser.add_argument("--potassium", type=int, default=450, help="Potassium in mg")
    eval_parser.add_argument("--gi", type=int, default=35, help="Glycemic index")
    eval_parser.add_argument("--texture", type=str, default="tender_grill", help="Texture rating")

    args = parser.parse_args()

    if args.command == "plan":
        flavor_profiles = {
            "Mediterranean": {"herbaceous": 0.9, "citrus_acid": 0.85, "umami": 0.7, "sweet": 0.1, "piquant": 0.2},
            "Mexican": {"herbaceous": 0.75, "citrus_acid": 0.8, "umami": 0.88, "sweet": 0.25, "piquant": 0.85},
            "East Asian": {"herbaceous": 0.6, "citrus_acid": 0.4, "umami": 0.95, "sweet": 0.2, "piquant": 0.1},
            "South Asian": {"herbaceous": 0.85, "citrus_acid": 0.65, "umami": 0.82, "sweet": 0.3, "piquant": 0.78},
            "Italian": {"herbaceous": 0.88, "citrus_acid": 0.6, "umami": 0.85, "sweet": 0.22, "piquant": 0.2}
        }
        target_flavor = flavor_profiles.get(args.cuisine, flavor_profiles["Mediterranean"])
        planner = AgenticPalatePlanner(qloo_api_key=args.qloo_key, use_sandbox=not bool(args.qloo_key))
        protocol = planner.generate_patient_protocol(
            patient_name=args.name,
            heritage_cuisine=args.cuisine,
            clinical_condition=args.condition,
            target_flavor_profile=target_flavor,
            city=args.city
        )
        print("\n🏛️ ================= PALATECARE AI PROTOCOL =================")
        print(f"Protocol ID:    {protocol['protocol_id']}")
        print(f"Patient:        {protocol['patient_name']}")
        print(f"Condition:      {protocol['clinical_condition']}")
        print(f"Heritage:       {protocol['heritage_cuisine']}")
        print(f"City Context:   {protocol['city_context']}")
        print(f"Agent Summary:  {protocol['agent_summary']}")
        print("-------------------------------------------------------------")
        print("🏆 TOP RECOMMENDED CULTURAL ENTITY:")
        top = protocol["top_recommendation"]
        if top:
            print(f"  • Name:             {top['name']} ({top['category']})")
            print(f"  • Alignment Index:  {round(top['composite_score']*100, 1)}% (Cultural: {top['cultural_affinity_score']}, Safety: {top['clinical_safety_score']})")
            print(f"  • Nutritional Gate: Na: {top['nutritional_metrics']['sodium_mg']}mg | K: {top['nutritional_metrics']['potassium_mg']}mg | GI: {top['nutritional_metrics']['glycemic_index']} | Texture: {top['nutritional_metrics']['texture']}")
        print("-------------------------------------------------------------")
        print("🍳 CULTURAL CULINARY ADAPTATIONS:")
        for a in protocol["cultural_culinary_adaptations"]:
            print(f"  [+] {a['original_ingredient']} ➔ {a['clinical_substitute']}")
        print("=============================================================\n")

        if args.export:
            with open(args.export, "w") as f:
                json.dump(protocol, f, indent=2)
            print(f"✅ Protocol successfully exported to {args.export}")

    elif args.command == "search":
        client = QlooClient(api_key=args.qloo_key, use_sandbox=not bool(args.qloo_key))
        results = client.search_entities(args.query)
        print(f"\n🔍 Found {len(results)} entities matching '{args.query}':")
        for r in results:
            print(f"  • {r.get('name')} [{r.get('category')}] - Tags: {', '.join(r.get('tags', []))}")
        print()

    elif args.command == "evaluate":
        matrix = ClinicalConstraintMatrix()
        mock_entity = {
            "name": "Custom Candidate Meal",
            "sodium_mg": args.sodium,
            "potassium_mg": args.potassium,
            "glycemic_index": args.gi,
            "texture_rating": args.texture
        }
        is_safe, score, violations = matrix.evaluate_entity_safety(args.condition, mock_entity)
        print(f"\n🩺 Clinical Safety Evaluation for {args.condition}:")
        print(f"  • Safe:   {'YES ✅' if is_safe else 'NO ❌'}")
        print(f"  • Score:  {score}")
        if violations:
            print("  • Violations:")
            for v in violations:
                print(f"    - {v}")
        print()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

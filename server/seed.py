#!/usr/bin/env python3

# Standard library imports
# from random import randint, choice as rc

# Remote library imports

# Local imports
from app import app
from models import db, DyeMaterial, Mordant, DyeResult

if __name__ == '__main__':
    with app.app_context():
        # Delete current data before seeding...
        DyeResult.query.delete()
        DyeMaterial.query.delete()
        Mordant.query.delete()

        # Begin seeding...
        print("Starting seed...")

        # dye_materials = []
        # mordants = []
        # dye_results = []

        dye_materials = [
                    DyeMaterial(name="Indigo", r=9, g=18, b=49, image="./images/indigo.jpg"),
                    DyeMaterial(name="Madder Root", r=204, g=51, b=51, image="./static/images/madder-root.png"),
                    DyeMaterial(name="Turmeric", r=255, g=221, b=51, image="https://example.com/turmeric.jpg"),
                    DyeMaterial(name="Red Cabbage", r=102, g=51, b=153, image="https://example.com/red_cabbage.jpg"),
                    DyeMaterial(name="Pokeweed Berries", r=204, g=0, b=102, image="https://example.com/pokeweed.jpg"),
                    DyeMaterial(name="Butterfly Pea Flower", r=51, g=102, b=204, image="https://example.com/butterfly_pea.jpg"),
                    DyeMaterial(name="Walnut Hulls", r=102, g=51, b=0, image="https://example.com/walnut_hulls.jpg"),
                    DyeMaterial(name="Onion Skins", r=255, g=165, b=0, image="https://example.com/onion_skins.jpg"),
                ]

        mordants = [
                    Mordant(name="Alum", r_effect=10, g_effect=10, b_effect=10, image="https://example.com/alum.jpg"),
                    Mordant(name="Iron", r_effect=-40, g_effect=-40, b_effect=-40, image="https://example.com/iron.jpg"),
                    Mordant(name="Copper", r_effect=-20, g_effect=20, b_effect=-20, image="https://example.com/copper.jpg"),
                    Mordant(name="Vinegar", r_effect=20, g_effect=0, b_effect=0, image="https://example.com/vinegar.jpg"),
                    Mordant(name="Ammonia", r_effect=0, g_effect=10, b_effect=30, image="https://example.com/ammonia.jpg"),
                    Mordant(name="Tannin", r_effect=5, g_effect=5, b_effect=5, image="https://example.com/tannin.jpg"),
                ]


        dye_results = [
            DyeResult(dye_material_id=1, mordant_id=1, final_hex="4B0082"),  # Indigo + Alum → Deep Blue
            DyeResult(dye_material_id=1, mordant_id=2, final_hex="2D1B1B"),  # Indigo + Iron → Dark Indigo
            DyeResult(dye_material_id=2, mordant_id=1, final_hex="FF5733"),  # Madder + Alum → Bright Red
            DyeResult(dye_material_id=2, mordant_id=3, final_hex="80461B"),  # Madder + Copper → Rusty Orange
            DyeResult(dye_material_id=3, mordant_id=1, final_hex="FFD700"),  # Turmeric + Alum → Vibrant Yellow
            DyeResult(dye_material_id=3, mordant_id=2, final_hex="A67B5B"),  # Turmeric + Iron → Mustard Brown
            DyeResult(dye_material_id=4, mordant_id=4, final_hex="D81B60"),  # Red Cabbage + Vinegar → Pink
            DyeResult(dye_material_id=4, mordant_id=5, final_hex="006400"),  # Red Cabbage + Ammonia → Green
            DyeResult(dye_material_id=5, mordant_id=2, final_hex="800020"),  # Pokeweed + Iron → Burgundy
            DyeResult(dye_material_id=6, mordant_id=3, final_hex="4682B4"),  # Butterfly Pea + Copper → Teal
            DyeResult(dye_material_id=7, mordant_id=2, final_hex="5D4037"),  # Walnut Hulls + Iron → Deep Brown
            DyeResult(dye_material_id=8, mordant_id=1, final_hex="FFA500"),  # Onion Skins + Alum → Bright Orange
        ]
# just has dye material id and mordant id
# on front end, have a way to generate what the RGB would be
# When user creates a new dye (combines dye material and mordant) -> (calculation would occur when dyeResult is generated)
# only able to create dye result on front end
# stretch goal for user authorization (so authorized users can add dye materials and resulting colors)
# stretch goal of using AI to figure out what the effect of a mordant is
#   use AI to figure out what the dye material + mordant resulting color would be
# open AI


        db.session.add_all(dye_materials + mordants + dye_results)
        db.session.commit()
        
        print("Dye materials, mordants, and dye results successfully seeded!")
#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports

# Local imports
from app import app
from models import db, DyeMaterial, Mordant, DyeResult

if __name__ == '__main__':
    with app.app_context():
        # Delete current data before seeding...
        DyeMaterial.query.delete()
        Mordant.query.delete()
        DyeResult.query.delete()

        # Begin seeding...
        print("Starting seed...")


        dye_material_1 = DyeMaterial(name="Indigo", base_color="Blue", image="https://example.com/indigo.jpg")
        dye_material_2 = DyeMaterial(name="Madder Root", base_color="Red", image="https://example.com/madder_root.jpg")
        dye_material_3 = DyeMaterial(name="Turmeric", base_color="Yellow", image="https://example.com/turmeric.jpg")
        dye_material_4 = DyeMaterial(name="Red Cabbage", base_color="Purple", image="https://example.com/red_cabbage.jpg")
        dye_material_5 = DyeMaterial(name="Pokeweed Berries", base_color="Magenta", image="https://example.com/pokeweed.jpg")       
        dye_material_6 = DyeMaterial(name="Butterfly Pea Flower", base_color="Blue", image="https://example.com/butterfly_pea.jpg")
        dye_material_7 = DyeMaterial(name="Walnut Hulls", base_color="Brown", image="https://example.com/walnut_hulls.jpg")
        dye_material_8 = DyeMaterial(name="Onion Skins", base_color="Orange", image="https://example.com/onion_skins.jpg")



        mordant_1 = Mordant(name="Alum", effect="Brightens color", image="https://example.com/alum.jpg")
        mordant_2 = Mordant(name="Iron", effect="Darkens color", image="https://example.com/iron.jpg")
        mordant_3 = Mordant(name="Copper", effect="Shifts colors towards green", image="https://example.com/copper.jpg")
        mordant_4 = Mordant(name="Vinegar", effect="Enhances red tones", image="https://example.com/vinegar.jpg")
        mordant_5 = Mordant(name="Ammonia", effect="Shifts color towards blue-green", image="https://example.com/ammonia.jpg")
        mordant_6 = Mordant(name="Tannin", effect="Increases colorfastness", image="https://example.com/tannin.jpg")



        dye_result_1 = DyeResult(dye_material_id=1, mordant_id=1, resulting_color="#4B0082", intensity=7)  # Indigo + Alum → Deep Blue
        dye_result_2 = DyeResult(dye_material_id=1, mordant_id=2, resulting_color="#2D1B1B", intensity=9)  # Indigo + Iron → Dark Indigo
        dye_result_3 = DyeResult(dye_material_id=2, mordant_id=1, resulting_color="#FF5733", intensity=8)  # Madder + Alum → Bright Red
        dye_result_4 = DyeResult(dye_material_id=2, mordant_id=3, resulting_color="#80461B", intensity=7)  # Madder + Copper → Rusty Orange
        dye_result_5 = DyeResult(dye_material_id=3, mordant_id=1, resulting_color="#FFD700", intensity=9)  # Turmeric + Alum → Vibrant Yellow
        dye_result_6 = DyeResult(dye_material_id=3, mordant_id=2, resulting_color="#A67B5B", intensity=7)  # Turmeric + Iron → Mustard Brown
        dye_result_7 = DyeResult(dye_material_id=4, mordant_id=4, resulting_color="#D81B60", intensity=6)  # Red Cabbage + Vinegar → Pink
        dye_result_8 = DyeResult(dye_material_id=4, mordant_id=5, resulting_color="#006400", intensity=5)  # Red Cabbage + Ammonia → Green
        dye_result_9 = DyeResult(dye_material_id=5, mordant_id=2, resulting_color="#800020", intensity=7)  # Pokeweed + Iron → Burgundy
        dye_result_10 = DyeResult(dye_material_id=6, mordant_id=3, resulting_color="#4682B4", intensity=6)  # Butterfly Pea + Copper → Teal
        dye_result_11 = DyeResult(dye_material_id=7, mordant_id=2, resulting_color="#5D4037", intensity=8)  # Walnut Hulls + Iron → Deep Brown
        dye_result_12 = DyeResult(dye_material_id=8, mordant_id=1, resulting_color="#FFA500", intensity=7)  # Onion Skins + Alum → Bright Orange



        db.session.add_all([
            dye_material_1, dye_material_2, dye_material_3, dye_material_4, dye_material_5, dye_material_6, dye_material_7, dye_material_8, 
            mordant_1, mordant_2, mordant_3, mordant_4, mordant_5, mordant_6, 
            dye_result_1, dye_result_2, dye_result_3, dye_result_4, dye_result_5, dye_result_6, dye_result_7, dye_result_8, dye_result_9, dye_result_10, dye_result_11, dye_result_12
        ])

        db.session.commit()
        print("Dye materials, mordants, and dye results successfully seeded!")
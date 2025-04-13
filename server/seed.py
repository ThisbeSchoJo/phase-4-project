#!/usr/bin/env python3

# Standard library imports
# from random import randint, choice as rc

# Remote library imports
from sqlalchemy import delete

# Local imports
from app import app
from models import db, DyeMaterial, Mordant, DyeResult

if __name__ == '__main__':
    with app.app_context():
        # Delete current data before seeding...
        db.session.execute(delete(DyeResult))
        db.session.execute(delete(DyeMaterial))
        db.session.execute(delete(Mordant))
        db.session.commit()

        # Begin seeding...
        print("Starting seed...")

        # dye_materials = []
        # mordants = []
        # dye_results = []

        dye_materials = [
                    DyeMaterial(name="Indigo", r=9, g=18, b=49, image="/images/indigo.png"),
                    DyeMaterial(name="Madder Root", r=204, g=51, b=51, image="/images/madder-root.png"),
                    DyeMaterial(name="Turmeric", r=255, g=221, b=51, image="/images/turmeric.png"),
                    DyeMaterial(name="Red Cabbage", r=102, g=51, b=153, image="/images/cabbage.png"),
                    DyeMaterial(name="Pokeweed Berries", r=204, g=0, b=102, image="/images/pokeweed.png"),
                    DyeMaterial(name="Butterfly Pea Flower", r=51, g=102, b=204, image="/images/butterfly-pea.png"),
                    DyeMaterial(name="Walnut Hulls", r=102, g=51, b=0, image="/images/black-walnut.png"),
                    DyeMaterial(name="Onion Skins", r=255, g=165, b=0, image="/images/onion-skins.png"),
                ]
        # ./images/zz-plant.jpg"

        mordants = [
                    Mordant(name="Alum", r_effect=10, g_effect=10, b_effect=10, image="/images/alum-stone.png"),
                    Mordant(name="Iron", r_effect=-40, g_effect=-40, b_effect=-40, image="/images/iron.png"),
                    Mordant(name="Copper", r_effect=-20, g_effect=20, b_effect=-20, image="/images/copper.png"),
                    Mordant(name="Vinegar", r_effect=20, g_effect=0, b_effect=0, image="/images/vinegar.png"),
                    Mordant(name="Ammonia", r_effect=0, g_effect=10, b_effect=30, image="/images/ammonia.png"),
                    Mordant(name="Tannin", r_effect=5, g_effect=5, b_effect=5, image="/images/black-tea.png"),
                ]


        dye_results = [
                    DyeResult(dye_material_id=6, mordant_id=2, final_hex="#0B3EA4", name="Indigo Whisper"),
                    DyeResult(dye_material_id=2, mordant_id=5, final_hex="#CC3D51", name="Spicy Sangria"),
                    DyeResult(dye_material_id=7, mordant_id=4, final_hex="#7A3300", name="Chai Season"),
                    DyeResult(dye_material_id=4, mordant_id=5, final_hex="#663DB7", name="Velvet Spell"),
                    DyeResult(dye_material_id=1, mordant_id=5, final_hex="#091C4F", name="Muse at Midnight"),
                    DyeResult(dye_material_id=3, mordant_id=2, final_hex="#D7B50B", name="Midas Mood"),
                    DyeResult(dye_material_id=5, mordant_id=4, final_hex="#DC0066", name="First Blush"),
                    DyeResult(dye_material_id=6, mordant_id=4, final_hex="#4566CC", name="Cloud Cover Crush"),
                    DyeResult(dye_material_id=4, mordant_id=6, final_hex="#6B389C", name="Lilac Afterparty"),
                    DyeResult(dye_material_id=7, mordant_id=6, final_hex="#6B3805", name="Maple Macchiato"),
                    DyeResult(dye_material_id=1, mordant_id=6, final_hex="#0E1D32", name="Witching Hour Waltz"),
                    DyeResult(dye_material_id=5, mordant_id=3, final_hex="#BC147A", name="Petal to the Metal"),
                    DyeResult(dye_material_id=3, mordant_id=6, final_hex="#FFE238", name="Sunbeam Serum"),
                    DyeResult(dye_material_id=4, mordant_id=4, final_hex="#7A3399", name="Lilac Mirage"),
                    DyeResult(dye_material_id=2, mordant_id=6, final_hex="#D13838", name="Raspberry Rendezvous"),
                    DyeResult(dye_material_id=3, mordant_id=5, final_hex="#FFDF51", name="Golden Hour Glow"),
                    DyeResult(dye_material_id=6, mordant_id=1, final_hex="#3D70D6", name="Twilight Spill"),
                    DyeResult(dye_material_id=2, mordant_id=4, final_hex="#DC3333", name="Spice Market"),
                    DyeResult(dye_material_id=1, mordant_id=3, final_hex="#000026", name="Eclipse Ink"),
                    DyeResult(dye_material_id=4, mordant_id=3, final_hex="#5245A7", name="Periwinkle Daydream"),
                    DyeResult(dye_material_id=5, mordant_id=5, final_hex="#CC0A84", name="Bubblegum Moon"),
                    DyeResult(dye_material_id=1, mordant_id=4, final_hex="#1D1231", name="Midnight Drizzle"),
                    DyeResult(dye_material_id=7, mordant_id=3, final_hex="#52450A", name="Toffee Dusk"),
                    DyeResult(dye_material_id=3, mordant_id=3, final_hex="#EBFF1F", name="Citrus Siren"),
                    DyeResult(dye_material_id=6, mordant_id=6, final_hex="#386BD1", name="Electric Mood Ring"),
                    DyeResult(dye_material_id=2, mordant_id=2, final_hex="#A60B0B", name="Cabernet Snap"),
                    DyeResult(dye_material_id=5, mordant_id=6, final_hex="#D1056B", name="Lip Stain Diaries"),
                    DyeResult(dye_material_id=1, mordant_id=1, final_hex="#131C3B", name="Stargaze & Chill"),
                    DyeResult(dye_material_id=7, mordant_id=1, final_hex="#6C3D0A", name="Cocoa in the Dark"),
                    DyeResult(dye_material_id=5, mordant_id=2, final_hex="#A6003E", name="Strawberry Mirage"),
                    DyeResult(dye_material_id=3, mordant_id=1, final_hex="#FFE73D", name="Butter Up"),
                    DyeResult(dye_material_id=6, mordant_id=5, final_hex="#3366E6", name="Blue Crush Hour"),
                    DyeResult(dye_material_id=2, mordant_id=3, final_hex="#BC473D", name="Terra Flame"),
                    DyeResult(dye_material_id=4, mordant_id=2, final_hex="#3E0B71", name="Iris Inkpot"),
                    DyeResult(dye_material_id=3, mordant_id=4, final_hex="#FFDD33", name="Lemon Lush"),
                    DyeResult(dye_material_id=4, mordant_id=1, final_hex="#6C3DA7", name="Lavender Voltage"),
                    DyeResult(dye_material_id=1, mordant_id=2, final_hex="#000000", name="Blackout Poetry"),
                    DyeResult(dye_material_id=7, mordant_id=2, final_hex="#3E0B00", name="Molasses Mood"),
                    DyeResult(dye_material_id=2, mordant_id=1, final_hex="#CE3D3D", name="Rosé Before Brosé"),
                    DyeResult(dye_material_id=5, mordant_id=1, final_hex="#D60A70", name="Berry Daring"),
                    DyeResult(dye_material_id=3, mordant_id=2, final_hex="#D7B50B", name="Goldenrod Remix"),
                    DyeResult(dye_material_id=6, mordant_id=3, final_hex="#1F7AE6", name="Blueberry Techno"),
                    DyeResult(dye_material_id=7, mordant_id=5, final_hex="#663D1E", name="Brown Sugar Theory"),
                    DyeResult(dye_material_id=2, mordant_id=5, final_hex="#CC3D51", name="Spicy Sangria"),
                ]

        db.session.add_all(dye_materials + mordants + dye_results)
        db.session.commit()
        
        print("Dye materials, mordants, and dye results successfully seeded!")
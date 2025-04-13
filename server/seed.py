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
            # Indigo + Alum (r+10, g+10, b+10) → #131C3B
            DyeResult(dye_material_id=1, mordant_id=1, final_hex="#131C3B"),
            # Indigo + Iron (r-40, g-40, b-40) → #000000
            DyeResult(dye_material_id=1, mordant_id=2, final_hex="#000000"),
            # Indigo + Copper (r-20, g+20, b-20) → #000026
            DyeResult(dye_material_id=1, mordant_id=3, final_hex="#000026"),
            # Indigo + Vinegar (r+20, g+0, b+0) → #1D1231
            DyeResult(dye_material_id=1, mordant_id=4, final_hex="#1D1231"),
            # Indigo + Ammonia (r+0, g+10, b+30) → #091C4F
            DyeResult(dye_material_id=1, mordant_id=5, final_hex="#091C4F"),
            # Indigo + Tannin (r+5, g+5, b+5) → #0E1D32
            DyeResult(dye_material_id=1, mordant_id=6, final_hex="#0E1D32"),
            
            # Madder Root (r=204, g=51, b=51) combinations
            # Madder + Alum (r+10, g+10, b+10) → #CE3D3D
            DyeResult(dye_material_id=2, mordant_id=1, final_hex="#CE3D3D"),
            # Madder + Iron (r-40, g-40, b-40) → #A60B0B
            DyeResult(dye_material_id=2, mordant_id=2, final_hex="#A60B0B"),
            # Madder + Copper (r-20, g+20, b-20) → #BC473D
            DyeResult(dye_material_id=2, mordant_id=3, final_hex="#BC473D"),
            # Madder + Vinegar (r+20, g+0, b+0) → #DC3333
            DyeResult(dye_material_id=2, mordant_id=4, final_hex="#DC3333"),
            # Madder + Ammonia (r+0, g+10, b+30) → #CC3D51
            DyeResult(dye_material_id=2, mordant_id=5, final_hex="#CC3D51"),
            # Madder + Tannin (r+5, g+5, b+5) → #D13838
            DyeResult(dye_material_id=2, mordant_id=6, final_hex="#D13838"),
            
            # Turmeric (r=255, g=221, b=51) combinations
            # Turmeric + Alum (r+10, g+10, b+10) → #FFE73D
            DyeResult(dye_material_id=3, mordant_id=1, final_hex="#FFE73D"),
            # Turmeric + Iron (r-40, g-40, b-40) → #D7B50B
            DyeResult(dye_material_id=3, mordant_id=2, final_hex="#D7B50B"),
            # Turmeric + Copper (r-20, g+20, b-20) → #EBFF1F
            DyeResult(dye_material_id=3, mordant_id=3, final_hex="#EBFF1F"),
            # Turmeric + Vinegar (r+20, g+0, b+0) → #FFDD33
            DyeResult(dye_material_id=3, mordant_id=4, final_hex="#FFDD33"),
            # Turmeric + Ammonia (r+0, g+10, b+30) → #FFDF51
            DyeResult(dye_material_id=3, mordant_id=5, final_hex="#FFDF51"),
            # Turmeric + Tannin (r+5, g+5, b+5) → #FFE238
            DyeResult(dye_material_id=3, mordant_id=6, final_hex="#FFE238"),
            
            # Red Cabbage (r=102, g=51, b=153) combinations
            # Red Cabbage + Alum (r+10, g+10, b+10) → #6C3DA7
            DyeResult(dye_material_id=4, mordant_id=1, final_hex="#6C3DA7"),
            # Red Cabbage + Iron (r-40, g-40, b-40) → #3E0B71
            DyeResult(dye_material_id=4, mordant_id=2, final_hex="#3E0B71"),
            # Red Cabbage + Copper (r-20, g+20, b-20) → #5245A7
            DyeResult(dye_material_id=4, mordant_id=3, final_hex="#5245A7"),
            # Red Cabbage + Vinegar (r+20, g+0, b+0) → #7A3399
            DyeResult(dye_material_id=4, mordant_id=4, final_hex="#7A3399"),
            # Red Cabbage + Ammonia (r+0, g+10, b+30) → #663DB7
            DyeResult(dye_material_id=4, mordant_id=5, final_hex="#663DB7"),
            # Red Cabbage + Tannin (r+5, g+5, b+5) → #6B389C
            DyeResult(dye_material_id=4, mordant_id=6, final_hex="#6B389C"),
            
            # Pokeweed Berries (r=204, g=0, b=102) combinations
            # Pokeweed + Alum (r+10, g+10, b+10) → #D60A70
            DyeResult(dye_material_id=5, mordant_id=1, final_hex="#D60A70"),
            # Pokeweed + Iron (r-40, g-40, b-40) → #A6003E
            DyeResult(dye_material_id=5, mordant_id=2, final_hex="#A6003E"),
            # Pokeweed + Copper (r-20, g+20, b-20) → #BC147A
            DyeResult(dye_material_id=5, mordant_id=3, final_hex="#BC147A"),
            # Pokeweed + Vinegar (r+20, g+0, b+0) → #DC0066
            DyeResult(dye_material_id=5, mordant_id=4, final_hex="#DC0066"),
            # Pokeweed + Ammonia (r+0, g+10, b+30) → #CC0A84
            DyeResult(dye_material_id=5, mordant_id=5, final_hex="#CC0A84"),
            # Pokeweed + Tannin (r+5, g+5, b+5) → #D1056B
            DyeResult(dye_material_id=5, mordant_id=6, final_hex="#D1056B"),
            
            # Butterfly Pea Flower (r=51, g=102, b=204) combinations
            # Butterfly Pea + Alum (r+10, g+10, b+10) → #3D70D6
            DyeResult(dye_material_id=6, mordant_id=1, final_hex="#3D70D6"),
            # Butterfly Pea + Iron (r-40, g-40, b-40) → #0B3EA4
            DyeResult(dye_material_id=6, mordant_id=2, final_hex="#0B3EA4"),
            # Butterfly Pea + Copper (r-20, g+20, b-20) → #1F7AE6
            DyeResult(dye_material_id=6, mordant_id=3, final_hex="#1F7AE6"),
            # Butterfly Pea + Vinegar (r+20, g+0, b+0) → #4566CC
            DyeResult(dye_material_id=6, mordant_id=4, final_hex="#4566CC"),
            # Butterfly Pea + Ammonia (r+0, g+10, b+30) → #3366E6
            DyeResult(dye_material_id=6, mordant_id=5, final_hex="#3366E6"),
            # Butterfly Pea + Tannin (r+5, g+5, b+5) → #386BD1
            DyeResult(dye_material_id=6, mordant_id=6, final_hex="#386BD1"),
            
            # Walnut Hulls (r=102, g=51, b=0) combinations
            # Walnut + Alum (r+10, g+10, b+10) → #6C3D0A
            DyeResult(dye_material_id=7, mordant_id=1, final_hex="#6C3D0A"),
            # Walnut + Iron (r-40, g-40, b-40) → #3E0B00
            DyeResult(dye_material_id=7, mordant_id=2, final_hex="#3E0B00"),
            # Walnut + Copper (r-20, g+20, b-20) → #52450A
            DyeResult(dye_material_id=7, mordant_id=3, final_hex="#52450A"),
            # Walnut + Vinegar (r+20, g+0, b+0) → #7A3300
            DyeResult(dye_material_id=7, mordant_id=4, final_hex="#7A3300"),
            # Walnut + Ammonia (r+0, g+10, b+30) → #663D1E
            DyeResult(dye_material_id=7, mordant_id=5, final_hex="#663D1E"),
            # Walnut + Tannin (r+5, g+5, b+5) → #6B3805
            DyeResult(dye_material_id=7, mordant_id=6, final_hex="#6B3805"),
            
            # Onion Skins (r=255, g=165, b=0) combinations
            # Onion + Alum (r+10, g+10, b+10) → #FFAF0A
            DyeResult(dye_material_id=8, mordant_id=1, final_hex="#FFAF0A"),
            # Onion + Iron (r-40, g-40, b-40) → #D77D00
            DyeResult(dye_material_id=8, mordant_id=2, final_hex="#D77D00"),
            # Onion + Copper (r-20, g+20, b-20) → #EBB90A
            DyeResult(dye_material_id=8, mordant_id=3, final_hex="#EBB90A"),
            # Onion + Vinegar (r+20, g+0, b+0) → #FFA500
            DyeResult(dye_material_id=8, mordant_id=4, final_hex="#FFA500"),
            # Onion + Ammonia (r+0, g+10, b+30) → #FFA51E
            DyeResult(dye_material_id=8, mordant_id=5, final_hex="#FFA51E"),
            # Onion + Tannin (r+5, g+5, b+5) → #FFAA05
            DyeResult(dye_material_id=8, mordant_id=6, final_hex="#FFAA05"),
        ]

        db.session.add_all(dye_materials + mordants + dye_results)
        db.session.commit()
        
        print("Dye materials, mordants, and dye results successfully seeded!")
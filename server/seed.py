#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
# from faker import Faker

# Local imports
from app import app
from models import db, Volcano

if __name__ == '__main__':
    # fake = Faker()
    with app.app_context():
        # Delete current volcano data before seeding...
        Volcano.query.delete()

        # Begin seeding...
        print("Starting seed...")

        volcano_1 = Volcano(location="Pompeii", image="https://as2.ftcdn.net/v2/jpg/05/30/53/17/1000_F_530531798_yJOJBlxketxdUv1axTObn0WVWY0lBre5.jpg")
        volcano_2 = Volcano(location="Hawaii", image="https://www.gannett-cdn.com/presto/2019/03/14/USAT/202d1217-b3d4-4dee-bc6b-9af009773203-AFP_AFP_1665JS.JPG?crop=2447,1376,x0,y897&width=3200&height=1680&fit=bounds")

        db.session.add(volcano_1, volcano_2)
        db.session.commit()
        print("Volcanoes successfully succeeded!")
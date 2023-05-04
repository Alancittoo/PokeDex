from random import randint, choice
from faker import Faker

import faker_commerce

fake = Faker()
fake.add_provider(faker_commerce.Provider)

def random_100():
    return randint(1, 100)


def random_image():
    images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
    ]
    index = randint(0, len(images) - 1)
    return images[index]


item_list = []

for pokemon_id in range(1, 126):
    for i in range(0, 3):
        item_list.append(
            {
                "pokemon_id": pokemon_id,
                "name": fake.ecommerce_name(),
                "price": random_100(),
                "happiness": random_100(),
                "image_url": random_image(),
            }
        )

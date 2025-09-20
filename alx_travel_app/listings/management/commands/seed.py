from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = "Seed database with sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Create sample users
        users = []
        for i in range(5):
            user, created = User.objects.get_or_create(
                username=fake.user_name(),
                defaults={"email": fake.email()}
            )
            users.append(user)

        # Create listings
        listings = []
        for i in range(10):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                price_per_night=random.randint(50, 500),
                location=fake.city(),
            )
            listings.append(listing)

        # Create bookings
        for i in range(20):
            booking = Booking.objects.create(
                listing=random.choice(listings),
                user=random.choice(users),
                check_in=fake.date_this_year(),
                check_out=fake.date_this_year(),
                guests=random.randint(1, 5),
            )

            # Add optional reviews
            if random.choice([True, False]):
                Review.objects.create(
                    booking=booking,
                    rating=random.randint(1, 5),
                    comment=fake.sentence(),
                )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))

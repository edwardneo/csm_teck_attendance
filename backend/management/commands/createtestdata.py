from django.core.management import BaseCommand
from backend.models import User, Student, Mentor, Section, Course, Attendance

import random

from faker import Faker

NUM_TO_CREATE = 20
COURSES = ["CS61A", "CS61B", "CS61C", "CS70"]


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        users = []
        usernames = set()
        # create users
        for i in range(NUM_TO_CREATE):
            while True:
                first = fake.first_name()
                last = fake.last_name()
                if f"{first}{last}" not in usernames:
                    break
            usernames.add(f"{first}{last}")
            user = User.objects.create(
                username=f"{first}{last}",
                email=f"{first}{last}@berkeley.edu",
                first_name=first,
                last_name=last,
            )
            users.append(user)

        # create courses
        for course_name in COURSES:
            course = Course.objects.create(name=course_name)

            # create mentors
            mentors = []
            potential_students = []
            for i, user in enumerate(users):
                is_mentor = (i == 0 or random.choice([True, False])) and len(
                    mentors
                ) < 3
                if is_mentor:
                    mentor = Mentor.objects.create(user=user, course=course)
                    mentors.append(mentor)
                else:
                    potential_students.append(user)

            # create sections for each mentor
            sections = []
            for mentor in mentors:
                section = Section.objects.create(mentor=mentor, capacity=10)
                sections.append(section)

            # create students
            for user in potential_students:
                section = random.choice(sections)
                student = Student.objects.create(
                    user=user,
                    section=section,
                    course=section.mentor.course,
                    active=random.choice([True, False]),
                    banned=False,
                )

                # create attendances for each student
                for _ in range(random.randint(5, 10)):
                    Attendance.objects.create(
                        student=student,
                        date=fake.date_time_this_year(),
                        presence=random.choice(["PR", "EX", "UN"]),
                    )

        # create admin user
        admin = User.objects.create(
            username="demo_user",
            email="demo_user@berkeley.edu",
            first_name="Demo",
            last_name="User",
            is_superuser=True,
            is_staff=True,
        )
        admin.set_password("pass")
        admin.save()

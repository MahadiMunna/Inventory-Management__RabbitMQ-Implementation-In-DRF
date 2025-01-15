from django.core.management.base import BaseCommand
from app.consumer import inventory_actions

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        inventory_actions()

# music/management/commands/import_data.py

import os
import json
from django.core.management.base import BaseCommand
from music.models import Singer, Song

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        singer_data_dir = 'D:/cpp/projects/helloworld/music2/music_site/data/singers'
        song_data_dir = 'D:/cpp/projects/helloworld/music2/music_site/data/songs'

        for filename in os.listdir(singer_data_dir):
            if filename.endswith('.json'):
                with open(os.path.join(singer_data_dir, filename), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    singer, created = Singer.objects.update_or_create(
                        singer_id=data['singer_id'],
                        defaults={
                            'singer_name': data['singer_name'],
                            'summ': data['singer_summ'],
                            'original_url': data['singer_url']
                        }
                    )

        for filename in os.listdir(song_data_dir):
            if filename.endswith('.json'):
                with open(os.path.join(song_data_dir, filename), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    try:
                        singer = Singer.objects.get(singer_name=data['singers'])
                        song, created = Song.objects.update_or_create(
                            song_id=data['song_id'],
                            defaults={
                                'title': data['song_name'],
                                'singer': singer,
                                'lyrics': data['lyrics'].lstrip('\n') ,
                                'original_url': data['song_url']
                            }
                        )
                    except singer.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f''))

        self.stdout.write(self.style.SUCCESS('Data import completed'))

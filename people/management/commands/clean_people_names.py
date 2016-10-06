import os, re
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from people.models import People

pattern = re.compile('[\W_]+', re.UNICODE)

class Command(BaseCommand):
  help = 'Clean people names, remove special characters.'
  
  def handle(self, *args, **options):
    try:
      peoples = People.objects.all()
      
      time_now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
      os.system("echo Task start at : %s >> clean_people_data.log" %(time_now))
      os.system("echo Task start at : %s >> failer_people_c_data.log" %(time_now))
      
      for people in peoples:
      
        try:
          people.full_name = pattern.sub(' ', people.full_name).strip()
          people.given_name = pattern.sub(' ', people.given_name).strip()
          people.family_name = pattern.sub(' ', people.family_name).strip()
          people.save()
          os.system("echo %s >> clean_people_data.log" %(people.id))
          print people.id
        except Exception as e:
          os.system("echo %s >> failer_people_c_data.log" %(people.id))
      
      self.stdout.write('Successfully cleaned peoples records.')
    except Exception as e:
      print e
      self.stdout.write('Something went wrong, operation terminated.')
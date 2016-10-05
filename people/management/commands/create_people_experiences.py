import os
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, date
from people.models import People, Experience
from company.models import Company

class Command(BaseCommand):
  help = 'Create people experiences records.'
  
  def handle(self, *args, **options):
    try:
      peoples = People.objects.all()
      
      time_now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
      os.system("echo Task start at : %s >> processed_experiences_data.log" %(time_now))
      os.system("echo Task start at : %s >> failer_experiences_data.log" %(time_now))
      
      for people in peoples:
        
        if people.experience and not people.experiences:
          experiences_list = []
          
          for experience in people.experience:
            
            experience['duration'] = None
            try:
              uid = exp['organization'][0]['unique_id']
              company = Company.objects.get(unique_id=uid)
              experience['organization'] = company
            except:
              experience['organization'] = None

            exp = Experience.objects.create(**experience)
            experiences_list.append(exp)
          
          try:
            people.experiences = experiences_list
            people.save()
            os.system("echo %s >> processed_experiences_data.log" %(people.id))
            print people.id
          
          except Exception as e:
            os.system("echo %s >> failer_experiences_data.log" %(people.id))
      
      self.stdout.write('Successfully created peoples experience records.')
    except Exception as e:
      print e
      self.stdout.write('Something went wrong, operation terminated.')
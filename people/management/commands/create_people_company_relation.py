import os
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from people.models import People

class Command(BaseCommand):
  help = 'Read company details from peoples experience list and create relations between Company and People record.'
  
  def handle(self, *args, **options):
    try:
      peoples = People.objects.all()
      time_now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
      os.system("echo Task start at : %s >> processed_people_data.log" %(time_now))
      os.system("echo Task start at : %s >> failer_people_data.log" %(time_now))
      for people in peoples:
        if people.experience and not people.companies:
          companies_list = []
          for experience in people.experience:
            try:
              for org in experience['organization']:
                if org['unique_id']:
                  companies_list.append(str(org['unique_id']))
            except Exception as e:
              e
          try:
            people.companies = companies_list
            people.save()
            os.system("echo %s >> processed_people_data.log" %(people.id))
            print people.id
          except Exception as e:
            os.system("echo %s >> failer_people_data.log" %(people.id))
      self.stdout.write('Successfully created relations between companies and peoples records.')
    except Exception as e:
      print e
      self.stdout.write('Something went wrong, operation terminated.')
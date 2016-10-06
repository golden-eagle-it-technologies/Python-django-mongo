import os, click, itertools
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, date
from people.models import People, Experience
from company.models import Company
from industries.models import Industry

class Command(BaseCommand):
  help = 'Create industry for peoples records.'
  
  def handle(self, *args, **options):
    try:
      peoples = People.objects.all()
      count = peoples.count()
      print 'Total number of records : %s' %(count)

      time_now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
      os.system("echo Task start at : %s >> processed_industry_data.log" %(time_now))
      os.system("echo Task start at : %s >> failer_industry_data.log" %(time_now))
      
      with click.progressbar(range(count)) as bar:
        for people, i in itertools.izip(peoples, bar):
          if people.industry and not people.industry_ref:
            try:
              name = str(people.industry).lower()
              industry = Industry.objects.get_or_create(name=name)
              people.industry_ref = industry[0]
              people.save()
              os.system("echo %s >> processed_industry_data.log" %(people.id))
            except:
              os.system("echo %s >> failer_industry_data.log" %(people.id))

      self.stdout.write('Successfully created peoples experience records.')
    except Exception as e:
      print e
      self.stdout.write('Something went wrong, operation terminated.')
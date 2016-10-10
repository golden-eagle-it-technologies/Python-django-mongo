import os, re, click, itertools
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, date

from company_dump.models import CompanyDump
from companies.models import Company
from industries.models import Industry

pattern = re.compile('[\W_]+', re.UNICODE)

class Command(BaseCommand):
  help = 'Build Company records from Raw Company Data.'
  
  def handle(self, *args, **options):
    try:
      
      company_fields = Company.fields_list()
      company_dump = CompanyDump.objects.all()
      cdump_count = company_dump.count()
      industries = Industry.objects.all()

      time_now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
      os.system("echo Task start at : %s >> processed_company_data.log" %(time_now))
      os.system("echo Task start at : %s >> failer_company_data.log" %(time_now))

      # with click.progressbar(range(cdump_count)) as bar:
        # for cdump, i in itertools.izip(company_dump, bar):
        for cdump in company_dump:

          # if not Company.objects(unique_id=cdump.unique_id):
            try:
              company = {}
              for item in company_fields:
                
                if item in cdump:
                  if item == 'name':
                    company[item] = pattern.sub(' ', cdump[item]).strip()
                  elif item == 'automatically_generated':
                    company[item] = True if cdump[item].lower() == 'true' else False
                  elif item in ['updated', 'last_visited']:
                    company[item] = datetime.strptime(cdump[item].replace('T',' '), '%Y-%m-%d %H:%M:%S')
                  elif item == 'industry':
                    industry = industries.filter(name=cdump[item].lower())
                    company[item] = industry[0] if industry else None
                  else:
                    company[item] = cdump[item]
                else:
                  company[item] = None

              Company.objects.create(**company)
              os.system("echo id : %s unique_id : %s >> processed_company_data.log" %(cdump.id, cdump.unique_id))
            except:
              os.system("echo id : %s unique_id : %s >> failer_company_data.log" %(cdump.id, cdump.unique_id))
        
      self.stdout.write('Successfully build company records.')
    except Exception as e:
      print e
      os.system("echo error : %s >> failer_company_data.log" %(e))
      self.stdout.write('Something went wrong, operation terminated.')
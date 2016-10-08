import os, re, click, itertools
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, date

from people_dump.models import PeopleDump
from users.models import User, Experience
from industries.models import Industry

pattern = re.compile('[\W_]+', re.UNICODE)

class Command(BaseCommand):
  help = 'Build User records from Raw People Data.'
  
  def handle(self, *args, **options):
    try:
      
      user_fields = User.fields_list()
      people_dump = PeopleDump.objects.all()
      pdump_count = people_dump.count()

      time_now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
      os.system("echo Task start at : %s >> processed_user_data.log" %(time_now))
      os.system("echo Task start at : %s >> failer_user_data.log" %(time_now))

      with click.progressbar(range(pdump_count)) as bar:
        for pdump, i in itertools.izip(people_dump, bar):

          if not User.objects(unique_id=pdump.unique_id):
            try:
              user = {}
              for item in user_fields:

                if item in pdump or (item == 'experiences' and 'experience' in pdump):
                  if item in ['full_name', 'given_name', 'family_name']:
                    user[item] = pattern.sub(' ', pdump[item]).strip()
                  elif item in ['updated', 'last_visited']:
                    user[item] = datetime.strptime(pdump[item].replace('T',' '), '%Y-%m-%d %H:%M:%S')
                  elif item == 'languages':
                    languages = []
                    for language in pdump[item]:
                      try:
                        languages.append(language['name'])
                      except:
                        pass
                    user[item] = languages
                  elif item == 'experiences':
                    experiences = []
                    try:
                      for expobj in pdump['experience']:
                        exp = Experience.build_experience(expobj)
                        if exp:
                          experiences.append(exp)
                    except:
                      pass
                    user[item] = experiences
                  elif item == 'industry':
                    industry = Industry.objects.filter(name=pdump[item].lower())
                    user[item] = industry[0] if industry else None
                  else:
                    user[item] = pdump[item]
                else:
                  user[item] = None

              User.objects.create(**user)
              os.system("echo id : %s unique_id : %s >> processed_user_data.log" %(pdump.id, pdump.unique_id))
            except:
              os.system("echo id : %s unique_id : %s >> failer_user_data.log" %(pdump.id, pdump.unique_id))
        
      self.stdout.write('Successfully build user records.')
    except Exception as e:
      print e
      self.stdout.write('Something went wrong, operation terminated.')
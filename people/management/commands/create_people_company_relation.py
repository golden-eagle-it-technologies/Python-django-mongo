from django.core.management.base import BaseCommand, CommandError
from people.models import People

class Command(BaseCommand):
  help = 'Read company details from peoples experience list and create relations between Company and People record.'
  
  def handle(self, *args, **options):
    try:
      peoples = People.objects.all()
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
            print people.id
          except Exception as e:
            e
      self.stdout.write('Successfully created relations between companies and peoples records.')
    except Exception as e:
      print e
      self.stdout.write('Something went wrong, operation terminated.')
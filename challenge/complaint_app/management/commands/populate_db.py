from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from complaint_app.models import UserProfile, Complaint
import os.path
import json

class Command(BaseCommand):
  help = "Seeds database with users, and complaints"

  def handle(self, *args, **options):
    BASE = os.path.dirname(os.path.abspath(__file__))
    cm_json = os.path.join(BASE, "councilMembers.json")
    with open(cm_json) as json_file:
      data = json.load(json_file)
      for cm in data:
        names = cm['name'].replace(', Sr.','').lower().split(' ')
        u = User.objects.create_user(
          names[0][0]+names[-1],
          first_name=names[0].capitalize(),
          last_name=names[-1].capitalize(),
          password='{}-{}'.format(names[-1],cm['district'])
        )
        u.save()
        up = UserProfile.objects.create(
          user=u,
          full_name=cm['name'],
          district=cm['district'],
          party=cm['political_party'] if 'political_party' in cm else None,
          borough=cm['borough']
        )
      print('Finished populating users')

    complaints_json = os.path.join(BASE, "data.json")
    with open(complaints_json) as json_file:
      data = json.load(json_file)
      for complaint in data:
        Complaint.objects.create(
          unique_key = complaint['unique_key'],
          account = complaint['account'],
          opendate = complaint['opendate'].replace('T00:00:00.000',''),
          complaint_type = complaint['complaint_type'] if 'complaint_type' in complaint else None,
          descriptor = complaint['descriptor'] if 'descriptor' in complaint else None,
          zip = complaint['zip'] if 'zip' in complaint else None,
          borough = complaint['borough'] if 'borough' in complaint else None,
          city = complaint['city'] if 'city' in complaint else None,
          council_dist = complaint['council_dist'] if 'council_dist' in complaint else None,
          community_board = complaint['community_board'] if 'community_board' in complaint else None,
          closedate = complaint['closedate'].replace('T00:00:00.000','') if 'closedate' in complaint else None
        )
      print('Finished populating complaints')


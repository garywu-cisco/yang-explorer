"""
Copyright 2017, Cisco Systems, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

@author: Gary Wu
"""

import os
from django.conf import settings
from django.core.management.base import BaseCommand
from explorer.models import User, UserProfile

class Command(BaseCommand):
    help = 'Reload UserProfile with updated CXML files'

    def add_arguments(self, parser):
        parser.add_argument('--user', default='guest',
                help='Reload UserProfiles belonging to this user')

    def handle(self, *args, **options):
        self._reload_cxml(username=options['user'])

    def _reload_cxml(self, username):
        user = User.objects.get(username=username)

        # delete all UserProfiles associated with this user
        user.userprofile_set.all().delete()

        # create new UserProfiles from CXML files
        for f in os.listdir(os.path.join(settings.BASE_DIR, 'data', 'users',
                                         username, 'cxml')):
            f_split = os.path.splitext(f)
            if f_split[1] == '.xml':
                profile = UserProfile(user=user, module=f_split[0])
                profile.save()

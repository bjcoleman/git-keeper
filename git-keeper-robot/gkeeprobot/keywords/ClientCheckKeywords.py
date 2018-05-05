# Copyright 2018 Nathan Sommer and Ben Coleman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from gkeeprobot.control.ClientControl import ClientControl
from gkeepcore.shell_command import CommandError

client_control = ClientControl()


class ClientCheckKeywords:

    def gkeep_add_succeeds(self, faculty, class_name):
        client_control.run(faculty, 'gkeep add {} {}.csv'.format(class_name, class_name))

    def gkeep_add_fails(self, faculty, class_name):
        try:
            client_control.run(faculty, 'gkeep add {} {}.csv'.format(class_name, class_name))
            raise CommandError('gkeep add should have non-zero return')
        except CommandError:
            pass

    def gkeep_modify_succeeds(self, faculty, class_name):
        client_control.run(faculty, 'gkeep modify {} {}.csv'.format(class_name, class_name))

    def gkeep_modify_fails(self, faculty, class_name):
        try:
            client_control.run(faculty, 'gkeep modify {} {}.csv'.format(class_name, class_name))
            raise CommandError('gkeep modify should have non-zero return')
        except CommandError:
            pass

    def gkeep_query_contains(self, faculty, sub_command, *expected_strings):
        results = client_control.run(faculty, 'gkeep query {}'.format(sub_command))
        for expected in expected_strings:
            assert expected in results

    def gkeep_query_does_not_contain(self, faculty, sub_command, *forbidden_strings):
        results = client_control.run(faculty, 'gkeep query {}'.format(sub_command))
        for forbidden in forbidden_strings:
            assert forbidden not in results
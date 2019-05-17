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


*** Settings ***
Resource    resources/setup.robot
Test Setup    Launch Gkeepd With Faculty    washington    adams
Force Tags    gkeep_upload

*** Test Cases ***
Valid Assignment Upload
    [Tags]  happy_path
    Setup Faculty Accounts    washington
    Add To Class    faculty=washington    class_name=cs1    student=kermit
    Add To Class    faculty=washington    class_name=cs1    student=gonzo
    Gkeep Add Succeeds    faculty=washington    class_name=cs1
    Add Assignment  washington  good_simple
    Gkeep Upload Succeeds   washington   cs1    good_simple
    Email Exists  washington    good_simple
    Clone Assignment    washington  washington  cs1  good_simple
    gkeep query contains  washington    assignments  U good_simple

Missing Email
    [Tags]  error
    Setup Faculty Accounts    washington
    Add To Class    faculty=washington    class_name=cs1    student=kermit
    Add To Class    faculty=washington    class_name=cs1    student=gonzo
    Gkeep Add Succeeds    faculty=washington    class_name=cs1
    Add Assignment  washington  missing_email
    Gkeep Upload Fails   washington   cs1    missing_email

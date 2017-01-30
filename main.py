#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
</head>
<body>

"""

class SignupPage(webapp2.RequestHandler):

    def get(self):
        header = "<h1>User Signup</h1>"

        username = """
        <form action="/usrnm" method = "post">
            <label>
                Username
            <input type = "text" name = "user-name"/>
            </label>
        </form>
        """
        page = header + username
        return page




page_footer = """
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(page_header)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/usrnm',SignupPage)
], debug=True)

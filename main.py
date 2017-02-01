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
    <h1>User Signup</h1>
<body>
"""

page_footer = """
</body>
</html>
"""

# form for adding the username,pw,pwverification,email.
user_info = """
    <form action="/" method="post">
        <label>Username
            <input type="text" name="username"/>
        </label>
        <br>

        <label>Password
            <input type="password" name="password"/>
        </label>
        <br>

        <label>Verify Password
            <input type="password" name="verify password"/>
        </label>
        <br>

        <label> Email(optional)
            <input type="text" name="Email"/>
        </label>



    <br>
    <br>
    <input type = "submit" value="Sign Up" />
    </form>
    """


class Index(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(page_header + user_info + page_footer)

    def post(self):

        self.redirect('/welcome')

class Welcome(webapp2.RequestHandler):
    def get(self):

        self.response.out.write("Welcome, %s%s" % (self.request.get('username'), '!'))



app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome',Welcome)
],debug=True)

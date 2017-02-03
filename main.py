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
import re
import cgi



USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)


PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)


EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return  not email or EMAIL_RE.match(email)




page_header = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .error {
            color: red;
        }
    </style>
    <title>User Signup</title>
</head>
    <h1>User Signup</h1>
<body>
"""

page_footer = """
</body>
</html>
"""


def main_page(emailerror='',
               verification='',
               invalidusernm='',
               invpassword='',
               username='',
               email=''):
    user_info = """
    <form action="/" method="post">
      <label>Username
          <input type="text" name="username" value={username}>
      </label>
      <span class="error">{invalidusernm}</span>
      <br>

      <label>Password
        <input type = "password" name="password" />
      </label>
      <span class="error">{invpassword}</span>
      <br>

      <label>Verify Password
        <input type = "password" name="verify" />
      </label>
      <span class="error">{verification}</span>
      <br>

      <label>Email(optional)
        <input type = "text" name="email" value={email}>
      </label>
      <span class="error">{emailerror}</span>
      <br>
      <input type="submit" value="Sign Up"/>

    </form>


    """.format(emailerror = emailerror,
               verification = verification,
               invalidusernm = invalidusernm,
               invpassword = invpassword,
               username=username,
               email=email)

    return user_info



class Index(webapp2.RequestHandler):
    def get(self):
        self.response.write(page_header + main_page() + page_footer)



    def post(self):
        success = True
        username = cgi.escape(self.request.get('username'))
        password = cgi.escape(self.request.get("password"))
        verify = cgi.escape(self.request.get("verify"))
        email = cgi.escape(self.request.get("email"))



        if valid_email(email):
            emailerror = ''
        else:
            emailerror = 'Invalid Email'
            success = False

        if valid_username(username):
            usn_error = ''
        else:
            usn_error = 'Invalid username.'
            success = False

        if valid_password(password):
            pwerror = ''
        else:
            pwerror = 'Invalid password'
            success = False

        if password != verify:
            ver_error="Passwords do not match."
            success = False
        else:
            ver_error = ''


        if success:

            self.redirect('/welcome?username={}'.format(username))
        else:
            self.response.write(page_header + main_page(
                emailerror=emailerror,
               verification=ver_error,
               invalidusernm=usn_error,
               invpassword=pwerror,
               username = username,
               email = email) + page_footer )




class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")

        self.response.write("Welcome, " + username + "!")





app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
],debug=True)

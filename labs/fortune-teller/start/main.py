#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
import jinja2
import os
import random


def get_fortune(astrological_sign):
    fortune_list = [
        'you will trip on something',
        'you will have a pretty good day',
        'you will find something as long as you\'re careful',
        'you will have a grumpy stomach',
        'you will find your long lost brother that you never knew about',
        'you will suffer from a cancerous meme you found. Ha, get it?',
        'you will stink for the day',
        'wait, virgo is a thing?',
        'you shall do the right thing today.',
        'a bee may sting you',
        'what the heck is a sagittarius?',
        'you will stub your toe',
    ]
    return random.choice(fortune_list)


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_directory.get_template('templates/fortune-start.html')
        self.response.write(start_template.render())
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
    def post(self):
        user_astrological_sign = self.request.get('user_astrological_sign')
        template_vars = {
            'astrological_sign': user_astrological_sign.capitalize(),
            'fortune': get_fortune(user_astrological_sign),
        }
        end_template = jinja_current_directory.get_template('templates/fortune-results.html')
        self.response.write(end_template.render(template_vars))

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

class GoodByeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('My response is Good Bye World.')

#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler), #maps '/predict' to the FortuneHandler
    ('/farewell', GoodByeHandler),
], debug=True)

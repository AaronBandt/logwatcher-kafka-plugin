#  Copyright 2015 CityGrid Media, LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGELOG.rst')) as f:
    CHANGELOG = f.read()

requires = [
    'LogWatcher',
    'kafka-python==0.9.4',
    ]

setup(name='logwatcher-kafka-plugin',
      version='1.0',
      description='LogWatcher Plugin for Sending log lines to a Kafka Topic',
      long_description=README + '\n\n' + CHANGELOG,
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: System Administrators ",
        ],
      author='Wil Heitritter',
      author_email='no-reply@noreply.com',
      url='',
      license='Apache',
      keywords='Logs Metrics Access Apache Ganglia Graphite devops Kafka Logstash',
      packages=['kafka_logger'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="logwatcher-kafka-plugin",
      )

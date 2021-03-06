# encoding: utf-8
#
# Copyright 2016 Cluster Labs, Inc.
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

from django import template
from django.utils.safestring import mark_safe

import json
import math

register = template.Library()

@register.filter(name='stars')
def stars(data):
  # TODO(Taylor): Deal with half stars.
  return mark_safe(u'<span style="color:orange">%s</span><span style="color:gray">%s</span>' % (
    u'★★★★★'[:int(data or 5)],
    u'★★★★★'[:int(math.ceil(5 - (data or 5)))],
  ))

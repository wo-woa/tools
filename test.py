# -*- coding: utf-8 -*-

import json

dic = '{"rs":1,"errcode":""}'
print(type(json.loads(dic)))
js = json.dumps(json.loads(dic), sort_keys=True, indent=4)
print(js)
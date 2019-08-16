#!/usr/bin/python
#str = "this is string example....wow!!!"
str = 'irs01.com/irt?_imt_id=oROptOEV3VF5ZG0vR1XrMQA&_iwt_UA=ua-youku-130001&_t='
print 'str:%s' %(str)
print "Encoded String(base64): " + str.encode('base64','strict')
print "Encoded String(utf-8): "  + str.decode('utf-8', 'ignore')

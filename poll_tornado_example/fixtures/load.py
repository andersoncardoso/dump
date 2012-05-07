# TODO this is all wrong now
#import sys, os
#PROJECT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
#sys.path.append(PROJECT)
#
#from models.models import Poll, Choice
#from mongoengine import connect
#
#connect('poll')
#
#p = Poll(question='This works?')
#p.save()
#
#c1 = Choice(poll=p, choice='yep')
#c1.save()
#
#c2 = Choice(poll=p, choice='maybe')
#c2.save()
#
#c3 = Choice(poll=p, choice='noo')
#c3.save()
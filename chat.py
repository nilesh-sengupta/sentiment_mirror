# -*- coding: utf-8 -*-
#Author Nilesh Sengupta
import random
from textblob import TextBlob
print('Hey there I am vision , What is your name ?' )
name = input()
print('Do you have nickname?')
ans = input()
if 'y' in ans.lower():
  nickname = input('what is your nickname: ')
  print('That is one cool nickname ' + nickname)
else:
  nickname = name[0:4]
  print('I will call you '+nickname +' then')
greetings = [
	'How are you doing today ' + nickname +'?',
	'Howdy ' + nickname + ' Whats up?(hint: Its not your ceiling',
	"What's up " + nickname +'?',
	'Greetings ' + nickname +', are you well?',
	'So, how are things today ' + nickname +'?'
]
print(random.choice(greetings))
ans = input()
blob = TextBlob(ans)

if blob.polarity > 0:
  print('That is cool')
else:
  print('Sorry to hear that buddy')
topics = [
	'coding',
	'python the programming language (PS : I am written in python *wink*)',
	'IPL',
	'the night sky',
	'Billie Eilish',
	'minecraft',
	'pewdipie'
]

questions = [
	'What is your take on ',
	'What do you think about ',
	'How do you feel about ',
	'What do you reckon about ',
	'I would like your opinion on '
]
for i in range(0, random.randint(3,4)):
  question = random.choice(questions)
  questions.remove(question)
  topic = random.choice(topics)
  topics.remove(topic)
  print(question + topic + '?')
  ans = input()
  blob = TextBlob(ans)
  if blob.polarity > 0.5:
    print('Really??? I love '+ topic +' too')
  elif blob.polarity > 0.1:
    print('We are a lot same I like '+ topic +' too')
  elif blob.polarity < -0.5:
    print('Ah I hate '+ topic +' too')
  elif blob.polarity < -0.5:
    print('I do not like '+ topic +'  too you know')
  else:
    print('You are very neutral on '+ topic)
  
  if blob.subjectivity > 0.6:
    print('and you are very biased on'+ topic)
  elif blob.subjectivity > 0.3:
    print('and you are  biased to an extent')
  else:
    print('and you are quite objective , I like that')
goodbyes = [
	'It was good talking to you ' + nickname + 'I will leave now',
	'OK I am bored, tell me something interesting next time',
	'Bye bye , will talk with you later',
	'got something urgent....raincheck ?',
	'will catch up with ya later '+ nickname
]
print(random.choice(goodbyes))
#!/usr/bin/python
import datetime
#Amazon aws time zone is EDT (NewYork) 
due = datetime.datetime(2014, 10, 10, 12, 0, 0, 0)
allow_upload = due > datetime.datetime.now()
rest_time=due-datetime.datetime.now()
prefix='hw1'

print("Content-type: text/html")
print
#import cgitb
#cgitb.enable()

print '''
<!DOCTYPE html>
<html>
<head>'''
print '<title>DS '+prefix+'</title>'
print '''
<meta charset="UTF-8">
<link href="Site.css" rel="stylesheet">
</head>
<body>
<nav id="nav01"></nav>

<div id="main">'''
if allow_upload:
  print '<h1>Upload your code: '+prefix+'</h1>'
  print '<h3>Rest time:'+str(rest_time)+'</h3>'
  print '<h3>Note: You do not permit uploads of your code within 10 mins.</h3>'
  print '<form enctype="multipart/form-data" method="post" action="cgi-bin/submit.cgi">'
  print 'Your Account(i.e. ds001):'
  print '<input type="text" name="user"><br>'
  print 'Your token:'
  print '<input type="text" name="token"><br>'
  print 'Upload header file:'
  print '<input type="file" name="hpp" value="Choose file" accept=".h"><br>'
  print 'Upload source file:'
  print '<input type="file" name="cpp" value="Choose file" accept=".cpp"><br>'
  print '<input type="hidden" value="'+prefix+'">'
  print '<input type="submit" value="upload_both">'
  print '</form>'
else:
  print "<h1>It's not allowed uploading homework now.</h1>"
print '''
  <footer id="foot01"></footer>
</div>
<script src="Script.js"></script>
</body>
</html>'''

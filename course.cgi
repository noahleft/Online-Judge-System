#!/usr/bin/python
# -*- coding: UTF-8 -*-

homework=[('Honor code','docs/Honor code.docx'),
          ('Account','docs/account.pdf'),
          ('Intro','docs/DS_intro.pdf'),
          ('HW#1','docs/DS_hw1.rar')]
lecture=[('Lecture 0','docs/lec0.pptx'),
         ('Lecture 1','docs/lec1.pptx'),
         ('Lecture 2','docs/lec2.pptx')]

print("Content-type: text/html")
print

print '''
<!DOCTYPE html>
<html>
<head>
<title>2014 Fall NCTUEE Data Structure</title>
<meta charset="UTF-8">
<link href="Site.css" rel="stylesheet">
</head>
<body>

<nav id="nav01"></nav>

<div id="main">
<h1>Course Material</h1>'''
print '<h3>Homework</h3>'
print '<table>'
for item in homework:
  print '<tr><td><a href="'+item[1]+'" download target="_blank">'+item[0]+'</a></td></tr>'
print '</table>'

print '<h3>Course Lecture:</h3>'
print '<table>'
for item in lecture:
  print '<tr><td><a href="'+item[1]+'" download target="_blank">'+item[0]+'</a></td></tr>'
print '</table>'

print '''
<div id="id01"></div>
<footer id="foot01"></footer>
</div>

<script src="Script.js"></script>

</body>
</html>'''

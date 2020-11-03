#!/usr/bin/python3
"""Create attachment for the email to send"""
import os
import reports
import emails
from datetime import date

if __name__ == '__main__':
  attachment = '/tmp/processed.pdf'
  title = 'Processed Update on {}'.format(date.today())
  paragraph = ''
  for item in os.listdir('supplier-data/descriptions'):
    if item.endswith('.txt'):
      with open('supplier-data/descriptions/{}'.format(item)) as f:
        info = f.read().split('\n')
        name = info[0]
        weight = info[1]
        paragraph += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
  reports.generate_report(attachment, title, paragraph)
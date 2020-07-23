import requests
import json
import sys


def banner():
    print('''
                           .____
                          /           |   |
                          |__.        `.__|
                          |               |
                          /----/          |
   .____                                              .    .    ___/
  /      , __   ,   . , _ , _     ___  .___    ___  _/_   /|  .'  /\ , __
  |__.   |'  `. |   | |' `|' `. .'   ` /   \  /   `  |     |  |  / | |'  `.
  |      |    | |   | |   |   | |----' |   ' |    |  |     |  |,'  | |    |
  /----/ /    | `._/| /   '   / `.___, /     `.__/|  \__/ _|_ /`---' /    |\n\n''')

    



banner()

domain = str(input('Enter domain name : '))
output = str(input('Enter output filename : '))


def writeintofile(content):
    file = open(output,"a")
    file.write(content)
    file.close()


url = 'https://public.intelx.io/phonebook/search?k=d7d1ed06-f0c5-49d4-a9ca-a167e6d2ffab'
post_data = '{"term":"'+domain+'","maxresults":10000,"media":0,"target":2,"terminate":[null],"timeout":20}'

res = requests.post(url, data=post_data)
res = res.content.decode("utf-8") 
res = json.loads(res)


url = 'https://public.intelx.io/phonebook/search/result?k=d7d1ed06-f0c5-49d4-a9ca-a167e6d2ffab&id='+str(res['id'])

res = requests.get(url)
res = res.content.decode("utf-8")
res = json.loads(res)


if(len(res['selectors']) == 0):
    print('\nNo emails found associated with '+domain)
    sys.exit()


print('')

for i in range(0, len(res['selectors'])):
    print(res['selectors'][i]['selectorvalue'])
    writeintofile(res['selectors'][i]['selectorvalue']+'\n')

print('\nTotal number of emails found : '+str(i+1))

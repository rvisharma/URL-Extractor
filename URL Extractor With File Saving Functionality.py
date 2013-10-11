'''
This program is an URL extracter which extracts the clickable links
from the url which is asked by the user.

Precondition:
1 - valid urls are those which starts which has ahref and http:// tags
2 - Only urls that are in the body of the page are extracted

Created By - Ravi R. Sharma
'''

import urllib.request
import tkinter.filedialog

# return the url_list from body_text
# where each item in a list is a url string
def get_url_list(url_count, body_text):

    # get the index number of starting of url with '"'
    # and ends with '"' right after first occurence of '"'
    first_quote_index = 0
    last_quote_index = 0

    # extract the urls from string body_text for url_count times.
    for num in range(url_count):
        
           # figures out the index of url starting and ending quote('"')
           first_quote_index = body_text.index('"http://', last_quote_index)
           last_quote_index = body_text.index('"', first_quote_index + 1)

           # append the url string to url_list
           url_list.append(body_text[first_quote_index+1:last_quote_index])
    
    return url_list

# prints out the url list
def print_url_list():
    num = 0
    for url in url_list:
        print(str(num+1) + ' : ' + url)
        num += 1

# returns the body_text from page_as_strings
def get_body_text(page_as_string):
    body_start_index = 0
    body_end_index = 0
    
    if ('<body' and '</body>') in page_as_string:
        body_start_index = page_as_string.index('<body')
        body_end_index = page_as_string.index('</body>')

    body_text = page_as_string[body_start_index : body_end_index]

    return body_text

# Write the url list in a file prompted to user.
def write_to_file(url_count, user_url):
    print('Saving to File...')
    save_file_name = 'links.txt'
    save_file = open(save_file_name, 'w')
    save_file.write('There are ' + str(url_count) + ' Clickable links in ' + user_url + '\n\n')
    
    num = 0
    for url in url_list:
        save_file.write(str(num+1) + ' : ' + url)
        save_file.write('\n')
        num += 1
    save_file.close()
    print('\nFile saved links.txt in the same folder as of source code')

    return input('\nPress Enter to Exit')
        
    
        
    

####################################
#      PROGRAM STARTS FROM HERE     #
####################################

# Input the address by asking the user
user_url = input('Enter the URL: ')
if not user_url.startswith('http://'):
    user_url = 'http://' + user_url
    

# Open the user_url and store it in the_page as bytes
the_page = urllib.request.urlopen(user_url)

# Read from the the_page convert it from bytes to string type
page_as_string = the_page.read().decode('utf8')

# extract the body out of the_page and store it in body_text
body_text = ''
body_text = get_body_text(page_as_string)

# Precondition #
# http:// url starts with this string
url_starter = '<a href="http://'

# count the number of urls to be extracted inside body_text
url_count = body_text.count(url_starter)

# url list where all the links will be appended
url_list = []

# Tell the user that there are url_count number of clickable links
if url_starter in body_text:
    print('There are ' + str(url_count) + ' Clickable links in ' + user_url)
    get_url_list(url_count, body_text)
    print('\n')
    
    # prints the url list in console
    print_url_list()

    # ask for saving url list into a file
    file_save = input('\nDo you want to save the list into a file? (Y/N) :  ')
    if file_save.lower() == 'y':
        write_to_file(url_count, user_url)
        
    else:
        # exit out of the program
        pass

else:
    print("There are no clickable links in this page")

import sys
import requests
from bs4 import BeautifulSoup

def follow_path(word):
    try:
        roads_to_philosophy=[]
        word2=word.replace(' ','_')
        wiki_page=(requests.get('https://en.wikipedia.org/wiki/'+word2)).text
        page_name=''

        #Let's start browsing!
        while page_name!='Philosophy':

            soup=BeautifulSoup(wiki_page, features='html.parser')
            title=soup.select('h1[id="firstHeading"]')
            page_name=title[0].getText()
            print(page_name)

            #adding redirected path
            if len(soup.select('span[class="mw-redirectedfrom"]'))>0:
                redirection_link=soup.select('a[class=mw-redirect]')[0]
                redirected_from=redirection_link.get('title')
                roads_to_philosophy.append(redirected_from)

            #adding article name to the path
            roads_to_philosophy.append(page_name)

            found_link=False
            paragraph_number=0
            next_article=''
            next_article_link=''

            #browsing through paragraphs for the first link
            while found_link==False:
                paragraph=soup.select('div[class="mw-parser-output"] > p')[paragraph_number]

                #if there are links to wiki in the paragraph
                if len(paragraph.select('a[href*="wiki"]'))>0:
                    links_to_wiki=paragraph.select('a[href*="wiki"]')

                    #finding a link not leading to Help
                    for link in links_to_wiki:
                        if 'Help:' not in link.get('title'):
                            next_article=link.get('title')
                            next_article_link='https://en.wikipedia.org/'+link.get('href')
                            found_link=True
                            break

                paragraph_number+=1

                if paragraph_number==len(soup.select('div[class="mw-parser-output"] > p'))-1:
                    print ("It leads to a dead end!")
                    return #escaping the While loop

            if next_article in roads_to_philosophy:
                print ("It leads to an infinite loop!")
                return #escaping the while loop

            wiki_page=(requests.get(next_article_link)).text

        print("{} roads from {} to philosophy".format(len(roads_to_philosophy),word))

    except:
        print ("Unexpected error.")
        return




if __name__=='__main__':
    follow_path(sys.argv[1])

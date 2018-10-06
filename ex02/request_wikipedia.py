import sys
import dewiki
import requests
import json

def request(word):

    if len(sys.argv)!=2:
        print('Enter one string to search!')
        return
    if type(sys.argv[1])!=str:
        print('Wrong argument type!')
        return

    try:
        api_search='https://en.wikipedia.org/w/api.php?action=opensearch&search='+word
        wiki_search=requests.get(api_search)
        page_search=wiki_search.json()
        article_name=page_search[1][0]
        api_parse='https://en.wikipedia.org/w/api.php?action=parse&page='+article_name+'&prop=wikitext&format=json&contentmodel=wikitext'
        article_content=(requests.get(api_parse)).json()
        content=article_content['parse']['wikitext']['*']
        content=dewiki.from_string(content)

        word=word.replace(' ','_')
        article_file=open(word+'.wiki','w+')
        article_file.write(content)
    except:
        print('Something went wrong during the search.')
        return



if __name__=="__main__":
    request(sys.argv[1])

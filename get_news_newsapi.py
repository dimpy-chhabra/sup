from newsapi import NewsApiClient

def switch_demo(argument):
    if argument == "cnn":
      return 1
    elif argument == "cnbc":
        return 2
    elif argument == "the-new-york-times":
        return 3
    elif argument == "usa-today":
        return 4
    elif argument == "fox-news":
        return 5
    elif argument == "buzzfeed":
        return 6    
    else:
        return -1


api = NewsApiClient(api_key='API_KEY')
pageNumber = 1
srcs = "usa-today,cnn,buzzfeed,fox-news,the-new-york-times,cnbc"
query = "facebook-cambridge-analytica"


while(1):
  top_headlines = api.get_everything(q=query,
  											sources=srcs,
                                            language='en',
                                            page=pageNumber)
  '''
  # /v2/top-headlines
  top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                            sources='bbc-news,the-verge',
                                            category='business',
                                            language='en',
                                            country='us')

  # /v2/everything
  all_articles = newsapi.get_everything(q='bitcoin',
                                        sources='bbc-news,the-verge',
                                        domains='bbc.co.uk,techcrunch.com',
                                        from_parameter='2017-12-01',
                                        to='2017-12-12',
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)

  # /v2/sources
  sources = newsapi.get_sources()
  '''


  mydict = {}
  mydict = top_headlines


  import csv
  from textblob import TextBlob
  import sys
  reload(sys)
  sys.setdefaultencoding('utf8')


  mylist = (mydict['articles'])

  #for x in mylist:
    #print x['description']
    #print x['source']['id']

  #ser is a serial number to keep track 
  if int(pageNumber)==1:
    ser = 1
  else:
    ser = (int(pageNumber)-1)*20 + 1

  with open('data_news_'+query+'.csv', 'a+') as csv_file:
      first = csv_file.read(1)
      writer = csv.writer(csv_file)
      if not first:
        #print('friendsfile is empty')
        writer.writerow(["sno", "description","title","author","publishedAt","source_name", "desc_subjectivity", "desc_polarity","titl_subjectivity", "titl_polarity"])

      
      
      for x in mylist:
        a = ser
        b = x['description']
        c = x['title']
        d = x['author']
        e = x['publishedAt']
        f = x['source']['name']
        g = TextBlob(b)
        h = TextBlob(c)
        i = g.sentiment.subjectivity
        j = g.sentiment.polarity
        k = h.sentiment.subjectivity
        l = h.sentiment.polarity
        m = switch_demo(x['source']['id'])

        #usa-today,cnn,buzzfeed,fox-news,the-new-york-times,cnbc
        
        writer.writerow([ a, b, c, d, e, m , i, j, k,l])
        ser = ser + 1
 
  print("News Items downloaded... "+str(20*(int(pageNumber))))
  pageNumber = pageNumber + 1     
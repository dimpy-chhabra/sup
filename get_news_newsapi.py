from newsapi import NewsApiClient

api = NewsApiClient(api_key='be461bf3d0514b2f8777d71f3df6a18a')
pageNumber = 1
srcs = "cnn,fox-news"
query = "Trump"
#-cambridge-analytica-havoc-data-privacy-security


while(1):
  top_headlines = api.get_everything(q=query, sources=srcs, language='en', page=pageNumber)
  
  mydict = {}
  mydict = top_headlines


  import csv
  from textblob import TextBlob
  import sys
  reload(sys)
  sys.setdefaultencoding('utf8')


  mylist = (mydict['articles'])

  if int(pageNumber)==1:
    ser = 1
  else:
    ser = (int(pageNumber)-1)*20 + 1

  with open('data_news_'+query+'.csv', 'a+') as csv_file:
      first = csv_file.read(1)
      writer = csv.writer(csv_file)
      if not first:
        #print('friendsfile is empty')
        writer.writerow(["sno", "description","title","author","source","publishedAt","desc_subjectivity", "desc_polarity","titl_subjectivity", "titl_polarity"])

      for x in mylist:
        a = ser
        b = x['description']
        c = x['title']
        d = x['author']
        e = x['publishedAt']
        g = TextBlob(b)
        h = TextBlob(c)
        i = g.sentiment.subjectivity
        j = g.sentiment.polarity
        k = h.sentiment.subjectivity
        l = h.sentiment.polarity
        m = x['source']['id']

        #usa-today,cnn,buzzfeed,fox-news,the-new-york-times,cnbc
        
        writer.writerow([ a, b, c, d, e ,m, i, j, k,l])
        ser = ser + 1
 
  print("News Items downloaded... "+str(20*(int(pageNumber))))
  pageNumber = pageNumber + 1     
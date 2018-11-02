from twitter_scraper_helmi import get_tweets

data = []
error = 0
for t in get_tweets('gojekindonesia', pages=1):
    data.append(t)
    if (t['status'] != 'ok'):
        error += 1
    
print('tweet found: ', len(data))
print('error: ', error)

for i, t in enumerate(data):
    print(t['tweet']['text'], '\n')
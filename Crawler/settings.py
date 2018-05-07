USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
FEED_FORMAT = 'json'
FEED_URI = './myfile.txt'
FEED_EXPORT_ENCODING = 'utf-8'

ITEM_PIPELINES = {'newscrawling.pipelines.MongoDBPipeline': 300, }

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "skilled_industry"
MONGODB_COLLECTION = "companies"

from elasticsearch import Elasticsearch
from time import time
from config import index_settings, doc_mapping

es = Elasticsearch('localhost:9200')

index_name='books'
doc_type='search'
body = {}
mapping = {}
mapping[doc_type] = doc_mapping
body['settings'] = index_settings
body['mappings'] = mapping

#####Create index###
# if not es.indices.exists(index = index_name):
#     print ('index does not exist, creating the index')
#     es.indices.create(index = index_name, body = body)
#     #time.sleep(2)
#     print ('index created successfully')
# else:
#     print ('An index with this name already exists')

##### Delete index #####
# es.indices.delete(index = index_name)

#example docs:
doc2 = {
'name' : 'My Elasticsearch Essentials',
'category' : ['Big Data', 'search engines', 'Analytics'],
'Publication' : 'Packt-Pub',
'Publishing Date' : '2015-31-12'
}

##### Insert records#####
es.index(index = index_name, doc_type = doc_type, body = doc2, id = 'NONE')
# es.index(index = index_name, doc_type = doc_type, body = doc1, id = '2')

##### Delete resorcd ####
#es.delete(index=index_name, doc_type=doc_type, id='1', ignore=404)


##### Retrive records and values####
# response = es.get(index=index_name, doc_type=doc_type, id='1', ignore=404)
# print (response)   ###the full record
# category_values = response.get('_source').get('category')     ####the field you want from a record
# print(category_values)

#### Queries #####
query = {
     "query": {
        "match_all": {}
     },
   }

response = es.search(index=index_name, doc_type=doc_type, body=query, size=2, request_timeout=20)
print (response)
# for hit in response['hits']['hits']:
#     print (hit.get('_source'))

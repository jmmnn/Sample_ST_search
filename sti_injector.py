from elasticsearch import Elasticsearch
from time import time
from config import index_settings, doc_mapping
import json
import randomDocs as rd

es = Elasticsearch('localhost:9200')

index_name='sti_search'
doc_type='site'
body = {}
mapping = {}
mapping[doc_type] = doc_mapping
body['settings'] = index_settings
body['mappings'] = mapping

# ###Create index###
if not es.indices.exists(index = index_name):
    print ('index does not exist, creating the index')
    es.indices.create(index = index_name, body = body)
    #time.sleep(2)
    print ('index created successfully')
else:
    print ('An index with this name already exists')
#
# # #### Delete index #####
#es.indices.delete(index = index_name)
# es.indices.delete(index = 'sti_search_test')


#Invoke generatkon of random docs
howMany = 3257    #enter here the number of random documents to index into elasticsearch
for i in range(howMany):
    es.index(index = index_name, doc_type = doc_type, body = rd.randomDoc(), id = i)
    print (i)

# ##### Insert records#####
# es.index(index = index_name, doc_type = doc_type, body = doc2, id = 'NONE')
# es.index(index = index_name, doc_type = doc_type, body = page1, id = '1')
# es.index(index = index_name, doc_type = doc_type, body = page2, id = '2')
#es.index(index = index_name, doc_type = doc_type, body = doc4, id = '4')
##### Delete resorcd ####
# es.delete(index=index_name, doc_type=doc_type, id='1', ignore=404)


##### Retrive records and values####
#response = es.get(index=index_name, doc_type=doc_type, id='1', ignore=404)
#response = es.get(index=index_name, doc_type=doc_type, id='12', ignore=404)
#print (response)   ###the full record
# category_values = response.get('_source').get('category')     ####the field you want from a record
# print(category_values)

#### Queries #####
# query = {
#      "query": {
#         "match_all": {}
#      },
#    }
#
# response = es.search(index=index_name, doc_type=doc_type, body=query, size=2, request_timeout=20)
# # print (response)
# for hit in response['hits']['hits']:
#     print (hit.get('_source'))

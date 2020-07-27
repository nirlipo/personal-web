from scholarly import scholarly
from fp.fp import FreeProxy

import time
import random
import json
import os.path
from os import path

#proxy = FreeProxy(rand=True, timeout=1, country_id=['US', 'CA']).get()  
#scholarly.use_proxy(http=proxy, https=proxy)
authoName = 'Nir Lipovetzky'

# if path.exists(f'{authoName}.json') :
#     f = open(f'{authoName}.json')
#     author = json.load(f)
# else:

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author(authoName)
author = next(search_query).fill()

# with open(f'{authoName}.json', 'w') as f:
#     f.write(str(author))
#     f.close()

#Wait before launching next query
time.sleep(random.uniform(30, 60.0)) #from 5 to 30 seconds

print(author)


biblio = ""
test = 0
for pub in author.publications:
    title = f"{pub.bib['title']}"
    print( f"--> Fetching {title}..." )
    try:
        bib_query = scholarly.search_pubs( title )
        pub_full = (next(bib_query))
        full_info = pub_full.bibtex
        biblio = f"{biblio} \n\n {full_info}"
        print(biblio)
    except Exception as e:
        print(e)
    time.sleep(random.uniform(30, 65.0)) #from 5 to 30 seconds
    

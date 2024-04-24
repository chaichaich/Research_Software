import requests  

def get_abstract(key): 
    url = "https://api.openalex.org/works" 
    param = {"Filter" : f"abstract.search:{key}"}
    response = requests.get(url, params=param) 
    response.raise_for_status() 
    data = response.json()
    return data

def test_abstract(work_id): 
    url = f"https://api.openalex.org/works/{work_id}" 
    response = requests.get(url) 
    data = response.json()
    print(data)
    abstract = data.get("abstract")
    return abstract



#test_abstract('S4306402226')



def search(key): #Search for openalex ids with a given key ensuring that   
    #the works have a abstract and are open access 
    formatted_key = '+'.join(key.split(' '))
    url = f'https://api.openalex.org/works?search={key}&filter=publication_year:{2013}\
        ,has_abstract:true,open_access.is_oa:true'
    response = requests.get(url)
    data = response.json()

    sort_results = sorted(data, key=lambda x:x.get('cited_by_count',0), reverse=True)
    return sort_results[:5]

print(search('Water Distribution Network'))
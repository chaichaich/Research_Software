from.utils import *
def get_suggestions(key,year): 
    '''Takes in a search and a year and returns the top 3 relevant pubications.'''
    search_results = search(key,year) 
    sorted_search_results = sort(search_results) 
    top_3 = sorted_search_results[:3] 
    work_ids = [] 
    for key in top_3.keys(): 
        work_ids.append(key[21:])

    for id in work_ids: 
        abstract = get_abstract(id) 
        keyword_rank = text_rank(abstract) 
        newKey = ' '.join(keyword_rank)
    
    suggested_search = search(newKey,year) 
    sorted_suggested_search = sort(suggested_search)
    suggested_top_3 = sorted_suggested_search[:3] 

    return suggested_top_3


        

        

    
    



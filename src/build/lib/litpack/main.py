from.utils import *
import networkx as nx
import requests
import click
def get_suggestions(key,year): 
    '''Takes in a search and a year and returns the top 3 relevant pubications.'''
    search_results = search(key,year) 
    sorted_search_results = sort(search_results) 

    top_3 = dict(list(sorted_search_results.items())[:3])
    work_ids = [] 
    for key in top_3.keys(): 
        work_ids.append(key[21:])

    for id in work_ids: 
        abstract = get_abstract(id) 
        keyword_rank = text_rank(abstract) 
        newKey = ' '.join(keyword_rank)
    
    suggested_search = search(newKey,year) 
    sorted_suggested_search = sort(suggested_search)
    suggested_top_3 = dict(list(sorted_suggested_search.items())[:3])

    output = []
    for key in suggested_top_3.keys():
        output.append(key)
    return suggested_top_3

@click.command(help ='OpenAlexInstitutions') 
@click.argument('key', nargs=-1) 
@click.argument('year', nargs=1)

def main(key,year): 
    print('Some useful articles to look at are', get_suggestions(key,year))

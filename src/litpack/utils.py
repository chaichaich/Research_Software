import networkx as nx
import requests

def get_abstract(id): 
    '''Returns the inverted_abstract_index'''
    url = f'https://api.openalex.org/works/{id}'
    print(url)
    response = requests.get(url)
    data = response.json()
    return data['abstract_inverted_index']

def search(key,year): 
    '''Takes in a search and a year and returns relevant pubications.'''
    formatted_key = '+'.join(key.split(' '))
    base = "https://api.openalex.org/works?"
    search_param = f'search={formatted_key}'
    filter_param = f'filter=has_abstract:true,open_access.is_oa:true'
    url = f'{base}{search_param}&{filter_param}&filter=publication_year{year}'
    response = requests.get(url)
    data = response.json()
    output = {} 
    for result in data['results']: 
        output[result['id']] = result['cited_by_count']
    return output

def sort(myDict): 
    '''Takes in a dictionary and returns a sorted dictionary.'''
    sorted_dict = dict(sorted(myDict.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict

def text_rank(abstract): 
    '''
    Ranks the words in an abstract using the TextRank algorithm.
    Adapted from https://medium.com/analytics-vidhya/sentence-extraction-using-textrank-algorithm-7f5c8fd568cd.
    '''
    max_words = 0
    for term, position in abstract.items(): 
        for i in position: 
            if i >= max_words: 
                max_words = i 

    stop_words = [
    "a", "about", "after", "all", "also", "always", "am", "an", "and", "any", "are", "at", "be", "been", 
    "being", "but", "by", "came", "can", "cant", "come", "could", "did", "didn't", "do", "does", "doesn't", 
    "doing", "don't", "else", "for", "from", "get", "give", "goes", "going", "had", "happen", "has", "have", 
    "having", "how", "i", "if", "ill", "i'm", "in", "into", "is", "isn't", "it", "its", "i've", "just", "keep", 
    "let", "like", "made", "make", "many", "may", "me", "mean", "more", "most", "much", "no", "not", "now", 
    "of", "only", "or", "our", "really", "say", "see", "some", "something", "take", "tell", "than", "that", 
    "the","The", "their", "them", "then", "they", "thing", "this", "to", "try", "up", "us", "use", "used", "uses", 
    "very", "want", "was", "way", "we", "what", "when", "where", "which", "who", "why", "will", "with", 
    "without", "wont", "you", "your", "youre",'the','on'
]
    
    ls = [0]*(max_words+1) 
    for term, position in abstract.items():
        for i in position:
            ls[i] = term
    #Remove stop words 

    ls = [word for word in ls if word not in stop_words]
    window = 4
    graph = {} 
    for i, token in enumerate(ls): 
        for j in range(max(0, i-window), min(len(ls), i+window+1)):
            if i!= j: 
                neighbor_token = ls[j] 
                if token not in graph: 
                    graph[token] = {} 
                if neighbor_token not in graph[token]:
                    graph[token][neighbor_token] = 1
                else: 
                    graph[token][neighbor_token] += 1
            
    pagerank = nx.pagerank(nx.Graph(graph))
    return sorted(pagerank, key=pagerank.get, reverse=True)

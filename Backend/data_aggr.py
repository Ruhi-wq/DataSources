import pandas as pd
import pymedx as PM1

# w-flow: utility section
def pmc_art_process(art):
    """
    takes in article and returns the dict 
    """
    return {
        "id": art.pmc_id,
        "abstract": art.abstract,
        "title": art.title,
        "doi": art.doi,
        "author": art.authors,
    }
    
def pm_art_process(art):
    """
    takes in article and returns the dict 
    """
    return {
        "abstract": art.abstract,
        "title": art.title,
        "doi": art.doi,
        "author": art.authors,
    }
    



# w-flow: Collection of different sources
def get_pubmedcen_ids(query, max_results=100):
    """
    Inputs a query and max_results
    returns a dataframe with the id, abstract and title
    """
    # Done: needed to return authors, abstract, title and doi

    obj = PM1.PubMedCentral()
    results = obj.query(query, max_results=max_results)
    art_dat = list (map(pmc_art_process, results))
    article_df = pd.DataFrame(art_dat)
    pfix = "https://pmc.ncbi.nlm.nih.gov/articles/PMC"
    article_df["url"] = pfix+ article_df["id"] + "/"
    return article_df
def get_pubmed_ids(query, max_results=100):
    """
    Inputs a query and max_results
    returns a dataframe with the id, abstract and title
    """
    obj = PM1.PubMed()
    results = obj.query(query,max_results=max_results)
    art_dat = list (map(pm_art_process, results))
    article_df = pd.DataFrame(art_dat)
    return article_df


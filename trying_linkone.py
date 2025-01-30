import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10933766/'
}
res = requests.get("https://pmc.ncbi.nlm.nih.gov/articles/PMC10933766/pdf/",headers=headers, allow_redirects=True)
print(res.status_code)

with open("PMC10933766.pdf", "wb") as f:
    f.write(res.content)
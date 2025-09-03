from aur import rpc

def _display_search_result(result):
    print(f'aur/{result["Name"]} {result["Name"]}')
    print(f'{result["Description"]}')

def run(term: str):
    data = rpc.search(term)
    count = data['resultcount']
    print(f'Got {count} results.')

    if count > 0:
        for result in data['results']:
            _display_search_result(result)
    else:
        print('Maybe try another keyword?')
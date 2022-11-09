import requests
import sys
import json
import dewiki


def request_wikipedia(page: str):
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
        "action": "parse",
        "page": page,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }

    try:
        r = requests.get(url=url, params=params)
        r.raise_for_status()
    except requests.HTTPError as exc:
        raise exc

    try:
        page_content = json.loads(r.text)
    except json.decoder.JSONDecodeError as exc:
        raise exc

    if page_content.get("error"):
        raise Exception(page_content["error"]["info"])
    return dewiki.from_string(page_content["parse"]["wikitext"]["*"])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit('Wrong amounts of args')
    try:
        req_wiki = request_wikipedia(sys.argv[1])
    except Exception as e:
        exit(e)
    try:
        with open('{name}.wiki'.format(name=sys.argv[1]), "w", encoding="utf-8") as f:
            f.write(req_wiki)
            f.close
    except Exception as e:
        exit(e)

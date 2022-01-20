## Usage
```bash
docker pull vladimiryeghiazaryan/smart-scraper
```
On execution map any directory of your choice to the `/scrape` folder and put your `request.json` parameters in that folder.
```bash
docker run -v <path/to/your/scraper/dir>:/scrape vladimiryeghiazaryan/smart-scraper
```
## **Examples:**
Request sample:
```javascript
{
  "urls": [
    "https://quotes.toscrape.com"
  ],
  "extract_rules": {
    "js_instructions": [
      {"click": ".header-box .col-md-4 a"},
      {"fill": ["#username","username"]},
      {"fill": ["#password","password"]},
      {"click": ".btn-primary"}
    ],
    "quotes": {
      "selector": ".quote",
      "type": "list",
      "output": {
        "text": ".text",
        "author": ".author",
        "tags": {
          "selector": ".tag",
          "type": "list"
        },
        "about": {
          "selector": "span a",
          "type": "page",
          "follow": "href",
          "output": {
            "author_name": ".author-title",
            "author_birth_date": ".author-born-date",
            "author_birth_location": ".author-born-location",
            "author_description": ".author-description"
          }
        },
        "goodreads": {
          "selector": "span a+ a",
          "type": "page",
          "follow": "href",
          "output": {
            "js_instructions": [{"click":".dataItem span+ a"}],
            "died": ".dataItem:nth-child(8)",
            "genre": {
              "selector":".dataItem:nth-child(14) a",
              "type": "list"
            },
            "influences": {
              "selector":".dataItem:nth-child(17) span a",
              "type": "list"
            }
          }
        }
      }
    }
  }
}
```
Expected response:
```javascript
[
{
  "quotes": [
    {
      "text": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
      "author": "Albert Einstein",
      "tags": [
        "change",
        "deep-thoughts",
        "thinking",
        "world"
      ],
      "about": {
        "author_name": "Albert Einstein\n",
        "author_birth_date": "March 14, 1879",
        "author_birth_location": "in Ulm, Germany",
        "author_description": "In 1879, Albert Einstein was born in Ulm, Germany. He completed his Ph.D. at the University of Zurich by 1909. His ..."
        "date": "2022-01-20-17:32:17",
        "url": "http://quotes.toscrape.com/author/Albert-Einstein/"
      },
      "goodreads": {
        "died": "April 18, 1955",
        "genre": [
          "Science",
          "Philosophy",
          "Physics"
        ],
        "influences": [
          "Bertrand Russell",
          "Sigmund Freud",
          "Baruch Spinoza",
          "Niels Bohr",
          "Karl Pear",
          "Bertrand Russell",
          "Sigmund Freud",
          "Baruch Spinoza",
          "Niels Bohr",
          "Karl Pearson",
          "Marie Curie",
          "Bernhard Riemann",
          "Edmond Halley",
          "Isaac Newton",
          "Michael Faraday",
          "James Clerk Maxwell",
          "Johannes Kepler",
          "Percy Williams Bridgman",
          "Emmy Noether",
          "Alfred Whitehead"
        ],
        "date": "2022-01-20-17:33:16",
        "url": "https://www.goodreads.com/author/show/9810.Albert_Einstein"
      }
    }
    ...]
...}
```
More request examples are avaliable in the [examples](https://github.com/vlad-yeghiazaryan/smart-scraper/tree/master/scrape/example) folder.
## Deployment:
After making your changes simply run:
```bash
docker build . -t <dockerhub_username>/<repo_name>:<tag_name>
```
```bash
docker push <dockerhub_username>/<repo_name>:<tag_name>
```


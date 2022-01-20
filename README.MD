## Execution order for ibm-fun-action:
```bash
docker build . -t vladimiryeghiazaryan/smart-scraper:latest
```
```bash
docker push vladimiryeghiazaryan/smart-scraper:latest
```
On execution map any directory of your choice to the `\scrape` folder and put your `request.txt` parameters in that folder.

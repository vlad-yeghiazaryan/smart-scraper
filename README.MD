## Usage
```bash
docker pull vladimiryeghiazaryan/smart-scraper
```
On execution map any directory of your choice to the `/scrape` folder and put your `request.json` parameters in that folder.
```bash
docker run -v path/to/my/scraper/dir:/scrape vladimiryeghiazaryan/smart-scraper
```
## Deployment:
After making your changes simply run:
```bash
docker build . -t <dockerhub_username>/<repo_name>:<tag_name>
```
```bash
docker push <dockerhub_username>/<repo_name>:<tag_name>
```


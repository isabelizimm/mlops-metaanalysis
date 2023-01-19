## Gathering repos to analyze

To begin, I used [GitHub's REST API](https://docs.github.com/en/rest/quickstart?apiVersion=2022-11-28) to collect data on repositories that might be relevant for this use case.


I ran commands: for topics_mlops_pg_{1-10}.json to get all the repositories with the topic `mlops`.

``` bash
cd data/repos
```


``` bash
gh api \ 
  -H "Accept: application/vnd.github+json" \
  "/search/repositories?q=topic:mlops&per_page=100&page=1" > topic_mlops_pg_1.json
```

Next, I was interested in looking at repos with the tag `model-management` but NOT `mlops`.

``` bash
gh api \ 
  -H "Accept: application/vnd.github+json" \
  "/search/repositories?q=topic:model-management&per_page=100&NOTtopic:mlops&page=1" > topic_modelmanagement_pg_1.json
```


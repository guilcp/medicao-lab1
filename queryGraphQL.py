
import requests
import csv
import datetime

headers = {"Authorization": "bearer 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"}

allResults = []

query = """
{
  search(query: "stars:>100", type: REPOSITORY, first: 10, after:null) {
    pageInfo {
      endCursor
      startCursor
    }
    nodes {
      ... on Repository {
        nameWithOwner
        createdAt
        pullRequests(first: 1) {
          totalCount
        }
        releases(first: 1) {
          totalCount
        }
        updatedAt
        primaryLanguage {
          name
        }
        issues: issues (first: 1){
          totalCount
        }
        closedIssues: issues (first: 1, states: CLOSED){
          totalCount
        }
      }
    }
  }
}
"""

endCursor = "null"

while (len(allResults) < 1000):
    request = requests.post('https://api.github.com/graphql',
                            json={'query': query}, headers=headers)
    result = request.json()
    allResults += result['data']['search']['nodes']
    query = query.replace(endCursor, '"'+result['data']
                          ['search']['pageInfo']['endCursor']+'"')
    endCursor = '"'+result['data']['search']['pageInfo']['endCursor']+'"'


print("All Results - {}".format(allResults))
print("All Results Size - ")
print(len(allResults))

fields = list(allResults[0].keys())

with open('dados.csv', 'w') as f:
    write = csv.DictWriter(f, fieldnames=fields, dialect='unix')
    write.writeheader()
    for result in allResults:
        result['pullRequests'] = result['pullRequests']['totalCount']
        result['releases'] = result['releases']['totalCount']
        if result['primaryLanguage'] is not None:
            result['primaryLanguage'] = result['primaryLanguage']['name']
        result['issues'] = result['issues']['totalCount']
        result['closedIssues'] = result['closedIssues']['totalCount']
        createdAt = datetime.datetime.strptime(
            result['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
        result['createdAt'] = datetime.datetime.strftime(
            createdAt, '%d/%m/%Y %H:%M:%S')
        updatedAt = datetime.datetime.strptime(
            result['updatedAt'], '%Y-%m-%dT%H:%M:%SZ')
        result['updatedAt'] = datetime.datetime.strftime(
            updatedAt, '%d/%m/%Y %H:%M:%S')
        write.writerow(result)

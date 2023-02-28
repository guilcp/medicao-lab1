
import requests
import csv

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
    # print(query)
    request = requests.post('https://api.github.com/graphql',
                            json={'query': query}, headers=headers)
    result = request.json()
    # print(result)
    allResults += result['data']['search']['nodes']
    query = query.replace(endCursor, '"'+result['data']
                          ['search']['pageInfo']['endCursor']+'"')
    endCursor = '"'+result['data']['search']['pageInfo']['endCursor']+'"'
    



print("All Results - {}".format(allResults))
print("All Results Size - ")
print(len(allResults))

# quit()

fields = list(allResults[0].keys())

with open('dados.csv', 'w') as f:
    write = csv.DictWriter(f, fieldnames=fields, dialect='unix')
    write.writeheader()
    for result in allResults:
        write.writerow(result)

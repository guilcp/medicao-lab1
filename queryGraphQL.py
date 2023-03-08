
import requests
import pandas as pd
import datetime
import matplotlib.pyplot as plot

# colocar token aqui
token = "eOVIR7AwkNb7mzKjuY4UoGSqedkBkL0dC4nu"

headers = {"Authorization": "bearer ghp_"+token}

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

error = 0
while (len(allResults) < 1000):
    request = requests.post('https://api.github.com/graphql',
                            json={'query': query}, headers=headers)
    result = request.json()
    if 'data' in result:
        allResults += result['data']['search']['nodes']
        query = query.replace(endCursor, '"'+result['data']
                              ['search']['pageInfo']['endCursor']+'"')
        endCursor = '"'+result['data']['search']['pageInfo']['endCursor']+'"'
    else:
        error += 1
        if (error > 5):
            print("Error na chamada da api do git hub")
            print(result)
            break
        else:
            continue


print("All Results - {}".format(allResults))
print("All Results Size - ")
print(len(allResults))

# fields = list(allResults[0].keys())

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


df = pd.DataFrame(allResults)

df.to_csv('dados.csv', index=False)

b_plot = df.boxplot(column='pullRequests')
b_plot.plot()
plot.show()
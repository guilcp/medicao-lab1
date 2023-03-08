
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

today = datetime.datetime.utcnow()

def age(createdAt):
  age = today.year - createdAt.year - ((today.month, today.day) < (createdAt.month, createdAt.day))
  return age

def ageInMonths(createdAt):
  time = today - updatedAt
  months = 0
  if time.seconds == 0 and time.microseconds == 0:
    months = time.days/30
  elif time.seconds == 0:
    months = time.days/30 + time.microseconds/(3600000*30)
  elif time.microseconds == 0:
    months = time.days + time.seconds/(3600*30)
  else:
    months = time.days/30 + time.seconds/(3600*30) + time.microseconds/(3600000*30)
  return months

def differenceInDays(updatedAt):
  time = today - updatedAt
  days = 0
  if time.seconds == 0 and time.microseconds == 0:
    days = time.days
  elif time.seconds == 0:
    days = time.days + time.microseconds/3600000
  elif time.microseconds == 0:
    days = time.days + time.seconds/3600
  else:
    days = time.days + time.seconds/3600 + time.microseconds/3600000
  return days

for result in allResults:
    result['pullRequests'] = result['pullRequests']['totalCount']
    releases = result['releases']['totalCount']
    result['releases'] = releases
    if result['primaryLanguage'] is not None:
        result['primaryLanguage'] = result['primaryLanguage']['name']
    result['issues'] = result['issues']['totalCount']
    closedIssues = result['closedIssues']['totalCount']
    result['closedIssues'] = closedIssues
    createdAt = datetime.datetime.strptime(
        result['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
    result['createdAt'] = datetime.datetime.strftime(
        createdAt, '%d/%m/%Y %H:%M:%S')
    updatedAt = datetime.datetime.strptime(
        result['updatedAt'], '%Y-%m-%dT%H:%M:%SZ')
    result['updatedAt'] = datetime.datetime.strftime(
        updatedAt, '%d/%m/%Y %H:%M:%S')
    result['ageInYears'] = age(createdAt)
    months = ageInMonths(createdAt)
    if months > 0:
      result['releasesMonth'] = releases/ageInMonths(createdAt)
    result['daysFromUpdate'] = differenceInDays(updatedAt)


df = pd.DataFrame(allResults)

df.to_csv('dados.csv', index=False)

ageHist = df.hist(column='ageInYears',bins=10)

plot.title('Quantidade de Repositórios x Idade (anos)')

plot.show()

pullRequestHist = df.hist(column='pullRequests',bins=10)

plot.title('Quantidade de Repositórios x Número de Pull Requests')

plot.show()

releasesHist = df.hist(column='releasesMonth',bins=10)

plot.title('Quantidade de Repositórios x Número de Releases por Mês')

plot.show()
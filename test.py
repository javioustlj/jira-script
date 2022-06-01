from jira import JIRA

jira_server = 'https://jiradc.ext.net.nokia.com/'
auth_jira = JIRA(jira_server, basic_auth=('username', 'password'))

issues = auth_jira.search_issues('key=FPB-677417')

# print(auth_jira.fields())

# for issue in issues:
#     print('#######ISSUE#########')
#     print(issue)
#     print(issue.fields.issuelinks)
#     # for link in issue.fields.issuelinks:
#     #     print(link)
#     # for subtask in issue.fields.subtasks:
#     #     print(subtask)

for issue in linkedIssues('FPB-677417'):
    print(issue)

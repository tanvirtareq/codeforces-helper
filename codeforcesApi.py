import urllib.request
import json

print("hello")

# url = "https://codeforces.com/api/problemset.problems?"

# response = urllib.request.urlopen(url)

# data = json.loads(response.read())

# # print(data)

# if data['status']=='OK':
#     a=0;
#     result=data['result']
#     problems=result['problems']
#     for problem in problems:
#         # print(problem)
#         a=a+1
#         # if a>5:
#         #     break
#     # print(problems)
#     print(a)
# else:
#     print("NO")

# url2 = "https://codeforces.com/api/user.status?handle=t17&from=1&count=100000"

# response = urllib.request.urlopen(url2)

# data2=json.loads(response.read())

# result=data2['result']
# print(result[1])

# print(data2)

a={
    'a':'a',
    'b':'c',
    1:2
}

print(a.get('d'))
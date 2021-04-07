import requests

nomer = imput("видите ваш номер телефона")

a = reguests.post("https://qiwi.com/oauth/authorize",
    jeson={"phone_namber": nomer},)
print(a.text)
input

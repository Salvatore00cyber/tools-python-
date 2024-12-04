import requests
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "==============================")
print(Fore.YELLOW + "  🌟 Instagram Password Reset  🌟")
print(Fore.CYAN + "==============================\n")

print("      #############################                 ")
print("     #  Copyrit of Salvatore     #   @Cyber_warrior ")
print("    #    @5ec_0                 #                   ")
print("   #############################                    ")
email = input(Fore.GREEN + "set email for reset : ")

url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
payload = f"email_or_username={email}"
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    'Content-Type': "application/x-www-form-urlencoded",
    'x-csrftoken': "r15fQwEdpDwDqwW2EkmYjOWCeyBiwQTc",
    'x-requested-with': "XMLHttpRequest",
    'x-ig-app-id': "936619743392459",
    'referer': "https://www.instagram.com/accounts/password/reset/",
    'Cookie': "mid=ZqPYMgABAAE1FS3FyA2mTh6D4nSn; csrftoken=r15fQwEdpDwDqwW2EkmYjOWCeyBiwQTc"
}

try:
    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        print(Fore.CYAN + "\n🎉 تم ارسال كود اعادة تعيين كلمة المرور واواواو")
    else:
        print(Fore.RED + f"\n❌ خطأ: {response.status_code}")
        print(Fore.RED + f"🛠 الرسالة: {response.text}")
except Exception as e:
    print(Fore.RED + f"\n❌ خطأ: {e}")

print(Fore.CYAN + Style.BRIGHT + "\n==============================")
print(Fore.YELLOW + "      Must      ")
print(Fore.CYAN + "==============================")

import builtwith

def detect_tech(url):
    tech = builtwith.builtwith(url)
    return tech

if __name__ == "__main__":
    url = "https://web-security-ute-2024-using-modern-django.vercel.app"
    print(detect_tech(url))
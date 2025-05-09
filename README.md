# 🌐 IP Info Checker

> **IP 주소만 입력하면 WHOIS 정보와 지리적 위치를 한 번에 확인!**  
> 보안 입문자도 쉽게 다룰 수 있는 간단하고 직관적인 Python 기반 OSINT 도구입니다.

---

## 🧠 소개

IP 주소 하나로 무엇을 알 수 있을까요?  
이 툴은 아래 두 가지 정보를 **명령줄에서 간단히** 확인할 수 있도록 도와줍니다:

- ✅ **WHOIS 조회**: 등록자, 네트워크 정보, 국가 등
- 🌍 **위치 조회 (GeoIP)**: 도시, 지역, 국가, ISP 등

보안 초보자도 네트워크 분석이나 인텔리전스 수집을 연습해볼 수 있도록 설계된 오픈소스 도구입니다.

---

## 🖥️ 실행 화면 예시

```
조회할 IP 주소를 입력하세요: 8.8.8.8

🔍 WHOIS 정보:
Name: LVLT-ORG-8-8-8
Country: US
CIDR: 8.8.8.0/24
Org: Google LLC

🌍 위치 정보:
City: Mountain View
Region: California
Country: United States
ISP: Google LLC
```

---

## ⚙️ 설치 방법

1. 저장소 클론 또는 ZIP 다운로드

```bash
git clone https://github.com/your-username/ip-info-checker.git
cd ip-info-checker
```

2. 필요한 라이브러리 설치

```bash
pip install -r requirements.txt
```

---

## 🚀 사용 방법

```bash
python ip_checker.py
```

IP 주소를 입력하면 WHOIS + 위치 정보를 자동으로 출력해줍니다.


## 🔧 사용 기술

- Python 3.x
- [ipwhois](https://pypi.org/project/ipwhois/) – WHOIS 정보 조회
- [requests](https://pypi.org/project/requests/) – 위치 정보 API 호출

위치 정보는 [ip-api.com](http://ip-api.com) 공개 API를 사용합니다.

---

## ⚠️ 유의 사항

- IP 위치 정보는 정확하지 않을 수 있으며, VPN/프록시 사용 시 왜곡됩니다.
- `ip-api.com`은 공개 API로 과도한 요청 시 차단될 수 있습니다.



---

감사합니다! 🫡
from ipwhois import IPWhois
import requests

def get_whois(ip):
    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap()
        return {
            "Name": result["network"]["name"],
            "Country": result["network"]["country"],
            "CIDR": result["network"]["cidr"],
            "Org": result["network"].get("org", "N/A")
        }
    except Exception as e:
        return {"error": str(e)}

def get_geoip(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        return {
            "City": res["city"],
            "Region": res["regionName"],
            "Country": res["country"],
            "ISP": res["isp"]
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    ip = input("조회할 IP 주소를 입력하세요: ")
    
    print("\n🔍 WHOIS 정보:")
    for k, v in get_whois(ip).items():
        print(f"{k}: {v}")

    print("\n🌍 위치 정보:")
    for k, v in get_geoip(ip).items():
        print(f"{k}: {v}")
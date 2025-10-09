import json

with open("sample-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data.get("imdata", [])

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20}  {'Speed':6}  {'MTU':6}")
print(f"{'-'*50} {'-'*20}  {'-'*6}  {'-'*6}")

for entry in items:
    inner = next(iter(entry.values()))
    attrs = inner.get("attributes", {})

    dn = attrs.get("dn", "")
    descr = attrs.get("descr", "")
    speed = attrs.get("speed") or "inherit"
    mtu = attrs.get("mtu", "")

    print(f"{dn:50} {descr:20}  {speed:6}  {mtu:6}")

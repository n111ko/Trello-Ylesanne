import json

def get_valid_email():
    while True:
        email = input("Sisestage e-mail: ")
        if "@" in email:
            return email
        print("❌ Vigane e-mail! Palun sisestage korrektne e-mail.")


company_name = input("sistage ettevõtte nimi: ")
contact_email = input("sistage e-mail: ")
data_collection = input("milliseid andmeid kogutakse? ")
data_usage = input("Kuidas andmed kasutatakse? ")
data_retention = input("Kui kaua need hoiatakse? ")
cookies = input("Kas teie veebileht kasutab küpsiseid? (jah/ei): ")

privacy_data = {
    "company_name": company_name,
    "contact_email": contact_email,
    "data_collection": data_collection,
    "data_usage": data_usage,
    "data_retention": data_retention,
    "cookies": cookies
}


with open("privacy_template.json", "w", encoding="utf-8") as file:
    json.dump(privacy_data, file, indent=4, ensure_ascii=False)

print("✅ JSON-fail oli loodud: privacy_template.json")


html_template = """<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privaatsuspoliitika</title>
</head>
<body>
    <h1>Privaatsuspoliitika - {company_name}</h1>
    <p><strong>Kontakt:</strong> {contact_email}</p>
    <h2>Milliseid andmeid me kogume?</h2>
    <p>{data_collection}</p>
    <h2>Kuidas me kasutame andmeid?</h2>
    <p>{data_usage}</p>
    <h2>Kui kaua me andmeid säilitame?</h2>
    <p>{data_retention}</p>
    <h2>Kas me kasutame küpsiseid?</h2>
    <p>{cookies}</p>
</body>
</html>"""

privacy_policy = html_template.format(**privacy_data)

with open("privacy_policy.html", "w", encoding="utf-8") as file:
    file.write(privacy_policy)

print("✅ fail oli loodud: privacy_policy.html")

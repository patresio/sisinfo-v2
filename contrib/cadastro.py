import json

import slugify

# materiais = [
#     ("CABO ADAPTADOR COM PLUG, 2XP2", "17.00", "4"),
#     ("HEADSET - 20 HZ", "17.00", "4"),
#     ("MICROFONE", "189.0", "4"),
#     ("WEBCAM", "161.00", "4"),
#     ("HD SSD 480 GB", "288.00", "4"),
#     ("CASE DE GAVETA PARA HD EXTERNO 2.5", "94.00", "4"),
#     ("PEN DRIVE 32GB", "40.00", "4"),
#     ("SSD 960 GB", "394.00", "4"),
#     ("SSD EXTERNO 1TB PORTATIL", "526.00", "4"),
#     ("SWITCH 10/100/1000 MBPS 5 PORTAS", "96.00", "5"),
#     ("SWITCH 10/100/1000 - 16 PORTAS", "329.00", "5"),
#     ("SWITCH 10/100/1000 - 8 PORTAS", "96.00", "5"),
#     ("SWITCH 28 PORTAS 10/100/1000", "1550.00", "5"),
#     ("TELA NT140FHM-N44 V8.1 PARA NOTEBOOK VAIO FE14 VJFE42F11X", "646.00", "6"),
#     ("BATERIA 634477 PARA NOTEBOOK VAIO FE14 VJFE42F11X", "220.00", "6"),
#     (
#         "FONTE S29A00 1.2A SAÍDA 19V 2.1A PARA NOTEBOOK VAIO FE14 VJFE42F11X",
#         "135.00",
#         "6",
#     ),
#     ("TECLADO PARA NOTEBOOK ACER ASPIRE 4749-6871", "114.00", "6"),
#     ("TECLADO PARA NOTEBOOK ACER ASPIRE V5-471-6677 MS2360", "114.00", "6"),
#     ("TECLADO PARA NOTEBOOK LENOVO IDEAPAD 330 81FE0002BR", "114.00", "6"),
#     ("TELA PARA NOTEBOOK  LENOVO G50-80 MODELO 80R0", "114.00", "6"),
#     ("NOTEBOOK INTEL CORE I3 8GB SSD 256 TELA 15.6 POLEGADAS", "2282.68", "7"),
#     ("NOTEBOOK INTEL CORE I5 8GB 1 TB TELA 15.6 POLEGADAS", "2530.00", "7"),
#     ("MONITOR LED 21,5 POLEGADAS INTELLINCY / LED-2105", "289.90", "8"),
#     ("APARELHO TELEFONICO COM FIO", "60.00", "9"),
#     ("APARELHO TELEFONICO SEM FIO", "126.05", "9"),
# ]

materiais = [
    ("Memória RAM 4GB DDR4 2400 Mhz", "65.00", "10"),
    ("Cabo de força para pc", "6.00", "10"),
    ("Fonte ATX 230 W para computador", "60.00", "10"),
    (
        "Gabinete Torre Atx para Computador com 1 baia externa e 2 baias internas ",
        "81.00",
        "10",
    ),
    ("HD SSD 240 GB", "179.00", "10"),
    ("MEMÓRIA RAM 8GB DDR4 2666 MHZ", "120.01", "10"),
    ("MOUSE OPTICO USB ", "6.50", "10"),
    ("MOUSE PAD", "5.99", "10"),
    ("par de Caixas de som para computador", "28.00", "10"),
    ("Placa Mãe Gigabyte H510m H  Soquete Lga 1200", "540.00", "10"),
    ("Placa Mãe Gigabyte H610M H DDR4 Intel Soquete LGA 1700", "610.00", "10"),
    ("Processador Cpu Intel Core i3-10100 3.6 GHZ LGA 1200 6 MB", "599.90", "10"),
    ("Processador cpu Intel core i5-11400 2.6 ghz LGA 1200 12mb", "850.00", "10"),
    ("Processador Intel Core i3-12100 3.3GHz LGA 1700 12MB", "740.00", "10"),
    ("Processador Intel Core i5-12400 2.5GHz LGA 1700 18MB", "760.00", "10"),
    ("Teclado USB para computador", "24.00", "10"),
]

# dados = []

dados = [
    {
        "model": "bidding_supplier.supplier",
        "fields": {
            "company": "CHERUBINI INFORMÁTICA ME",
            "trade": "CHERUBINI",
            "cnpj": "45152139000199",
            "slug": "cherubini",
            "address": "",
            "created_at": "2024-04-17T10:00:36.058Z",
            "update_at": "2024-04-17T10:00:48.761Z",
        },
    }
]

for material in materiais:
    slug = slugify.slugify(material[0])
    produto = {
        "model": "dashboard.material",
        "fields": {
            "name": f"{material[0]}",
            "slug": f"{slug[:45]}-{material[2]}",
            "status": "1",
            "bidding": 1,
            "price": f"{material[1]}",
            "readjustment": 0.0,
            "supplier": int(material[2]),
        },
    }
    dados.append(produto)

with open("./jsons/materials/primeiralicitacao_cherubini.json", "w") as json_file:
    json.dump(dados, json_file, indent=4)

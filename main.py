from maps.GakushokuSample import GakushokuSample
from maps.K25141_osusume import K25141_osusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(),
        K25141_osusume(),
          ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
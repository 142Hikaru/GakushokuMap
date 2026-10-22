from maps.GakushokuSample import GakushokuSample
from maps.murayamaryouri import murayamaryouri
from maps.K25141_osusume import K25141_osusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [murayamaryouri(),
        K25141_osusume(),
        GakushokuSample(),
       ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
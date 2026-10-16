from maps.GakushokuSample import GakushokuSample
from maps.osusumekai import osusumekai

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(),osusumekai() ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
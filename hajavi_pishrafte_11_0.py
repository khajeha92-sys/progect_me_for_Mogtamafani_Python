#IN THE NAME OF GOD
#MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
# CLASS 11

import json

# Exercise 1: Add more historical details to each city

def city_country(iran_cities, extra_history):

    # Add to each city
    for city in iran_cities["شهرها"]:
        if city["نام"] in extra_history:
            city["جزئیات_تاریخی"] = extra_history[city["نام"]]

    # Save result
    with open("exercise1_result.json", "w", encoding="utf-8") as f:
        json.dump(iran_cities, f, indent=2, ensure_ascii=False)

    print("Exercise 1 complete! Saved to exercise1_result.json")

# Exercise 2: Create a timeline of Iranian citis
def timelinee(timeline, period_order, sorted_timeline):
    
    #Lpad data after E1
    with open("exercise1_result.json", "r", encoding="utf-8") as f:
        iran_cities = json.load(f)

    for city in iran_cities["شهرها"]:
        period = city["دوره_تاسیس"]
        if period not in timeline:
            timeline[period] = []
        timeline[period].append(city["نام"])

    for period in period_order:
        if period in timeline:
            sorted_timeline[period] = timeline[period]

    # Save
    with open("exercise2_result.json", "w", encoding="utf-8") as fh:
        json.dump(sorted_timeline, fh, indent=2, ensure_ascii=False)

    print(" Exercise 2 complete! Saved to exercise1_result.json")
    print("\nTimeline:")
    for period, cities in sorted_timeline.items():
        print(f"  {period}: {', '.join(cities)}")

    

# Exercise 3: Compare city histories
def city_histories():
    # Load
    with open("exercise1_result.json", "r", encoding="utf-8") as f:
        iran_cities = json.load(f)

    cities = iran_cities["شهرها"]

    #  Capitals
    print(" Cities that were capitals:")
    capitals = []
    for city in cities:
        if city["پایتخت"] or "پایتخت" in city["دوره_تاسیس"]:
            capitals.append(city["نام"])
            print(f"   • {city['نام']} - {city['دوره_تاسیس']}")

    # 2. Ancient cities
    print("\n️ Cities with ancient roots:")
    ancient = []
    for city in cities:
        if "هخامنشی" in city["پیشینه_باستانی"] or "ساسانی" in city["پیشینه_باستانی"]:
            ancient.append(city["نام"])
            print(f"   • {city['نام']} - {city['پیشینه_باستانی']}")

    # population 
    print("\n Population ranking:")
    sorted_by_pop = sorted(cities, key=lambda x: x["جمعیت"], reverse=True)
    for i, city in enumerate(sorted_by_pop, 1):
        print(f"   {i}. {city['نام']}: {city['جمعیت']:,}")

    # attractions 
    print("\n Number of attractions:")
    for city in cities:
        print(f"   • {city['نام']}: {len(city['جاذبه‌ها'])} attractions")

    #save
    comparison = {
    "capitals": capitals,
    "ancient_cities": ancient,
    "population_ranking": [
        {"rank": i+1, "name": c["نام"], "population": c["جمعیت"]}
        for i, c in enumerate(sorted_by_pop)
        ]
    }

    with open("exercise3_comparison.json", "w", encoding="utf-8") as f:
        json.dump(comparison, f, indent=2, ensure_ascii=False)

    print("\n Exercise 3 complete! Saved to exercise3_comparison.json")

    
#data's
def main():
    #1.:
    print('1.')
    iran_cities = {
    "کشور": "ایران",
    "تعداد_کل": 5,
    "شهرها": [
        {
            "نام": "تهران",
            "استان": "تهران",
            "جمعیت": 8693706,
            "جاذبه‌ها": ["برج میلاد", "آزادی", "تجریش", "پل طبیعت"],
            "پایتخت": True,
            "دوره_تاسیس": "دوره قاجار (به عنوان پایتخت)",
            "پیشینه_باستانی": "ری باستان (دوره هخامنشی و ساسانی)"
        },
        {
            "نام": "اصفهان",
            "استان": "اصفهان",
            "جمعیت": 1961260,
            "جاذبه‌ها": ["نقش جهان", "سی وسه پل", "منار جنبان"],
            "پایتخت": False,
            "دوره_تاسیس": "دوره صفوی (به عنوان پایتخت)",
            "پیشینه_باستانی": "دوره ساسانیان و پیش از آن"
        },
        {
            "نام": "شیراز",
            "استان": "فارس",
            "جمعیت": 1565572,
            "جاذبه‌ها": ["تخت جمشید", "حافظیه", "سعدیه", "ارگ کریم‌خان"],
            "پایتخت": False,
            "دوره_تاسیس": "دوره هخامنشی (منطقه)",
            "پیشینه_باستانی": "دوره هخامنشی، ساسانی و پس از اسلام"
        },
        {
            "نام": "تبریز",
            "استان": "آذربایجان شرقی",
            "جمعیت": 1773033,
            "جاذبه‌ها": ["بازار بزرگ تبریز", "مسجد کبود", "ارگ علیشاه", "خانه مشروطه"],
            "پایتخت": False,
            "دوره_تاسیس": "دوره ساسانیان",
            "پیشینه_باستانی": "دوره ساسانیان و پیش از آن"
        },
        {
            "نام": "مشهد",
            "استان": "خراسان رضوی",
            "جمعیت": 3001184,
            "جاذبه‌ها": ["حرم امام رضا", "آرامگاه فردوسی", "باغ وحش وکیل‌آباد"],
            "پایتخت": False,
            "دوره_تاسیس": "دوره سامانیان",
            "پیشینه_باستانی": "دوره ساسانیان و پس از اسلام"
        }
    ]
}

    # Add historical details
    extra_history = {
        "تهران": {
            "دوره‌های_مهم": ["قاجار", "پهلوی", "انقلاب اسلامی"],
            "رویدادهای_تاریخی": [
                "۱۷۸۶: انتخاب به عنوان پایتخت",
                "۱۹۰۶: انقلاب مشروطه",
                "۱۹۷۹: انقلاب اسلامی"
            ],
            "شهرهای_همسایه_باستانی": ["ری", "شمیران"]
        },
        "اصفهان": {
            "دوره‌های_مهم": ["ساسانیان", "صفویان", "قاجار"],
            "رویدادهای_تاریخی": [
                "۱۵۹۸: پایتخت صفویان شد",
                "۱۶۲۹: ساخت میدان نقش جهان",
                "۱۶۵۰: ساخت پل سی وسه پل"
            ],
            "لقب": "نصف جهان"
        },
        "شیراز": {
            "دوره‌های_مهم": ["هخامنشی", "ساسانی", "پس از اسلام"],
            "رویدادهای_تاریخی": [
                "۵۱۸ پیش از میلاد: تخت جمشید",
                "سده ۱۴: حافظ و سعدی",
                "۱۷۶۶: ارگ کریم‌خان"
            ],
            "لقب": "شهر راز"
        },
        "تبریز": {
            "دوره‌های_مهم": ["ساسانیان", "ایلخانیان", "صفویان"],
            "رویدادهای_تاریخی": [
                "سده ۳: تأسیس در دوره ساسانی",
                "۱۲۹۵: پایتخت ایلخانیان",
                "۱۹۰۶: مرکز جنبش مشروطه"
            ],
            "لقب": "شهر اولین‌ها"
        },
        "مشهد": {
            "دوره‌های_مهم": ["ساسانی", "سامانی", "صفوی"],
            "رویدادهای_تاریخی": [
                "۸۱۸: شهادت امام رضا (ع)",
                "۹۹۶: آرامگاه فردوسی",
                "۱۶۱۲: توسعه حرم امام رضا"
            ],
            "لقب": "شهر مقدس"
        }
    }
    city_country(iran_cities, extra_history)

    print('=' * 63)
    print('2.')

    #create timeline
    timeline = {}

    #sort
    period_order = [
        "دوره هخامنشی (منطقه)",
        "دوره ساسانیان",
        "دوره سامانیان",
        "دوره صفوی (به عنوان پایتخت)",
        "دوره قاجار (به عنوان پایتخت)"
    ]

    sorted_timeline = {}

    timelinee(timeline, period_order, sorted_timeline)
    
    print('=' * 63)
    print('3.')
    city_histories()


    print('THE END')
    
main()    

print('\n MADE IN AMIRABAS KHAJEH')

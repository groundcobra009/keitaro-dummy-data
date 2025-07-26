import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# 設定
np.random.seed(42)
random.seed(42)

# 店舗情報
store_regions = {
    '北海道': ['札幌店', '旭川店', '函館店'],
    '東北': ['仙台店', '青森店', '盛岡店', '秋田店'],
    '関東': ['東京都心店', '横浜店', '千葉店', '大宮店', '立川店', '川崎店'],
    '中部': ['名古屋店', '静岡店', '新潟店', '金沢店'],
    '関西': ['大阪梅田店', '京都店', '神戸店', '奈良店'],
    '中国': ['広島店', '岡山店', '鳥取店'],
    '四国': ['高松店', '松山店'],
    '九州': ['福岡店', '長崎店', '熊本店', '鹿児島店']
}

# 商品カテゴリと商品
categories = {
    '生鮮食品': {
        'products': ['牛肉', '豚肉', '鶏肉', '魚介類', '野菜', '果物'],
        'avg_price': [800, 400, 300, 600, 200, 350],
        'margin': 0.25
    },
    '加工食品': {
        'products': ['パン', '牛乳', '卵', 'チーズ', 'ヨーグルト', '冷凍食品'],
        'avg_price': [150, 200, 250, 400, 180, 350],
        'margin': 0.30
    },
    '日用品': {
        'products': ['洗剤', 'トイレットペーパー', 'ティッシュ', 'シャンプー', '歯磨き粉'],
        'avg_price': [300, 400, 250, 500, 200],
        'margin': 0.35
    },
    '飲料': {
        'products': ['水', 'お茶', 'コーヒー', 'ジュース', 'ビール', '日本酒'],
        'avg_price': [100, 120, 150, 130, 200, 800],
        'margin': 0.40
    },
    'お菓子': {
        'products': ['チョコレート', 'ポテトチップス', 'クッキー', 'ガム', '飴'],
        'avg_price': [200, 150, 250, 100, 120],
        'margin': 0.45
    }
}

# データ生成期間（2023年1月〜2024年12月）
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

# 曜日別売上係数
weekday_factors = {
    0: 0.9,   # 月曜日
    1: 0.85,  # 火曜日
    2: 0.85,  # 水曜日
    3: 0.9,   # 木曜日
    4: 1.1,   # 金曜日
    5: 1.3,   # 土曜日
    6: 1.2    # 日曜日
}

# 月別季節係数
seasonal_factors = {
    1: 0.85,   # 1月
    2: 0.8,    # 2月
    3: 0.9,    # 3月
    4: 0.95,   # 4月
    5: 1.0,    # 5月
    6: 0.95,   # 6月
    7: 1.05,   # 7月
    8: 1.1,    # 8月
    9: 0.95,   # 9月
    10: 1.0,   # 10月
    11: 1.05,  # 11月
    12: 1.2    # 12月
}

# データ生成
data = []

# 各店舗のベース売上高を設定
store_base_sales = {}
for region, stores in store_regions.items():
    for store in stores:
        if '東京' in store or '大阪' in store:
            base = random.randint(800000, 1200000)
        elif region in ['関東', '関西', '中部']:
            base = random.randint(500000, 800000)
        else:
            base = random.randint(300000, 600000)
        store_base_sales[store] = base

# 日付ごとにデータ生成
current_date = start_date
while current_date <= end_date:
    weekday = current_date.weekday()
    month = current_date.month
    
    for region, stores in store_regions.items():
        for store in stores:
            # 店舗のベース売上に曜日と季節の係数を適用
            base_daily_sales = store_base_sales[store] / 30
            daily_factor = weekday_factors[weekday] * seasonal_factors[month]
            
            # カテゴリごとの売上を生成
            for category, info in categories.items():
                products = info['products']
                avg_prices = info['avg_price']
                margin = info['margin']
                
                for i, product in enumerate(products):
                    # 商品ごとの販売数量（正規分布でランダム化）
                    base_quantity = int(base_daily_sales / avg_prices[i] / len(categories) / len(products) * daily_factor)
                    quantity = max(0, int(np.random.normal(base_quantity, base_quantity * 0.2)))
                    
                    if quantity > 0:
                        # 価格の変動（±10%）
                        unit_price = int(avg_prices[i] * random.uniform(0.9, 1.1))
                        sales_amount = quantity * unit_price
                        cost = int(sales_amount * (1 - margin))
                        profit = sales_amount - cost
                        
                        # 顧客数（商品数に基づく推定）
                        customers = max(1, int(quantity / random.uniform(1.5, 3.5)))
                        
                        # 在庫数（販売数の1.5〜3倍）
                        inventory = int(quantity * random.uniform(1.5, 3.0))
                        
                        record = {
                            '日付': current_date.strftime('%Y-%m-%d'),
                            '年': current_date.year,
                            '月': current_date.month,
                            '日': current_date.day,
                            '曜日': ['月', '火', '水', '木', '金', '土', '日'][weekday],
                            '地域': region,
                            '店舗名': store,
                            'カテゴリ': category,
                            '商品名': product,
                            '販売数量': quantity,
                            '単価': unit_price,
                            '売上金額': sales_amount,
                            '原価': cost,
                            '粗利益': profit,
                            '粗利率': round(profit / sales_amount * 100, 1),
                            '顧客数': customers,
                            '在庫数': inventory,
                            '在庫回転率': round(quantity / inventory * 30, 2) if inventory > 0 else 0
                        }
                        
                        data.append(record)
    
    current_date += timedelta(days=1)

# DataFrameに変換
df = pd.DataFrame(data)

# 集計用の追加カラム
df['年月'] = df['年'].astype(str) + '-' + df['月'].astype(str).str.zfill(2)
df['四半期'] = 'Q' + ((df['月'] - 1) // 3 + 1).astype(str)

# CSVファイルに保存
df.to_csv('supermarket_sales_data.csv', index=False, encoding='utf-8-sig')

# サマリー統計の作成
summary_stats = {
    '総レコード数': len(df),
    '期間': f"{start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}",
    '店舗数': len(df['店舗名'].unique()),
    '商品数': len(df['商品名'].unique()),
    '総売上金額': f"¥{df['売上金額'].sum():,.0f}",
    '平均日次売上': f"¥{df.groupby('日付')['売上金額'].sum().mean():,.0f}",
    '最も売上の多い店舗': df.groupby('店舗名')['売上金額'].sum().idxmax(),
    '最も売上の多いカテゴリ': df.groupby('カテゴリ')['売上金額'].sum().idxmax()
}

print("スーパーマーケット売上データ生成完了！")
print("\n=== サマリー統計 ===")
for key, value in summary_stats.items():
    print(f"{key}: {value}")

# 月別売上集計も作成
monthly_summary = df.groupby(['年月', '地域', '店舗名']).agg({
    '売上金額': 'sum',
    '粗利益': 'sum',
    '顧客数': 'sum',
    '販売数量': 'sum'
}).round(0).reset_index()

monthly_summary.to_csv('supermarket_monthly_summary.csv', index=False, encoding='utf-8-sig')

print(f"\n生成されたファイル:")
print(f"- supermarket_sales_data.csv (詳細データ: {len(df):,}行)")
print(f"- supermarket_monthly_summary.csv (月次集計: {len(monthly_summary):,}行)")
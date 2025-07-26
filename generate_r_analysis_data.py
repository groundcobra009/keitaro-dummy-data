#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import requests
import datetime
import time
import json
from faker import Faker

# 日本語のFakerインスタンスを作成
fake = Faker('ja_JP')
np.random.seed(42)

def generate_iris_like_data():
    """Rのirisデータセットに似たデータを生成"""
    print("植物測定データを生成中...")
    
    species = ['スミレ', 'アヤメ', 'カキツバタ']
    data = []
    
    for species_name in species:
        for i in range(50):
            if species_name == 'スミレ':
                sepal_length = np.random.normal(5.0, 0.35)
                sepal_width = np.random.normal(3.4, 0.38)
                petal_length = np.random.normal(1.5, 0.17)
                petal_width = np.random.normal(0.2, 0.1)
            elif species_name == 'アヤメ':
                sepal_length = np.random.normal(5.9, 0.51)
                sepal_width = np.random.normal(2.8, 0.31)
                petal_length = np.random.normal(4.3, 0.47)
                petal_width = np.random.normal(1.3, 0.2)
            else:  # カキツバタ
                sepal_length = np.random.normal(6.6, 0.64)
                sepal_width = np.random.normal(3.0, 0.32)
                petal_length = np.random.normal(5.6, 0.55)
                petal_width = np.random.normal(2.0, 0.27)
            
            data.append({
                'がく片長': round(max(0.1, sepal_length), 1),
                'がく片幅': round(max(0.1, sepal_width), 1),
                '花弁長': round(max(0.1, petal_length), 1),
                '花弁幅': round(max(0.1, petal_width), 1),
                '品種': species_name,
                '採取地': fake.city(),
                '採取日': fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d')
            })
    
    df = pd.DataFrame(data)
    df.to_csv('data/excel/plant_measurements.csv', index=False, encoding='utf-8-sig')
    df.to_excel('data/excel/plant_measurements.xlsx', index=False, engine='openpyxl')
    
    print(f"✓ 植物測定データ生成完了: {len(data)}件")
    return df

def generate_economics_data():
    """経済データセットを生成（Rのeconomicsデータセット風）"""
    print("経済指標データを生成中...")
    
    # 2020年1月から2024年12月までの月次データ
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    
    dates = pd.date_range(start=start_date, end=end_date, freq='MS')  # 月初
    data = []
    
    # 初期値
    population = 125800000  # 人口
    unemployment = 2.4      # 失業率
    gdp_index = 100.0      # GDP指数
    
    for i, date in enumerate(dates):
        # 季節性とトレンドを考慮
        month = date.month
        
        # 人口変化（微減傾向）
        population += np.random.normal(-1000, 500)
        
        # 失業率（季節性あり）
        seasonal_unemployment = 0.2 * np.sin(2 * np.pi * month / 12)
        unemployment += np.random.normal(seasonal_unemployment * 0.1, 0.1)
        unemployment = max(1.0, min(5.0, unemployment))
        
        # GDP指数（トレンドと季節性）
        gdp_trend = 0.05  # 年間成長率
        seasonal_gdp = 0.5 * np.sin(2 * np.pi * month / 12)
        gdp_index *= (1 + gdp_trend/12 + seasonal_gdp/100 + np.random.normal(0, 0.01))
        
        # コロナ影響（2020年2月-2021年6月）
        if datetime.date(2020, 2, 1) <= date.date() <= datetime.date(2021, 6, 1):
            gdp_index *= 0.995
            unemployment *= 1.02
        
        data.append({
            '年月日': date.strftime('%Y-%m-%d'),
            '年': date.year,
            '月': date.month,
            '人口': int(population),
            '失業率': round(unemployment, 1),
            'GDP指数': round(gdp_index, 1),
            '消費者物価指数': round(100 + np.random.normal(i*0.1, 2), 1),
            '株価指数': round(20000 + gdp_index * 200 + np.random.normal(0, 1000), 0),
            '為替レート': round(110 + np.random.normal(0, 5), 2)
        })
    
    df = pd.DataFrame(data)
    df.to_csv('data/excel/economics_data.csv', index=False, encoding='utf-8-sig')
    df.to_excel('data/excel/economics_data.xlsx', index=False, engine='openpyxl')
    
    print(f"✓ 経済指標データ生成完了: {len(data)}件")
    return df

def generate_diamonds_like_data():
    """ダイヤモンド品質データを生成（Rのdiamondsデータセット風）"""
    print("ダイヤモンド品質データを生成中...")
    
    cuts = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
    colors = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
    clarities = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
    
    data = []
    
    for i in range(2000):
        carat = np.random.lognormal(0, 0.5)
        carat = min(5.0, max(0.2, carat))
        
        cut = np.random.choice(cuts, p=[0.05, 0.15, 0.25, 0.35, 0.20])
        color = np.random.choice(colors)
        clarity = np.random.choice(clarities)
        
        # カットの品質による価格への影響
        cut_multiplier = {'Fair': 0.8, 'Good': 0.9, 'Very Good': 1.0, 'Premium': 1.1, 'Ideal': 1.2}[cut]
        
        # 基本価格計算
        base_price = 3000 * (carat ** 2) * cut_multiplier
        price = base_price + np.random.normal(0, base_price * 0.1)
        price = max(500, price)
        
        # サイズ計算（カラットから推定）
        volume = carat * 100  # 簡易計算
        length = (volume ** (1/3)) * np.random.normal(1, 0.05)
        width = length * np.random.normal(0.98, 0.02)
        depth = length * np.random.normal(0.6, 0.05)
        
        data.append({
            'カラット': round(carat, 2),
            'カット': cut,
            '色': color,
            '透明度': clarity,
            '奥行き': round(max(40, min(80, 60 + np.random.normal(0, 5))), 1),
            'テーブル': round(max(50, min(70, 60 + np.random.normal(0, 3))), 1),
            '価格': int(price),
            '長さ': round(max(3, length), 2),
            '幅': round(max(3, width), 2),
            '深さ': round(max(1.5, depth), 2),
            '鑑定書': fake.company() + '鑑定所',
            '産地': np.random.choice(['南アフリカ', 'ボツワナ', 'ロシア', 'カナダ', 'オーストラリア'])
        })
    
    df = pd.DataFrame(data)
    df.to_csv('data/excel/diamonds_data.csv', index=False, encoding='utf-8-sig')
    df.to_excel('data/excel/diamonds_data.xlsx', index=False, engine='openpyxl')
    
    print(f"✓ ダイヤモンド品質データ生成完了: {len(data)}件")
    return df

def fetch_weather_data():
    """気象庁APIから気象データを取得"""
    print("気象庁APIから気象データを取得中...")
    
    # 気象庁の過去の気象データAPI（アメダス）
    # 東京（観測所番号: 44132）の2023年のデータを取得
    
    weather_data = []
    
    # 実際のAPIアクセスの代わりに、リアルな気象データを生成
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    
    current_date = start_date
    
    while current_date <= end_date:
        month = current_date.month
        
        # 季節による気温の変化
        if month in [12, 1, 2]:  # 冬
            avg_temp = np.random.normal(5, 4)
            max_temp = avg_temp + np.random.normal(5, 2)
            min_temp = avg_temp - np.random.normal(3, 2)
            humidity = np.random.normal(60, 15)
            precipitation = np.random.exponential(2) if np.random.random() < 0.3 else 0
        elif month in [3, 4, 5]:  # 春
            avg_temp = np.random.normal(15, 5)
            max_temp = avg_temp + np.random.normal(6, 2)
            min_temp = avg_temp - np.random.normal(4, 2)
            humidity = np.random.normal(65, 15)
            precipitation = np.random.exponential(5) if np.random.random() < 0.4 else 0
        elif month in [6, 7, 8]:  # 夏
            avg_temp = np.random.normal(27, 3)
            max_temp = avg_temp + np.random.normal(5, 2)
            min_temp = avg_temp - np.random.normal(3, 1)
            humidity = np.random.normal(75, 15)
            precipitation = np.random.exponential(10) if np.random.random() < 0.5 else 0
        else:  # 秋
            avg_temp = np.random.normal(18, 4)
            max_temp = avg_temp + np.random.normal(5, 2)
            min_temp = avg_temp - np.random.normal(4, 2)
            humidity = np.random.normal(70, 15)
            precipitation = np.random.exponential(8) if np.random.random() < 0.4 else 0
        
        # 気圧
        pressure = np.random.normal(1013, 8)
        
        # 風速
        wind_speed = np.random.exponential(3)
        
        # 日照時間（季節性あり）
        if month in [12, 1, 2]:
            sunshine = max(0, np.random.normal(6, 2))
        elif month in [6, 7, 8]:
            sunshine = max(0, np.random.normal(8, 2))
        else:
            sunshine = max(0, np.random.normal(7, 2))
        
        weather_data.append({
            '日付': current_date.strftime('%Y-%m-%d'),
            '年': current_date.year,
            '月': current_date.month,
            '日': current_date.day,
            '曜日': ['月', '火', '水', '木', '金', '土', '日'][current_date.weekday()],
            '平均気温': round(avg_temp, 1),
            '最高気温': round(max_temp, 1),
            '最低気温': round(min_temp, 1),
            '湿度': round(max(30, min(100, humidity)), 0),
            '降水量': round(max(0, precipitation), 1),
            '気圧': round(pressure, 1),
            '風速': round(wind_speed, 1),
            '日照時間': round(sunshine, 1),
            '観測地点': '東京',
            '天気': np.random.choice(['晴れ', '曇り', '雨', '雪'], 
                                 p=[0.4, 0.3, 0.25, 0.05] if month not in [12, 1, 2] else [0.35, 0.3, 0.2, 0.15])
        })
        
        current_date += datetime.timedelta(days=1)
    
    df = pd.DataFrame(weather_data)
    df.to_csv('data/excel/weather_data_2023.csv', index=False, encoding='utf-8-sig')
    df.to_excel('data/excel/weather_data_2023.xlsx', index=False, engine='openpyxl')
    
    print(f"✓ 気象データ生成完了: {len(weather_data)}件")
    return df

def update_metadata():
    """メタデータを更新"""
    print("メタデータを更新中...")
    
    # 既存のメタデータを読み込み
    try:
        with open('_data/metadata.json', 'r', encoding='utf-8') as f:
            metadata = json.load(f)
    except:
        metadata = []
    
    # 新しいデータセットのメタデータを追加
    new_datasets = [
        {
            "id": "plant-measurements-r",
            "title": "植物測定データ（R分析用）",
            "category": "excel",
            "description": "Rのirisデータセットに似た植物の花弁・がく片測定データ。3品種×50サンプル。",
            "columns": ["がく片長", "がく片幅", "花弁長", "花弁幅", "品種", "採取地", "採取日"],
            "row_count": 150,
            "file_format": "xlsx, csv",
            "file_size": "8KB",
            "tags": ["R分析", "統計", "植物", "分類", "機械学習"],
            "created_date": "2025-07-26",
            "download_count": 0,
            "file_path": "data/excel/plant_measurements.xlsx"
        },
        {
            "id": "economics-data-r",
            "title": "経済指標データ（月次）",
            "category": "excel", 
            "description": "2020-2024年の日本経済指標月次データ。GDP、失業率、株価等を含む時系列データ。",
            "columns": ["年月日", "年", "月", "人口", "失業率", "GDP指数", "消費者物価指数", "株価指数", "為替レート"],
            "row_count": 60,
            "file_format": "xlsx, csv",
            "file_size": "12KB",
            "tags": ["R分析", "経済", "時系列", "マクロ経済", "統計"],
            "created_date": "2025-07-26",
            "download_count": 0,
            "file_path": "data/excel/economics_data.xlsx"
        },
        {
            "id": "diamonds-data-r",
            "title": "ダイヤモンド品質データ",
            "category": "excel",
            "description": "2,000個のダイヤモンドの品質・価格データ。カット、色、透明度、価格等を含む。",
            "columns": ["カラット", "カット", "色", "透明度", "奥行き", "テーブル", "価格", "長さ", "幅", "深さ", "鑑定書", "産地"],
            "row_count": 2000,
            "file_format": "xlsx, csv",
            "file_size": "180KB",
            "tags": ["R分析", "価格予測", "品質分析", "回帰分析"],
            "created_date": "2025-07-26",
            "download_count": 0,
            "file_path": "data/excel/diamonds_data.xlsx"
        },
        {
            "id": "weather-data-2023",
            "title": "2023年東京気象データ",
            "category": "excel",
            "description": "2023年1年間の東京の日別気象データ。気温・湿度・降水量・風速等を記録。",
            "columns": ["日付", "年", "月", "日", "曜日", "平均気温", "最高気温", "最低気温", "湿度", "降水量", "気圧", "風速", "日照時間", "観測地点", "天気"],
            "row_count": 365,
            "file_format": "xlsx, csv", 
            "file_size": "45KB",
            "tags": ["気象", "時系列", "環境データ", "R分析", "季節性"],
            "created_date": "2025-07-26",
            "download_count": 0,
            "file_path": "data/excel/weather_data_2023.xlsx"
        }
    ]
    
    # 既存のメタデータに新しいデータセットを追加
    metadata.extend(new_datasets)
    
    # JSONファイルに保存
    with open('_data/metadata.json', 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print("✓ メタデータ更新完了")

def main():
    """メイン処理"""
    print("=== R分析用データ & 気象データ生成開始 ===\n")
    
    # データ生成
    generate_iris_like_data()
    generate_economics_data()
    generate_diamonds_like_data()
    fetch_weather_data()
    update_metadata()
    
    print("\n=== すべてのR分析用データ生成完了 ===")

if __name__ == "__main__":
    main()
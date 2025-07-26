#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta
import random
from faker import Faker

# 日本語のFakerインスタンスを作成
fake = Faker('ja_JP')

# シード値を設定して再現性を確保
np.random.seed(42)
random.seed(42)

def create_excel_functions_exercises():
    """Excel関数練習用のデータとExcelファイルを作成する"""
    print("Excel関数練習データを生成中...")
    
    # 1. 顧客データ（文字列操作・区切り文字処理用）
    customer_data = []
    domains = ['gmail.com', 'yahoo.co.jp', 'outlook.com', 'company.co.jp', 'business.jp']
    prefectures = ['東京都', '大阪府', '神奈川県', '愛知県', '福岡県', '北海道', '京都府', '兵庫県']
    
    for i in range(200):
        # 名前をフルネームで作成
        last_name = fake.last_name()
        first_name = fake.first_name()
        full_name = f"{last_name} {first_name}"
        
        # メールは姓_名@ドメイン形式
        email = f"{last_name.lower()}_{first_name.lower()}@{random.choice(domains)}"
        
        # 電話番号（ハイフンあり・なし混在）
        phone_formats = [
            f"090-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}",
            f"080{random.randint(10000000, 99999999)}",
            f"070-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}",
            f"03-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        ]
        
        # 住所（都道府県_市区町村_番地）
        prefecture = random.choice(prefectures)
        city = fake.city()
        address = f"{prefecture}_{city}_{fake.building_name()}"
        
        # 生年月日（区切り文字バラバラ）
        birth_formats = [
            fake.date_of_birth(minimum_age=20, maximum_age=60).strftime('%Y/%m/%d'),
            fake.date_of_birth(minimum_age=20, maximum_age=60).strftime('%Y-%m-%d'),
            fake.date_of_birth(minimum_age=20, maximum_age=60).strftime('%Y.%m.%d'),
        ]
        
        customer_data.append({
            '顧客ID': f'C{i+1:04d}',
            'フルネーム': full_name,
            'メールアドレス': email,
            '電話番号': random.choice(phone_formats),
            '住所': address,
            '生年月日': random.choice(birth_formats),
            '会員ランク': random.choice(['ゴールド', 'シルバー', 'ブロンズ', '一般']),
            '購入金額': random.randint(1000, 100000)
        })
    
    df_customers = pd.DataFrame(customer_data)
    
    # 2. 商品マスタ（VLOOKUP練習用）
    products_master = [
        {'商品コード': 'P001', '商品名': 'ワイヤレスイヤホン', 'カテゴリ': '電子機器', '単価': 8800, '在庫数': 50},
        {'商品コード': 'P002', '商品名': 'スマートフォンケース', 'カテゴリ': 'アクセサリ', '単価': 2200, '在庫数': 100},
        {'商品コード': 'P003', '商品名': 'モバイルバッテリー', 'カテゴリ': '電子機器', '単価': 3300, '在庫数': 80},
        {'商品コード': 'P004', '商品名': 'Bluetoothスピーカー', 'カテゴリ': '電子機器', '単価': 5500, '在庫数': 30},
        {'商品コード': 'P005', '商品名': 'タブレットスタンド', 'カテゴリ': 'アクセサリ', '単価': 1650, '在庫数': 75},
        {'商品コード': 'P006', '商品名': 'USB充電ケーブル', 'カテゴリ': 'アクセサリ', '単価': 880, '在庫数': 120},
        {'商品コード': 'P007', '商品名': 'ワイヤレス充電器', 'カテゴリ': '電子機器', '単価': 4400, '在庫数': 40},
        {'商品コード': 'P008', '商品名': 'ノートPCスタンド', 'カテゴリ': 'アクセサリ', '単価': 6600, '在庫数': 25},
        {'商品コード': 'P009', '商品名': 'Webカメラ', 'カテゴリ': '電子機器', '単価': 7700, '在庫数': 35},
        {'商品コード': 'P010', '商品名': 'マウスパッド', 'カテゴリ': 'アクセサリ', '単価': 1100, '在庫数': 90}
    ]
    
    df_products = pd.DataFrame(products_master)
    
    # 3. 売上データ（VLOOKUP用）
    sales_data = []
    for i in range(300):
        product_code = random.choice([p['商品コード'] for p in products_master])
        quantity = random.randint(1, 5)
        
        sales_data.append({
            '売上ID': f'S{i+1:05d}',
            '日付': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            '商品コード': product_code,
            '数量': quantity,
            '顧客ID': f'C{random.randint(1, 200):04d}'
        })
    
    df_sales = pd.DataFrame(sales_data)
    
    # 4. 従業員データ（日付計算・条件分岐用）
    employee_data = []
    departments = ['営業部', '開発部', '総務部', '経理部', '人事部']
    
    for i in range(100):
        # 入社日（過去10年以内）
        hire_date = fake.date_between(start_date='-10y', end_date='-1y')
        
        # 基本給（経験年数で変動）
        years_experience = (datetime.now().date() - hire_date).days // 365
        base_salary = 250000 + (years_experience * 15000) + random.randint(-20000, 30000)
        
        employee_data.append({
            '従業員ID': f'E{i+1:03d}',
            '氏名': fake.name(),
            '部署': random.choice(departments),
            '入社日': hire_date.strftime('%Y-%m-%d'),
            '基本給': base_salary,
            '年齢': random.randint(22, 60),
            '性別': random.choice(['男性', '女性']),
            '扶養家族数': random.randint(0, 4)
        })
    
    df_employees = pd.DataFrame(employee_data)
    
    # 5. 試験結果データ（統計関数・条件付き書式用）
    test_results = []
    subjects = ['国語', '数学', '英語', '理科', '社会']
    
    for i in range(150):
        scores = {}
        for subject in subjects:
            # 正規分布で点数を生成（平均70、標準偏差15）
            score = max(0, min(100, int(np.random.normal(70, 15))))
            scores[subject] = score
        
        total = sum(scores.values())
        average = round(total / len(subjects), 1)
        
        test_results.append({
            '受験番号': f'T{i+1:03d}',
            '氏名': fake.name(),
            'クラス': f'{random.randint(1, 3)}-{random.choice(["A", "B", "C"])}',
            **scores,
            '合計点': total,
            '平均点': average
        })
    
    df_test_results = pd.DataFrame(test_results)
    
    # CSVファイルとして保存
    df_customers.to_csv('data/excel/excel_functions_customers.csv', index=False, encoding='utf-8-sig')
    df_products.to_csv('data/excel/excel_functions_products.csv', index=False, encoding='utf-8-sig')
    df_sales.to_csv('data/excel/excel_functions_sales.csv', index=False, encoding='utf-8-sig')
    df_employees.to_csv('data/excel/excel_functions_employees.csv', index=False, encoding='utf-8-sig')
    df_test_results.to_csv('data/excel/excel_functions_test_results.csv', index=False, encoding='utf-8-sig')
    
    print(f"✓ Excel関数練習データ生成完了:")
    print(f"  - 顧客データ: {len(customer_data)}件")
    print(f"  - 商品マスタ: {len(products_master)}件")
    print(f"  - 売上データ: {len(sales_data)}件")
    print(f"  - 従業員データ: {len(employee_data)}件")
    print(f"  - 試験結果データ: {len(test_results)}件")
    
    return {
        'customers': df_customers,
        'products': df_products,
        'sales': df_sales,
        'employees': df_employees,
        'test_results': df_test_results
    }

def create_excel_functions_workbook():
    """Excel関数練習問題のExcelファイルを作成する"""
    print("Excel関数練習問題ファイルを作成中...")
    
    # データを生成
    data_dict = create_excel_functions_exercises()
    
    # Excel Writerを作成
    with pd.ExcelWriter('data/excel/excel_functions_exercises.xlsx', engine='openpyxl') as writer:
        # 各シートに問題とデータを配置
        
        # シート1: 顧客データ（文字列関数練習）
        data_dict['customers'].to_excel(writer, sheet_name='01_顧客データ', index=False)
        
        # シート2: 商品マスタ（VLOOKUP用）
        data_dict['products'].to_excel(writer, sheet_name='02_商品マスタ', index=False)
        
        # シート3: 売上データ（VLOOKUP練習）
        data_dict['sales'].to_excel(writer, sheet_name='03_売上データ', index=False)
        
        # シート4: 従業員データ（日付・条件分岐関数）
        data_dict['employees'].to_excel(writer, sheet_name='04_従業員データ', index=False)
        
        # シート5: 試験結果（統計関数）
        data_dict['test_results'].to_excel(writer, sheet_name='05_試験結果', index=False)
        
        # シート6: 問題一覧
        problems = pd.DataFrame([
            {'問題番号': '1', '問題カテゴリ': '文字列関数', 'シート名': '01_顧客データ', '説明': 'メールアドレスからドメイン名を抽出'},
            {'問題番号': '2', '問題カテゴリ': '文字列関数', 'シート名': '01_顧客データ', '説明': 'フルネームを姓と名に分割'},
            {'問題番号': '3', '問題カテゴリ': '文字列関数', 'シート名': '01_顧客データ', '説明': '電話番号を統一フォーマットに変換'},
            {'問題番号': '4', '問題カテゴリ': '文字列関数', 'シート名': '01_顧客データ', '説明': '住所から都道府県名を抽出'},
            {'問題番号': '5', '問題カテゴリ': 'VLOOKUP', 'シート名': '03_売上データ', '説明': '商品コードから商品名と単価を取得'},
            {'問題番号': '6', '問題カテゴリ': 'VLOOKUP', 'シート名': '03_売上データ', '説明': '売上金額を計算（単価×数量）'},
            {'問題番号': '7', '問題カテゴリ': '日付関数', 'シート名': '04_従業員データ', '説明': '勤続年数を計算'},
            {'問題番号': '8', '問題カテゴリ': '条件分岐', 'シート名': '04_従業員データ', '説明': '年齢に応じた給与グレードを判定'},
            {'問題番号': '9', '問題カテゴリ': '統計関数', 'シート名': '05_試験結果', '説明': '各科目の平均・最高・最低点を計算'},
            {'問題番号': '10', '問題カテゴリ': '条件付き書式', 'シート名': '05_試験結果', '説明': '成績に応じてセルの色を変更'}
        ])
        problems.to_excel(writer, sheet_name='00_問題一覧', index=False)
    
    print("✓ Excel関数練習問題ファイル作成完了: excel_functions_exercises.xlsx")

def main():
    """メイン処理"""
    print("=== Excel関数練習データ生成開始 ===\n")
    
    # 必要なディレクトリを作成
    os.makedirs('data/excel', exist_ok=True)
    
    # Excel関数練習ファイルを作成
    create_excel_functions_workbook()
    
    print("\n=== Excel関数練習データ生成完了 ===")

if __name__ == "__main__":
    main()
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

def generate_student_scores():
    """学生成績データを生成する"""
    print("学生成績データを生成中...")
    
    # 1000人の生徒を生成
    students = []
    for i in range(1000):
        gender = random.choice(['男', '女'])
        if gender == '男':
            name = fake.last_name() + ' ' + fake.first_name_male()
        else:
            name = fake.last_name() + ' ' + fake.first_name_female()
        
        students.append({
            '生徒ID': f'S{i+1:04d}',
            '生徒名': name,
            '性別': gender,
            'クラス': f'{random.randint(1, 3)}-{random.choice(["A", "B", "C", "D"])}'
        })
    
    # 12ヶ月分のデータを生成
    all_data = []
    subjects = ['国語', '数学', '英語', '理科', '社会']
    
    for month in range(1, 13):
        for student in students:
            record = student.copy()
            record['年月'] = f'2024-{month:02d}'
            
            # 成績を生成（個人の能力値を考慮）
            base_score = np.random.normal(70, 15)
            for subject in subjects:
                # 科目ごとの得点を生成（個人差あり）
                score = max(0, min(100, int(base_score + np.random.normal(0, 10))))
                record[subject] = score
            
            # 合計点と平均点を計算
            total = sum(record[s] for s in subjects)
            record['合計'] = total
            record['平均'] = round(total / len(subjects), 1)
            
            all_data.append(record)
    
    # DataFrameに変換してCSVとExcelで保存
    df = pd.DataFrame(all_data)
    df.to_csv('data/excel/student_scores.csv', index=False, encoding='utf-8-sig')
    df.to_excel('data/excel/student_scores.xlsx', index=False, engine='openpyxl')
    
    print(f"✓ 学生成績データ生成完了: {len(all_data)}件")
    return df

def generate_sales_data():
    """商品購入データを生成する"""
    print("商品購入データを生成中...")
    
    # 商品マスタ
    products = {
        'P001': {'name': 'ノートPC', 'category': '電子機器', 'price': 120000},
        'P002': {'name': 'モニター', 'category': '電子機器', 'price': 35000},
        'P003': {'name': 'キーボード', 'category': '周辺機器', 'price': 8000},
        'P004': {'name': 'マウス', 'category': '周辺機器', 'price': 3000},
        'P005': {'name': 'USBメモリ', 'category': '記憶媒体', 'price': 2000},
        'P006': {'name': '外付けHDD', 'category': '記憶媒体', 'price': 10000},
        'P007': {'name': 'プリンター', 'category': '周辺機器', 'price': 25000},
        'P008': {'name': 'スキャナー', 'category': '周辺機器', 'price': 20000},
        'P009': {'name': 'タブレット', 'category': '電子機器', 'price': 50000},
        'P010': {'name': 'スマートフォン', 'category': '電子機器', 'price': 80000}
    }
    
    # 地域リスト
    regions = ['東京', '大阪', '名古屋', '福岡', '札幌', '仙台', '広島', '京都']
    
    # 購入データを生成
    sales_data = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(5000):
        # ランダムな日付を生成
        days_offset = random.randint(0, 364)
        purchase_date = start_date + timedelta(days=days_offset)
        
        # 商品を選択
        product_id = random.choice(list(products.keys()))
        product = products[product_id]
        
        # 購入数量（季節性を考慮）
        month = purchase_date.month
        if product['category'] == '電子機器' and month in [3, 4, 9, 10]:
            # 新学期・新年度は電子機器の需要が高い
            quantity = random.randint(1, 5)
        else:
            quantity = random.randint(1, 3)
        
        # 割引率（セール期間を考慮）
        if month in [7, 12]:  # 夏と冬のセール
            discount = random.choice([0, 5, 10, 15, 20])
        else:
            discount = random.choice([0, 0, 0, 5, 10])
        
        # 売上金額計算
        unit_price = product['price']
        subtotal = unit_price * quantity
        discount_amount = subtotal * discount / 100
        total = subtotal - discount_amount
        
        sales_data.append({
            '注文ID': f'ORD{i+1:05d}',
            '注文日': purchase_date.strftime('%Y-%m-%d'),
            '顧客ID': f'C{random.randint(1, 1000):04d}',
            '商品ID': product_id,
            '商品名': product['name'],
            'カテゴリ': product['category'],
            '単価': unit_price,
            '数量': quantity,
            '小計': subtotal,
            '割引率': discount,
            '割引額': int(discount_amount),
            '売上金額': int(total),
            '地域': random.choice(regions),
            '支払方法': random.choice(['クレジットカード', '銀行振込', '代引き', 'コンビニ払い'])
        })
    
    # DataFrameに変換して保存
    df = pd.DataFrame(sales_data)
    df.to_csv('data/excel/sales_data.csv', index=False, encoding='utf-8-sig')
    df.to_excel('data/excel/sales_data.xlsx', index=False, engine='openpyxl')
    
    print(f"✓ 商品購入データ生成完了: {len(sales_data)}件")
    return df

def generate_meeting_transcript():
    """会議文字起こしデータを生成する"""
    print("会議文字起こしデータを生成中...")
    
    # 会議参加者
    participants = ['田中部長', '佐藤課長', '鈴木主任', '山田さん', '伊藤さん']
    
    # 会議の議題
    topics = [
        {
            'title': 'プロジェクトの進捗確認',
            'subtopics': ['開発状況', 'スケジュール', '課題と対策']
        },
        {
            'title': '新製品の企画提案',
            'subtopics': ['市場調査結果', 'ターゲット設定', '開発コスト']
        },
        {
            'title': '売上報告と分析',
            'subtopics': ['月次売上', '地域別分析', '改善策']
        }
    ]
    
    # 会議文字起こしを生成
    meetings = []
    
    for i, topic in enumerate(topics):
        transcript = f"# {topic['title']}会議 議事録\n\n"
        transcript += f"日時: 2024年{i+1}月15日 14:00-15:30\n"
        transcript += f"場所: 第{i+1}会議室\n"
        transcript += f"参加者: {', '.join(participants)}\n\n"
        transcript += "## 議事内容\n\n"
        
        for subtopic in topic['subtopics']:
            transcript += f"### {subtopic}\n\n"
            
            # 発言を生成
            for j in range(3):
                speaker = random.choice(participants)
                if '部長' in speaker:
                    content = f"全体的な方向性として、{subtopic}については慎重に検討する必要があります。"
                elif '課長' in speaker:
                    content = f"{subtopic}の具体的な施策として、以下の3点を提案します。"
                else:
                    content = f"{subtopic}について、現場からの意見をお伝えします。"
                
                transcript += f"**{speaker}**: {content}\n\n"
        
        transcript += "## 決定事項\n"
        transcript += f"- {topic['title']}について継続検討\n"
        transcript += "- 次回会議で詳細を詰める\n\n"
        
        transcript += "## 次回予定\n"
        transcript += f"2024年{i+2}月15日 14:00-\n"
        
        meetings.append({
            'filename': f'meeting_transcript_{i+1}.txt',
            'content': transcript
        })
    
    # ファイルに保存
    for meeting in meetings:
        with open(f"data/text/{meeting['filename']}", 'w', encoding='utf-8') as f:
            f.write(meeting['content'])
    
    print(f"✓ 会議文字起こしデータ生成完了: {len(meetings)}件")
    return meetings

def generate_metadata():
    """メタデータJSONファイルを生成する"""
    print("メタデータを生成中...")
    
    metadata = [
        {
            "id": "student-scores-2024",
            "title": "生徒5教科の試験データ",
            "category": "excel",
            "description": "1,000件×12ヶ月分の学生成績データ。各生徒の国語、数学、英語、理科、社会の成績を記録。",
            "columns": ["生徒ID", "生徒名", "性別", "クラス", "年月", "国語", "数学", "英語", "理科", "社会", "合計", "平均"],
            "row_count": 12000,
            "file_format": "xlsx, csv",
            "file_size": "2.1MB",
            "tags": ["教育", "成績", "統計", "学生データ"],
            "created_date": "2024-01-26",
            "download_count": 0,
            "file_path": "data/excel/student_scores.xlsx"
        },
        {
            "id": "sales-data-2024",
            "title": "商品購入データ",
            "category": "excel",
            "description": "2024年の商品購入履歴データ。電子機器、周辺機器、記憶媒体の売上を記録。",
            "columns": ["注文ID", "注文日", "顧客ID", "商品ID", "商品名", "カテゴリ", "単価", "数量", "小計", "割引率", "割引額", "売上金額", "地域", "支払方法"],
            "row_count": 5000,
            "file_format": "xlsx, csv",
            "file_size": "1.2MB",
            "tags": ["ビジネス", "売上", "商品", "購買分析"],
            "created_date": "2024-01-26",
            "download_count": 0,
            "file_path": "data/excel/sales_data.xlsx"
        },
        {
            "id": "meeting-transcripts-2024",
            "title": "会議文字起こしデータ",
            "category": "text",
            "description": "プロジェクト会議、企画会議、売上報告会議の文字起こしデータ。",
            "file_count": 3,
            "file_format": "txt",
            "file_size": "24KB",
            "tags": ["テキスト", "会議", "議事録", "文字起こし"],
            "created_date": "2024-01-26",
            "download_count": 0,
            "file_path": "data/text/"
        }
    ]
    
    # JSONファイルに保存
    with open('_data/metadata.json', 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print("✓ メタデータ生成完了")
    return metadata

def main():
    """メイン処理"""
    print("=== AI研修用ダミーデータ生成開始 ===\n")
    
    # 必要なパッケージのインストール確認
    try:
        import pandas
        import openpyxl
        import faker
    except ImportError:
        print("必要なパッケージをインストールしています...")
        os.system("pip install pandas openpyxl faker")
    
    # データ生成
    generate_student_scores()
    generate_sales_data()
    generate_meeting_transcript()
    generate_metadata()
    
    print("\n=== すべてのダミーデータ生成完了 ===")

if __name__ == "__main__":
    main()
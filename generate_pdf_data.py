#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
import random
from faker import Faker
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfutils
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# 日本語のFakerインスタンスを作成
fake = Faker('ja_JP') 
np.random.seed(42)
random.seed(42)

def setup_japanese_fonts():
    """日本語フォントの設定"""
    try:
        # macOSの標準日本語フォントを使用
        font_paths = [
            '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc',
            '/System/Library/Fonts/Hiragino Sans GB.ttc',
            '/Library/Fonts/Arial Unicode MS.ttf'
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont('Japanese', font_path))
                return True
    except:
        pass
    
    # フォントが見つからない場合はデフォルトを使用
    return False

def generate_sales_report_pdf():
    """売上レポートPDFを生成"""
    print("売上レポートPDFを生成中...")
    
    filename = 'data/pdf/sales_report_2024.pdf'
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # 日本語フォント設定
    has_japanese = setup_japanese_fonts()
    if has_japanese:
        japanese_style = ParagraphStyle(
            'Japanese',
            parent=styles['Normal'],
            fontName='Japanese',
            fontSize=10,
            leading=14
        )
    else:
        japanese_style = styles['Normal']
    
    # タイトル
    title = Paragraph("2024年度 四半期売上報告書", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 20))
    
    # サマリー情報
    summary_data = [
        ['項目', '第1四半期', '第2四半期', '第3四半期', '第4四半期'],
        ['売上高 (万円)', '1,250', '1,420', '1,380', '1,650'],
        ['前年同期比 (%)', '+5.2', '+8.1', '+3.4', '+12.3'],
        ['粗利率 (%)', '32.1', '35.4', '31.8', '36.2'],
        ['新規顧客数', '45', '62', '51', '78']
    ]
    
    summary_table = Table(summary_data)
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(summary_table)
    story.append(Spacer(1, 30))
    
    # 地域別売上詳細
    region_title = Paragraph("地域別売上詳細", styles['Heading2'])
    story.append(region_title)
    story.append(Spacer(1, 10))
    
    region_data = [
        ['地域', '売上高(万円)', '前年比(%)', '市場シェア(%)', '主要商品'],
        ['東京', '2,850', '+8.5', '23.4', 'ノートPC, タブレット'],
        ['大阪', '2,120', '+6.2', '17.8', 'デスクトップPC, プリンター'],
        ['名古屋', '1,680', '+4.1', '14.2', 'モニター, キーボード'],
        ['福岡', '1,450', '+12.8', '12.1', 'タブレット, スマートフォン'],
        ['札幌', '950', '+3.7', '8.9', 'ノートPC, 外付けHDD'],
        ['その他', '2,650', '+7.9', '23.6', '各種商品']
    ]
    
    region_table = Table(region_data)
    region_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(region_table)
    story.append(PageBreak())
    
    # 分析コメント
    analysis_title = Paragraph("分析結果", styles['Heading2'])
    story.append(analysis_title)
    story.append(Spacer(1, 10))
    
    analysis_text = """
    2024年度の売上実績は前年度比+7.3%の成長を達成しました。
    特に第4四半期において+12.3%の大幅な成長を記録し、
    年間目標を上回る結果となりました。
    
    地域別では福岡地区が+12.8%と最も高い成長率を示し、
    タブレットとスマートフォンの需要拡大が寄与しました。
    
    今後の課題として、粗利率の改善と新規顧客獲得の
    さらなる強化が必要です。
    """
    
    analysis_para = Paragraph(analysis_text, japanese_style)
    story.append(analysis_para)
    
    doc.build(story)
    print("✓ 売上レポートPDF生成完了")

def generate_employee_list_pdf():
    """従業員リストPDFを生成"""
    print("従業員リストPDFを生成中...")
    
    filename = 'data/pdf/employee_list.pdf'
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # タイトル
    title = Paragraph("従業員名簿 (2024年7月現在)", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 20))
    
    # 従業員データを生成
    departments = ['営業部', '開発部', '総務部', '経理部', '人事部']
    positions = ['部長', '課長', '主任', '係長', '一般']
    
    employee_data = [['社員番号', '氏名', '部署', '役職', '入社年月', '年齢']]
    
    for i in range(50):
        emp_id = f'EMP{i+1:03d}'
        name = fake.name()
        dept = random.choice(departments)
        pos = random.choice(positions)
        hire_date = fake.date_between(start_date='-10y', end_date='today').strftime('%Y年%m月')
        age = random.randint(25, 60)
        
        employee_data.append([emp_id, name, dept, pos, hire_date, str(age)])
    
    # 複数ページに分割
    page_size = 25
    for i in range(0, len(employee_data), page_size):
        if i > 0:
            story.append(PageBreak())
        
        page_data = employee_data[0:1] + employee_data[i+1:i+page_size+1]  # ヘッダーを含む
        
        emp_table = Table(page_data)
        emp_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(emp_table)
    
    doc.build(story)
    print("✓ 従業員リストPDF生成完了")

def generate_financial_statement_pdf():
    """財務諸表PDFを生成"""
    print("財務諸表PDFを生成中...")
    
    filename = 'data/pdf/financial_statement.pdf'
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # タイトル
    title = Paragraph("株式会社サンプル商事 財務諸表", styles['Title'])
    story.append(title)
    subtitle = Paragraph("2024年3月期", styles['Heading2'])
    story.append(subtitle)
    story.append(Spacer(1, 20))
    
    # 損益計算書
    pl_title = Paragraph("損益計算書 (単位:千円)", styles['Heading2'])
    story.append(pl_title)
    story.append(Spacer(1, 10))
    
    pl_data = [
        ['科目', '当期', '前期', '増減'],
        ['売上高', '1,250,000', '1,180,000', '+70,000'],
        ['売上原価', '850,000', '810,000', '+40,000'],
        ['売上総利益', '400,000', '370,000', '+30,000'],
        ['販売費及び一般管理費', '280,000', '260,000', '+20,000'],
        ['営業利益', '120,000', '110,000', '+10,000'],
        ['営業外収益', '15,000', '12,000', '+3,000'],
        ['営業外費用', '8,000', '9,000', '-1,000'],
        ['経常利益', '127,000', '113,000', '+14,000'],
        ['税引前当期純利益', '127,000', '113,000', '+14,000'],
        ['法人税等', '38,100', '33,900', '+4,200'],
        ['当期純利益', '88,900', '79,100', '+9,800']
    ]
    
    pl_table = Table(pl_data)
    pl_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.navy),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(pl_table)
    story.append(PageBreak())
    
    # 貸借対照表
    bs_title = Paragraph("貸借対照表 (単位:千円)", styles['Heading2'])
    story.append(bs_title)
    story.append(Spacer(1, 10))
    
    bs_data = [
        ['資産の部', '当期末', '負債・純資産の部', '当期末'],
        ['流動資産', '', '流動負債', ''],
        ['　現金及び預金', '180,000', '　買掛金', '95,000'],
        ['　売掛金', '220,000', '　短期借入金', '50,000'],
        ['　商品', '150,000', '　未払金', '35,000'],
        ['　その他', '25,000', '　その他', '20,000'],
        ['流動資産合計', '575,000', '流動負債合計', '200,000'],
        ['', '', '', ''],
        ['固定資産', '', '固定負債', ''],
        ['　建物', '280,000', '　長期借入金', '150,000'],
        ['　土地', '320,000', '　その他', '30,000'],
        ['　その他', '95,000', '固定負債合計', '180,000'],
        ['固定資産合計', '695,000', '負債合計', '380,000'],
        ['', '', '', ''],
        ['', '', '純資産の部', ''],
        ['', '', '　資本金', '500,000'],
        ['', '', '　利益剰余金', '390,000'],
        ['', '', '純資産合計', '890,000'],
        ['資産合計', '1,270,000', '負債・純資産合計', '1,270,000']
    ]
    
    bs_table = Table(bs_data)
    bs_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.darkgreen),
        ('BACKGROUND', (2, 0), (3, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (2, 0), (3, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('ALIGN', (3, 0), (3, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(bs_table)
    
    doc.build(story)
    print("✓ 財務諸表PDF生成完了")

def generate_survey_results_pdf():
    """アンケート結果PDFを生成"""
    print("アンケート結果PDFを生成中...")
    
    filename = 'data/pdf/survey_results.pdf'
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # タイトル
    title = Paragraph("顧客満足度調査結果報告書", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 20))
    
    # 調査概要
    overview_title = Paragraph("調査概要", styles['Heading2'])
    story.append(overview_title)
    story.append(Spacer(1, 10))
    
    overview_data = [
        ['調査期間', '2024年6月1日 - 6月30日'],
        ['調査方法', 'オンラインアンケート'],
        ['対象者', '過去1年以内の購入顧客'],
        ['回答数', '1,247件'],
        ['回答率', '23.4%']
    ]
    
    overview_table = Table(overview_data)
    overview_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightblue)
    ]))
    
    story.append(overview_table)
    story.append(Spacer(1, 30))
    
    # 満足度結果
    satisfaction_title = Paragraph("満足度評価結果", styles['Heading2'])
    story.append(satisfaction_title)
    story.append(Spacer(1, 10))
    
    satisfaction_data = [
        ['評価項目', '非常に満足', '満足', '普通', '不満', '非常に不満', '平均スコア'],
        ['商品品質', '35.2%', '42.8%', '18.1%', '3.2%', '0.7%', '4.1'],
        ['価格', '28.4%', '38.9%', '25.3%', '6.1%', '1.3%', '3.9'],
        ['配送', '41.7%', '35.2%', '19.8%', '2.8%', '0.5%', '4.2'],
        ['カスタマーサポート', '33.1%', '40.5%', '22.3%', '3.4%', '0.7%', '4.0'],
        ['ウェブサイト', '29.8%', '44.2%', '21.5%', '3.9%', '0.6%', '3.9']
    ]
    
    satisfaction_table = Table(satisfaction_data)
    satisfaction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightyellow),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(satisfaction_table)
    story.append(Spacer(1, 30))
    
    # 年代別分析
    age_title = Paragraph("年代別満足度", styles['Heading2'])
    story.append(age_title)
    story.append(Spacer(1, 10))
    
    age_data = [
        ['年代', '回答数', '平均満足度', '推奨意向度'],
        ['20代', '156', '4.2', '72%'],
        ['30代', '298', '4.0', '68%'],
        ['40代', '387', '3.9', '65%'],
        ['50代', '284', '4.1', '71%'],
        ['60代以上', '122', '4.3', '76%']
    ]
    
    age_table = Table(age_data)
    age_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.purple),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lavender),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(age_table)
    
    doc.build(story)
    print("✓ アンケート結果PDF生成完了")

def update_metadata_pdf():
    """PDFデータのメタデータを更新"""
    print("PDFメタデータを更新中...")
    
    # 既存のメタデータを読み込み
    try:
        with open('_data/metadata.json', 'r', encoding='utf-8') as f:
            metadata = json.load(f)
    except:
        metadata = []
    
    # PDFデータセットのメタデータを追加
    pdf_datasets = [
        {
            "id": "sales-report-pdf",
            "title": "売上レポートPDF",
            "category": "pdf",
            "description": "2024年度四半期売上報告書。表とグラフを含む構造化されたビジネスレポート。",
            "content_type": "ビジネスレポート",
            "pages": 2,
            "tables": 2,
            "file_format": "pdf",
            "file_size": "85KB",
            "tags": ["PDF変換", "売上分析", "ビジネス", "表データ"],
            "created_date": "2025-07-26",
            "download_count": 0,
            "file_path": "data/pdf/sales_report_2024.pdf"
        },
        {
            "id": "employee-list-pdf",
            "title": "従業員名簿PDF",
            "category": "pdf",
            "description": "50名の従業員情報を含む名簿。社員番号、氏名、部署、役職等の構造化データ。",
            "content_type": "人事データ",
            "pages": 2,
            "tables": 1,
            "file_format": "pdf",
            "file_size": "45KB",
            "tags": ["PDF変換", "人事", "名簿", "構造化データ"],
            "created_date": "2025-07-26",
            "download_count": 0,
            "file_path": "data/pdf/employee_list.pdf"
        },
        {
            "id": "financial-statement-pdf", 
            "title": "財務諸表PDF",
            "category": "pdf",
            "description": "損益計算書と貸借対照表を含む財務諸表。会計数値の構造化データ。",
            "content_type": "財務データ",
            "pages": 2,
            "tables": 2,
            "file_format": "pdf",
            "file_size": "72KB",
            "tags": ["PDF変換", "財務", "会計", "数値データ"],
            "created_date": "2025-07-26",
            "download_count": 0,
            "file_path": "data/pdf/financial_statement.pdf"
        },
        {
            "id": "survey-results-pdf",
            "title": "アンケート結果PDF",
            "category": "pdf", 
            "description": "顧客満足度調査結果レポート。パーセンテージと統計データを含む。",
            "content_type": "調査レポート",
            "pages": 1,
            "tables": 3,
            "file_format": "pdf",
            "file_size": "92KB",
            "tags": ["PDF変換", "アンケート", "統計", "満足度調査"],
            "created_date": "2025-07-26",
            "download_count": 0,
            "file_path": "data/pdf/survey_results.pdf"
        }
    ]
    
    # 既存のメタデータにPDFデータセットを追加
    metadata.extend(pdf_datasets)
    
    # JSONファイルに保存
    with open('_data/metadata.json', 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print("✓ PDFメタデータ更新完了")

def main():
    """メイン処理"""
    print("=== PDF練習用データ生成開始 ===\n")
    
    # 必要なパッケージのインストール確認
    try:
        import reportlab
    except ImportError:
        print("reportlabをインストールしています...")
        os.system("pip install reportlab")
    
    # データ生成
    generate_sales_report_pdf()
    generate_employee_list_pdf()
    generate_financial_statement_pdf()
    generate_survey_results_pdf()
    update_metadata_pdf()
    
    print("\n=== すべてのPDF練習用データ生成完了 ===")

if __name__ == "__main__":
    main()
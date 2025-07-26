# AI研修用ダミーデータリポジトリ

このリポジトリは、AI研修やAI学習に必要な各種ダミーデータを提供しています。著作権やプライバシーに配慮した安全なデータを使用して、様々なAI技術を学習できます。

## 📁 ディレクトリ構造

```
/
├── data/                 # データファイル格納ディレクトリ
│   ├── excel/           # Excel/CSVデータ
│   ├── text/            # テキストデータ
│   └── pdf/             # PDFドキュメント（今後追加予定）
├── assets/              # Webサイト用アセット
│   ├── css/
│   ├── js/
│   └── images/
├── guides/              # 利用ガイド
├── _data/               # メタデータ
│   └── metadata.json    # データの詳細情報
├── generate_dummy_data.py  # データ生成スクリプト
└── README.md           # このファイル
```

## 🚀 クイックスタート

### 1. リポジトリのクローン

```bash
git clone https://github.com/[username]/ai-training-dummy-data.git
cd ai-training-dummy-data
```

### 2. データの利用

各データは `data/` ディレクトリ内に格納されています。

```bash
# Excelデータを確認
ls data/excel/

# テキストデータを確認
ls data/text/
```

## 📊 利用可能なデータ

### 1. 教育データ

#### 学生成績データ (`student_scores.xlsx`, `student_scores.csv`)
- **内容**: 1,000人の生徒×12ヶ月分の成績データ
- **列**: 生徒ID、生徒名、性別、クラス、年月、国語、数学、英語、理科、社会、合計、平均
- **レコード数**: 12,000件
- **用途**: 
  - 成績推移の分析
  - 科目間の相関分析
  - クラス別・性別の統計分析
  - 機械学習による成績予測

### 2. ビジネスデータ

#### 商品購入データ (`sales_data.xlsx`, `sales_data.csv`)
- **内容**: 2024年の商品購入履歴
- **列**: 注文ID、注文日、顧客ID、商品ID、商品名、カテゴリ、単価、数量、小計、割引率、割引額、売上金額、地域、支払方法
- **レコード数**: 5,000件
- **用途**:
  - 売上分析・予測
  - 顧客購買パターン分析
  - 地域別・時系列分析
  - 商品推薦システムの構築

#### スーパーマーケット売上データ (`supermarket_sales_data.csv`, `supermarket_monthly_summary.csv`)
- **内容**: 全国30店舗のスーパーマーケットチェーンの売上データ（2023年1月〜2024年12月）
- **詳細データ列**: 日付、年、月、日、曜日、地域、店舗名、カテゴリ、商品名、販売数量、単価、売上金額、原価、粗利益、粗利率、顧客数、在庫数、在庫回転率
- **月次集計列**: 年月、地域、店舗名、売上金額、粗利益、顧客数、販売数量
- **レコード数**: 
  - 詳細データ: 468,961件
  - 月次集計: 720件
- **地域**: 北海道、東北、関東、中部、関西、中国、四国、九州（全8地域）
- **カテゴリ**: 生鮮食品、加工食品、日用品、飲料、お菓子
- **用途**:
  - BIツールでのダッシュボード作成
  - 地域別・店舗別売上分析
  - 商品カテゴリ別パフォーマンス分析
  - 季節性・曜日別売上トレンド分析
  - 在庫管理の最適化
  - 粗利率分析

### 3. テキストデータ

#### 会議文字起こしデータ (`meeting_transcript_*.txt`)
- **内容**: 3種類の会議の文字起こし
  - プロジェクト進捗確認会議
  - 新製品企画提案会議
  - 売上報告・分析会議
- **用途**:
  - 自然言語処理の練習
  - 要約生成
  - 議事録自動作成
  - キーワード抽出

## 💡 活用例

### ChatGPT/Claudeでの使用例

1. **データ分析**
   ```
   「student_scores.csvを読み込んで、クラス別の平均成績を分析してください」
   ```

2. **可視化**
   ```
   「sales_data.csvから月別売上推移グラフを作成してください」
   ```

3. **テキスト要約**
   ```
   「meeting_transcript_1.txtの内容を3行で要約してください」
   ```

### Pythonでの使用例

```python
import pandas as pd

# 学生成績データの読み込み
df_scores = pd.read_csv('data/excel/student_scores.csv')

# 基本統計量の確認
print(df_scores.describe())

# クラス別平均点
class_avg = df_scores.groupby('クラス')['平均'].mean()
print(class_avg)
```

### Excelでの使用例

1. `student_scores.xlsx`を開く
2. ピボットテーブルで月別・クラス別集計
3. グラフで可視化

## 🔧 データの再生成

新しいダミーデータを生成する場合：

```bash
# 仮想環境の有効化
source venv/bin/activate  # Mac/Linux
# または
venv\Scripts\activate  # Windows

# データ生成
python generate_dummy_data.py
```

## 📝 注意事項

- すべてのデータは架空のものです
- 個人情報は含まれていません
- 商用利用可能（出典明記推奨）
- データの二次配布は禁止

## 🤝 貢献方法

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/new-data`)
3. 変更をコミット (`git commit -m 'Add new dataset'`)
4. ブランチにプッシュ (`git push origin feature/new-data`)
5. プルリクエストを作成

## 📄 ライセンス

MIT License - 詳細は[LICENSE](LICENSE)ファイルを参照

## 📞 サポート

質問や提案がある場合は、[Issues](https://github.com/groundcobra009/keitaro-dummy-data/issues)で報告してください。

---

**最終更新日**: 2025年7月26日
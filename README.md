# 🤖 AI研修用ダミーデータリポジトリ

このリポジトリは、AI研修やAI学習に必要な各種ダミーデータを提供しています。著作権やプライバシーに配慮した安全なデータを使用して、様々なAI技術を学習できます。✨

## 📁 ディレクトリ構造

```
/
├── data/                 # データファイル格納ディレクトリ
│   ├── excel/           # Excel/CSVデータ
│   ├── text/            # テキストデータ
│   ├── audio/           # 音声書き起こしデータ
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

# 音声書き起こしデータを確認
ls data/audio/
```

## 📋 データファイル一覧表

### Excel/CSVデータ（`data/excel/`）

| ファイル名 | 日本語説明 | レコード数 | 主な用途 |
|-----------|-----------|---------|---------|
| `student_scores.xlsx/.csv` | 🎓 学生成績データ | 12,000件 | 教育データ分析、成績予測 |
| `sales_data.xlsx/.csv` | 🛒 商品購入データ | 5,000件 | 売上分析、顧客分析 |
| `supermarket_sales_data.csv` | 🏪 スーパー売上詳細 | 468,961件 | BIダッシュボード、時系列分析 |
| `supermarket_monthly_summary.csv` | 📊 スーパー月次集計 | 720件 | 月次レポート、トレンド分析 |
| `plant_measurements.xlsx/.csv` | 🌸 植物測定データ（iris風） | 150件 | R分析、分類・クラスター分析 |
| `economics_data.xlsx/.csv` | 📈 経済指標データ | 60件 | 時系列分析、経済予測 |
| `diamonds_data.xlsx/.csv` | 💎 ダイヤモンド品質データ | 2,000件 | 価格予測、回帰分析 |
| `weather_data_2023.xlsx/.csv` | 🌤️ 2023年東京気象データ | 365件 | 季節性分析、環境データ分析 |
| `excel_functions_exercises.xlsx` | 📝 Excel関数練習問題 | 複数シート | Excel関数学習、業務効率化 |
| `messy_sales_report.csv` | 🔧 汚い営業レポート | - | データクレンジング練習 |
| `messy_employee_data.csv` | 🔧 汚い従業員データ | - | データ前処理練習 |
| `messy_inventory_warehouse_a.csv` | 🔧 汚い在庫データA | - | ETL処理練習 |
| `messy_inventory_warehouse_b.csv` | 🔧 汚い在庫データB | - | データ統合練習 |

### PDFデータ（`data/pdf/`）

| ファイル名 | 日本語説明 | ページ数 | 主な用途 |
|-----------|-----------|---------|---------|
| `sales_report_2024.pdf` | 📄 2024年度売上レポート | 2ページ | PDF→CSV変換練習 |
| `employee_list.pdf` | 👥 従業員名簿 | 2ページ | 人事データ抽出練習 |
| `financial_statement.pdf` | 💰 財務諸表 | 2ページ | 会計データ変換練習 |
| `survey_results.pdf` | 📝 顧客満足度調査結果 | 1ページ | 調査データ構造化練習 |

### テキストデータ（`data/text/`）

| ファイル名 | 日本語説明 | 内容 | 主な用途 |
|-----------|-----------|------|---------|
| `meeting_transcript_1.txt` | 📋 プロジェクト会議議事録 | 正式な文書 | 自然言語処理、要約生成 |
| `meeting_transcript_2.txt` | 📋 企画会議議事録 | 正式な文書 | テキスト分析、キーワード抽出 |
| `meeting_transcript_3.txt` | 📋 売上報告会議議事録 | 正式な文書 | 議事録自動作成練習 |
| `word_wildcard_practice.txt` | 🔍 Word ワイルドカード練習問題 | 15問の練習問題 | Word検索置換技術習得 |
| `word_wildcard_guide.md` | 📖 ワイルドカード使い方ガイド | 完全ガイド | 正規表現・パターンマッチング学習 |
| `dictionary_words_recommendation.txt` | 📚 辞書登録推奨単語リスト | 業界別専門用語 | 作業効率化、IME辞書管理 |

### 音声データ（`data/audio/`）

| ファイル名 | 日本語説明 | 内容 | 主な用途 |
|-----------|-----------|------|---------|
| `meeting_audio_transcript_1.txt` | 🎤 営業会議音声書き起こし | 話し言葉・雑談含む | 議事録作成練習 |
| `meeting_audio_transcript_2.txt` | 🎤 開発会議音声書き起こし | 話し言葉・雑談含む | 音声認識結果整形 |
| `meeting_audio_transcript_3.txt` | 🎤 進捗会議音声書き起こし | 話し言葉・雑談含む | 会話データ分析 |

## 🎯 学習目的別ファイル選択ガイド

### 📊 データ分析初心者
| 目的 | 推奨ファイル | 理由 |
|------|-------------|------|
| **📈 Excel基本操作** | `student_scores.xlsx` | 構造が分かりやすく、ピボットテーブル練習に最適 |
| **📊 グラフ作成** | `weather_data_2023.csv` | 時系列データで季節性が見える |
| **📝 関数練習** | `excel_functions_exercises.xlsx` | 段階的な関数学習ができる |

### 🔬 データサイエンス学習
| 目的 | 推奨ファイル | 理由 |
|------|-------------|------|
| **🐍 Python pandas入門** | `sales_data.csv` | 適度なサイズで多様な分析が可能 |
| **📊 R統計解析** | `plant_measurements.csv` | iris風データで分類分析の定番 |
| **📈 時系列分析** | `economics_data.csv` | トレンドと季節性を持つ経済データ |
| **🤖 機械学習** | `diamonds_data.csv` | 回帰・分類問題に適したサイズと特徴量 |

### ⚡ 業務効率化・自動化
| 目的 | 推奨ファイル | 理由 |
|------|-------------|------|
| **🔧 データクレンジング** | `messy_*.csv`シリーズ | 実務でよくある汚いデータパターン |
| **📄 PDF処理** | `*.pdf`シリーズ | 表形式データの抽出練習 |
| **📝 Word自動化** | `word_wildcard_*.txt` | 文書整形の効率化技術 |
| **💾 大量データ処理** | `supermarket_sales_data.csv` | 46万件の大容量データ |

### 🤖 AI・自然言語処理
| 目的 | 推奨ファイル | 理由 |
|------|-------------|------|
| **📝 文書要約** | `meeting_transcript_*.txt` | 正式な議事録形式 |
| **🎤 音声認識後処理** | `meeting_audio_transcript_*.txt` | 話し言葉の整形練習 |
| **🔍 テキスト分析** | 全テキストファイル | 多様な文書形式で包括的学習 |

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

### 3. R分析専用データセット

#### 植物測定データ (`plant_measurements.xlsx`, `plant_measurements.csv`)
- **内容**: Rのirisデータセットに似た植物の花弁・がく片測定データ
- **列**: がく片長、がく片幅、花弁長、花弁幅、品種、採取地、採取日
- **レコード数**: 150件（3品種×50サンプル）
- **用途**:
  - 分類分析の練習
  - クラスター分析
  - 主成分分析（PCA）
  - 判別分析

#### 経済指標データ (`economics_data.xlsx`, `economics_data.csv`)
- **内容**: 2020-2024年の日本経済指標月次データ
- **列**: 年月日、年、月、人口、失業率、GDP指数、消費者物価指数、株価指数、為替レート
- **レコード数**: 60件
- **用途**:
  - 時系列分析
  - 経済予測モデル
  - 相関分析
  - 回帰分析

#### ダイヤモンド品質データ (`diamonds_data.xlsx`, `diamonds_data.csv`)
- **内容**: 2,000個のダイヤモンドの品質・価格データ
- **列**: カラット、カット、色、透明度、奥行き、テーブル、価格、長さ、幅、深さ、鑑定書、産地
- **レコード数**: 2,000件
- **用途**:
  - 価格予測モデル
  - 多重回帰分析
  - 品質要因分析
  - データ可視化

#### 2023年東京気象データ (`weather_data_2023.xlsx`, `weather_data_2023.csv`)
- **内容**: 2023年1年間の東京の日別気象データ
- **列**: 日付、年、月、日、曜日、平均気温、最高気温、最低気温、湿度、降水量、気圧、風速、日照時間、観測地点、天気
- **レコード数**: 365件
- **用途**:
  - 季節性分析
  - 気温予測モデル
  - 時系列パターン分析
  - 環境データ分析

### 4. テキストデータ

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

### 5. 音声データ（議事録練習用）

#### 音声書き起こしデータ (`meeting_audio_transcript_*.txt`)
- **内容**: 3種類の会議の音声書き起こし（話し言葉）
  - 営業会議（売上進捗と戦略議論）
  - 製品開発ブレインストーミング（新商品アイデア出し）
  - プロジェクト進捗報告会（システム改修進捗）
- **特徴**: 実際の話し言葉を再現（言い淀み、相槌、雑談含む）
- **用途**:
  - 議事録作成練習
  - 音声認識結果の整形
  - 会話データの分析
  - 要約・整理スキルの向上

### 6. PDFデータ（変換練習用）

#### ビジネスレポートPDF
- **売上レポート** (`sales_report_2024.pdf`)
  - 四半期売上データを含む2ページのレポート
  - 表形式データ：地域別売上、サマリー情報
  - PDF→CSV変換練習に最適

- **従業員名簿** (`employee_list.pdf`)
  - 50名の従業員情報（社員番号、氏名、部署、役職等）
  - 構造化された表データ
  - 人事データ処理の練習用

- **財務諸表** (`financial_statement.pdf`)
  - 損益計算書と貸借対照表
  - 会計数値データの抽出練習
  - 財務分析用データ変換

- **アンケート結果** (`survey_results.pdf`)
  - 顧客満足度調査結果
  - パーセンテージと統計データ
  - 調査データの構造化練習

- **用途**:
  - PDF→CSV変換技術の習得
  - テキスト抽出とデータ構造化
  - pypdfやpdfplumberの使用練習
  - OCR処理の学習
  - レポート自動化スキル向上

### 7. Excel関数練習問題

#### Excel関数練習ファイル (`excel_functions_exercises.xlsx`)
Excel関数の実践的な使い方を学べる総合練習問題集です。文字列操作、VLOOKUP、日付計算、統計関数など、業務でよく使う関数を体系的に学習できます。

**ファイル構成**:
- **問題一覧シート**: 全10問の概要と難易度
- **顧客データシート**: 文字列関数練習用（200件）
- **商品マスタシート**: VLOOKUP用参照表（10商品）
- **売上データシート**: VLOOKUP練習用（300件）
- **従業員データシート**: 日付・条件分岐関数用（100件）
- **試験結果シート**: 統計関数・条件付き書式用（150件）

#### 📚 練習問題詳細

##### 【問題1-4】文字列関数（初級～中級）
**使用データ**: 顧客データシート

1. **メールアドレス分割**: `RIGHT`, `FIND`, `LEN`関数を使ってメールアドレスからドメイン名を抽出
   - 例: `tanaka_hanako@gmail.com` → `gmail.com`

2. **氏名分割**: `LEFT`, `FIND`関数でフルネームを姓と名に分割
   - 例: `田中 花子` → 姓:`田中` 名:`花子`

3. **電話番号統一**: `SUBSTITUTE`, `LEN`関数で電話番号を統一フォーマット（XXX-XXXX-XXXX）に変換
   - 例: `09012345678` → `090-1234-5678`

4. **住所抽出**: `LEFT`, `FIND`関数で住所から都道府県名を抽出
   - 例: `東京都_新宿区_歌舞伎町` → `東京都`

##### 【問題5-6】VLOOKUP関数（中級）
**使用データ**: 売上データ + 商品マスタシート

5. **商品情報取得**: `VLOOKUP`で商品コードから商品名と単価を自動取得
6. **売上金額計算**: VLOOKUP結果を使って売上金額（単価×数量）を計算

##### 【問題7-8】日付・条件分岐関数（中級～上級）
**使用データ**: 従業員データシート

7. **勤続年数計算**: `DATEDIF`, `TODAY`関数で入社日から勤続年数を計算
8. **給与グレード判定**: `IF`, ネスト関数で年齢・勤続年数に応じた給与グレードを判定
   - 新人(22-25歳)、中堅(26-35歳)、ベテラン(36歳以上)

##### 【問題9-10】統計・条件付き書式（上級）
**使用データ**: 試験結果シート

9. **統計分析**: `AVERAGE`, `MAX`, `MIN`, `STDEV`で各科目の基本統計量を計算
10. **条件付き書式**: 成績に応じてセル色を自動変更
    - 90点以上: 青色、80-89点: 緑色、70-79点: 黄色、70点未満: 赤色

#### 🎯 学習効果
- **文字列処理**: 実務でよくある区切り文字での分割処理をマスター
- **データ参照**: VLOOKUPによるマスタ連携の基本を習得
- **自動計算**: 日付計算や条件分岐で業務効率化を実現
- **データ可視化**: 条件付き書式でデータの視覚的把握力を向上

#### 💡 活用シーン
- 顧客データの整形・分析
- 売上データの集計・レポート作成
- 人事データの管理・分析
- 成績管理・統計処理

### 8. データ整形練習用データ

#### 汚いCSVファイル（整形練習用）
- **営業レポート** (`messy_sales_report.csv`)
  - 不統一な数値フォーマット（¥記号、カンマ、単位混在）
  - 途中に集計行挿入
  - 異なる日付形式
  - 不要なヘッダー・フッター

- **従業員データ** (`messy_employee_data.csv`)
  - 重複データ（スペース違い）
  - 欠損値
  - 年齢・給与の表記ゆれ
  - 電話番号・メールアドレスの形式バラバラ

- **在庫データ** (`messy_inventory_warehouse_a.csv`, `messy_inventory_warehouse_b.csv`)
  - 商品コードの不統一
  - 数量の単位混在
  - 空行挿入
  - 複数ファイルに分散

- **用途**:
  - データクレンジング練習
  - pandas/Excel操作技術向上
  - データ前処理スキル習得
  - ETL処理の学習

### 9. Word正規表現・ワイルドカード練習

#### ワイルドカード練習問題 (`word_wildcard_practice.txt`)
- **内容**: Wordの「検索と置換」機能で使用するワイルドカード（正規表現）の練習問題
- **問題レベル**: 基本（15問）
  - 電話番号・日付・メールアドレスの統一
  - HTMLタグ除去、重複スペース整理
  - 社員番号形式チェック、引用文整形
- **特徴**: 実務でよく発生するパターンを重視
- **用途**:
  - Wordワイルドカードの習得
  - 文書整形作業の効率化
  - パターンマッチングの理解
  - 正規表現の基礎学習

#### ワイルドカード使い方ガイド (`word_wildcard_guide.md`)
- **内容**: Microsoft Wordワイルドカード機能の完全ガイド
- **基本文法**: `?` `*` `[...]` `{n,m}` `()` などの使い方
- **実践パターン集**: 電話番号、日付、メール、価格の処理例
- **高度なテクニック**: HTMLタグ除去、番号付きリスト整形
- **学習ステップ**: 初級→中級→上級の段階的学習法
- **デバッグのコツ**: エラー対処法とトラブルシューティング

### 10. 辞書登録推奨単語

#### 辞書登録推奨単語リスト (`dictionary_words_recommendation.txt`)
- **内容**: IME辞書に登録すると作業効率が向上する単語集
- **カテゴリ構成**:
  - **ビジネス用語**: ステークホルダー、アジェンダ、マイルストーン等
  - **IT・技術用語**: API、クラウド、アルゴリズム、フレームワーク等
  - **マーケティング用語**: SEO、コンバージョン、エンゲージメント等
  - **財務・会計用語**: キャッシュフロー、ROI、EBITDA等
  - **人事・組織用語**: ダイバーシティ、テレワーク、オンボーディング等
  - **法務・コンプライアンス**: ガバナンス、GDPR、トレーサビリティ等
  - **特殊記号・単位**: ©、®、™、€、$等
- **業界特化**: 医療、製造業など業界別専門用語
- **登録のコツ**: 効率的な辞書管理方法

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

4. **議事録作成**
   ```
   「meeting_audio_transcript_1.txtから正式な議事録を作成してください」
   ```

5. **データクレンジング**
   ```
   「messy_employee_data.csvの重複と欠損値を処理してください」
   ```

6. **PDF変換**
   ```
   「sales_report_2024.pdfから売上データを抽出してCSVに変換してください」
   ```

7. **Wordワイルドカード**
   ```
   「word_wildcard_practice.txtの電話番号統一問題をWordのワイルドカードで解決してください」
   ```

8. **辞書登録**
   ```
   「dictionary_words_recommendation.txtからIT業界でよく使う20語を選んで辞書登録用リストを作成してください」
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

# PDFからデータを抽出（pdfplumber使用例）
import pdfplumber

# PDFファイルを開いてテーブルを抽出
with pdfplumber.open('data/pdf/sales_report_2024.pdf') as pdf:
    # 最初のページからテーブルを取得
    first_page = pdf.pages[0]
    tables = first_page.extract_tables()
    
    # テーブルをDataFrameに変換
    if tables:
        df_sales = pd.DataFrame(tables[0][1:], columns=tables[0][0])
        print(df_sales)
```

### Rでの使用例

```r
# 植物測定データの読み込み（iris風データ）
plant_data <- read.csv('data/excel/plant_measurements.csv', fileEncoding = 'UTF-8')

# 基本統計量
summary(plant_data[,1:4])

# 散布図行列
pairs(plant_data[,1:4], col = plant_data$品種)

# 主成分分析
pca_result <- prcomp(plant_data[,1:4], scale = TRUE)
biplot(pca_result)

# 経済データの時系列分析
economics <- read.csv('data/excel/economics_data.csv', fileEncoding = 'UTF-8')
economics$年月日 <- as.Date(economics$年月日)

# GDP指数の時系列プロット
plot(economics$年月日, economics$GDP指数, type = 'l', 
     main = 'GDP指数の推移', xlab = '年月', ylab = 'GDP指数')

# 気象データの季節性分析
weather <- read.csv('data/excel/weather_data_2023.csv', fileEncoding = 'UTF-8')
weather$日付 <- as.Date(weather$日付)

# 月別平均気温
monthly_temp <- aggregate(平均気温 ~ 月, data = weather, FUN = mean)
barplot(monthly_temp$平均気温, names.arg = monthly_temp$月,
        main = '月別平均気温', xlab = '月', ylab = '気温（℃）')

# ダイヤモンドデータの価格予測
diamonds <- read.csv('data/excel/diamonds_data.csv', fileEncoding = 'UTF-8')

# 価格とカラットの関係
plot(diamonds$カラット, diamonds$価格, 
     main = 'カラットと価格の関係', xlab = 'カラット', ylab = '価格')

# 線形回帰モデル
model <- lm(価格 ~ カラット + as.factor(カット), data = diamonds)
summary(model)

# PDFからデータを抽出（pdftools使用例）
library(pdftools)
library(tabulizer)

# PDFからテーブルを抽出
pdf_file <- "data/pdf/financial_statement.pdf"
tables <- extract_tables(pdf_file)

# 最初のテーブルをデータフレームに変換
if(length(tables) > 0) {
  financial_data <- as.data.frame(tables[[1]])
  colnames(financial_data) <- financial_data[1,]
  financial_data <- financial_data[-1,]
  print(financial_data)
}
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

# スーパーマーケットデータを生成
python generate_supermarket_data.py

# Excel関数練習問題を生成
python generate_excel_functions_data.py

# 汚いデータを生成（データ整形練習用）
python generate_messy_excel_data.py

# R分析用データと気象データを生成
python generate_r_analysis_data.py

# PDF練習用データを生成
python generate_pdf_data.py
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
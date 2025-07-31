# GAS (Google Apps Script) ファイル集

このフォルダには、Google Apps Scriptで作成された自動化スクリプトが含まれています。

## フォルダ構成

```
GAS/
├── README.md                    # このファイル
└── Query関数練習問題/
    └── query_function_practice.gs  # Query関数練習シート作成スクリプト
```

## 各フォルダの説明

### Query関数練習問題/
Google SheetsのQuery関数を学習するための練習シートを自動作成するスクリプトが含まれています。

**ファイル:**
- `query_function_practice.gs` - Query関数練習シート作成スクリプト

**機能:**
- サンプルデータ（社員データ・売上データ）の自動生成
- 基本的なQuery関数の使用例シート作成
- 高度なQuery関数の使用例シート作成
- 10問の練習問題シート作成
- 練習問題の解答例シート作成

## 使用方法

1. Google Apps Script (https://script.google.com) にアクセス
2. 新しいプロジェクトを作成
3. 該当フォルダ内の`.gs`ファイルの内容をコピー&ペースト
4. スクリプトを実行

## 注意事項

- スクリプト実行前にGoogle Sheetsへのアクセス権限を許可してください
- 作成されるスプレッドシートは自動的にGoogleドライブに保存されます
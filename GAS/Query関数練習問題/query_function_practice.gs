/**
 * Google Sheets Query関数練習シート作成スクリプト
 * 複数のシートを作成し、サンプルデータと練習問題を設定します
 */

function createQueryPracticeSheets() {
  // 新しいスプレッドシートを作成
  const spreadsheet = SpreadsheetApp.create('Query関数練習シート');
  
  // デフォルトのシートの名前を変更して再利用
  const defaultSheet = spreadsheet.getSheets()[0];
  if (defaultSheet.getName() === 'シート1') {
    defaultSheet.setName('サンプルデータ');
  }
  
  // 各シートを作成（サンプルデータは既に存在するので除外）
  createBasicQueriesSheet(spreadsheet);
  createAdvancedQueriesSheet(spreadsheet);
  createPracticeProblemsSheet(spreadsheet);
  createAnswerSheet(spreadsheet);
  
  // サンプルデータシートの内容を設定
  setupSampleDataSheet(defaultSheet);
  
  // スプレッドシートのURLを出力
  console.log('スプレッドシートが作成されました: ' + spreadsheet.getUrl());
  return spreadsheet.getUrl();
}

/**
 * サンプルデータシートの内容を設定
 */
function setupSampleDataSheet(sheet) {
  // 社員データ
  const employeeData = [
    ['社員ID', '氏名', '部署', '役職', '入社年', '給与', '年齢', '性別'],
    ['E001', '田中太郎', '営業部', '課長', 2018, 450000, 35, '男'],
    ['E002', '佐藤花子', '営業部', '主任', 2019, 380000, 28, '女'],
    ['E003', '鈴木次郎', '開発部', '部長', 2015, 600000, 42, '男'],
    ['E004', '高橋美咲', '開発部', 'エンジニア', 2021, 320000, 25, '女'],
    ['E005', '田村健太', '人事部', '課長', 2017, 420000, 38, '男'],
    ['E006', '山田優子', '人事部', '主任', 2020, 350000, 30, '女'],
    ['E007', '中村雅志', '営業部', 'エンジニア', 2022, 280000, 24, '男'],
    ['E008', '小林恵美', '開発部', 'エンジニア', 2020, 340000, 27, '女'],
    ['E009', '加藤直樹', '総務部', '課長', 2016, 440000, 40, '男'],
    ['E010', '木村由美', '総務部', '主任', 2019, 360000, 32, '女'],
    ['E011', '斎藤隆', '営業部', 'エンジニア', 2023, 260000, 23, '男'],
    ['E012', '松本真理', '開発部', '主任', 2018, 390000, 33, '女']
  ];
  
  // データを挿入
  const range = sheet.getRange(1, 1, employeeData.length, employeeData[0].length);
  range.setValues(employeeData);
  
  // ヘッダー行の書式設定
  const headerRange = sheet.getRange(1, 1, 1, employeeData[0].length);
  headerRange.setBackground('#4285f4');
  headerRange.setFontColor('white');
  headerRange.setFontWeight('bold');
  
  // 列幅を自動調整
  sheet.autoResizeColumns(1, employeeData[0].length);
  
  // 売上データを別の範囲に追加
  const salesData = [
    ['', '', '', '', '', '', '', ''],
    ['売上データ', '', '', '', '', '', '', ''],
    ['日付', '社員ID', '商品名', '数量', '単価', '売上金額', '地域', '顧客タイプ'],
    ['2024-01-15', 'E001', 'ノートPC', 2, 80000, 160000, '東京', '法人'],
    ['2024-01-18', 'E002', 'マウス', 10, 2000, 20000, '大阪', '個人'],
    ['2024-01-20', 'E001', 'キーボード', 5, 8000, 40000, '東京', '法人'],
    ['2024-02-05', 'E007', 'ノートPC', 1, 80000, 80000, '名古屋', '個人'],
    ['2024-02-12', 'E002', 'モニター', 3, 25000, 75000, '大阪', '法人'],
    ['2024-02-15', 'E011', 'マウス', 15, 2000, 30000, '福岡', '個人'],
    ['2024-03-03', 'E001', 'ノートPC', 3, 80000, 240000, '東京', '法人'],
    ['2024-03-10', 'E007', 'キーボード', 8, 8000, 64000, '名古屋', '法人'],
    ['2024-03-22', 'E002', 'モニター', 2, 25000, 50000, '大阪', '個人']
  ];
  
  const salesRange = sheet.getRange(employeeData.length + 2, 1, salesData.length, salesData[0].length);
  salesRange.setValues(salesData);
  
  // 売上データのヘッダー行の書式設定
  const salesHeaderRange = sheet.getRange(employeeData.length + 4, 1, 1, salesData[0].length);
  salesHeaderRange.setBackground('#34a853');
  salesHeaderRange.setFontColor('white');
  salesHeaderRange.setFontWeight('bold');
}

/**
 * 基本的なQuery関数練習シートを作成
 */
function createBasicQueriesSheet(spreadsheet) {
  const sheet = spreadsheet.insertSheet('基本クエリ練習');
  
  const content = [
    ['Query関数基本練習', '', '', ''],
    ['', '', '', ''],
    ['1. 全データ取得', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT *")', '', '', ''],
    ['', '', '', ''],
    ['2. 特定の列だけ取得（氏名と部署）', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT B,C")', '', '', ''],
    ['', '', '', ''],
    ['3. 条件付き検索（営業部のみ）', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT * WHERE C=\'営業部\'")', '', '', ''],
    ['', '', '', ''],
    ['4. 数値条件（給与40万円以上）', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT B,C,D,F WHERE F>=400000")', '', '', ''],
    ['', '', '', ''],
    ['5. 並び替え（給与降順）', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT * ORDER BY F DESC")', '', '', ''],
    ['', '', '', ''],
    ['6. 集計（部署別平均給与）', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT C,AVG(F) GROUP BY C")', '', '', '']
  ];
  
  const range = sheet.getRange(1, 1, content.length, content[0].length);
  range.setValues(content);
  
  // タイトル行の書式設定
  sheet.getRange(1, 1).setBackground('#ff9900').setFontColor('white').setFontWeight('bold').setFontSize(14);
  
  // Query関数のセルを識別しやすくする
  for (let i = 0; i < content.length; i++) {
    if (content[i][0] && content[i][0].toString().startsWith('=QUERY')) {
      sheet.getRange(i + 1, 1).setBackground('#f0f0f0').setFontFamily('Courier New');
    }
  }
  
  sheet.autoResizeColumns(1, 4);
}

/**
 * 高度なQuery関数練習シートを作成
 */
function createAdvancedQueriesSheet(spreadsheet) {
  const sheet = spreadsheet.insertSheet('高度クエリ練習');
  
  const content = [
    ['Query関数高度な練習', '', '', ''],
    ['', '', '', ''],
    ['1. 複数条件（AND条件）', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT * WHERE C=\'開発部\' AND F>300000")', '', '', ''],
    ['', '', '', ''],
    ['2. 複数条件（OR条件）', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT * WHERE D=\'課長\' OR D=\'部長\'")', '', '', ''],
    ['', '', '', ''],
    ['3. 文字列検索（LIKE演算子）', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT * WHERE B LIKE \'%田%\'")', '', '', ''],
    ['', '', '', ''],
    ['4. 範囲条件（BETWEEN）', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT * WHERE G BETWEEN 25 AND 35")', '', '', ''],
    ['', '', '', ''],
    ['5. カウント集計', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT C,COUNT(A) GROUP BY C")', '', '', ''],
    ['', '', '', ''],
    ['6. 最大値・最小値', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT C,MAX(F),MIN(F) GROUP BY C")', '', '', ''],
    ['', '', '', ''],
    ['7. 売上データからの集計', '', '', ''],
    ['=QUERY(サンプルデータ!A16:H25,"SELECT C,SUM(F) GROUP BY C LABEL SUM(F) \'合計売上\'")', '', '', ''],
    ['', '', '', ''],
    ['8. 日付範囲での検索', '', '', ''],
    ['=QUERY(サンプルデータ!A16:H25,"SELECT * WHERE A >= date \'2024-02-01\' AND A < date \'2024-03-01\'")', '', '', '']
  ];
  
  const range = sheet.getRange(1, 1, content.length, content[0].length);
  range.setValues(content);
  
  // タイトル行の書式設定
  sheet.getRange(1, 1).setBackground('#9c27b0').setFontColor('white').setFontWeight('bold').setFontSize(14);
  
  // Query関数のセルを識別しやすくする
  for (let i = 0; i < content.length; i++) {
    if (content[i][0] && content[i][0].toString().startsWith('=QUERY')) {
      sheet.getRange(i + 1, 1).setBackground('#f0f0f0').setFontFamily('Courier New');
    }
  }
  
  sheet.autoResizeColumns(1, 4);
}

/**
 * 練習問題シートを作成
 */
function createPracticeProblemsSheet(spreadsheet) {
  const sheet = spreadsheet.insertSheet('練習問題');
  
  const problems = [
    ['Query関数 練習問題', '', '', ''],
    ['', '', '', ''],
    ['以下の問題をQuery関数を使って解いてください。', '', '', ''],
    ['答えは「解答例」シートで確認できます。', '', '', ''],
    ['', '', '', ''],
    ['【問題1】基本的な検索', '', '', ''],
    ['女性社員のみを表示してください。', '', '', ''],
    ['答え：', '', '', ''],
    ['', '', '', ''],
    ['【問題2】数値条件', '', '', ''],
    ['給与が35万円以上の社員の氏名、部署、給与を表示してください。', '', '', ''],
    ['答え：', '', '', ''],
    ['', '', '', ''],
    ['【問題3】文字列検索', '', '', ''],
    ['氏名に「田」が含まれる社員を全て表示してください。', '', '', ''],
    ['答え：', '', '', ''],
    ['', '', '', ''],
    ['【問題4】複数条件', '', '', ''],
    ['開発部で給与が35万円以上の社員を表示してください。', '', '', ''],
    ['答え：', '', '', ''],
    ['', '', '', ''],
    ['【問題5】並び替え', '', '', ''],
    ['全社員を年齢の若い順に並び替えて表示してください。', '', '', ''],
    ['答え：', '', '', ''],
    ['', '', '', ''],
    ['【問題6】集計', '', '', ''],
    ['部署別の社員数を求めてください。', '', '', ''],
    ['答え：', '', '', ''],
    ['', '', '', ''],
    ['【問題7】役職別集計', '', '', ''],
    ['役職別の平均給与を求めてください。', '', '', ''],
    ['答え：', '', '', ''],
    ['', '', '', ''],
    ['【問題8】売上データ分析', '', '', ''],
    ['2024年2月の売上データのみを表示してください。', '', '', ''],
    ['答え：', '', '', ''],
    ['', '', '', ''],
    ['【問題9】高度な集計', '', '', ''],
    ['地域別の売上合計を求めてください。', '', '', ''],
    ['答え：', '', '', ''],
    ['', '', '', ''],
    ['【問題10】複合条件', '', '', ''],
    ['法人顧客で売上金額が5万円以上の取引を表示してください。', '', '', ''],
    ['答え：', '', '', '']
  ];
  
  const range = sheet.getRange(1, 1, problems.length, problems[0].length);
  range.setValues(problems);
  
  // タイトル行の書式設定
  sheet.getRange(1, 1).setBackground('#d32f2f').setFontColor('white').setFontWeight('bold').setFontSize(16);
  
  // 問題番号の書式設定
  for (let i = 0; i < problems.length; i++) {
    if (problems[i][0] && problems[i][0].toString().includes('【問題')) {
      sheet.getRange(i + 1, 1).setBackground('#ffeb3b').setFontWeight('bold');
    }
  }
  
  sheet.autoResizeColumns(1, 4);
}

/**
 * 解答例シートを作成
 */
function createAnswerSheet(spreadsheet) {
  const sheet = spreadsheet.insertSheet('解答例');
  
  const answers = [
    ['Query関数 解答例', '', '', ''],
    ['', '', '', ''],
    ['【問題1】女性社員のみを表示', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT * WHERE H=\'女\'")', '', '', ''],
    ['', '', '', ''],
    ['【問題2】給与35万円以上の社員', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT B,C,F WHERE F>=350000")', '', '', ''],
    ['', '', '', ''],
    ['【問題3】氏名に「田」が含まれる社員', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT * WHERE B LIKE \'%田%\'")', '', '', ''],
    ['', '', '', ''],
    ['【問題4】開発部で給与35万円以上', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT * WHERE C=\'開発部\' AND F>=350000")', '', '', ''],
    ['', '', '', ''],
    ['【問題5】年齢の若い順に並び替え', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT * ORDER BY G ASC")', '', '', ''],
    ['', '', '', ''],
    ['【問題6】部署別社員数', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT C,COUNT(A) GROUP BY C LABEL COUNT(A) \'社員数\'")', '', '', ''],
    ['', '', '', ''],
    ['【問題7】役職別平均給与', '', '', ''],
    ['=QUERY(サンプルデータ!A1:H13,"SELECT D,AVG(F) GROUP BY D LABEL AVG(F) \'平均給与\'")', '', '', ''],
    ['', '', '', ''],
    ['【問題8】2024年2月の売上データ', '', '', ''],
    ['=QUERY(サンプルデータ!A16:H25,"SELECT * WHERE A >= date \'2024-02-01\' AND A < date \'2024-03-01\'")', '', '', ''],
    ['', '', '', ''],
    ['【問題9】地域別売上合計', '', '', ''],
    ['=QUERY(サンプルデータ!A16:H25,"SELECT G,SUM(F) GROUP BY G LABEL SUM(F) \'売上合計\'")', '', '', ''],
    ['', '', '', ''],
    ['【問題10】法人顧客で売上5万円以上', '', '', ''],
    ['=QUERY(サンプルデータ!A16:H25,"SELECT * WHERE H=\'法人\' AND F>=50000")', '', '', '']
  ];
  
  const range = sheet.getRange(1, 1, answers.length, answers[0].length);
  range.setValues(answers);
  
  // タイトル行の書式設定
  sheet.getRange(1, 1).setBackground('#2e7d32').setFontColor('white').setFontWeight('bold').setFontSize(16);
  
  // 問題番号の書式設定
  for (let i = 0; i < answers.length; i++) {
    if (answers[i][0] && answers[i][0].toString().includes('【問題')) {
      sheet.getRange(i + 1, 1).setBackground('#c8e6c9').setFontWeight('bold');
    }
    // Query関数のセルを識別しやすくする
    if (answers[i][0] && answers[i][0].toString().startsWith('=QUERY')) {
      sheet.getRange(i + 1, 1).setBackground('#f0f0f0').setFontFamily('Courier New');
    }
  }
  
  sheet.autoResizeColumns(1, 4);
}

/**
 * スクリプトを実行する関数
 */
function main() {
  createQueryPracticeSheets();
}
# 3-Minute Presentation Script

## 1. Project Introduction

這個作品是 Final Inspection Bottleneck Copilot v0.2。

我用 100% synthetic manufacturing inspection data 建立一個簡單、可重現的資料分析流程，目標是用 Python 和 pandas 分析 lot、station、shift 的 defect rate，並初步找出可能的 bottleneck signal。

專案沒有使用任何公司真實資料或機密製造數據。

## 2. Why I Built This Project

我的工作背景來自 PCB 製造現場與跨部門協作，但這個公開作品刻意採用 generic manufacturing schema，不把分析流程綁死在特定公司或單一製程。

我希望展示的是：如何把「站點、缺陷、延遲、終檢瓶頸」這類製造問題，轉成可計算、可驗證、可重現的資料分析 workflow。

## 3. Dataset and Method

synthetic_defect_log.csv 包含：

- lot_id
- station
- shift
- input_qty
- defect_qty
- defect_type
- delay_hours

核心公式是：

```text
defect_rate = defect_qty / input_qty
```

在 station / shift 層級，我不是直接平均每筆 lot 的 defect rate，而是先加總 defect_qty 與 input_qty，再重新計算 weighted defect rate。

## 4. Key Findings

在這份 synthetic data 裡：

- AOI defect rate：5.29%
- Final Inspection defect rate：7.00%
- Day shift defect rate：5.11%
- Night shift defect rate：7.56%

同時 Final Inspection 的 synthetic total delay_hours 最高，因此在這個 demo 裡被視為 bottleneck candidate。

這些數字只代表 synthetic demo，不是任何真實工廠 benchmark。

## 5. What I Learned

這個作品讓我練習：

- Python 與 pandas DataFrame
- groupby / aggregation
- weighted defect-rate 計算
- CSV / text report 輸出
- matplotlib 圖表
- input/schema validation
- README 與公開資料安全邊界

AI 工具在開發過程中作為 coding/review aid；實際分析邏輯則保持 deterministic、可讀、可檢查。

## 6. Next Step

下一步若要擴充，可以加入較大的 synthetic dataset、時間序列趨勢、異常門檻、confidence / human-review gate，或把分析結果包成簡單 API / dashboard。

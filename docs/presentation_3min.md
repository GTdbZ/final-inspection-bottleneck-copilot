# 3-Minute Presentation Script

## 1. Project Introduction

這個作品是 Final Inspection Bottleneck Copilot v0.1。

我用 100% synthetic PCB 終檢資料，建立一個簡單的製造資料分析流程，目標是用 Python 和 pandas 分析 lot、station、shift 的 defect rate，並初步找出可能的 bottleneck station。

這個作品沒有使用任何公司真實資料，也沒有使用機密製造數據。

## 2. Why I Built This Project

我的背景是 PCB / PDE 製造工程，平常會接觸到 lot、站點、缺陷、交期延遲、終檢瓶頸等問題。

我想用這個作品展示我如何把製造現場經驗轉成資料分析流程，也展示我正在學習 Python、pandas 和 AI-assisted vibe coding。

## 3. Dataset and Method

我先建立 synthetic_defect_log.csv，欄位包含：

- lot_id
- station
- shift
- input_qty
- defect_qty
- defect_type
- delay_hours

接著用 pandas 建立 DataFrame，並計算：

defect_rate = defect_qty / input_qty

再依照 station 和 shift 做 groupby 分析，產出 station_summary.csv 和 shift_summary.csv。

## 4. Key Findings

在這份 synthetic data 裡，AOI 的 defect rate 是 5.29%，Final Inspection 的 defect rate 是 7.0%。

同時，Final Inspection 的 delay_hours 也比 AOI 高。

所以在 v0.1 版本裡，我初步判斷 Final Inspection 是 bottleneck candidate。

另外，shift 分析顯示 Night shift 的 defect rate 是 7.56%，高於 Day shift 的 5.11%，因此 Night shift 也可以被標記為高風險班別。

## 5. What I Learned

這個作品讓我練習了：

- Python variable、dict、list
- pandas DataFrame
- groupby
- defect_rate 計算
- CSV 匯出
- matplotlib 圖表
- README 文件整理
- AI-assisted vibe coding reviewer 流程

我不是單純請 AI 幫我寫 code，而是用工程驗收的方式檢查公式、欄位命名、資料是否為 synthetic data，以及分析結果是否合理。

## 6. Next Step

下一版我會加入更多 synthetic lot data，並加入 defect_type Pareto chart，讓分析更接近實際製造現場的異常分類。

v0.1 目前先聚焦在可解釋、可展示、可口頭說明的最小版本。
# Final Inspection Data Schema

This document defines the fields present in the final inspection dataset (`mock_data/final_inspection_sample.csv`).

## Field Definitions

| Field Name | Data Type | Description | Allowed / Example Values |
| :--- | :--- | :--- | :--- |
| `lot_id` | String | Unique identifier for a batch/lot of manufactured parts. | `LOT-101`, `LOT-102`, etc. |
| `date` | Date (YYYY-MM-DD) | The date when the inspection was performed. | `2026-06-19` |
| `station` | String | The inspection station where the lot was processed. | `FI-AOI`, `FI-VI`, `FI-Packing`, `FI-Recheck` |
| `wait_time_min` | Integer | The time the lot spent waiting in queue before inspection started (in minutes). | `0` to `180` |
| `defect_type` | String | The primary defect identified during inspection. Empty if no defect was found. | `scratch`, `contamination`, `open_short`, `label_error`, `dimension_ng`, `cosmetic_ng`, or empty (for no defect / pass) |
| `operator_group` | String | The identifier of the technician/operator shift group performing the inspection. | `Group-A`, `Group-B`, `Group-C` |
| `rework_flag` | Boolean (0/1) | Indicates if the lot required rework due to inspection results (0 = No, 1 = Yes). | `0`, `1` |

---
title: Month Date Totals
description: 
published: true
date: 2025-11-07T02:19:25.651Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:14.680Z
---

# 📅 Month Date Totals

## 🧪 Feature Overview

This feature is **still a WIP**, but is considered **stable for general use**.

By default, **VotingPlugin** stores monthly totals under the key `MonthTotal`, which resets automatically each month.  
However, this default system doesn’t preserve previous months’ totals after a reset.

The **Month Date Totals** system introduces a new format:  
**`MonthTotal-MONTH-YEAR`**, for example:  
`MonthTotal-DECEMBER-2024`

This allows VotingPlugin to:

- ✅ Automatically reset monthly totals instantly on the first of each month  
- 📊 Keep a full history of past months’ totals (viewable anytime)  
- 🔄 Keep the standard `MonthTotal` value in sync for legacy features  

---

## 📘 Example Behavior

| Setting | Behavior |
|----------|-----------|
| **Disabled (default)** | Uses a single `MonthTotal` key, resets each month, overwriting prior data. |
| **Enabled** | Stores month totals in the format `MonthTotal-MONTH-YEAR` and automatically updates `MonthTotal`. |

---

## 🧾 Command

Use `/vote previousmonthtotals`  
→ Lists all previous months with available vote total data.

---

## ⚙️ Configuration Example

```yaml
    ###########################################
    # Month Date Totals
    # Experimental feature
    # Same options apply for proxy servers
    ###########################################

    # Copies MonthTotal into a new format (MonthTotal-MONTH-YEAR)
    # Safe to enable; keeps MonthTotal synced
    StoreMonthTotalsWithDate: false

    # Uses MonthTotal-MONTH-YEAR as the active total tracker
    # Requires StoreMonthTotalsWithDate enabled
    # Early-stage feature; may still have minor bugs
    UseMonthDateTotalsAsPrimaryTotal: false
```

---

## 🔍 Notes

- Enabling `StoreMonthTotalsWithDate` is safe and recommended for networks wanting monthly tracking history.  
- Enabling `UseMonthDateTotalsAsPrimaryTotal` switches **all total tracking** to this new date-based format — only enable this if you understand the implications.  
- Both options support proxy setups and automatically synchronize across servers when `GlobalData` is enabled.

> 🧠 **Tip:** Keep `StoreMonthTotalsWithDate` enabled even if you don’t use the new system yet — it future-proofs your data with no downside.
{.is-info}

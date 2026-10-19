# EMA Hourly Continuation — MANA/USDT P34_89

**Symbol:** MANA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.5889 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -5.9680 |
| sortino_ratio | -2.2153 |
| max_drawdown | 0.9403 |
| cagr | -0.6642 |
| net_avg_win | 42.6689 |
| net_avg_loss | -59.5623 |
| avg_hold_time_bars | 8.2874 |
| exposure | 0.2622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

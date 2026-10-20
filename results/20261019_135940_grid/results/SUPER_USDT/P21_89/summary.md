# EMA Hourly Continuation — SUPER/USDT P21_89

**Symbol:** SUPER/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.6642 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9705 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -3.2570 |
| sortino_ratio | -1.2261 |
| max_drawdown | 0.7784 |
| cagr | -0.4397 |
| net_avg_win | 43.2042 |
| net_avg_loss | -63.9510 |
| avg_hold_time_bars | 11.8828 |
| exposure | 0.3824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

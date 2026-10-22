# EMA Hourly Continuation — ONDO/USDT P12_89

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.6300 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.9138 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -4.3325 |
| sortino_ratio | -1.6740 |
| max_drawdown | 0.8737 |
| cagr | -0.5523 |
| net_avg_win | 41.8312 |
| net_avg_loss | -58.0131 |
| avg_hold_time_bars | 14.4108 |
| exposure | 0.4959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CPOOL/USDT P8_55

**Symbol:** CPOOL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.8289 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9733 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -1.4987 |
| sortino_ratio | -0.5607 |
| max_drawdown | 0.4914 |
| cagr | -0.2305 |
| net_avg_win | 68.7007 |
| net_avg_loss | -81.6774 |
| avg_hold_time_bars | 13.1460 |
| exposure | 0.4093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

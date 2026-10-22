# EMA Hourly Continuation — RENDER/USDT P12_100

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.7068 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9782 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -2.8816 |
| sortino_ratio | -1.0450 |
| max_drawdown | 0.6841 |
| cagr | -0.3898 |
| net_avg_win | 56.5068 |
| net_avg_loss | -77.9992 |
| avg_hold_time_bars | 19.7989 |
| exposure | 0.5925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

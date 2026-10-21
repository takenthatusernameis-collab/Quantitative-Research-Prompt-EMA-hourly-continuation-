# EMA Hourly Continuation — CGPT/USDT P34_200

**Symbol:** CGPT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.8400 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9878 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -0.9843 |
| sortino_ratio | -0.2442 |
| max_drawdown | 0.2869 |
| cagr | -0.1080 |
| net_avg_win | 87.9061 |
| net_avg_loss | -102.5890 |
| avg_hold_time_bars | 33.5748 |
| exposure | 0.4594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

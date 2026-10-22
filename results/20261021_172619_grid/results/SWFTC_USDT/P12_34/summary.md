# EMA Hourly Continuation — SWFTC/USDT P12_34

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6696 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.8956 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -2.8065 |
| sortino_ratio | -0.8969 |
| max_drawdown | 0.6469 |
| cagr | -0.3371 |
| net_avg_win | 55.0497 |
| net_avg_loss | -73.8070 |
| avg_hold_time_bars | 8.4651 |
| exposure | 0.1928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

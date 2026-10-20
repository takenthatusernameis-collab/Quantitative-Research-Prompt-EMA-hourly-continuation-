# EMA Hourly Continuation — FIDA/USDT P12_200

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.5882 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8446 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -3.1501 |
| sortino_ratio | -0.9210 |
| max_drawdown | 0.6748 |
| cagr | -0.3547 |
| net_avg_win | 47.7663 |
| net_avg_loss | -69.1088 |
| avg_hold_time_bars | 37.1356 |
| exposure | 0.7310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

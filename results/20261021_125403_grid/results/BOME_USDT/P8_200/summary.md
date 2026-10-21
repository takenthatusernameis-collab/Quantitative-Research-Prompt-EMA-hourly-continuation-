# EMA Hourly Continuation — BOME/USDT P8_200

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.8321 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9518 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -0.9048 |
| sortino_ratio | -0.2181 |
| max_drawdown | 0.2758 |
| cagr | -0.0973 |
| net_avg_win | 79.7130 |
| net_avg_loss | -93.1515 |
| avg_hold_time_bars | 61.3531 |
| exposure | 0.7976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — TAIKO/USDT P50_200

**Symbol:** TAIKO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.6504 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -2.5195 |
| sortino_ratio | -0.6606 |
| max_drawdown | 0.5364 |
| cagr | -0.2667 |
| net_avg_win | 61.8043 |
| net_avg_loss | -88.8026 |
| avg_hold_time_bars | 26.1385 |
| exposure | 0.4081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — GALA/USDT P55_200

**Symbol:** GALA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.7736 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9202 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -1.2798 |
| sortino_ratio | -0.2954 |
| max_drawdown | 0.3218 |
| cagr | -0.1278 |
| net_avg_win | 78.8349 |
| net_avg_loss | -93.7210 |
| avg_hold_time_bars | 33.9163 |
| exposure | 0.4055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — STRAX/USDT P144_200

**Symbol:** STRAX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.4397 |
| net_win_rate | 0.4120 |
| gross_profit_factor | 0.6485 |
| gross_win_rate | 0.4120 |
| sharpe_ratio | -3.8133 |
| sortino_ratio | -0.8904 |
| max_drawdown | 0.6524 |
| cagr | -0.3384 |
| net_avg_win | 45.9064 |
| net_avg_loss | -73.1487 |
| avg_hold_time_bars | 8.4120 |
| exposure | 0.1027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — SAND/USDT P34_200

**Symbol:** SAND/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.8425 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0403 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -0.8901 |
| sortino_ratio | -0.2137 |
| max_drawdown | 0.2506 |
| cagr | -0.0952 |
| net_avg_win | 83.0598 |
| net_avg_loss | -102.9056 |
| avg_hold_time_bars | 41.6143 |
| exposure | 0.5296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

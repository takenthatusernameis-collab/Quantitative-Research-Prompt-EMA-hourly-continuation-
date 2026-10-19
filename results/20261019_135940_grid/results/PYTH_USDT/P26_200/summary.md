# EMA Hourly Continuation — PYTH/USDT P26_200

**Symbol:** PYTH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.7723 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9930 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.5003 |
| sortino_ratio | -0.3847 |
| max_drawdown | 0.4248 |
| cagr | -0.1668 |
| net_avg_win | 76.4832 |
| net_avg_loss | -97.8361 |
| avg_hold_time_bars | 40.6372 |
| exposure | 0.6059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

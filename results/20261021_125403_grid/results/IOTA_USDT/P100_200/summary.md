# EMA Hourly Continuation — IOTA/USDT P100_200

**Symbol:** IOTA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.7472 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9612 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -1.4435 |
| sortino_ratio | -0.3331 |
| max_drawdown | 0.3498 |
| cagr | -0.1424 |
| net_avg_win | 73.9227 |
| net_avg_loss | -95.9319 |
| avg_hold_time_bars | 14.2000 |
| exposure | 0.1678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

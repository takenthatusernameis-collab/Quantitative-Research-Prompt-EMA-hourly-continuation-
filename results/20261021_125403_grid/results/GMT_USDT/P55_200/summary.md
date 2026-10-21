# EMA Hourly Continuation — GMT/USDT P55_200

**Symbol:** GMT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8508 |
| net_win_rate | 0.5122 |
| gross_profit_factor | 1.0387 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -0.8063 |
| sortino_ratio | -0.1961 |
| max_drawdown | 0.2322 |
| cagr | -0.0881 |
| net_avg_win | 80.1958 |
| net_avg_loss | -98.9744 |
| avg_hold_time_bars | 27.9233 |
| exposure | 0.3643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

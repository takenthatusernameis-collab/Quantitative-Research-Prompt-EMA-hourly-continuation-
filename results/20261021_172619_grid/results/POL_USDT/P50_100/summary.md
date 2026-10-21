# EMA Hourly Continuation — POL/USDT P50_100

**Symbol:** POL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7101 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 0.9711 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -1.6609 |
| sortino_ratio | -0.4452 |
| max_drawdown | 0.4422 |
| cagr | -0.1850 |
| net_avg_win | 55.8932 |
| net_avg_loss | -80.5457 |
| avg_hold_time_bars | 11.0546 |
| exposure | 0.1749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

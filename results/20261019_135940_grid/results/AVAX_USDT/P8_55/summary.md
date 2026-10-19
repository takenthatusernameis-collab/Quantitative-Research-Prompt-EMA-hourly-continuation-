# EMA Hourly Continuation — AVAX/USDT P8_55

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.5801 |
| net_win_rate | 0.4552 |
| gross_profit_factor | 0.9458 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -6.5984 |
| sortino_ratio | -3.0062 |
| max_drawdown | 0.9753 |
| cagr | -0.7659 |
| net_avg_win | 28.1428 |
| net_avg_loss | -40.5446 |
| avg_hold_time_bars | 10.0514 |
| exposure | 0.4797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

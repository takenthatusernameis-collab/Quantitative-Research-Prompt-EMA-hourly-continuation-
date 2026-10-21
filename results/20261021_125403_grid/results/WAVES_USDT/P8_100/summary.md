# EMA Hourly Continuation — WAVES/USDT P8_100

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.7073 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -2.6935 |
| sortino_ratio | -0.9297 |
| max_drawdown | 0.6818 |
| cagr | -0.3493 |
| net_avg_win | 56.9770 |
| net_avg_loss | -73.4666 |
| avg_hold_time_bars | 22.2879 |
| exposure | 0.5947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

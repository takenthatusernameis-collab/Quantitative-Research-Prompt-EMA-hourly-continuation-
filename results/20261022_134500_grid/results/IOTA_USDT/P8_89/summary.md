# EMA Hourly Continuation — IOTA/USDT P8_89

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 729 |
| net_profit_factor | 0.5764 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -4.3810 |
| sortino_ratio | -1.6619 |
| max_drawdown | 0.8752 |
| cagr | -0.5496 |
| net_avg_win | 35.0401 |
| net_avg_loss | -51.9703 |
| avg_hold_time_bars | 19.6818 |
| exposure | 0.6522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — HNT/USDT P8_100

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.5541 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.7931 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -4.8526 |
| sortino_ratio | -1.9139 |
| max_drawdown | 0.9028 |
| cagr | -0.5986 |
| net_avg_win | 31.6415 |
| net_avg_loss | -46.4493 |
| avg_hold_time_bars | 17.3825 |
| exposure | 0.6218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

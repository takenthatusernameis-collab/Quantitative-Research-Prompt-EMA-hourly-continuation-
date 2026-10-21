# EMA Hourly Continuation — SAFE/USDT P55_100

**Symbol:** SAFE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7692 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0063 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.4797 |
| sortino_ratio | -0.3949 |
| max_drawdown | 0.3939 |
| cagr | -0.1663 |
| net_avg_win | 70.2007 |
| net_avg_loss | -92.8767 |
| avg_hold_time_bars | 10.2362 |
| exposure | 0.1608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

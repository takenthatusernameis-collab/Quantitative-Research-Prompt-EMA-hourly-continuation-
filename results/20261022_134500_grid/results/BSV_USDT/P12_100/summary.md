# EMA Hourly Continuation — BSV/USDT P12_100

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.4792 |
| net_win_rate | 0.4016 |
| gross_profit_factor | 0.7559 |
| gross_win_rate | 0.4150 |
| sharpe_ratio | -7.1366 |
| sortino_ratio | -2.7175 |
| max_drawdown | 0.9674 |
| cagr | -0.7399 |
| net_avg_win | 29.6295 |
| net_avg_loss | -41.4970 |
| avg_hold_time_bars | 17.3293 |
| exposure | 0.5884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

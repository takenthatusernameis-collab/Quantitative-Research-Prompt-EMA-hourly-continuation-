# EMA Hourly Continuation — ZRX/USDT P55_100

**Symbol:** ZRX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.4826 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.8581 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -5.9923 |
| sortino_ratio | -2.1232 |
| max_drawdown | 0.9287 |
| cagr | -0.6485 |
| net_avg_win | 30.3604 |
| net_avg_loss | -50.9343 |
| avg_hold_time_bars | 5.4678 |
| exposure | 0.1583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — RIO/USDT P50_89

**Symbol:** RIO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.6380 |
| net_win_rate | 0.4257 |
| gross_profit_factor | 0.7580 |
| gross_win_rate | 0.4257 |
| sharpe_ratio | -2.5861 |
| sortino_ratio | -0.6385 |
| max_drawdown | 0.5260 |
| cagr | -0.2553 |
| net_avg_win | 70.9634 |
| net_avg_loss | -82.4648 |
| avg_hold_time_bars | 6.6337 |
| exposure | 0.0923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

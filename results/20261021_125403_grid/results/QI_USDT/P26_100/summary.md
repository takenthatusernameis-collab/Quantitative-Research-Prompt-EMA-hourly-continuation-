# EMA Hourly Continuation — QI/USDT P26_100

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.9180 |
| net_win_rate | 0.5482 |
| gross_profit_factor | 1.2017 |
| gross_win_rate | 0.5482 |
| sharpe_ratio | -0.4978 |
| sortino_ratio | -0.1504 |
| max_drawdown | 0.2106 |
| cagr | -0.0714 |
| net_avg_win | 79.8739 |
| net_avg_loss | -105.5545 |
| avg_hold_time_bars | 16.6881 |
| exposure | 0.3292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

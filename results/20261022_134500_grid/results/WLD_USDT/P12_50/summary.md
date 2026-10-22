# EMA Hourly Continuation — WLD/USDT P12_50

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1053 |
| net_profit_factor | 0.6934 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 1.0545 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -4.2474 |
| sortino_ratio | -1.9452 |
| max_drawdown | 0.9063 |
| cagr | -0.6038 |
| net_avg_win | 39.0928 |
| net_avg_loss | -55.4215 |
| avg_hold_time_bars | 7.2498 |
| exposure | 0.3470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

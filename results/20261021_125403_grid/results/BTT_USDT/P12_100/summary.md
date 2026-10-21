# EMA Hourly Continuation — BTT/USDT P12_100

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.6443 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9337 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -3.0610 |
| sortino_ratio | -0.8660 |
| max_drawdown | 0.6569 |
| cagr | -0.3317 |
| net_avg_win | 61.6660 |
| net_avg_loss | -86.0456 |
| avg_hold_time_bars | 35.2152 |
| exposure | 0.6323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — RAY/USDT P100_144

**Symbol:** RAY/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.4593 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8547 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -5.0324 |
| sortino_ratio | -1.5546 |
| max_drawdown | 0.8645 |
| cagr | -0.5389 |
| net_avg_win | 33.3839 |
| net_avg_loss | -59.5739 |
| avg_hold_time_bars | 4.3326 |
| exposure | 0.0953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — QI/USDT P20_26

**Symbol:** QI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.5481 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8730 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -3.4907 |
| sortino_ratio | -0.9410 |
| max_drawdown | 0.6752 |
| cagr | -0.3491 |
| net_avg_win | 48.6297 |
| net_avg_loss | -77.4561 |
| avg_hold_time_bars | 4.9831 |
| exposure | 0.0798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

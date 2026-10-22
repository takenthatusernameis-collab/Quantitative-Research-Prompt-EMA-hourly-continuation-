# EMA Hourly Continuation — KNC/USDT P50_144

**Symbol:** KNC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7084 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9714 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -2.1748 |
| sortino_ratio | -0.6229 |
| max_drawdown | 0.5602 |
| cagr | -0.2475 |
| net_avg_win | 62.6144 |
| net_avg_loss | -86.6369 |
| avg_hold_time_bars | 16.0525 |
| exposure | 0.2919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

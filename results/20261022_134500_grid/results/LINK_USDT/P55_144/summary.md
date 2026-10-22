# EMA Hourly Continuation — LINK/USDT P55_144

**Symbol:** LINK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.5870 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -3.5584 |
| sortino_ratio | -1.0695 |
| max_drawdown | 0.7571 |
| cagr | -0.4092 |
| net_avg_win | 46.1063 |
| net_avg_loss | -74.9064 |
| avg_hold_time_bars | 11.0799 |
| exposure | 0.2332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

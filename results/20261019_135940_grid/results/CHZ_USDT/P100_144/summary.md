# EMA Hourly Continuation — CHZ/USDT P100_144

**Symbol:** CHZ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.4799 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.8880 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -5.1697 |
| sortino_ratio | -1.6212 |
| max_drawdown | 0.8628 |
| cagr | -0.5390 |
| net_avg_win | 36.4436 |
| net_avg_loss | -61.7147 |
| avg_hold_time_bars | 4.0826 |
| exposure | 0.0898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

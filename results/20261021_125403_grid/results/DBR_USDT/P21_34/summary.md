# EMA Hourly Continuation — DBR/USDT P21_34

**Symbol:** DBR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.5421 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -3.7490 |
| sortino_ratio | -1.0233 |
| max_drawdown | 0.6407 |
| cagr | -0.3786 |
| net_avg_win | 53.5655 |
| net_avg_loss | -86.1353 |
| avg_hold_time_bars | 7.2842 |
| exposure | 0.1210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

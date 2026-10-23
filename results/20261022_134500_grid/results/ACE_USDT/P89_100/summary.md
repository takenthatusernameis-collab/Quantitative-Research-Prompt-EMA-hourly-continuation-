# EMA Hourly Continuation — ACE/USDT P89_100

**Symbol:** ACE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.3328 |
| net_win_rate | 0.4360 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -6.5496 |
| sortino_ratio | -2.0533 |
| max_drawdown | 0.9251 |
| cagr | -0.6399 |
| net_avg_win | 21.8398 |
| net_avg_loss | -50.7239 |
| avg_hold_time_bars | 3.6095 |
| exposure | 0.0791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

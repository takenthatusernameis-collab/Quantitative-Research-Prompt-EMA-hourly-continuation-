# EMA Hourly Continuation — DGB/USDT P26_50

**Symbol:** DGB/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6658 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.9137 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -2.6977 |
| sortino_ratio | -0.7532 |
| max_drawdown | 0.5866 |
| cagr | -0.2922 |
| net_avg_win | 64.5737 |
| net_avg_loss | -85.5202 |
| avg_hold_time_bars | 6.4398 |
| exposure | 0.1118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

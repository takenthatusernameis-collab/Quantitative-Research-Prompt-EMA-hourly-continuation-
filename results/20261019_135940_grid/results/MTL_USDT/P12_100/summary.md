# EMA Hourly Continuation — MTL/USDT P12_100

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6485 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9874 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -3.6061 |
| sortino_ratio | -1.1495 |
| max_drawdown | 0.7600 |
| cagr | -0.4290 |
| net_avg_win | 56.0728 |
| net_avg_loss | -78.8610 |
| avg_hold_time_bars | 27.7720 |
| exposure | 0.6560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

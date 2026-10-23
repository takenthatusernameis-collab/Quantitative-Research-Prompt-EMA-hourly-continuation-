# EMA Hourly Continuation — XYO/USDT P100_144

**Symbol:** XYO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.3595 |
| net_win_rate | 0.3760 |
| gross_profit_factor | 0.7114 |
| gross_win_rate | 0.3870 |
| sharpe_ratio | -8.7115 |
| sortino_ratio | -3.1324 |
| max_drawdown | 0.9815 |
| cagr | -0.7934 |
| net_avg_win | 23.1459 |
| net_avg_loss | -38.7887 |
| avg_hold_time_bars | 4.0395 |
| exposure | 0.1157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ACE/USDT P8_12

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1287 |
| net_profit_factor | 0.2774 |
| net_win_rate | 0.4095 |
| gross_profit_factor | 0.8859 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -11.9388 |
| sortino_ratio | -6.0845 |
| max_drawdown | 0.9996 |
| cagr | -0.9564 |
| net_avg_win | 7.2818 |
| net_avg_loss | -18.2024 |
| avg_hold_time_bars | 3.3240 |
| exposure | 0.1936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

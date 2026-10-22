# EMA Hourly Continuation — LUNC/USDT P55_100

**Symbol:** LUNC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.4109 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.8250 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -6.1779 |
| sortino_ratio | -2.2703 |
| max_drawdown | 0.9427 |
| cagr | -0.6766 |
| net_avg_win | 20.7157 |
| net_avg_loss | -44.1432 |
| avg_hold_time_bars | 5.0854 |
| exposure | 0.1570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

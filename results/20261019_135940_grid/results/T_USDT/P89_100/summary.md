# EMA Hourly Continuation — T/USDT P89_100

**Symbol:** T/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.2702 |
| net_win_rate | 0.3819 |
| gross_profit_factor | 0.7676 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -8.8162 |
| sortino_ratio | -3.0064 |
| max_drawdown | 0.9821 |
| cagr | -0.7953 |
| net_avg_win | 16.9016 |
| net_avg_loss | -38.6521 |
| avg_hold_time_bars | 4.2877 |
| exposure | 0.1092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

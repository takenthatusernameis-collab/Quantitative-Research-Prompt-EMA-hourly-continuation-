# EMA Hourly Continuation — CWEB/USDT P20_26

**Symbol:** CWEB/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1156 |
| net_profit_factor | 0.1663 |
| net_win_rate | 0.2059 |
| gross_profit_factor | 0.5097 |
| gross_win_rate | 0.2457 |
| sharpe_ratio | -20.3324 |
| sortino_ratio | -10.9333 |
| max_drawdown | 1.0000 |
| cagr | -0.9979 |
| net_avg_win | 8.3831 |
| net_avg_loss | -13.0666 |
| avg_hold_time_bars | 3.2984 |
| exposure | 0.1733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

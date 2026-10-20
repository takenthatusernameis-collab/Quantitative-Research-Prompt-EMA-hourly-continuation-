# EMA Hourly Continuation — PHA/USDT P21_144

**Symbol:** PHA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.6170 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8760 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -3.6116 |
| sortino_ratio | -1.2072 |
| max_drawdown | 0.7757 |
| cagr | -0.4411 |
| net_avg_win | 47.0512 |
| net_avg_loss | -65.1131 |
| avg_hold_time_bars | 19.3678 |
| exposure | 0.5027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

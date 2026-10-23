# EMA Hourly Continuation — STRAX/USDT P8_34

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1320 |
| net_profit_factor | 0.4708 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.8014 |
| gross_win_rate | 0.4379 |
| sharpe_ratio | -10.1171 |
| sortino_ratio | -5.1540 |
| max_drawdown | 0.9985 |
| cagr | -0.9251 |
| net_avg_win | 16.3910 |
| net_avg_loss | -24.2525 |
| avg_hold_time_bars | 5.9659 |
| exposure | 0.3600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ZIL/USDT P55_144

**Symbol:** ZIL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7991 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0571 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -1.3112 |
| sortino_ratio | -0.3525 |
| max_drawdown | 0.3404 |
| cagr | -0.1499 |
| net_avg_win | 74.0103 |
| net_avg_loss | -98.0685 |
| avg_hold_time_bars | 16.1600 |
| exposure | 0.2571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ZIL/USDT P8_144

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6351 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9546 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -3.0360 |
| sortino_ratio | -0.9329 |
| max_drawdown | 0.6953 |
| cagr | -0.3575 |
| net_avg_win | 51.8809 |
| net_avg_loss | -73.5232 |
| avg_hold_time_bars | 34.9474 |
| exposure | 0.7545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — FIL/USDT P12_20

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.6509 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -1.9849 |
| sortino_ratio | -0.4413 |
| max_drawdown | 0.4377 |
| cagr | -0.1824 |
| net_avg_win | 63.2491 |
| net_avg_loss | -92.4321 |
| avg_hold_time_bars | 4.8250 |
| exposure | 0.0526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
